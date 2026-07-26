# Reproducibility Audit Report

## 6.1. Paper Audited

**Keshavamurthy, R., Boutelle, C., Nakazawa, Y., Joseph, H., Joseph, D. W., Dilius, P., Gibson, A. D., & Wallace, R. M. (2024).** Machine learning to improve the understanding of rabies epidemiology in low surveillance settings. *Scientific Reports, 14*, Article 25851. https://doi.org/10.1038/s41598-024-76089-3

**Why this paper:** this is the anchor citation of my own systematic review and protocol (§3.4, §4.5) — it directly justified my choice of XGBoost over logistic regression and my class-imbalance handling strategy (oversampling). Auditing it tells me whether the methodological precedent I am building on is itself reproducible — which turns out to matter (see §6.4).

## 6.2. Reproducibility Scorecard

Scored on seven reproducibility dimensions (seeds, splits, multiple runs, statistical significance, effect size/CI, compute documentation, code & data availability) — Yes / Partial / No — with the exact supporting text quoted from the paper.

| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | **Random seeds reported?** | **No** | No mention of `random_state`, `seed`, or any equivalent anywhere in *Materials and methods*. The stochastic components of the study — ROS/SMOTE resampling, XGBoost's own internal randomness (tree/feature subsampling), and the train/validation split itself — are all seed-sensitive procedures, yet no seed value is given for any of them. |
| 2 | **Data splits described?** | **Partial** | A held-out "validation data" set is referenced ("*the predicted probability cutoff of 0.5 was used to obtain rabies-positive and negative predictions for validation data*" — Table 3 caption), and a 5-fold CV is explicitly described, but only for two narrow purposes: XGB hyperparameter grid search ("*grid search technique with a 5-fold cross-validation split was performed to identify the optimal combination of hyperparameters*") and isotonic probability calibration ("*we applied isotonic regression with a 5-fold cross-validation*"). The split producing the *main* Table 3 metrics (SN, SP, AC, PR-AUC, ROC-AUC, BS) is never described: no split ratio, no split method (random vs. stratified vs. temporal — relevant here, since the data span June 2018–Nov 2023), and no confirmation of whether it is a single split or itself cross-validated. |
| 3 | **Multiple runs (variance reported)?** | **No** | Table 3 reports a single point estimate per model/rebalancing combination (e.g., XGB-ROS: SN=0.95, SP=0.97, AC=0.97, PR-AUC=0.66, ROC-AUC=0.96, BS=0.030). No mean ± std, no repeated-run variability, anywhere in the paper — despite the 5-fold CV machinery already being used elsewhere (item 2), it was never used to report a variance band on the headline metrics. |
| 4 | **Statistical significance test used?** | **No** | Model comparisons are entirely descriptive: *"Overall, XGB had better predictive performance compared to LR"*; *"The XGB-ROS and XGB-SMOTE had the highest SN of 0.95."* No paired test (e.g., McNemar's, paired bootstrap, DeLong's test for AUC) is used to establish whether these differences are statistically distinguishable from noise. |
| 5 | **Effect size / confidence intervals shown?** | **No** | Every metric in Table 3 and Table 4 is a bare point estimate. No CIs anywhere for SN, SP, AC, PR-AUC, ROC-AUC, or BS — not even for the headline 95% claims (e.g., "*confirmed cases = 85.2%*" in the risk-stratification table has no interval, despite n=95 confirmed cases being small enough that a CI would be informative). |
| 6 | **Compute documented?** | **No** | No hardware, runtime, or compute-cost information anywhere. Software versions are given for the language and two packages only ("*Python 3.11.7*"; "*sklearn*"; "*XGBoost*"), which is a partial nod to environment reproducibility, but there is no mention of what hardware the grid search or 13,073-row training pipeline ran on, or how long it took. |
| 7 | **Code & data available?** | **No** | **Data:** "*The datasets used during the current study are available from the corresponding author on reasonable request*" — a request-gated statement, not open access; nobody can independently pull the data to verify results. **Code:** no code availability statement, no repository link, anywhere in the paper. A stranger cannot re-run this study from what is published. |

## 6.3. Overall Reproducibility Score

**1 / 7 items fully met, 1 partial, 5 not met.**

This paper would score poorly on the NeurIPS-style reproducibility checklist (Pineau et al., 2021): it reports *what* was done at a conceptual level (which models, which rebalancing techniques, which metrics) but not *how to redo it* (no seeds, no exact split, no variance, no code, no open data). In plain terms: a stranger with only this paper in hand could not reproduce Table 3's numbers, even approximately.

## 6.4. Relevance to My Own Research

This is the useful and slightly uncomfortable part of the exercise: **this paper is my anchor citation, and it is less reproducible than my own pipeline.**

- My protocol (§3.6, Validation) now specifies fixed seeds, an explicit spatial cross-validation scheme grouped by `block_id`, and PR-AUC + sensitivity-at-fixed-specificity as primary metrics *precisely because* AUC-ROC alone is misleading under class imbalance — a point I took directly from this paper's own PR-AUC-over-ROC-AUC argument (*"PR-AUC was preferred to select the best-performing model in our study as it prioritizes minority class more compared to ROC-AUC"* — citing Ozenne et al., 2015). The irony is that the paper that taught me to prefer PR-AUC does not itself report any variance or CI on its PR-AUC values, so I cannot tell whether XGB-ROS's PR-AUC of 0.66 is meaningfully different from XGB's 0.72 (Table 3) — the difference could easily be within noise.
- This does **not** invalidate using Keshavamurthy et al. (2024) as a methodological precedent — the modeling *choices* (XGB > LR for this problem type, oversampling for rare-event sensitivity, PR-AUC over ROC-AUC) are well-reasoned and consistent with the broader literature (Fernandez et al., 2018; Ozenne et al., 2015, both cited in the paper). What it means is that I should **not** cite this paper's specific numeric results (e.g., "XGB-ROS achieved 0.95 sensitivity") as an established benchmark to beat or match — those numbers have no reported uncertainty, so treating them as precise targets would import the same false optimism that reproducibility audits like this one are meant to catch.
- Practically: my own `05_pipeline` now does what this paper does not — fixed seeds, described spatial splits, PR-AUC and Sens@Spec90 with fold-level variance (mean ± std across 5 folds), and an open, re-runnable dataset generator. I am, on the reproducibility dimension specifically, already ahead of my own anchor reference.

## 6.5. What Would Need to Change for This Paper to Pass a Stranger Test

1. Report the exact train/validation split (ratio, method, and whether it respects the time dimension of the data to avoid temporal leakage).
2. Fix and report random seeds for ROS/SMOTE resampling and for XGBoost's stochastic components.
3. Report variance (mean ± std, or bootstrap CIs) on SN, SP, AC, PR-AUC, ROC-AUC, and BS — the 5-fold CV infrastructure already exists in the paper for other purposes and could be reused for this.
4. Add a formal statistical test (e.g., DeLong's test for AUC/PR-AUC comparisons, or McNemar's for classification agreement) before claiming one model/technique "performed better" than another.
5. Deposit code (even a minimal script) and, where patient-privacy rules allow, a de-identified version of the dataset or a synthetic stand-in — the current "on reasonable request" clause is a known weak form of data availability (cf. Gabelica et al., 2022, on how rarely "available on request" data is actually shared).

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used for structuring this audit report and formatting the scorecard table. The reproducibility assessment itself — reading the paper, identifying which scorecard items are met/partial/unmet, and the connections drawn to my own protocol in §6.4 — represents the original intellectual work of the author, based on direct reading of the audited paper (Keshavamurthy et al., 2024). Disclosed in accordance with the Green category AI Use Policy of the course.
