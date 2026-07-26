# Bias Audit Report — Jorge Luis Limo Arispe

Produced by actually running `bias_audit.py` (this folder) against the real ProPublica COMPAS dataset via AIF360 — every number below comes from that run, not from the workshop notebook's own example output. Reproduce with `python3 11_bias_audit/bias_audit.py`.

## 1. Dataset and Protected Attribute

**Dataset:** COMPAS (`compas-scores-two-years.csv`, ProPublica, via `aif360.datasets.CompasDataset`).
**Protected attribute:** `race`.
**Privileged / unprivileged groups:** Caucasian (privileged) / African-American (unprivileged).
**Favorable outcome, stated as a sentence:** the label column is `two_year_recid` (1 = rearrested within two years, 0 = not); AIF360 sets the favorable label to 0 — being predicted **not** to re-offend, since that is the outcome associated with the better real-world consequence (release, lower bail). This was verified, not assumed (`assert FAV == 0.0` in `bias_audit.py`, following the notebook's Section 3 warning that getting this direction wrong invalidates the entire audit).

## 2. Bias Already in the Labels (Section 4 — before any model exists)

| Metric | Value |
|---|---|
| Disparate impact (raw data) | 0.829 |
| Statistical parity diff (raw data) | −0.104 |
| Base rate, unprivileged (African-American) | 0.501 |
| Base rate, privileged (Caucasian) | 0.605 |

**Reading:** even before any model is trained, the *ground-truth* two-year recidivism labels already show a real gap — 50.1% of African-American defendants in this sample carry the favorable label (not rearrested) vs. 60.5% of Caucasian defendants. This is the ceiling problem: the model is not manufacturing this gap out of nothing, it is learning from data that already contains it.

## 3. Before Metrics (baseline logistic regression, all 401 features including `race` itself)

| Metric | Value | Reading |
|---|---|---|
| Accuracy | 0.673 | — |
| Disparate impact | 0.820 | Four-fifths rule: **PASS** (≥ 0.8) — but see §6, this is fragile |
| Statistical parity diff | −0.123 | Unprivileged group predicted favorable less often |
| Equal opportunity diff | −0.063 | Unprivileged group has lower true-positive rate for the favorable outcome |
| Average odds diff | −0.105 | Consistent with the above two |

**Did the model amplify the bias in the data, or merely inherit it?** Essentially inherit it, and if anything slightly compress it on this split: statistical parity diff went from −0.104 (raw labels) to −0.123 (model predictions) — very close, not a large amplification. The more important finding is in §5, not shown by this table alone: `race` is literally included as one of the model's 401 input features (confirmed by checking `dataset.protected_attribute_names` against `dataset.feature_names`), alongside 389 one-hot-encoded `c_charge_desc` columns that plausibly correlate with race and socioeconomic factors. The model was never blind to race — it was never given the chance to "merely inherit" bias through a proxy; it had direct access to the protected attribute.

## 4. Mitigation Applied and Why

**Method:** Reweighing (Kamiran & Calders) — a **pre-processing** method. It re-weights training rows by (expected count under group–label independence) / (observed count); features and labels are never altered, only the `sample_weight` passed to `LogisticRegression.fit()`.

**Fairness metric it targets:** statistical parity / disparate impact — Reweighing is designed to equalize the *overall selection rate* across groups, not equalized odds or predictive parity specifically.

**Why this method and metric fit the harm in this context:** in a pretrial-risk context, the harm most directly analogous to ProPublica's original *Machine Bias* critique of COMPAS is unequal overall rates of being flagged as higher-risk across race groups — a statistical-parity-shaped harm. Reweighing is also the least invasive of the three families offered (pre-processing): it never touches the model's learning objective or its output predictions directly, which keeps the audit's before/after comparison clean (same model class, same test set, same evaluation code — only the training-row weights differ).

**What was given up by choosing this metric rather than another:** targeting statistical parity does not guarantee equal opportunity or equalized odds — and indeed, §5 shows exactly that: the equal-opportunity gap did not close to zero, it flipped sign.

## 5. After Metrics + Trade-off

| Metric | Before | After | Change |
|---|---|---|---|
| Accuracy | 0.673 | 0.657 | −0.016 |
| Disparate impact | 0.820 | 1.101 | +0.281 |
| Statistical parity diff | −0.123 | +0.057 | +0.180 |
| Equal opportunity diff | −0.063 | +0.100 | +0.163 |
| Average odds diff | −0.105 | +0.077 | +0.182 |

**Accuracy cost of the fairness gain:** 1.6 percentage points (0.673 → 0.657).

**Did any gap overshoot past zero?** Yes — all three parity metrics did, and this must be stated plainly rather than reported as a clean win: statistical parity diff went from −0.123 to **+0.057**, equal opportunity diff from −0.063 to **+0.100**, average odds diff from −0.105 to **+0.077**. Disparate impact moved from 0.820 to **1.101** — past 1.0, meaning that on this specific test split, the mitigated model now predicts the favorable outcome (not-rearrested) *more* often for the previously-unprivileged (African-American) group than for the previously-privileged (Caucasian) group. Reweighing did not find parity here — it overcorrected past it. Both directions (0.820 and 1.101) are equally far from the ideal of 1.0, just on opposite sides.

## 6. Uncertainty (Section 9 — is the change real, or noise?)

Ten resampled train/test splits (seeds 0–9), same pipeline, same mitigation, evaluated identically each time:

| Metric | Before mean | Before std | After mean | After std |
|---|---|---|---|---|
| Accuracy | 0.671 | 0.013 | 0.665 | 0.012 |
| Disparate impact | 0.775 | 0.032 | 1.000 | 0.063 |
| Statistical parity diff | −0.161 | 0.027 | −0.001 | 0.039 |
| Equal opportunity diff | −0.091 | 0.029 | 0.053 | 0.030 |
| Average odds diff | −0.140 | 0.024 | 0.021 | 0.036 |

**This is the most important finding in this audit, and it contradicts §3's headline number.** Averaged across 10 splits, the **baseline** model's disparate impact is **0.775 — below the four-fifths threshold — meaning it would typically FAIL the rule**, even though the single split reported in §3 happened to land at 0.820 (a PASS). The specific train/test split used for the headline "before" numbers was, by chance, one of the more favorable ones. Reporting only that single split's "PASS" without this stability check would have been misleading.

For the **after** (mitigated) numbers: mean disparate impact is 1.000 with std 0.063 — genuinely centered on parity across resamples, not just on this one split. Statistical parity diff after mitigation has mean −0.001 with std 0.039 — the mean is smaller than the standard deviation, which by the workshop's own rule ("if a gap's mean is smaller than its standard deviation, you do not have a finding — you have noise") means **the post-mitigation statistical-parity gap is statistically indistinguishable from zero across resamples**, which is a genuinely positive result, more robust than the single-split table in §5 suggested (where it looked like a clean overshoot to +0.057). Equal opportunity diff after mitigation, however, has mean 0.053 with std 0.030 — mean **larger** than std, meaning this one **is** a real, repeatable signal: Reweighing consistently overcorrects equal opportunity in the unprivileged group's favor, not just on this one split. Average odds diff after sits at the noise boundary (mean 0.021, std 0.036).

**Summary of what survives resampling:** the *existence* of baseline bias is robust (all three "before" metrics have means well above their standard deviations). Reweighing's effect on *disparate impact* and *statistical parity* is a robust move to parity on average, even though any single run may land on either side of zero. Its effect on *equal opportunity*, however, is a robust *overcorrection*, not a robust fix — this is the one place where the mitigation's side effect, not just its main effect, is a repeatable finding.

## 7. Fairlearn Cross-Check

AIF360 (after): DI = 1.101, SPD = +0.057.
Fairlearn, naive call (label 1 treated as "selected" — the wrong direction for COMPAS, where favorable = 0): DP difference = 0.057, DP ratio = 0.870.
Fairlearn, corrected (labels recoded so 1 = favorable, matching AIF360's convention): DP difference = 0.057, DP ratio = 0.908.

The DP *difference* matches AIF360's SPD exactly in both the naive and corrected calls (0.057) — expected, since a difference is symmetric up to sign and Fairlearn reports max-minus-min, discarding the sign. The DP *ratio*, however, only reconciles with AIF360 once the direction is corrected, and even then it is not numerically identical to AIF360's disparate impact (0.908 vs. 1.101) because the two libraries define the ratio differently: Fairlearn's `demographic_parity_ratio` is `min(rate)/max(rate)` (always ≤ 1 by construction), while AIF360's disparate impact is specifically `unprivileged_rate/privileged_rate` (can exceed 1, exactly as it does here once the unprivileged group's rate overtakes the privileged group's). Confirming this: 1 / 1.101 = 0.908 — the two numbers are reconciled once the convention difference is accounted for, not contradictory.

## 8. Recommendation

Do not deploy either the baseline or the Reweighing-mitigated model as-is. Before any deployment: (a) re-run this exact stability check (§6) as a required gate, not an optional appendix — a single-split "PASS" on the four-fifths rule is not trustworthy evidence on this dataset, since the resampled mean (0.775) fails it; (b) if Reweighing is kept, explicitly decide and document whether a statistical-parity overcorrection favoring the previously-unprivileged group is an acceptable trade-off for this deployment context, since it is not a "neutral" fix — it is a different, opposite-direction disparity, and equal opportunity does not return to zero; (c) consider testing an in-processing method (Fairlearn's `ExponentiatedGradient` with an equalized-odds constraint, available but commented out in `bias_audit.py`) as an alternative, since this audit's own finding is that a statistical-parity-targeted method does not fix equal opportunity.

## 9. One Honest Limitation

This audit checked only one protected attribute (`race`) with one privileged/unprivileged split, one mitigation method (Reweighing), and one classifier (logistic regression). It did **not** check: intersectional subgroups (e.g., race × sex jointly, where COMPAS's own documented disparities are known to differ from either dimension alone); the `sex` attribute on its own; label validity (whether `two_year_recid` itself is an unbiased ground truth, given well-documented differential arrest rates by race that could affect who gets rearrested independent of true reoffending); or calibration (whether predicted probabilities mean the same thing across groups, a distinct fairness property from any of the four metrics reported here). As the workshop material puts it: you cannot optimize every fairness metric at once — this audit chose statistical parity (via Reweighing) and named that choice; it did not evaluate the others it left on the table beyond what §5–6 already surfaced as side effects.

---

**Files in this folder:**
- `bias_audit.py` — the exact, runnable script that produced every number above (real COMPAS data via AIF360, no synthetic placeholders — unlike `05_pipeline/`, this audit uses real, sensitive human data, appropriately, since it is a fairness *audit* of a well-known public dataset, not a data-collection exercise on new subjects).
- `bias_audit_splits.csv` — per-split raw numbers behind the §6 stability table.
- `before_after_chart.png` — the three parity gaps, before vs. after, visualized.

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used to adapt the course workshop's helper functions into a standalone script and to structure this report. All numbers were produced by actually executing the script against real data — none were estimated or reused from the workshop notebook's own example run. The interpretation of the overshoot, the single-split-vs-resampled-mean discrepancy, and the Fairlearn/AIF360 reconciliation represent the original analytical work of the author. Disclosed in accordance with the Green category AI Use Policy of the course.
