# Model Card

Following the structure proposed by Mitchell et al. (2019), *Model Cards for Model Reporting*.

## Model Details

- **Developed by:** Jorge Luis Limo Arispe, UNMSM Doctoral Program in Deep Technologies.
- **Date:** July 2026.
- **Model type:** Two binary classifiers evaluated in parallel — (1) Logistic Regression (`sklearn.linear_model.LogisticRegression`, `solver='lbfgs'`, `C=1.0`) and (2) Random Forest (`sklearn.ensemble.RandomForestClassifier`, `n_estimators=100`).
- **Training procedure:** 5-fold spatial cross-validation (`GroupKFold` grouped by `block_id`), features standardized with `StandardScaler` fit on the training fold only (§Rule 1, `05_pipeline/src/train.py`).
- **License:** MIT (per `02_PROJECT_BRIEF.pdf` / repo README).
- **Repository / contact:** https://github.com/JorgeLimo/unmsm-research-methods-jorgelimo — corresponding author via course platform.
- **Citation:** this repository, `05_pipeline/`.

⚠️ **This is not the doctoral research model.** It is a reproducibility-infrastructure exercise: a placeholder pipeline built to validate Git + DVC + MLflow + Docker before real CDC-MINSA/SENASA data is available (see Data Contingency Plan, `03_protocol/protocol_v0.1.md` §3.6, and the pipeline itself, `05_pipeline/`). Everything below describes *this placeholder model*, not the future doctoral model.

## Intended Use

- **Primary intended use:** demonstrate a working, seed-controlled, spatially-aware reproducibility pipeline that the real doctoral model will later reuse unchanged, once real epidemiological records replace the synthetic dataset.
- **Primary intended users:** the author, course instructor, and any peer reviewer verifying the reproducibility claims in `05_pipeline/README.md`.
- **Out-of-scope uses:** any operational or decision-support use (e.g., actually estimating wild rabies risk for a real location) is explicitly out of scope. The model is trained on signal-free synthetic data and has no real predictive validity — see Training Data below.

## Factors

- **Relevant factors:** the two models are compared against each other (logreg vs. random_forest) and, within random_forest, across five seeds (13, 21, 42, 87, 100) to characterize seed sensitivity — not across any real-world demographic or geographic factor, since none of the input variables correspond to real places or populations.
- **Evaluation factors:** the 10 synthetic `block_id` groups (simulating spatial units) are the only stratification factor evaluated, via `GroupKFold`.

## Metrics

- **Reported:** AUC-ROC, PR-AUC, sensitivity at 90% specificity (Sens@Spec90), and accuracy — mean ± std across the 5 spatial folds, per seed (`05_pipeline/README.md`, Experiment Results table).
- **Why these and not just accuracy/AUC-ROC:** per the Data Contingency and Validation sections of the protocol (§3.6), wild rabies is a rare-event problem; AUC-ROC alone is known to look optimistic under class imbalance, so PR-AUC and Sens@Spec90 are reported as primary, with AUC-ROC kept only for comparability with the working hypothesis's AUC-ROC ≥ 0.80 target.
- **Decision thresholds:** none applied yet — the current exercise reports ranking/probability-quality metrics, not a deployed classification threshold.

## Evaluation Data & Training Data

**Both evaluation and training data come from the same synthetic source** (`05_pipeline/data/create_dataset.py`), so this section covers both:

- 500 synthetic rows, 10 spatial blocks (`block_id`, 50 rows each), features generated independently and uniformly at random (`ndvi`, `temperature`, `precipitation`, `forest_loss`, `bat_occurrence`, `population_density`, `dist_to_forest`) and a synthetic 50/50-balanced binary `target` with **no engineered relationship to the features** — by design, so that near-chance performance (AUC-ROC ≈ 0.53–0.56, see README) is the *expected, correct* result, serving as a leakage sanity check rather than a measure of predictive skill.
- Full provenance, generation code, and column-by-column description are in the Datasheet (`07_model_card/datasheet.md`) — this Model Card intentionally does not duplicate that detail (see Gebru et al., 2021, on keeping Model Cards and Datasheets as complementary, non-redundant documents).

## Quantitative Analyses

See `05_pipeline/README.md` Experiment Results table for the full per-seed, per-model breakdown (unitary results only — no intersectional analysis applies here, since there is no real demographic dimension in synthetic data).

**Cross-platform finding worth flagging here too:** `random_forest` metrics showed small but real differences when the exact same seed was re-run on macOS vs. Linux (e.g., seed 42, fold 0: AUC-ROC 0.6327 on Linux vs. 0.6192 on macOS), while `logreg` was bit-identical across platforms. This is documented in the pipeline README as a live example of "compute reproducibility challenges" (Pineau et al., 2021) and is relevant to this Model Card because it means the exact numbers reported are platform-dependent for the random_forest model specifically — a caveat a model card is meant to surface.

## Ethical Considerations

- No real individuals, animals, or locations are represented in the training or evaluation data — the synthetic nature of the dataset removes the standard privacy/fairness concerns a real epidemiological rabies model would raise (those are addressed separately for the *future* real-data model in the Ethics Protocol, `09_ethics/`, and Data Management Plan, `10_data_mgmt/`).
- The one ethical property this exercise *does* carry forward: honest labeling. Reporting near-chance metrics as "near-chance, as expected" rather than omitting them or reframing them favorably is itself a small scientific-integrity practice — the same principle that governs how AI assistance is disclosed throughout this repository (see the AI Assistance Disclosure at the end of this document).

## Caveats and Recommendations

- **Do not cite these numbers as predictive performance** — they measure pipeline correctness (no leakage, correct spatial grouping, working seed control), not rabies-risk predictive skill.
- **Do not compare these numbers to Keshavamurthy et al. (2024)'s Table 3** (audited in `06_repro_audit/`) — different data, different purpose; any surface-level similarity in metric names is coincidental.
- Before the real-data model is trained, this Model Card must be re-written from scratch: real training/evaluation data description, real intended use (early-warning decision support for SENASA/CDC-MINSA), real factors (region, species, season), and a full fairness analysis across regions with historically unequal surveillance coverage (flagged as a risk in the Paradigm Justification, §1.5, and the Ethical Considerations of the protocol, §3.7).

## Discussion — Would Preregistration Work for This Research?

Yes, largely — and parts of it already function like an informal preregistration. The protocol (`03_protocol/protocol_v0.1.md`) already fixes, before any real data is seen: the specific algorithms to compare (RF, XGBoost, LSTM), the primary validation strategy (spatial cross-validation), the primary metrics given the known class imbalance (PR-AUC, Sens@Spec90, with AUC-ROC ≥ 0.80 as a working hypothesis threshold), and the unit of analysis and positive-class definition (district-month). Committing to these choices *before* seeing CDC-MINSA/SENASA data is exactly what a formal preregistration (e.g., via OSF) would require, and it protects against two well-documented failure modes in ML research: HARKing (hypothesizing after results are known — picking whichever metric or threshold makes the model look best post hoc) and multiple-comparisons inflation (silently trying many model/feature/threshold combinations and reporting only the best one), both of which are easier to fall into precisely because rare-event, imbalanced problems like this one offer many degrees of freedom in how "success" gets defined.

Where preregistration would be harder to apply rigidly: the exploratory feature-engineering step (which specific NDVI window, which climatic lag, which land-use variables end up mattering) is genuinely data-dependent and may need to be partly exploratory once real records arrive — a fully locked preregistration would either have to accept a coarser, less-informed initial feature set, or explicitly separate a preregistered "confirmatory" model (the one used for the AUC-ROC ≥ 0.80 hypothesis test) from a labeled "exploratory" analysis (feature importance via SHAP, used to *generate* hypotheses for future work, not to test this one). That confirmatory/exploratory split is the standard way registered-report-style ML studies handle this tension, and it would fit this project without much friction, given the protocol already separates "Expected Results" (confirmatory) from open research questions (exploratory) in §3.5 and §3.8.

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used for structuring this Model Card against the Mitchell et al. (2019) template and for grammar/style editing. All technical descriptions of the pipeline, the choice of what to disclose as limitations, and the preregistration discussion represent the original work of the author, based on the actual pipeline in this repository. Disclosed in accordance with the Green category AI Use Policy of the course.
