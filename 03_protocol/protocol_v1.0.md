# Complete Research Protocol Draft (v1.0)

UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS — Faculty of Systems Engineering and Computer Science — Graduate Unit
*Predictive Model for Zoonotic Transmission Risk of Wild Rabies in Wildlife-Human Contact Zones Using Machine Learning with a One Health Approach in Peru*
Ing. Jorge Luis Limo Arispe — Lima, Perú, 2026

---

## Front Matter — AI Use Disclosure

Per the Session 13 instruction to bring every deliverable produced since Session 1 into this draft, "including today's policy — it goes in the front matter":

This protocol was prepared with AI assistance (Claude, Anthropic) under the Green/Amber/Red framework detailed in my Personal AI Use Policy (`12_integrity/ai_use_policy.md`), which is incorporated by reference. For Sessions 1–5 (this document's §1–§6 core content), I supplied first drafts and used AI primarily for outlining, grammar, and structural editing. For Sessions 6–12 (the reproducibility audit, model card/datasheet, ethics protocol, data management plan, bias audit, and integrity materials referenced throughout this draft), the pattern of use was more substantial: I supplied source materials — papers, my own prior drafts, data I generated and ran myself — and AI produced analytical prose directly from them, which I then reviewed and accepted. Whether that pattern is best described as Green ("outlining") or Amber ("paragraph-level drafting beyond editing my own draft") is a classification I am actively clarifying with the instructor, since a more precise description of the actual workflow may change an earlier informal assessment. I am disclosing this openly here, rather than waiting for that clarification to conclude, consistent with my own policy's RED-line commitment to never present AI-assisted output without disclosure.

---

## 1. Title

Predictive Model for Zoonotic Transmission Risk of Wild Rabies in Wildlife-Human Contact Zones Using Machine Learning with a One Health Approach in Peru.

## 2. Abstract

Wild rabies transmitted by *Desmodus rotundus* is the leading cause of human and bovine rabies mortality in Peru. Current surveillance is predominantly reactive, with no integrated predictive system combining ecological, climatic, and epidemiological data. This research develops and validates a machine learning-based predictive model — comparing Random Forest, XGBoost, and LSTM — trained on open-source georeferenced data (2010–2024) under the One Health framework, instantiated as a functional early warning prototype for SENASA and CDC-MINSA. The study is built on a fully reproducible infrastructure (Git, DVC, MLflow, Docker; `05_pipeline/`), governed by an explicit ethics protocol and data management plan (`09_ethics/`, `10_data_mgmt/`), and informed by a pre-deployment bias-audit discipline established through hands-on practice on a real fairness benchmark (`11_bias_audit/`). The expected contribution is a reproducible, open-source One Health risk index applicable to other priority zoonoses in the Amazon basin.

## 3. Introduction & Problem Statement

### Problem Statement

Wild rabies in Peru represents an active and underestimated public health threat. Between 1990 and 2019, 57% of 399 reported human rabies cases corresponded to wild transmission. Two new cases were confirmed in the Amazonas region in 2024. The surveillance system is predominantly reactive. Three structural factors converge: accelerated deforestation of the Peruvian Amazon, expansion of the agricultural and livestock frontier, and the absence of an integrated early warning system articulating spatial distribution of the reservoir, climatic variables, land use, and historical epidemiological records.

### Relevance — The "So What?" Test

This research directly addresses the gap between the documented epidemiological burden of wild rabies in Peru and the non-existence of AI-based predictive tools integrating ecological, climatic, and epidemiological data under the One Health framework. Results will enable SENASA and CDC-MINSA to target vaccination and surveillance resources in highest-risk zones identified by the model, benefiting Amazonian native communities and Andean rural populations with limited access to health services. The open-source model and software will be replicable for leptospirosis, leishmaniasis, and avian influenza across the Amazon basin.

## 4. Literature Review

Keshavamurthy et al. (2024) compared XGBoost and logistic regression for predicting rabies probability using case-history and clinical-sign data in a low-surveillance setting (Haiti), finding XGBoost achieved superior sensitivity and PR-AUC after addressing class imbalance with oversampling — directly informing the algorithm selection and imbalance-handling strategy for the present study. A dedicated reproducibility audit of this anchor paper (`06_repro_audit/reproducibility_audit.md`) found it does not report seeds, exact splits, or result variance — a limitation that directly shaped this protocol's own Validation subsection below, since I chose not to repeat that gap in my own methodology. Benavides et al. (2020) demonstrated that human rabies by *D. rotundus* follows river corridors and deforestation patterns in Colombia and Peru, validating the integration of land use variables and spatial distribution of the reservoir as essential predictors. Blackwood et al. (2013) established that immigration rates between bat colonies and population density are fundamental variables to explain transmission dynamics. Plowright et al. (2017) showed that land use changes and habitat loss are the main drivers of increased contact rates between wildlife reservoirs and human populations. Meyer et al. (2019) proposed spatial cross-validation as the appropriate evaluation strategy for geospatial ML models.

## 5. Research Questions / Hypotheses

### General Research Question

To what extent can a machine learning model, trained on epidemiological, ecological, and climatic data from open public sources, accurately estimate the spatio-temporal risk of zoonotic wild rabies transmission in wildlife-human contact zones in Peru under the One Health framework?

### Specific Research Questions

- Which ecological, climatic, and socioeconomic variables show the strongest association with wild rabies outbreaks in Amazonian and Andean regions of Peru during 2010–2024?
- Which supervised ML algorithm (Random Forest, XGBoost, or LSTM) achieves the best predictive performance as measured by AUC-ROC and sensitivity metrics?
- How does the spatial variation of wild rabies transmission risk relate to forest cover loss and expansion of the agricultural frontier in Peru?
- Can a functional early warning prototype demonstrate sufficient utility and usability for decision-makers at SENASA and CDC-MINSA?

### Working Hypothesis

A supervised ML model integrating *D. rotundus* spatial distribution, deforestation indices (NDVI, forest cover change), climatic variables (temperature, precipitation), and historical epidemiological records will achieve an AUC-ROC ≥ 0.80, outperforming classical logistic regression models and demonstrating geographic generalizability through spatial cross-validation.

## 6. Methodology

### Research Paradigm

Computational / Quantitative Empirical paradigm with a Design Science Research component (full justification: `01_paradigm/paradigm_justification.md`; method selection against two alternatives: `02_method/method_fit_matrix.md`).

### Data Sources

- **Epidemiological:** CDC-MINSA wild rabies case registry and SENASA bovine rabies surveillance (2010–2024).
- **Reservoir distribution:** *D. rotundus* georeferenced occurrence records from GBIF and IUCN Red List.
- **Environmental:** NDVI and forest cover change from MODIS/Landsat (MapBiomas, Global Forest Watch, Hansen et al., 2013).
- **Climatic:** Temperature and precipitation from SENAMHI and WorldClim v2.1.
- **Socioeconomic:** Population density, land use, health access indices from INEI and MINAM.

### Algorithms

Three supervised ML algorithms: Random Forest (robust ensemble, interpretable via variable importance); XGBoost (regularized gradient boosting, superior on heterogeneous tabular data); LSTM (recurrent neural network for long temporal dependencies in outbreak series).

### Unit of Analysis & Positive Class Definition

Given that wild rabies transmission events are rare, the unit of analysis is defined as **district-month** (a Peruvian administrative district observed within a given calendar month, 2010–2024). The **positive class** is defined as: at least one confirmed human or bovine wild rabies case attributed to *D. rotundus* transmission reported by CDC-MINSA/SENASA for that district-month; all other district-months are labeled negative. This resolution is fine enough to capture spatial and seasonal risk signal while remaining coarse enough for reliable matching with monthly ecological/climatic covariates.

### Validation

Spatial cross-validation (Meyer et al., 2019) dividing data into contiguous geographic blocks, grouped by district to prevent spatial leakage between neighboring units. Because positive district-months are expected to be rare relative to the total (severe class imbalance), AUC-ROC alone can look misleadingly optimistic and is not sufficient on its own. Primary metrics: Precision-Recall AUC (PR-AUC) and sensitivity at a fixed specificity of 90% (Sens@Spec90), both robust to class imbalance. Reported for comparability: AUC-ROC (target ≥ 0.80), specificity, F1-score, Brier score. SHAP values for variable importance and interpretability. **Fixed seeds, an exact, documented train/test split procedure, and reported result variance across seeds are non-negotiable parts of this plan** — the specific gap identified when this same standard was applied to my own anchor citation (`06_repro_audit/`) and is already implemented and tested on placeholder data (`05_pipeline/`, five seeds, mean ± std per fold).

### Reproducibility & Documentation Plan

A fully reproducible pipeline (Git + DVC + MLflow + Docker) has already been built and stress-tested on synthetic placeholder data — including a real "stranger test" (fresh-clone, dependency install, and re-run) and a documented cross-platform finding that tree-based model results vary slightly between macOS and Linux even with fixed seeds, which will be re-verified once real data arrives (`05_pipeline/README.md`). A Model Card (Mitchell et al., 2019) and Datasheet (Gebru et al., 2021) already document the placeholder model and dataset (`07_model_card/`) and will be rewritten from scratch, not incrementally patched, once real CDC-MINSA/SENASA data replaces the synthetic placeholder — since almost every entry in those documents (data provenance, confidentiality status, appropriate use) changes with that transition.

### Fairness & Bias Audit Plan

Before any prototype is presented to SENASA/CDC-MINSA for decision support, the model will undergo a bias audit modeled on the methodology practiced in `11_bias_audit/`: measuring group-fairness gaps (disparate impact, statistical parity, equal opportunity, average odds) across regions with historically unequal surveillance coverage, applying a mitigation method if a gap is found, and — critically — **re-checking any result across multiple resampled train/test splits before trusting it**, since the hands-on audit exercise on COMPAS demonstrated directly that a single split's "pass" on a fairness threshold (0.820, above the four-fifths rule) did not survive resampling (mean 0.775 across 10 splits, a fail) — a single-split fairness claim on this project's own real model will not be accepted internally without the same stability check.

### Data Contingency Plan

Access to complete, national-scale CDC-MINSA and SENASA wild rabies case records is the primary bottleneck of this research. Rather than letting this single point of failure delay the whole timeline, the following contingency plan applies:

**Trigger:** If, by Month 4, formal data-sharing agreements with CDC-MINSA and/or SENASA are not yet signed — or preliminary records show large gaps (e.g., more than 30% of districts in the target region lack usable monthly records for 2010–2024) — the study scope falls back to the regional pilot below instead of stalling.

**Fallback — regional pilot:** Restrict the initial predictive model to the **Amazonas region**, which already has confirmed 2024 wild rabies cases documented and is a SENASA priority surveillance zone with comparatively better historical reporting than the national average. The model is validated at regional scale first and extended nationally as additional departments' records become available, reusing the same reproducible pipeline.

**Unaffected by this bottleneck:** Environmental and reservoir-distribution layers are all open-access and not subject to institutional approval delays. Feature engineering and the reproducibility pipeline can therefore proceed on schedule regardless of epidemiological data access status.

## 7. Ethical Considerations

Full protocol: `09_ethics/ethics_protocol.md`. Summary of the governing commitments:

This is a **secondary analysis of existing administrative surveillance data**, not direct human-subjects research — no individuals are recruited, interviewed, or sampled. Because re-contacting the subjects of historical case records is impracticable, this protocol requests a **waiver of individual informed consent** from the UNMSM ethics committee, justified by aggregation to the district-month unit of analysis (which limits re-identification exposure), the impracticability of re-contact, and the substantial public-health benefit relative to the incremental risk. Because a large share of the affected population is Amazonian and Andean, including indigenous communities, this protocol also commits to **community-level consultation under the CARE Principles** (Carroll et al., 2020) before any prototype deployment — individual consent waivers do not substitute for collective consultation.

Key risks identified and mitigated: re-identification via small cell counts (mitigated by the anonymization strategy below); community stigmatization from "high-risk zone" labeling (mitigated by framing outputs as internal resource-prioritization inputs, not public labels); biased model performance across historically under-monitored regions, reproducing the same surveillance gap the model aims to fix — the COMPAS lesson applied directly to this research (`09_ethics/ethics_protocol.md` §9.11) and the reason the Fairness & Bias Audit Plan above exists; and dual-use risk, where a "low-risk" classification could be misread as justification to reduce investment in an under-monitored (not genuinely low-risk) area.

Legal and institutional framework: Belmont Report principles (respect, beneficence, justice); Peru's Ley N° 29733 (Personal Data Protection) and Ley N° 31814 (AI Promotion Law); CONCYTEC's Código Nacional de Integridad Científica; UNMSM ethics committee review prior to any fieldwork or prototype deployment.

## 8. Expected Results

- Integrated, georeferenced database of wild rabies cases, *D. rotundus* distribution, climatic variables, vegetation indices, and land use for Peru 2010–2024, deposited following FAIR principles and anonymized per the Data Management Plan (`10_data_mgmt/data_management_plan.md`: aggregation with k≥5 small-cell suppression, differential privacy on any public-facing risk map).
- Identification of variables most associated with wild rabies outbreaks via SHAP analysis.
- Validated predictive model (best of RF, XGBoost, LSTM) achieving AUC-ROC ≥ 0.80 with geographic generalizability, reported alongside PR-AUC, Sens@Spec90, and result variance across seeds — not a single point estimate.
- A completed bias audit of the final model, with before/after mitigation metrics and a resampling-based stability check, prior to any deployment recommendation to SENASA/CDC-MINSA.
- A Model Card and Datasheet for the final (real-data) model, rewritten from the current placeholder versions.
- Functional early warning prototype with dynamic risk maps for SENASA and CDC-MINSA.
- Open-source software package (Python, MIT License) replicable to other Amazon basin zoonoses.
- At least one manuscript prepared for submission to an indexed international journal.

## 9. Timeline & Budget

### Preliminary Timeline (36 months)

- **Month 1:** Submit formal data-access requests to CDC-MINSA and SENASA in parallel with (not after) the UNMSM ethics committee submission. Begin acquisition of open-access environmental/climatic/reservoir layers, which do not depend on that access.
- **Months 1–4:** Ethics approval process continues; open-access layers integrated regardless of epidemiological data status.
- **Month 4 — Go/no-go checkpoint:** If national-scale CDC-MINSA/SENASA access is not yet confirmed, activate the fallback and restrict initial scope to the Amazonas regional pilot.
- **Months 4–6:** Epidemiological data integration and database quality control.
- **Months 7–12:** Exploratory data analysis, feature engineering, baseline model, spatial cross-validation setup.
- **Months 13–20:** Development, training, and comparison of RF, XGBoost, LSTM; SHAP analysis; reproducibility pipeline finalized on real data.
- **Months 20–21:** Bias audit and Model Card/Datasheet rewrite for the real-data model, prior to any prototype demonstration.
- **Months 21–26:** Early warning prototype design, development, and usability evaluation with SENASA/CDC-MINSA, including the CARE-aligned community consultation in the pilot region.
- **Months 27–32:** Manuscript writing, peer review, open-source software release.
- **Months 33–36:** Doctoral thesis writing, internal review, and final defense.

### Preliminary Budget Estimate

- Cloud computing (AWS/GCP): ~S/. 8,000
- Conference travel (1–2 international): ~S/. 12,000
- Software licenses and tools: ~S/. 1,500
- Miscellaneous: ~S/. 2,000

## 10. Bibliography

Benavides, J. A., et al. (2020). Defining new pathways to manage the ongoing emergence of bat rabies in Latin America. *Viruses, 12*(9), 1002.

Blackwood, J. C., et al. (2013). Resolving the roles of immunity, pathogenesis, and immigration for rabies persistence in vampire bats. *PNAS, 110*(51), 20837–20842.

Carroll, S. R., Garba, I., Figueroa-Rodríguez, O. L., et al. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal, 19*(1), 43.

CDC-MINSA. (2020). Vigilancia de enfermedades zoonóticas. Ministerio de Salud del Perú.

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *KDD 2016*, 785–794.

Dwork, C., McSherry, F., Nissim, K., & Smith, A. (2006). Calibrating noise to sensitivity in private data analysis. *Theory of Cryptography Conference*, 265–284.

FAO/OIE/OMS. (2019). Taking a multisectoral, One Health approach. WHO.

Gebru, T., Morgenstern, J., Vecchione, B., et al. (2021). Datasheets for datasets. *Communications of the ACM, 64*(12), 86–92.

Hansen, M. C., et al. (2013). High-resolution global maps of 21st-century forest cover change. *Science, 342*(6160), 850–853.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.

Hevner, A. R., et al. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105.

Kamiran, F., & Calders, T. (2012). Data preprocessing techniques for classification without discrimination. *Knowledge and Information Systems, 33*(1), 1–33.

Keshavamurthy, R., Boutelle, C., Nakazawa, Y., Joseph, H., Joseph, D. W., Dilius, P., Gibson, A. D., & Wallace, R. M. (2024). Machine learning to improve the understanding of rabies epidemiology in low surveillance settings. *Scientific Reports, 14*, Article 25851. https://doi.org/10.1038/s41598-024-76089-3

Meyer, H., et al. (2019). Importance of spatial predictor variable selection in machine learning applications. *Ecological Modelling, 411*, 108815.

Mitchell, M., Wu, S., Zaldivar, A., et al. (2019). Model cards for model reporting. *Proceedings of the Conference on Fairness, Accountability, and Transparency*, 220–229.

National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. (1979). *The Belmont Report*.

OPS. (2022). EWARS: Sistema de alerta temprana y respuesta. OPS/OMS.

Pineau, J., et al. (2021). Improving reproducibility in machine learning research. *Journal of Machine Learning Research, 22*(164), 1–20.

Plowright, R. K., et al. (2017). Pathways to zoonotic spillover. *Nature Reviews Microbiology, 15*, 502–510.

Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570.

---

**Cross-references — every deliverable this draft integrates:**

| Session | File | Integrated in |
|---|---|---|
| 1 | `01_paradigm/paradigm_justification.md` | §6 Research Paradigm |
| 2 | `02_method/method_fit_matrix.md` | §6 Research Paradigm |
| 4 | `04_literature/` (systematic review, PRISMA, gap analysis) | §4 Literature Review |
| 5 | `05_pipeline/` | §6 Reproducibility & Documentation Plan |
| 6 | `06_repro_audit/reproducibility_audit.md` | §4, §6 Validation |
| 7 | `07_model_card/` | §6 Reproducibility & Documentation Plan, §8 |
| 9 | `09_ethics/ethics_protocol.md` | §7 Ethical Considerations |
| 10 | `10_data_mgmt/data_management_plan.md` | §7, §8 |
| 11 | `11_bias_audit/bias_audit_report.md` | §6 Fairness & Bias Audit Plan, §7, §8 |
| 12 | `12_integrity/ai_use_policy.md`, `retracted_paper_analysis.md` | Front matter, throughout |

---

**AI Assistance Disclosure:** see Front Matter above for the full, session-specific disclosure. This document itself was assembled by integrating the content of prior deliverables (each independently disclosed in its own file) into a single draft — no new substantive analysis was introduced here beyond the cross-referencing and synthesis connecting those prior pieces to each other.
