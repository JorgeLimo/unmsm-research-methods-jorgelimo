# UNMSM Research Methods — Jorge Limo

Doctoral capstone project for *Research Methods and Scientific Integrity in AI and Advanced Technologies* — UNMSM, Doctoral Program in Deep Technologies.

**Author:** Jorge Luis Limo Arispe
**Topic:** Predictive Model for Zoonotic Transmission Risk of Wild Rabies in Wildlife-Human Contact Zones Using Machine Learning with a One Health Approach in Peru

## Repository Structure

- `01_paradigm/` — Paradigm Justification Statement (Session 1)
- `02_method/` — Method-Fit Matrix (Session 2)
- `03_protocol/` — Research Protocol versions v0.1 → v2.0 (Sessions 3, 13, 15)
- `04_literature/` — Systematic Literature Review + PRISMA diagram + Gap Analysis (Session 4)
- `05_pipeline/` — Reproducible ML pipeline: Git + DVC + MLflow + Docker (Session 5)

## Reproduce the Pipeline

See full instructions in [`05_pipeline/README.md`](05_pipeline/README.md).

Quick start:
\`\`\`bash
cd 05_pipeline
pip install -r requirements.txt
dvc pull
python src/train.py --seed 42
\`\`\`
