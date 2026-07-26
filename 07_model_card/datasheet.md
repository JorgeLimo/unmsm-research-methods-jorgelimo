# Datasheet for Dataset: `rabies_data.csv` (synthetic)

Following the structure proposed by Gebru et al. (2021), *Datasheets for Datasets*.

⚠️ **This dataset is entirely synthetic.** It contains no real epidemiological, ecological, or climatic records. It exists to validate reproducibility infrastructure (Git, DVC, MLflow, Docker, spatial cross-validation) ahead of the real CDC-MINSA/SENASA data described in the Data Contingency Plan (`03_protocol/protocol_v0.1.md`, §3.6).

## Motivation

**For what purpose was the dataset created?**
To provide a small, fully reproducible stand-in dataset for the reproducibility-infrastructure pipeline (`05_pipeline/`), so that the Git/DVC/MLflow/Docker stack and the spatial cross-validation strategy could be built, tested, and documented *before* real wild rabies surveillance data is secured — since data access is this project's main bottleneck (§1.5, §3.6 of the protocol).

**Who created it and on whose behalf?**
Jorge Luis Limo Arispe, as part of the UNMSM Doctoral Program in Deep Technologies course "Research Methods and Scientific Integrity in AI." Not created on behalf of any institution; not derived from CDC-MINSA, SENASA, or any other real data holder.

**Who funded the creation of the dataset?**
Not applicable — generated programmatically (`05_pipeline/data/create_dataset.py`), no funding involved.

## Composition

**What do the instances represent?**
Each row is a synthetic "site-observation" with a spatial block assignment, coordinates, and seven feature values — structurally analogous to what a real district-month observation would look like (matching the Unit of Analysis defined in the protocol, §3.6), but with no real-world referent.

**How many instances are there?**
500 rows, evenly split across 10 synthetic spatial blocks (`block_id` 0–9, 50 rows each).

**Does the dataset contain all possible instances, or a sample?**
Not applicable in the usual sense — it is a fixed-size synthetic draw (`n=500`, `np.random.seed(42)`), fully deterministic and regenerable, not a sample of any larger real population.

**What data does each instance consist of?**

| Column | Description |
|---|---|
| `block_id` | Synthetic spatial block (0–9), simulating a district/grid cell — the grouping unit for spatial CV. |
| `lat`, `lon` | Synthetic coordinates jittered around a fixed per-block center within Peru's approximate bounding box. Not real geography. |
| `ndvi` | Uniform random, 0.1–0.9. |
| `temperature` | Uniform random, 18–32 °C. |
| `precipitation` | Uniform random, 50–400 mm. |
| `forest_loss` | Uniform random, 0–1. |
| `bat_occurrence` | Uniform random integer, 0–9. |
| `population_density` | Uniform random, 1–500. |
| `dist_to_forest` | Uniform random, 0–50 km. |
| `target` | Uniform random binary (0/1), ~50/50 balanced. **Generated independently of every feature above** — there is no encoded relationship for a model to learn, by design. |

**Is any information missing from individual instances?**
No — the generator produces complete rows with no missing values, by construction.

**Are relationships between instances made explicit?**
Yes: `block_id` groups rows into 10 disjoint spatial units; `lat`/`lon` are consistent with each row's assigned block center. No other instance-to-instance relationships exist (e.g., no temporal ordering, no repeated-subject structure).

**Are there recommended data splits?**
Yes — `GroupKFold` (5 folds) grouped by `block_id`, as implemented in `05_pipeline/src/train.py`, ensuring no spatial block is split across train and test.

**Are there errors, sources of noise, or redundancies?**
The entire dataset is "noise" by design with respect to `target` — this is the intended sanity-check property (see Model Card, §Training Data), not a defect for this exercise. It would be a defect if mistaken for real predictive data.

**Does the dataset contain confidential data or data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?**
No — fully synthetic, no real individuals, animals, or locations.

## Collection Process

**How was the data associated with each instance acquired?**
Not collected — generated programmatically via `numpy.random`, with a fixed seed (`np.random.seed(42)`) for full determinism. Anyone can regenerate an identical file by running `python3 data/create_dataset.py`.

**Over what timeframe was the data collected?**
Not applicable — generated in a single script execution (July 2026); no real-world collection period.

## Preprocessing, Cleaning, and Labeling

**Was any preprocessing/cleaning/labeling of the data done?**
No preprocessing beyond generation — the raw generator output is used as-is by `train.py`, which itself performs the actual preprocessing (`StandardScaler`, fit on the training fold only, per Rule 1 documented in the pipeline README).

## Uses

**Has the dataset been used for any tasks already?**
Yes — exclusively to validate the reproducibility pipeline (`05_pipeline/`): confirming that Git + DVC + MLflow + Docker + spatial `GroupKFold` work end-to-end, and that a stranger can reproduce the exact reported metrics from a fresh clone.

**Is there anything about the composition of the dataset or the way it was collected that might impact future uses?**
Critically, yes: because `target` has no engineered relationship to any feature, **this dataset must never be used to draw any conclusion about wild rabies risk, real feature importance, or real model performance.** Any resemblance between a trained model's behavior on this data and real epidemiological patterns would be coincidental.

**Are there tasks for which the dataset should not be used?**
Any operational, publication-facing, or decision-support use. It should not be cited outside the context of this reproducibility exercise.

## Distribution

**How is the dataset distributed?**
Version-controlled via DVC (`data/rabies_data.csv.dvc` pointer, tracked in Git); the underlying data file is regenerable by anyone from `create_dataset.py`, which is the practical distribution mechanism today (see the DVC remote note below).

**Is there a license?**
MIT, matching the repository license (`02_PROJECT_BRIEF.pdf`).

## Maintenance

**Who maintains the dataset?**
Jorge Luis Limo Arispe, as part of this repository.

**Will the dataset be updated?**
Yes — it will be **replaced entirely**, not incrementally updated, once real CDC-MINSA/SENASA records are secured (per the Data Contingency Plan). At that point this datasheet must be rewritten from scratch, since almost every answer above (real vs. synthetic identity, collection process, confidentiality, appropriate uses) changes.

⚠️ **Known limitation carried over from the pipeline README:** the DVC remote currently points to a local folder on the author's machine, not a shared location. This is acceptable for this synthetic, seed-regenerable dataset (see `05_pipeline/README.md`), but will become a hard requirement to fix once real, non-regenerable data replaces it — a real dataset cannot be "regenerated with a fixed seed" by a stranger, so a shared remote will be the only way to satisfy this datasheet's own distribution claims.

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used for structuring this datasheet against the Gebru et al. (2021) template and for grammar/style editing. All descriptions of the dataset's actual composition and generation process represent the original work of the author, based on the actual `create_dataset.py` script in this repository. Disclosed in accordance with the Green category AI Use Policy of the course.
