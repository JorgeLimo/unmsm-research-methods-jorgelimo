# Research Question + Method-Fit Matrix

## 2.1. Research Question (Method-Ready Precision)

To what extent can a supervised machine learning model — comparing Random Forest, XGBoost, and LSTM — trained on open-source epidemiological, ecological, and climatic data for the period 2010–2024, accurately estimate the spatio-temporal risk of zoonotic wild rabies transmission in wildlife-human contact zones in Peru under the One Health framework, and can the validated model be instantiated as a functional early warning prototype for decision-makers at SENASA and CDC-MINSA?

## 2.2. Three Candidate Methods

| Method | Method 1 — Computational ML Experiment | Method 2 — Design Science Research (DSR) | Method 3 — Simulation-Based Research |
|---|---|---|---|
| **Description** | Train, benchmark and validate RF, XGBoost and LSTM on georeferenced epidemiological + satellite data. Output: predictive model with AUC-ROC metrics. | Build the early warning prototype artifact, evaluate on utility & usability with SENASA/CDC-MINSA teams. Output: deployable decision-support tool. | Agent-based/compartmental simulation of *D. rotundus* population dynamics under deforestation scenarios. Output: synthetic scenario risk maps. |

## 2.3. E.D.F.C.V. Scoring Matrix (1–5 per criterion)

| Criterion | Key Question | Method 1 (ML Experiment) | Method 2 (Design Science) | Method 3 (Simulation) |
|---|---|---|---|---|
| **E** – Epistemological Fit | Does this method match the Computational/Positivist paradigm? | 5/5 | 4/5 | 3/5 |
| **D** – Data Availability | Can I access CDC-MINSA, SENASA, GBIF, MODIS/Landsat, SENAMHI data within 3 years? | 4/5 | 3/5 | 2/5 |
| **F** – Feasibility | Time, compute cost, ethics approval — realistic within a 3-year doctoral timeline? | 4/5 | 4/5 | 2/5 |
| **C** – Contribution Type | Does this method produce a validated predictive model + One Health risk index? | 5/5 | 4/5 | 3/5 |
| **V** – Venue Fit | Will One Health, PLOS Comp. Bio., Sci. Reports and IEEE EMBC accept this method? | 5/5 | 4/5 | 3/5 |
| **TOTAL** | | **23/25** | **19/25** | **13/25** |

> Scores are preliminary and intended only as methodological justification.

## 2.4. Defense of the Winner: Method 1 — ML Experiment

**Why Method 1 wins:**

The research question asks to "accurately estimate spatio-temporal risk" and "compare algorithm performance by AUC-ROC" — both quantitative empirical claims that can only be answered by training and benchmarking actual ML models on real data. The ML Experiment is the only method that produces the validated risk index with reproducible performance metrics required by target journals and by SENASA/CDC-MINSA. All data sources are publicly available and accessible within the doctoral timeline.

**Why not Method 2 (Design Science alone):**

Building the prototype without first validating the predictive model would result in a decision-support tool without sufficient empirical evidence of reliability. Therefore, prototype development is positioned as a secondary phase following model validation. DSR is retained as a secondary component (the prototype phase) nested within the ML Experiment, not as the primary method.

**Why not Method 3 (Simulation):**

Agent-based simulation requires parameterization data (colony sizes, immigration rates) largely unavailable at national scale in Peru. Without reliable parameterization, outputs carry high epistemic uncertainty and cannot be validated against observed case data.

**One open tension:**

The distinction between Method 1 and Method 2 remains conceptually close, as the prototype represents the practical implementation of the validated predictive model rather than an entirely independent research output. This dual empirical and artifact-oriented structure may require careful methodological framing depending on publication venue.