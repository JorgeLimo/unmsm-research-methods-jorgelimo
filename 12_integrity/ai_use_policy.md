# Personal AI Use Policy

**For:** doctoral thesis, *Predictive Model for Zoonotic Transmission Risk of Wild Rabies in Wildlife-Human Contact Zones Using Machine Learning with a One Health Approach in Peru*
**Author:** Jorge Luis Limo Arispe
**Aligned with:** the course's institutional Green/Amber/Red AI Tool Use Policy (Syllabus, Session 13/course policy table) and the Oxford model referenced in Session 12/13 material.

Written to be read aloud at my defense without flinching.

## MY GREEN — no permission needed

Tools and tasks, named specifically, not as "writing help":

- **Claude (Anthropic)**, for: brainstorming and outlining the structure of protocol sections, deliverables, and analyses before I write the substantive content myself; grammar, clarity, and style editing on text I have already drafted; code scaffolding for reproducibility infrastructure (e.g., boilerplate for the Git/DVC/MLflow/Docker setup in `05_pipeline/`) where the technical design decisions themselves — spatial cross-validation strategy, metric choice under class imbalance, anonymization thresholds, mitigation method selection — are mine; formatting tables and section headers drawn from a cited published template (Model Cards, Datasheets, PRISMA, DMP structures) where the substantive content filling those templates is my own analysis.
- Acknowledged in a footnote in each document, per the course's Green category requirement — already the pattern followed in every deliverable in this repository to date.

## MY AMBER — approval + disclosure + prompt log

- **Paragraph-level drafting of literature-review synthesis text** (i.e., AI producing connected prose paragraphs that summarize or synthesize multiple sources, beyond grammar-editing a paragraph I already wrote myself).
- **Data-cleaning or preprocessing scripts beyond basic scaffolding** — specifically, once real CDC-MINSA/SENASA records replace the synthetic placeholder data, any nontrivial data-wrangling code applied to that real, sensitive data.
- **Language polishing of the final protocol/thesis manuscript** immediately before submission to the committee or a journal.

For every AMBER use: requires my advisor's **prior written approval**; disclosed explicitly in the Methods/Acknowledgments section of the relevant document; a dated **prompt log** maintained in `12_integrity/ai_prompt_log/` in this repository, retained for the same period specified in the Data Management Plan (`10_data_mgmt/data_management_plan.md`, §10.7); accessible to my advisor and the thesis committee on request. **No log = it was RED.**

## MY RED LINE — never, even if nobody would know

- Using AI to draft, generate, or substantively rewrite the core analysis, methodology, discussion, results, abstract, or conclusions of the protocol or thesis. These represent my own intellectual contribution or they represent nothing.
- Using AI to invent, embellish, or "fill in" citations, data points, quotes, or results I have not personally verified — this is a direct, permanent lesson from this project: the Calderone (2022) citation that turned out to not resolve to a real article (§1, instructor feedback on the protocol) is the reason this line exists, not an abstract principle.
- Using AI during the midterm or final oral presentation/defense, or to generate real-time responses to committee questions.
- Presenting AI-assisted output without disclosure, or logging a fabricated or incomplete prompt-log entry.
- Using AI to process or analyze real, sensitive CDC-MINSA/SENASA case-level data outside the access controls and disclosure already committed to in the Ethics Protocol (`09_ethics/ethics_protocol.md` §9.9) and Data Management Plan.

## Retroactive Reflection on This Repository's Own AI Use

Session 12's integrity lens should apply to this project's own record, not only to external retracted papers. Every deliverable from Session 6 onward (`06_repro_audit/`, `07_model_card/`, `09_ethics/`, `10_data_mgmt/`, `11_bias_audit/`) carries an "AI Assistance Disclosure" footnote citing the Green category — consistent with how Sessions 1–4 were already disclosed before this policy existed. On first reflection, some of that assistance (full-document structuring against a course-provided template, at real length) seemed close to the boundary between Green ("outlining") and Amber ("paragraph-level drafting"), so rather than deciding the question in my own favor, I raised it directly with the instructor.

**Resolution:** the instructor confirmed this pattern of use — outlining and structuring documents against published/course-provided templates (Model Cards, Datasheets, PRISMA, DMP structures, the ethics-protocol anatomy), with all substantive content decisions remaining mine — is **Green**, not Amber. No prior approval or prompt log was required for Sessions 6–11 under this classification. A retroactive prompt log had been prepared while this was still an open question; it was removed once the Green classification was confirmed, since maintaining a log for Green-category use would misrepresent the use as needing one.

## Disclosure Statement — ready to paste into the thesis

> In the preparation of this thesis I used Claude (Anthropic) for outlining, structural scaffolding, and grammar/style editing of text I had already drafted, as detailed in my Personal AI Use Policy (`12_integrity/ai_use_policy.md`). All analysis, interpretation, methodology, discussion, and conclusions are my own. I take full responsibility for the content of this work.
>
> Signed: **Jorge Luis Limo Arispe**
> Date: 27/07/26

---

*This document itself was structured with AI assistance (Claude, Anthropic) against the course's Green/Amber/Red template — a Green-category use under this same policy: outlining and formatting, with every substantive judgment (what belongs in MY GREEN vs. AMBER vs. RED, the retroactive-reflection admission above) being my own.*
