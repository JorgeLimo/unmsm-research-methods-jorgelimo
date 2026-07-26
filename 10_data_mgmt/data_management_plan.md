# Data Management Plan

Applied to the research dataset described in the protocol (`03_protocol/protocol_v0.1.md` §3.6, Data Sources) and building directly on the confidentiality commitments already made in the Ethics Protocol (`09_ethics/ethics_protocol.md` §9.6).

## 10.1. Data Description

Five data streams, combined at the district-month unit of analysis (§3.6):

| Stream | Format | Approx. volume | How generated |
|---|---|---|---|
| Epidemiological (CDC-MINSA, SENASA) | Structured institutional records (CSV/DB export) | ~14 years × ~1,900 Peruvian districts × 12 months — sparse, most cells zero | Administrative surveillance, obtained via data-sharing agreement (not yet secured — see Data Contingency Plan) |
| *D. rotundus* occurrence | Georeferenced points (CSV/GeoJSON) | Variable, GBIF/IUCN query result | Open-access biodiversity API |
| Environmental (NDVI, forest cover) | Raster → extracted tabular values | Monthly composites, 2010–2024 | MODIS/Landsat/MapBiomas/Global Forest Watch, open access |
| Climatic | Tabular time series | Monthly, per station/grid | SENAMHI, WorldClim v2.1, open access |
| Socioeconomic | Tabular, district-level | Static/periodic | INEI, MINAM, open government data |

All five streams are joined into a single analytic table at district-month resolution — the same resolution already defined for statistical reasons (rare-event unit of analysis) and now reused here as a confidentiality control (§10.3).

## 10.2. FAIR Compliance

| FAIR element | Plan |
|---|---|
| **Findable** | Derived, de-identified analytic dataset (not raw institutional records) deposited in Zenodo with a DOI upon first publication; rich metadata (variable dictionary, unit of analysis, date range, spatial extent) attached. |
| **Accessible** | Public repository access for the derived dataset and all code (already the case for the synthetic placeholder in `05_pipeline/`); raw CDC-MINSA/SENASA records remain access-restricted per the data-sharing agreement — FAIR's "Accessible" does not require *unrestricted* access, only clear, documented access conditions. |
| **Interoperable** | Standard formats (CSV/GeoJSON), documented variable names matching the Datasheet (`07_model_card/datasheet.md`) conventions, standard CRS for spatial data. |
| **Reusable** | CC-BY license on the derived dataset and its metadata (code remains MIT, per §3.8); full codebook; clear provenance statement distinguishing "open-access input layers" from "restricted-access epidemiological input" so reusers know exactly what they can and cannot re-obtain. |

## 10.3. Anonymization Strategy

This section makes the confidentiality commitment from the Ethics Protocol (§9.6) technically concrete.

**Primary control — aggregation + small-cell suppression (k-anonymity logic).** The district-month unit of analysis already aggregates individual case records, which is structurally similar to a k-anonymity constraint (Sweeney, 2002): rather than releasing person-level rows, each analytic unit represents a group. However, aggregation alone does not guarantee a safe k in sparsely populated rural districts with very few investigations in a given month. Rule: for any district-month cell used in a **publicly shared** table, if the total number of investigations in that cell is below **k = 5**, the cell is merged with the temporally adjacent month(s) (rolling window) or, if still below threshold, suppressed from public release. Internal model training may use finer-grained cells under the access controls in §10.4, since the disclosure risk model differs between "data visible only to the author under a signed agreement" and "data visible to the public."

**Why l-diversity is only partially applicable here:** l-diversity (Machanavajjhala et al., 2007) guards against a k-anonymous group being *homogeneous* in its sensitive attribute — but confirmed rabies cases are rare by definition, so most groups will legitimately be homogeneously negative. This is not a privacy failure to "fix" (it reflects true disease rarity, not a re-identification shortcut), but it does mean the sensitive disclosure risk here is less "can an attacker learn Alice's rabies status from a homogeneous group" and more "can an attacker learn that a specific small community had *any* confirmed case at all." The k=5 suppression rule above targets exactly that latter risk.

**Secondary control — differential privacy on public-facing outputs.** The early-warning prototype's risk maps (§3.9, Months 21–26) are the artifact most likely to be seen outside the research team, and model outputs can themselves leak information about rare training records (Rocher et al., 2019, on re-identification from generative-model outputs — directly relevant since this is exactly a small-cell, rare-event setting). Before any public-facing risk map is released, calibrated noise (Laplace mechanism, Dwork et al., 2006) will be added to any published count or rate derived from cells with fewer than 20 total investigations, with an initial conservative privacy budget of **ε = 1.0**, to be revisited with a privacy specialist before deployment.

**Explicitly out of scope:** no direct identifiers (names, addresses, individual case IDs) are ever included in any analytic table, public or internal — this is a hard constraint, not a tunable privacy parameter.

## 10.4. Storage & Backup

- **Raw institutional data** (CDC-MINSA/SENASA, once secured): stored in an access-controlled location outside the public GitHub/DVC remote, encrypted at rest, accessible only to the author under the terms of the data-sharing agreement. Not the same storage as the project's public DVC remote (currently a local folder, per `05_pipeline/README.md` — that remote is reserved for the synthetic/derived data only, never raw institutional records).
- **Derived, de-identified analytic tables**: version-controlled via the same Git + DVC workflow already built and tested (`05_pipeline/`).
- **Backup policy:** 3-2-1 rule — 3 copies, on 2 different media, 1 off-site (e.g., local disk + institutional/cloud backup + the DVC remote itself once migrated off a single local machine, per the open item already flagged in `05_pipeline/README.md`).

## 10.5. Legal Compliance

**Legal Compliance Checklist**

| Requirement | Applies? | Status / plan |
|---|---|---|
| Ley N° 29733 (Personal Data Protection, reglamento DS 016-2024-JUS, in force 30 Mar 2025) | ✅ Always (Peru baseline) | Consent-waiver justification documented in Ethics Protocol §9.3; ARCO rights preserved through source institutions |
| GDPR (EU Regulation 2016/679) | ⚠️ Conditional | Not expected to apply — no EU data subjects and no processing on EU-based infrastructure currently planned. Re-assess if any future collaborator, cloud region, or co-author introduces an EU nexus. |
| Cross-border data transfer mechanism | ⚠️ Conditional | Applies if cloud computing (AWS/GCP, budgeted in §3.9) uses non-Peru regions. Plan: select a Peru/Latin-America cloud region where available; if not available, document the transfer mechanism (standard contractual clauses / adequacy) before any transfer. |
| CONCYTEC Código Nacional de Integridad Científica | ✅ Always | Retention and audit-trail obligations reflected in §10.7 |
| Ley N° 31814 (AI Promotion Law, 2023) | ✅ Applies to prototype phase | Transparency/accountability principles carried into the Ethics Protocol's AI-specific considerations (§9.9) |
| CARE Principles (Indigenous data governance) | ✅ Applies | Community-level consultation commitment already made in Ethics Protocol §9.3; carried into this DMP's sharing plan (§10.6) |
| Data breach notification | ✅ Applies if breach occurs | Peru's authority (Autoridad Nacional de Protección de Datos Personales) notification procedure to be followed; target within 48 hours of detection, consistent with common international breach-notification standards (e.g., GDPR Art. 33's 72-hour benchmark, adapted here to a stricter internal target) |

## 10.6. Sharing Plan

| Artifact | Shared? | Where | License | Conditions |
|---|---|---|---|---|
| Code (`05_pipeline/` and all repo code) | Yes, public | GitHub | MIT | None beyond attribution |
| Derived, de-identified analytic dataset (district-month, k≥5 enforced) | Yes, public, upon first publication | Zenodo | CC-BY | DOI + full codebook required (§10.2) |
| Raw CDC-MINSA/SENASA institutional records | No | Access-restricted storage only | Per data-sharing agreement | Not for redistribution, per agreement terms (§9.7) |
| Public-facing risk maps (prototype phase) | Conditional | To be defined with SENASA/CDC-MINSA | TBD | Differential-privacy noise applied first (§10.3); community consultation per CARE principles before release in the Amazonas pilot region |

## 10.7. Retention Period

- **Derived/de-identified data and code:** retained indefinitely once deposited (Zenodo/GitHub), consistent with FAIR "Reusable" and CONCYTEC's expectation of durable, auditable research records.
- **Raw institutional data:** retained only for the duration specified in the data-sharing agreement (to be finalized — an open item, same as flagged in the Ethics Protocol §9.7) plus any minimum required for doctoral-thesis defense and post-publication audit (commonly 5–10 years under comparable agreements); secure deletion (cryptographic erasure of encrypted storage) at the end of that period, logged and dated.
- **Trigger for early review:** if the Data Contingency Plan's fallback (Amazonas regional pilot, `03_protocol/protocol_v0.1.md` §3.6) is activated, this DMP's retention and sharing terms will be re-scoped to that region specifically before being extended nationally.

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used for structuring this Data Management Plan against the course's 7-section template and for grammar/style editing. The anonymization threshold choices, the distinction between k-anonymity and differential privacy applicability, and the legal compliance checklist represent the original work of the author. Disclosed in accordance with the Green category AI Use Policy of the course.
