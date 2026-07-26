import warnings, os, urllib.request, numpy as np, pandas as pd
warnings.filterwarnings("ignore")

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import aif360
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric, ClassificationMetric
from aif360.algorithms.preprocessing import Reweighing

compas_dir = os.path.join(os.path.dirname(aif360.__file__), "data", "raw", "compas")
os.makedirs(compas_dir, exist_ok=True)
csv_path = os.path.join(compas_dir, "compas-scores-two-years.csv")
url = "https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv"
if not os.path.exists(csv_path) or os.path.getsize(csv_path) < 1_000_000:
    urllib.request.urlretrieve(url, csv_path)
size = os.path.getsize(csv_path)
assert size > 1_000_000, f"COMPAS download looks truncated ({size} bytes). Re-run this script."
print(f"COMPAS data present ({size:,} bytes).")

RANDOM_STATE = 4
PROTECTED = "race"
TEST_FRACTION = 0.30

GROUP_LABELS = {
    "race": {1: "Caucasian (privileged)", 0: "African-American (unprivileged)"},
}
privileged_groups   = [{PROTECTED: 1}]
unprivileged_groups = [{PROTECTED: 0}]

def make_pred_dataset(base_dataset, model, X, favorable_label):
    fav_col = list(model.classes_).index(favorable_label)
    out = base_dataset.copy(deepcopy=True)
    out.labels = model.predict(X).reshape(-1, 1)
    out.scores = model.predict_proba(X)[:, fav_col].reshape(-1, 1)
    return out

def audit(dataset_true, dataset_pred, unpriv, priv):
    cm = ClassificationMetric(dataset_true, dataset_pred,
                              unprivileged_groups=unpriv, privileged_groups=priv)
    di = cm.disparate_impact()
    return {
        "Accuracy":                cm.accuracy(),
        "Disparate impact":        di,
        "Statistical parity diff": cm.statistical_parity_difference(),
        "Equal opportunity diff":  cm.equal_opportunity_difference(),
        "Average odds diff":       cm.average_odds_difference(),
    }

def fourfifths_flag(di):
    return "PASS (>= 0.8)" if di >= 0.8 else "FAIL (< 0.8): potential disparate impact"

dataset = CompasDataset()
train, test = dataset.split([1 - TEST_FRACTION], shuffle=True, seed=RANDOM_STATE)

FAV = dataset.favorable_label
UNFAV = dataset.unfavorable_label

print("=== Section 3: data & direction ===")
print("Label column      :", dataset.label_names)
print("Favorable label   :", FAV)
print("Unfavorable label :", UNFAV)
print("Protected attrs   :", dataset.protected_attribute_names)
print("Train / test sizes:", train.features.shape[0], "/", test.features.shape[0])
assert FAV == 0.0

print()
print("=== Section 4: bias in raw labels (train split) ===")
raw = BinaryLabelDatasetMetric(train, unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)
print(f"Disparate impact (data):        {raw.disparate_impact():.3f}")
print(f"Statistical parity diff (data): {raw.mean_difference():.3f}")
print(f"Base rate, unprivileged:        {raw.base_rate(privileged=False):.3f}")
print(f"Base rate, privileged:          {raw.base_rate(privileged=True):.3f}")

print()
print("=== Section 5: feature check ===")
feat = dataset.feature_names
print("Number of features:", len(feat))
for p in dataset.protected_attribute_names:
    print(f"   {p:5s} in features: {p in feat}")
charge_desc = [f for f in feat if f.startswith("c_charge_desc=")]
print(f"   c_charge_desc one-hot columns: {len(charge_desc)}, other features: {len(feat) - len(charge_desc)}")

print()
print("=== Section 6: baseline model ===")
scaler  = StandardScaler().fit(train.features)
X_train = scaler.transform(train.features)
X_test  = scaler.transform(test.features)
y_train = train.labels.ravel()

baseline = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)
baseline.fit(X_train, y_train)

train_pred = make_pred_dataset(train, baseline, X_train, FAV)
test_pred  = make_pred_dataset(test,  baseline, X_test,  FAV)

before = audit(test, test_pred, unprivileged_groups, privileged_groups)
print("BEFORE mitigation")
for k,v in before.items():
    print(f"  {k:26s}: {v: .3f}")
print("  Four-fifths rule          :", fourfifths_flag(before["Disparate impact"]))

print()
print("=== Section 7: mitigation (Reweighing) ===")
RW = Reweighing(unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups)
train_rw = RW.fit_transform(train)

mitigated = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)
mitigated.fit(X_train, y_train, sample_weight=train_rw.instance_weights)

test_pred_mit = make_pred_dataset(test, mitigated, X_test, FAV)
after = audit(test, test_pred_mit, unprivileged_groups, privileged_groups)
print("AFTER mitigation (Reweighing)")
for k,v in after.items():
    print(f"  {k:26s}: {v: .3f}")
print("  Four-fifths rule          :", fourfifths_flag(after["Disparate impact"]))

print()
print("=== Section 8: before/after comparison ===")
compare = pd.DataFrame({"Before": before, "After": after})
compare["Change"] = compare["After"] - compare["Before"]
print(compare.round(3))

acc_cost = before["Accuracy"] - after["Accuracy"]
di_gain  = after["Disparate impact"] - before["Disparate impact"]
print(f"\nDisparate impact moved {di_gain:+.3f} toward parity (1.0 is parity).")
print(f"Accuracy changed {(-acc_cost):+.3f}.")

for k in ["Statistical parity diff", "Equal opportunity diff", "Average odds diff"]:
    if np.sign(before[k]) != np.sign(after[k]) and abs(after[k]) > 1e-9:
        print(f"NOTE: {k} crossed zero (sign flip) — before={before[k]:.3f}, after={after[k]:.3f}")

print()
print("=== Section 9: stability across 10 resampled splits ===")
N_SPLITS = 10
rows = []
for s in range(N_SPLITS):
    tr, te = dataset.split([1 - TEST_FRACTION], shuffle=True, seed=s)
    sc = StandardScaler().fit(tr.features)
    Xtr, Xte = sc.transform(tr.features), sc.transform(te.features)
    ytr = tr.labels.ravel()

    b_clf = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE).fit(Xtr, ytr)
    b_m = audit(te, make_pred_dataset(te, b_clf, Xte, FAV), unprivileged_groups, privileged_groups)

    w = Reweighing(unprivileged_groups=unprivileged_groups, privileged_groups=privileged_groups).fit_transform(tr)
    a_clf = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)
    a_clf.fit(Xtr, ytr, sample_weight=w.instance_weights)
    a_m = audit(te, make_pred_dataset(te, a_clf, Xte, FAV), unprivileged_groups, privileged_groups)

    row = {"split": s}
    for k in b_m: row[f"before_{k}"] = b_m[k]
    for k in a_m: row[f"after_{k}"] = a_m[k]
    rows.append(row)

df = pd.DataFrame(rows)
metrics_list = ["Accuracy","Disparate impact","Statistical parity diff","Equal opportunity diff","Average odds diff"]
print(f"{'Metric':28s} {'Before mean':>12s} {'Before std':>11s} {'After mean':>11s} {'After std':>10s}")
for m in metrics_list:
    bmean, bstd = df[f"before_{m}"].mean(), df[f"before_{m}"].std()
    amean, astd = df[f"after_{m}"].mean(), df[f"after_{m}"].std()
    print(f"{m:28s} {bmean:12.3f} {bstd:11.3f} {amean:11.3f} {astd:10.3f}")

print()
print("=== Section 10: Fairlearn cross-check ===")
from fairlearn.metrics import demographic_parity_difference, demographic_parity_ratio
sens_test = test.protected_attributes[:, test.protected_attribute_names.index(PROTECTED)]
y_true = test.labels.ravel()
y_hat  = test_pred_mit.labels.ravel()
y_true_f = (y_true == FAV).astype(int)
y_hat_f  = (y_hat  == FAV).astype(int)

print("AIF360 (after)      : DI = %.3f | SPD = %+.3f" % (after["Disparate impact"], after["Statistical parity diff"]))
dp_diff_naive = demographic_parity_difference(y_true, y_hat, sensitive_features=sens_test)
dp_ratio_naive = demographic_parity_ratio(y_true, y_hat, sensitive_features=sens_test)
print("Fairlearn NAIVE (label 1 = selected, WRONG direction for COMPAS): DP diff=%.3f  DP ratio=%.3f" % (dp_diff_naive, dp_ratio_naive))
dp_diff_correct = demographic_parity_difference(y_true_f, y_hat_f, sensitive_features=sens_test)
dp_ratio_correct = demographic_parity_ratio(y_true_f, y_hat_f, sensitive_features=sens_test)
print("Fairlearn CORRECTED (recoded so 1=favorable):                    DP diff=%.3f  DP ratio=%.3f" % (dp_diff_correct, dp_ratio_correct))

out_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bias_audit_splits.csv")
df.to_csv(out_csv, index=False)
print(f"Saved per-split results to {out_csv}")