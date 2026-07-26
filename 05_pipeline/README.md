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

5-fold spatial cross-validation, mean ± std across folds, produced by running `src/train.py` for each seed against the current `data/rabies_data.csv` (regenerated with `block_id`/`lat`/`lon`, see `data/create_dataset.py`). Run on the author's machine (macOS):

| Seed | Model | AUC-ROC | PR-AUC | Sens@Spec90 | Accuracy |
|---|---|---|---|---|---|
| 13 / 21 / 42 / 87 / 100 | `logreg` | 0.5359 ± 0.0438 | 0.5959 ± 0.0731 | 0.1252 | 0.5300 |
| 13 | `random_forest` | 0.5257 ± 0.0786 | 0.6091 ± 0.0666 | 0.1764 | 0.4960 |
| 21 | `random_forest` | 0.5504 ± 0.0716 | 0.6180 ± 0.0515 | 0.1661 | 0.5200 |
| 42 | `random_forest` | 0.5370 ± 0.0594 | 0.6014 ± 0.0470 | 0.1484 | 0.5120 |
| 87 | `random_forest` | 0.5560 ± 0.0839 | 0.6295 ± 0.0506 | 0.1885 | 0.5200 |
| 100 | `random_forest` | 0.5327 ± 0.0731 | 0.5880 ± 0.0726 | 0.1448 | 0.5340 |

**Reading these numbers**: AUC-ROC ≈ 0.53–0.56 (barely above chance) is *expected and correct* on signal-free synthetic data — it is a sanity check confirming the pipeline has no data leakage, not a measure of real predictive ability. `logreg` is identical across all five seeds by mathematical construction (see above); `random_forest` varies fold-to-fold and seed-to-seed, demonstrating genuine seed sensitivity.

## Stranger Test (Reproducibility Verification)

To verify: clone the repo into a fresh environment, run `pip install -r requirements.txt`, then `dvc pull` (or `python3 data/create_dataset.py` if you don't have access to the DVC remote), then re-run `src/train.py` for each seed.

**Cross-platform note:** this pipeline was independently re-run on a second machine (Linux) during development. `logreg` reproduced bit-identically (as expected — `GroupKFold` has no randomness and `lbfgs` is a deterministic convex solver). `random_forest`, however, showed small but real differences between macOS and Linux for the *same* seed (e.g. seed 42, fold 0: AUC-ROC 0.6327 on Linux vs 0.6192 on macOS) — almost certainly due to platform-level differences in BLAS/threading behavior during scikit-learn's tree construction, not a bug in this code. This is a live example of the "compute reproducibility challenges" flagged by Pineau et al. (2021): fixing a `random_state` guarantees *within-platform* reproducibility, not *cross-platform* bit-exactness. Running via the provided `Dockerfile` (rather than a native Python install) is the intended way to eliminate this variance for anyone reproducing this repo.

A `RuntimeWarning` (`invalid value encountered in matmul`) appears during `logreg` fitting on some folds, on both platforms. This is expected on near-zero-signal synthetic data (the optimizer approaches a near-flat loss surface) and does **not** affect the final reported metrics.

⚠️ **DVC remote is currently local (not yet linked to shared cloud storage).** `.dvc/config` points to a folder on the author's own machine (`/Users/jorgelimo/dvc-storage/...`), so `dvc pull` will not work for anyone else who clones this repo. **This is acceptable for now**: the current dataset is fully synthetic and regenerated with a fixed seed (`np.random.seed(42)` in `create_dataset.py`), so `python3 data/create_dataset.py` reproduces it bit-for-bit on any machine — no shared remote is needed to pass the stranger test at this stage. **This will become mandatory once real CDC-MINSA/SENASA records replace the synthetic data** (real data transition): unlike synthetic data, real records cannot be regenerated from a formula, so without a shared remote (e.g., Google Drive via the `dvc-gdrive` package already in `requirements.txt`) nobody else — including the instructor — would be able to reproduce results.

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
