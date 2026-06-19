# Paradigm Justification Statement

## Research Paradigms for AI: Positivism, Interpretivism & Computational Thinking

### 1.1. Research Topic & Context

Wild rabies transmitted by the vampire bat *Desmodus rotundus* is the leading cause of human and bovine rabies mortality in Peru, particularly in Amazonian and Andean communities with limited access to health services. Between 1990 and 2019, 57% of 399 reported human rabies cases (228 cases) corresponded to wild transmission, with an average of 7 annual cases in the last two decades of that period. Two new cases were confirmed in the Amazonas region in 2024, evidencing that transmission risk remains active. Current surveillance is predominantly reactive: detection typically occurs after the virus has already been transmitted to livestock or humans (CDC-MINSA, 2020). No integrated predictive system exists that articulates spatial distribution data of the reservoir, climatic and environmental variables, land use, and historical epidemiological records — a gap that limits the capacity to activate preventive measures with sufficient advance notice.

### 1.2. Preliminary Research Question

To what extent can a machine learning model, trained on epidemiological, ecological, and climatic data from open public sources, accurately estimate the spatio-temporal risk of zoonotic wild rabies transmission in wildlife-human contact zones in Peru under the One Health framework?

**Three formulations of the same research question:**

**Version A — Predictive focus:** Which combination of ecological, climatic, and socioeconomic variables best predicts wild rabies transmission risk in Peruvian Amazonian and Andean regions (2010–2024), as measured by AUC-ROC and sensitivity metrics across Random Forest, XGBoost, and LSTM models?

**Version B — Applied/system focus:** Can a validated, open-source early warning prototype — integrating ML-predicted risk maps with SENASA and CDC-MINSA operational workflows — demonstrate sufficient utility and usability to support real-time public health decision-making in wild rabies-endemic zones of Peru?

**Version C — Causal/ecological focus:** How does forest cover loss and expansion of the agricultural and livestock frontier modulate the spatio-temporal risk of zoonotic wild rabies transmission from *D. rotundus* toward human populations in Peru during 2010–2024?

### 1.3. Chosen Paradigm & Justification

This research adopts a **Computational / Quantitative Empirical paradigm** with a secondary **Design Science Research (DSR)** component. The core epistemological stance is positivist: the zoonotic transmission risk of wild rabies is an objective, measurable phenomenon whose underlying structure can be learned from empirical data and validated through reproducible metrics such as AUC-ROC, sensitivity, and spatial cross-validation.

I reject pure interpretivism because understanding the "lived experience" of exposed communities, while valuable for intervention design, does not generate the quantitative risk indices needed to activate early warning protocols at institutional scale. I reject a purely qualitative approach because it cannot produce spatially generalizable, replicable predictions required by SENASA and CDC-MINSA.

I do not adopt Design Science Research as the primary paradigm because developing a prototype without prior empirical validation of the predictive model may limit the reliability of the resulting decision-support tool. In a public health context, methodological robustness and prior validation are necessary before system implementation. The computational paradigm is appropriate because the research problem is fundamentally one of pattern recognition over high-dimensional, spatially structured, multi-source data — satellite-derived NDVI, historical epidemiological records, climatic time series, and reservoir distribution models — a domain where machine learning algorithms demonstrably outperform classical statistical models (Calderone, 2022). The DSR component is secondary but essential: the validated model is instantiated as a functional early warning prototype, contributing both theoretical knowledge (the One Health risk index) and a practical artifact (the decision-support system).

### 1.4. Implications of Paradigm Choice

**Data type:** The research will work exclusively with structured quantitative data — georeferenced epidemiological case records, satellite imagery (MODIS/Landsat NDVI), land cover change layers (MapBiomas, Global Forest Watch), climatic variables (SENAMHI, WorldClim), and *D. rotundus* spatial distribution models — for the period 2010–2024.

**Methods:** The paradigm dictates supervised machine learning with spatial cross-validation (Meyer et al., 2019), SHAP value analysis for variable importance, and AUC-ROC as the primary performance criterion; the prototype evaluation follows DSR utility and usability criteria (Hevner et al., 2004).

**Contribution:** A novel, reproducible One Health risk index for wild rabies in Peru, three trained and benchmarked ML models, and an open-source early warning prototype — all replicable to other priority zoonoses in the Amazon basin.

### 1.5. One Doubt or Tension

My principal uncertainty concerns data availability and quality: official records of wild rabies cases from CDC-MINSA and SENASA for the 2010–2024 period may be incomplete, geographically imprecise, or inconsistently coded across years, which could introduce label noise into the training dataset and bias the model toward well-monitored regions.