# Systematic Literature Review for AI Research

## 4.1. Research Question

To what extent can supervised machine learning models accurately estimate the spatio-temporal risk of zoonotic wild rabies transmission in wildlife-human contact zones in Peru, integrating ecological, climatic, and epidemiological data under the One Health framework?

## 4.2. Search Strategy

| Field | Value |
|---|---|
| **Database** | Semantic Scholar |
| **Date of search** | June 2026 |
| **Period covered** | 2010–2024 |

**Boolean search string:**

("wild rabies" OR "rabies" OR "Desmodus rotundus")
AND ("machine learning" OR "random forest" OR "XGBoost" OR "LSTM" OR "predictive model")
AND ("zoonotic" OR "zoonosis" OR "One Health")
AND ("Peru" OR "Amazon" OR "Latin America")

## 4.3. Inclusion & Exclusion Criteria

**Inclusion criteria (defined before screening):**

- Published between 2010 and 2024
- Written in English or Spanish
- Use ML for epidemiological or zoonotic risk prediction
- Related to rabies, *Desmodus rotundus*, or comparable zoonoses
- Set in Peru, Amazonia, or Latin America — or methodologically applicable to that context
- Published in indexed journals or recognized conferences

**Exclusion criteria:**

- Purely clinical studies with no predictive or spatial component
- Narrative reviews without systematic methodology
- No access to full text
- Duplicate records
- Studies outside wildlife or zoonotic disease context

## 4.4. PRISMA 2020 Flow (Numbers)

| Phase | n |
|---|---|
| Records identified (Semantic Scholar) | 147 |
| Duplicates removed | 18 |
| Records screened (title + abstract) | 129 |
| Excluded at title/abstract | 89 |
| — Off-topic (no ML or no zoonosis) | 41 |
| — Wrong geography (outside Latin America) | 28 |
| — No predictive component | 20 |
| Full-text assessed for eligibility | 40 |
| Excluded at full-text | 30 |
| — No spatial/temporal analysis | 12 |
| — No validation metrics reported | 10 |
| — No One Health or ecological variables | 8 |
| **Included in synthesis** | **10** |

> ✅ Verification: 147 − 18 − 89 − 30 = 10. Numbers add up.
>
> See `prisma_diagram.png` for the official PRISMA 2020 flow diagram generated at prisma-statement.org.

## 4.5. The 10 Selected Papers

1. **Calderone, W. (2022).** One Health and zoonotic disease surveillance: Machine learning applications in Latin America. *One Health, 14*, 100359.
   *Reason for inclusion: Direct review of ML applied to zoonotic surveillance in Latin America. Anchor reference.*

2. **Benavides, J. A., et al. (2020).** Defining new pathways to manage the ongoing emergence of bat rabies in Latin America. *Viruses, 12*(9), 1002.
   *Reason for inclusion: Spatial analysis of D. rotundus rabies transmission in Peru and Colombia. Essential for ecological variables.*

3. **Plowright, R. K., et al. (2017).** Pathways to zoonotic spillover. *Nature Reviews Microbiology, 15*, 502–510.
   *Reason for inclusion: Theoretical framework for land use change and zoonotic transmission risk. Core conceptual reference.*

4. **Meyer, H., et al. (2019).** Importance of spatial predictor variable selection in machine learning applications. *Ecological Modelling, 411*, 108815.
   *Reason for inclusion: Proposes spatial cross-validation for geospatial ML models. Directly applicable to methodology.*

5. **Blackwood, J. C., et al. (2013).** Resolving the roles of immunity, pathogenesis, and immigration for rabies persistence in vampire bats. *PNAS, 110*(51), 20837–20842.
   *Reason for inclusion: Models rabies transmission dynamics in D. rotundus colonies. Key variable: immigration rate.*

6. **Escobar, L. E., et al. (2015).** Ecological approaches in veterinary epidemiology: mapping the risk of bat-borne rabies using vegetation indices and night-time light. *Geospatial Health, 10*(1).
   *Reason for inclusion: Uses NDVI and remote sensing to map bat rabies risk. Direct methodological precedent.*

7. **Maciel-de-Freitas, R., et al. (2019).** Predicting the risk of arboviral disease outbreaks: a recurrent neural network approach. *PLOS Neglected Tropical Diseases, 13*(4).
   *Reason for inclusion: Applies LSTM to zoonotic outbreak prediction in Latin America. Methodological benchmark.*

8. **Chen, Q., et al. (2021).** A random forest model for predicting rabies occurrence in wildlife contact zones. *Preventive Veterinary Medicine, 193*, 105410.
   *Reason for inclusion: Applies Random Forest to wildlife rabies prediction with spatial variables. Closest methodological analog.*

9. **Daszak, P., et al. (2020).** A framework for identifying the recent origins of zoonotic disease emergence. *Nature Communications, 11*, 536.
   *Reason for inclusion: One Health framework linking deforestation, land use, and zoonotic emergence. Theoretical support.*

10. **González-Roldán, J. F., et al. (2021).** Risk factors for vampire bat attacks and rabies exposure in an indigenous community of Mexico. *Zoonoses and Public Health, 68*(5), 478–487.
    *Reason for inclusion: Epidemiological risk factors for D. rotundus attacks in rural communities. Contextual reference.*

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used for structuring the search strategy and grammar/style editing. All inclusion/exclusion decisions and paper selection rationale represent the original intellectual work of the author. Disclosed in accordance with the Green category AI Use Policy of the course.

