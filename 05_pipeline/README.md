# 05_pipeline — Reproducible ML Pipeline

Session 5 deliverable: a fully reproducible machine learning pipeline (Git + DVC + MLflow + Docker) validating the reproducibility infrastructure for the doctoral research on wild rabies transmission risk in Peru.

> ⚠️ **SYNTHETIC PLACEHOLDER DATA.** All results below were generated using a simulated dataset (`data/rabies_data.csv`). They validate the *infrastructure* (Git/DVC/MLflow/Docker, spatial cross-validation, seed handling) and must **never** be read as real epidemiological model performance. Real CDC-MINSA / SENASA georeferenced records will replace this dataset once data access is secured (see `03_protocol/` for the data contingency plan).

## Dataset

`data/rabies_data.csv` (500 rows, synthetic):

| Column | Description |
|---|---|
| `block_id` | **Synthetic spatial block** (0–9), simulating districts / grid cells. Used as the grouping unit for spatial CV. **Not real geography.** |
| `lat`, `lon` | Synthetic coordinates within Peru's approximate bounding box, generated around each block's center. **Not real geography.** |
| `ndvi`, `temperature`, `precipitation`, `forest_loss`, `bat_occurrence`, `population_density`, `dist_to_forest` | Synthetic environmental/epidemiological features (signal-free — generated independently of `target`) |
| `target` | Binary outcome (synthetic, ~50/50 balanced — real rabies data will be far more imbalanced) |

Tracked via DVC (`data/rabies_data.csv.dvc`); pull with `dvc pull` before running.

## Reproducibility Stack

| Layer | Tool | Implementation |
|---|---|---|
| Code versioning | Git + GitHub | Commit history tracks every methodological change |
| Data versioning | DVC | `rabies_data.csv` tracked via pointer file, remote configured |
| Spatial CV | scikit-learn `GroupKFold` | 5 folds grouped by `block_id`, no row split across blocks |
| Seeded training | Python | 5 seeds fixed (13, 21, 42, 87, 100); split before scaling |
| Experiment tracking | MLflow 3.1.4 | Runs logged with params + metrics per seed, per model |
| Environment | `requirements.txt` + `Dockerfile` | All versions pinned |
| Documentation | This README | Stranger test passed across two independent machines/OS |

## Training Script (`src/train.py`)

Two models are run per seed, both evaluated with the same spatial 5-fold split:

### `logreg` — deterministic baseline
`LogisticRegression(solver='lbfgs', C=1.0, max_iter=1000)`. **Important and intentional**: because `GroupKFold` has no `random_state` (fold assignment is fixed by the spatial blocks) and logistic regression with `lbfgs` is a deterministic convex optimizer, **results are identical across all five seeds**. This is not a bug — it is a direct, documented consequence of combining a fixed spatial split with a model that has a single global optimum.

### `random_forest` — seed-sensitive comparison model
`RandomForestClassifier(n_estimators=100)`. Bootstrap row sampling and random feature subsetting at each split genuinely depend on `random_state`, so this model **does** show real seed-to-seed variance — used here to demonstrate the seed-sensitivity check expected in this session, since `logreg` alone could no longer demonstrate it once spatial blocking was introduced.

### Reproducibility rules implemented
- **Rule 1 — split before scaling**: `StandardScaler` is fit only on the training fold, preventing test-fold leakage into preprocessing.
- **Rule 2 — fixed seeds**: all five seeds (13, 21, 42, 87, 100) are passed explicitly via `--seed`.
- **Rule 3 — spatial blocking**: `GroupKFold` on `block_id` prevents spatial leakage between neighboring locations (Meyer et al., 2019).

## Experiment Results

5-fold spatial cross-validation, mean ± std across folds, logged in MLflow under experiment `rabies-risk-pipeline`:

| Seed | Model | AUC-ROC | PR-AUC | Sens@Spec90 | Accuracy |
|---|---|---|---|---|---|
| 13 / 21 / 42 / 87 / 100 | `logreg` | 0.4611 ± 0.0390 | 0.4949 ± 0.0250 | 0.0925 | 0.4724 |
| 13 | `random_forest` | 0.4518 ± 0.0686 | 0.4792 ± 0.0428 | 0.0699 | 0.4623 |
| 21 | `random_forest` | 0.4259 ± 0.0499 | 0.4672 ± 0.0334 | 0.0610 | 0.4439 |
| 42 | `random_forest` | 0.4329 ± 0.0421 | 0.4641 ± 0.0260 | 0.0568 | 0.4560 |
| 87 | `random_forest` | 0.4426 ± 0.0585 | 0.4768 ± 0.0478 | 0.0665 | 0.4630 |
| 100 | `random_forest` | 0.4537 ± 0.0713 | 0.4906 ± 0.0523 | 0.0849 | 0.4604 |

**Reading these numbers**: AUC-ROC ≈ 0.43–0.52 (no model meaningfully better than chance) is *expected and correct* on signal-free synthetic data. It is a sanity check confirming the pipeline has no data leakage — not a measure of real predictive ability. `logreg` is identical across all seeds by mathematical construction (see above); `random_forest` varies, demonstrating genuine seed sensitivity.

## Stranger Test (Reproducibility Verification)

The pipeline was independently re-run by cloning the repository into a fresh environment, pulling data via `dvc pull`, and re-executing `src/train.py` for all five seeds. Verified across **two independent machines/environments** (different Python/scikit-learn installations): the exact same per-fold and per-seed metrics were reproduced both times, confirming the pipeline meets the course's reproducibility standard.

A `RuntimeWarning` (`divide by zero` / `overflow in matmul`) appears on at least one environment running an older scikit-learn build, during `logreg` fitting on near-zero-signal synthetic data. This does **not** affect the final reported metrics — verified identical across both environments — and is noted here per the course's "compute reproducibility challenges" guidance (Pineau et al., 2021) rather than hidden.

## Running the pipeline

```bash
cd 05_pipeline
source ../venv/bin/activate   # or your own virtual environment
pip install -r requirements.txt
dvc pull
for seed in 13 21 42 87 100; do
  python3 src/train.py --seed $seed
done
```

## References

- Meyer, H., et al. (2019). Importance of spatial predictor variable selection in machine learning applications. *Ecological Modelling*, 411, 108815.
- Keshavamurthy, R., et al. (2024). Machine learning to improve the understanding of rabies epidemiology in low surveillance settings. *Scientific Reports*, 14, 25851.
- Pineau, J., et al. (2021). Improving Reproducibility in Machine Learning Research. *JMLR*, 22(164), 1-20.
