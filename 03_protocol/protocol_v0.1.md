# Research Protocol Outline (v0.1)

## 3.1. Title

Predictive Model for Zoonotic Transmission Risk of Wild Rabies in Wildlife-Human Contact Zones Using Machine Learning with a One Health Approach in Peru.

## 3.2. Abstract

Wild rabies transmitted by *Desmodus rotundus* is the leading cause of human and bovine rabies mortality in Peru. Current surveillance is predominantly reactive, with no integrated predictive system combining ecological, climatic, and epidemiological data. This research develops and validates a machine learning-based predictive model — comparing Random Forest, XGBoost, and LSTM — trained on open-source georeferenced data (2010–2024) under the One Health framework, instantiated as a functional early warning prototype for SENASA and CDC-MINSA. The expected contribution is a reproducible, open-source One Health risk index applicable to other priority zoonoses in the Amazon basin.

## 3.3. Introduction & Problem Statement

### Problem Statement

Wild rabies in Peru represents an active and underestimated public health threat. Between 1990 and 2019, 57% of 399 reported human rabies cases corresponded to wild transmission. Two new cases were confirmed in the Amazonas region in 2024. The surveillance system is predominantly reactive. Three structural factors converge: accelerated deforestation of the Peruvian Amazon, expansion of the agricultural and livestock frontier, and the absence of an integrated early warning system articulating spatial distribution of the reservoir, climatic variables, land use, and historical epidemiological records.

### Relevance — The "So What?" Test

This research directly addresses the gap between the documented epidemiological burden of wild rabies in Peru and the non-existence of AI-based predictive tools integrating ecological, climatic, and epidemiological data under the One Health framework. Results will enable SENASA and CDC-MINSA to target vaccination and surveillance resources in highest-risk zones identified by the model, benefiting Amazonian native communities and Andean rural populations with limited access to health services. The open-source model and software will be replicable for leptospirosis, leishmaniasis, and avian influenza across the Amazon basin.

## 3.4. Literature Review

Calderone (2022) — systematic review of 87 studies (2010–2021) — concludes that Random Forest and XGBoost show the best performance in spatially structured epidemiological contexts, while LSTM models show advantages for time series with long temporal dependencies. Benavides et al. (2020) demonstrated that human rabies by *D. rotundus* follows river corridors and deforestation patterns in Colombia and Peru, validating the integration of land use variables and spatial distribution of the reservoir as essential predictors. Blackwood et al. (2013) established that immigration rates between bat colonies and population density are fundamental variables to explain transmission dynamics. Plowright et al. (2017) showed that land use changes and habitat loss are the main drivers of increased contact rates between wildlife reservoirs and human populations. Meyer et al. (2019) proposed spatial cross-validation as the appropriate evaluation strategy for geospatial ML models.

## 3.5. Research Questions / Hypotheses

### General Research Question

To what extent can a machine learning model, trained on epidemiological, ecological, and climatic data from open public sources, accurately estimate the spatio-temporal risk of zoonotic wild rabies transmission in wildlife-human contact zones in Peru under the One Health framework?

### Specific Research Questions

- Which ecological, climatic, and socioeconomic variables show the strongest association with wild rabies outbreaks in Amazonian and Andean regions of Peru during 2010–2024?
- Which supervised ML algorithm (Random Forest, XGBoost, or LSTM) achieves the best predictive performance as measured by AUC-ROC and sensitivity metrics?
- How does the spatial variation of wild rabies transmission risk relate to forest cover loss and expansion of the agricultural frontier in Peru?
- Can a functional early warning prototype demonstrate sufficient utility and usability for decision-makers at SENASA and CDC-MINSA?

### Working Hypothesis

A supervised ML model integrating *D. rotundus* spatial distribution, deforestation indices (NDVI, forest cover change), climatic variables (temperature, precipitation), and historical epidemiological records will achieve an AUC-ROC ≥ 0.80, outperforming classical logistic regression models and demonstrating geographic generalizability through spatial cross-validation.

## 3.6. Methodology

### Research Paradigm

Computational / Quantitative Empirical paradigm with a Design Science Research component.

### Data Sources

- **Epidemiological:** CDC-MINSA wild rabies case registry and SENASA bovine rabies surveillance (2010–2024).
- **Reservoir distribution:** *D. rotundus* georeferenced occurrence records from GBIF and IUCN Red List.
- **Environmental:** NDVI and forest cover change from MODIS/Landsat (MapBiomas, Global Forest Watch, Hansen et al. 2013).
- **Climatic:** Temperature and precipitation from SENAMHI and WorldClim v2.1.
- **Socioeconomic:** Population density, land use, health access indices from INEI and MINAM.

### Algorithms

Three supervised ML algorithms: Random Forest (robust ensemble, interpretable via variable importance); XGBoost (regularized gradient boosting, superior on heterogeneous tabular data); LSTM (recurrent neural network for long temporal dependencies in outbreak series).

### Validation

Spatial cross-validation (Meyer et al., 2019) dividing data into contiguous geographic blocks. Primary metric: AUC-ROC ≥ 0.80. Secondary: sensitivity, specificity, F1-score, Brier score. SHAP values for variable importance and interpretability.

## 3.7. Ethical Considerations

This research works exclusively with publicly available, aggregated, and anonymized institutional data. No direct data collection from human subjects or animals is planned. The research will adhere to Peru's CONCYTEC ethics guidelines and Law 29733 on Personal Data Protection. UNMSM ethics committee consultation will be sought prior to any fieldwork. The model will be evaluated for potential geographic and demographic bias using fairness metrics to reduce disparities in predictive performance across regions and population groups, particularly in remote areas with historically limited access to health services.

## 3.8. Expected Results

- Integrated, georeferenced database of wild rabies cases, *D. rotundus* distribution, climatic variables, vegetation indices, and land use for Peru 2010–2024, deposited following FAIR principles.
- Identification of variables most associated with wild rabies outbreaks via SHAP analysis.
- Validated predictive model (best of RF, XGBoost, LSTM) achieving AUC-ROC ≥ 0.80 with geographic generalizability.
- Functional early warning prototype with dynamic risk maps for SENASA and CDC-MINSA.
- Open-source software package (Python, MIT License) replicable to other Amazon basin zoonoses.
- At least one manuscript prepared for submission to an indexed international journal.

## 3.9. Timeline & Budget

### Preliminary Timeline (36 months)

- **Months 1–6:** Ethics approval, data collection and integration, database construction and quality control.
- **Months 7–12:** Exploratory data analysis, feature engineering, baseline model, spatial cross-validation setup.
- **Months 13–20:** Development, training, and comparison of RF, XGBoost, LSTM; SHAP analysis; reproducibility pipeline.
- **Months 21–26:** Early warning prototype design, development, and usability evaluation with SENASA/CDC-MINSA.
- **Months 27–32:** Manuscript writing, peer review, open-source software release.
- **Months 33–36:** Doctoral thesis writing, internal review, and final defense.

### Preliminary Budget Estimate

- Cloud computing (AWS/GCP): ~S/. 8,000
- Conference travel (1–2 international): ~S/. 12,000
- Software licenses and tools: ~S/. 1,500
- Miscellaneous: ~S/. 2,000

## Bibliography

Benavides, J. A., et al. (2020). Defining new pathways to manage the ongoing emergence of bat rabies in Latin America. *Viruses, 12*(9), 1002.

Blackwood, J. C., et al. (2013). Resolving the roles of immunity, pathogenesis, and immigration for rabies persistence in vampire bats. *PNAS, 110*(51), 20837–20842.

Calderone, W. (2022). One Health and zoonotic disease surveillance: Machine learning applications in Latin America. *One Health, 14*, 100359.

CDC-MINSA. (2020). Vigilancia de enfermedades zoonóticas. Ministerio de Salud del Perú.

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *KDD 2016*, 785–794.

FAO/OIE/OMS. (2019). Taking a multisectoral, One Health approach. WHO.

Hansen, M. C., et al. (2013). High-resolution global maps of 21st-century forest cover change. *Science, 342*(6160), 850–853.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer.

Hevner, A. R., et al. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105.

Meyer, H., et al. (2019). Importance of spatial predictor variable selection in machine learning applications. *Ecological Modelling, 411*, 108815.

OPS. (2022). EWARS: Sistema de alerta temprana y respuesta. OPS/OMS.

Plowright, R. K., et al. (2017). Pathways to zoonotic spillover. *Nature Reviews Microbiology, 15*, 502–510.

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used for outlining, grammar and style editing, and structural organization of this document. All methodological decisions, research design, paradigm justification, and intellectual contributions represent the original work of the author. This disclosure is made in accordance with the AI Tool Use Policy of the course (Green category — brainstorming, outlining, grammar/style editing).