# Draft Ethics Protocol for Doctoral Research

Applying the Belmont Report (1979) principles and Peru's research-ethics framework to: *Predictive Model for Zoonotic Transmission Risk of Wild Rabies in Wildlife-Human Contact Zones Using Machine Learning with a One Health Approach in Peru.*

Structured against the course's "Anatomy of an AI research ethics protocol" (Session 9): Purpose & participants → Data collection → Informed consent → Risks → Benefits → Confidentiality → Data storage & retention → Conflict of interest, plus the AI-specific additions reviewers now expect.

## 9.1. Purpose & Participants

**Purpose:** develop and validate a machine learning model estimating the spatio-temporal risk of zoonotic wild rabies transmission (*Desmodus rotundus*) in wildlife-human contact zones in Peru, and instantiate it as an early-warning prototype for SENASA and CDC-MINSA (protocol §3.1–3.2).

**Participants:** this study has **no directly recruited human participants** — no interviews, no surveys, no biological sampling from people. It is a **secondary analysis of existing administrative and surveillance data**: CDC-MINSA wild rabies case registries and SENASA bovine rabies surveillance records (2010–2024), combined with open-access ecological/climatic layers (GBIF, IUCN, MODIS/Landsat, SENAMHI, WorldClim, INEI, MINAM). The **data subjects** are the individuals and animals whose exposure/case records already exist in these institutional registries, collected for public-health surveillance purposes, not for this research. The **indirect stakeholders** are Amazonian and Andean communities whose districts will be scored by the resulting risk model and whose resource allocation (vaccination, surveillance) may be influenced by it (§1.1, §3.3).

This distinction matters for every section below: this is closer to a **records-based epidemiological study** than to human-subjects research involving direct interaction, which changes what "consent" and "risk" mean in practice (see §9.3, §9.4).

## 9.2. Data Collection

| Source | What | How obtained |
|---|---|---|
| CDC-MINSA | Wild rabies case registry (human and bovine) | Formal institutional data-sharing request (Data Contingency Plan, `03_protocol/protocol_v0.1.md` §3.6) |
| SENASA | Bovine rabies surveillance | Formal institutional data-sharing request |
| GBIF / IUCN | *D. rotundus* occurrence records | Open API, no request needed |
| MODIS/Landsat, MapBiomas, Global Forest Watch | NDVI, forest cover change | Open access |
| SENAMHI, WorldClim v2.1 | Climatic variables | Open access |
| INEI, MINAM | Population density, land use, health access indices | Open government data |

**No web scraping or social media data is used anywhere in this study** — a deliberate scope decision, since scraped/social data carries a materially different (and weaker) consent story than the institutional administrative records used here (see AI-specific additions, §9.9).

## 9.3. Informed Consent

Because this is secondary use of pre-existing administrative surveillance data rather than direct data collection from living people, **individual informed consent from each case record's subject is not being newly obtained for this research**, and re-contacting subjects (often people bitten years earlier, some in remote areas) would be largely impracticable. This is a standard and legitimate situation in records-based epidemiology, but it must be justified explicitly rather than assumed:

- **Legal basis of the original collection:** CDC-MINSA and SENASA collect these records under Peru's public-health surveillance mandate, not for secondary research — so this study's use of them is a *secondary* use requiring its own ethical justification, independent of the original collection's legality.
- **Consent waiver request:** this protocol will formally request a **waiver of individual informed consent for secondary analysis** from the UNMSM ethics committee, on the grounds that (a) the data will be analyzed only in aggregated, de-identified form (district-month, per the Unit of Analysis defined in §3.6), (b) re-contacting subjects is impracticable at the scale and time depth involved (2010–2024), and (c) the research presents minimal incremental risk to subjects beyond the original data collection (§9.4).
- **Ley N° 29733 standard:** consent must ordinarily be free, prior, express, and informed, with subjects retaining ARCO rights (Access, Rectification, Cancellation, Opposition). Because this research relies on a consent waiver rather than fresh consent, the data-sharing agreement with CDC-MINSA/SENASA must document that the *original* collection had an adequate legal basis (public health mandate) and that ARCO rights continue to be honored through the source institutions, not through this research directly.
- **CARE principles (indigenous data sovereignty):** a large share of the affected population is Amazonian and Andean, including indigenous communities. Individual consent waivers do not substitute for **collective** consultation. Following CARE (Collective Benefit, Authority to Control, Responsibility, Ethics), this protocol commits to consulting regional health authorities and, before any prototype deployment phase (§3.9, Months 21–26), community representatives in the pilot region (Amazonas, per the Data Contingency Plan) — not merely individual data subjects.

## 9.4. Risks

| Risk | To whom | Mitigation |
|---|---|---|
| Re-identification via small cell counts | Individual data subjects, in sparsely populated rural districts | Aggregation to district-month unit of analysis (not individual-level); formal anonymization strategy deferred to and detailed in the Data Management Plan (`10_data_mgmt/`) |
| Community stigmatization ("high-risk zone" labeling) | Amazonian/Andean communities | Communicate risk scores as a resource-prioritization tool for health authorities, not a public-facing label; avoid publishing community-identifiable risk maps at fine resolution |
| Biased performance across historically under-monitored regions | Communities with less surveillance history | Explicit fairness evaluation across regions before deployment (flagged already as a data-quality tension in §1.5); do not deploy in a region without first checking model performance is not systematically worse there |
| Misuse for resource *reduction* in "low-risk" labeled areas that are actually under-monitored (not truly low-risk) | Under-monitored communities | Model outputs framed as decision-support inputs only; final resource-allocation decisions remain with SENASA/CDC-MINSA officials, not automated (§9.9) |
| Data breach of institutional records during transfer/storage | Data subjects | Data-sharing agreement with access controls; raw institutional data never committed to the public GitHub repository (§9.7) |

## 9.5. Benefits

**Direct benefit to data subjects:** none — this is retrospective analysis, not an intervention affecting the people whose historical records are used.

**Societal benefit:** improved early-warning capacity for SENASA/CDC-MINSA to target vaccination and surveillance resources toward highest-risk zones (§3.3, "So What?" test); potential reduction in preventable human and bovine rabies deaths in Amazonian native communities and Andean rural populations with historically limited health-service access; open-source design intended to be replicable to other neglected zoonoses (leptospirosis, leishmaniasis, avian influenza) across the Amazon basin.

**Justification of the burden:** re-using sensitive health-surveillance data without fresh individual consent is only justifiable because the societal benefit (better-targeted, life-saving surveillance in underserved populations) is substantial and the incremental risk to any individual subject, given aggregation to district-month, is low (§9.4).

## 9.6. Confidentiality

- No direct identifiers (names, exact addresses, individual case IDs) will appear in the analytic dataset or in the public repository at any point.
- The **district-month unit of analysis** (defined for statistical reasons in §3.6, Unit of Analysis & Positive Class Definition) doubles as a confidentiality control: aggregating to this level is structurally similar to a k-anonymity constraint, since it groups multiple individuals per analytic unit rather than exposing person-level records. The formal anonymization technique (k-anonymity threshold, l-diversity, or differential privacy, as appropriate) will be specified in the Data Management Plan (`10_data_mgmt/`, Session 10).
- Only aggregated, de-identified, derived features will be tracked in the public DVC/GitHub pipeline — raw institutional CDC-MINSA/SENASA records are never intended for public distribution, consistent with the license terms expected in the eventual data-sharing agreement.

## 9.7. Data Storage & Retention

- **Real epidemiological data** (once secured) will be stored separately from the public repository, under access controls consistent with the terms of the CDC-MINSA/SENASA data-sharing agreement — not committed to Git/DVC in raw form.
- **Derived, de-identified feature tables** (the actual model inputs) are the only artifacts version-controlled and shared, following the same DVC workflow already built and tested in `05_pipeline/` on synthetic data.
- **Retention period:** for the duration of the doctoral program (36 months, §3.9) plus any additional retention period required by CONCYTEC's scientific-integrity framework or the eventual data-sharing agreement (commonly 5–10 years for reproducibility/audit purposes in comparable agreements) — the exact period is an open item pending the signed agreement, and will be finalized once access is secured (Data Contingency Plan, §3.6).
- **Access:** limited to the author and, under controlled conditions, the thesis committee; no public redistribution of raw institutional records is planned.

## 9.8. Conflict of Interest

- **Funding:** none currently disclosed beyond the doctoral program itself; no commercial or industry funding is involved in this phase of the research. Any future funding, consulting arrangement, or paid collaboration with SENASA, CDC-MINSA, or a third party must be disclosed as an amendment to this protocol when it arises.
- **Dual roles:** the author has no employment or advisory relationship with SENASA or CDC-MINSA beyond the academic data-sharing agreement being negotiated for this research.
- **Intellectual property:** the software and risk index are intended for open-source release under an MIT license (§3.8, Expected Results) — no proprietary claim is planned over the resulting model or prototype.

## 9.9. AI-Specific Considerations

- **Training-data provenance & licensing:** documented in full in the Datasheet for the (currently synthetic) pipeline dataset (`07_model_card/datasheet.md`); the real-data version of this datasheet will document the licensing terms of GBIF, WorldClim, MapBiomas, and INEI/MINAM sources, alongside the CDC-MINSA/SENASA data-sharing agreement's terms.
- **Consent status of scraped/social data:** not applicable — this study deliberately uses no scraped or social-media data (§9.2).
- **Model-deployment harms:** the DSR prototype phase (§2.4, secondary method) could produce a decision-support tool whose false negatives (missed high-risk zones) cost lives, or whose false positives misallocate scarce surveillance resources. Mitigation: the model is designed as a **decision-support input**, not an automated trigger — final resource-allocation decisions remain with SENASA/CDC-MINSA officials, consistent with usability evaluation planned in §3.9 (Months 21–26).
- **Dual-use risk:** could a "low-risk zone" classification be repurposed to justify reduced investment or land-use decisions (e.g., agricultural expansion) in areas that are actually under-monitored rather than genuinely low-risk? This risk is judged low but non-zero, and is named here per Belmont's Justice principle (who bears the burden of an error). Mitigation is the same as in §9.4: risk maps will be communicated as inputs for health-resource prioritization, not as general-purpose land-use or safety certifications.

## 9.10. Legal & Institutional Framework Applied

| Instrument | Relevance to this research |
|---|---|
| **Belmont Report (1979)** — Respect for Persons, Beneficence, Justice | Structures this entire protocol (§9.1–9.9) |
| **Ley N° 29733** — Personal Data Protection (in force since 2011; reg. DS 003-2013-JUS, updated DS 016-2024-JUS) | Governs the consent-waiver justification (§9.3) and ARCO rights preservation through source institutions |
| **Ley N° 31814** (2023) — Promotion of AI in Peru | Applies to the eventual early-warning prototype: principles of ethics, transparency, security, and accountability for AI development and use (§9.9) |
| **CONCYTEC — Código Nacional de Integridad Científica** (updated 2024, RP 028 & 035-2024-CONCYTEC-P) | Governs data retention/audit expectations (§9.7) and overall scientific-integrity obligations, consistent with the course's Green/Amber/Red AI-use policy already followed throughout this repository |
| **CARE Principles** (Collective Benefit, Authority to Control, Responsibility, Ethics) | Governs community-level (not just individual-level) engagement given the Amazonian/Andean population affected (§9.3) |
| **UNMSM Ethics Committee** | Formal review and approval of the consent waiver (§9.3) will be sought prior to any fieldwork or prototype deployment, per §3.7 of the protocol |

## 9.11. Case Study Reflection: Lessons from COMPAS

The course's Session 9 lab examined COMPAS as a case where a Justice failure (the error-rate burden fell disproportionately on Black defendants) was compounded by a Beneficence failure (deployment without adequate harm auditing). Applying that lesson directly to this research: the equivalent failure mode here would be a rabies-risk model that performs worse in historically under-monitored Amazonian districts precisely *because* those districts have sparser training data — silently reproducing the surveillance gap the model is meant to fix, and then having that biased output used to (mis)allocate real vaccination and surveillance resources. This is why §9.4 and §9.9 commit to an explicit before-deployment fairness check across regions, not just an aggregate accuracy check — the same lesson COMPAS should have taught the field, applied here before it becomes a real harm rather than after.

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used for structuring this ethics protocol against the course's ethics-protocol anatomy and for grammar/style editing. All risk identification, consent-waiver reasoning, and the application of Belmont/CARE/COMPAS lessons to this specific research represent the original work of the author. Disclosed in accordance with the Green category AI Use Policy of the course.
