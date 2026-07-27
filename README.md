# UNMSM Research Methods — Jorge Limo

Doctoral capstone project for *Research Methods and Scientific Integrity in AI and Advanced Technologies* — UNMSM, Doctoral Program in Deep Technologies.

**Author:** Jorge Luis Limo Arispe
**Topic:** Predictive Model for Zoonotic Transmission Risk of Wild Rabies in Wildlife-Human Contact Zones Using Machine Learning with a One Health Approach in Peru

## Repository Structure

- `01_paradigm/` — Paradigm Justification Statement (Session 1)
- `02_method/` — Method-Fit Matrix (Session 2)
- `03_protocol/` — Research Protocol versions v0.1 → v1.0 → v2.0 (Sessions 3, 13, 15)
- `04_literature/` — Systematic Literature Review + PRISMA diagram + Gap Analysis (Session 4)
- `05_pipeline/` — Reproducible ML pipeline: Git + DVC + MLflow + Docker (Session 5)
- `06_repro_audit/` — Reproducibility Audit of the anchor citation, Keshavamurthy et al. (2024) (Session 6)
- `07_model_card/` — Model Card + Datasheet for the pipeline's model and dataset (Session 7)
- *(Session 8 — Midterm integration checkpoint: no new repo file, feedback folded into the protocol)*
- `09_ethics/` — Ethics Protocol, applying Belmont + CONCYTEC + CARE (Session 9)
- `10_data_mgmt/` — Data Management Plan: FAIR, anonymization, legal compliance checklist (Session 10)
- `11_bias_audit/` — Bias Audit Report: AIF360/Fairlearn on real COMPAS data, before/after mitigation (Session 11)
- `12_integrity/` — Retracted Paper Analysis + Personal AI Use Policy (Session 12)

## Reproduce the Pipeline (Session 5)

See full instructions in [`05_pipeline/README.md`](05_pipeline/README.md).

Quick start:
\`\`\`bash
cd 05_pipeline
pip install -r requirements.txt
python3 data/create_dataset.py   # regenerates the synthetic dataset (fixed seed, no DVC remote access needed)
python3 src/train.py --seed 42
\`\`\`

## Reproduce the Bias Audit (Session 11)

See full instructions in [`11_bias_audit/bias_audit_report.md`](11_bias_audit/bias_audit_report.md).

Quick start:
\`\`\`bash
cd 11_bias_audit
pip install aif360 fairlearn "pandas<3"
python3 bias_audit.py   # downloads real COMPAS data automatically on first run
\`\`\`
