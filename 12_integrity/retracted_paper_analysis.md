# Retracted Paper Analysis

## 1. Paper Identified

**Zhang, M., Wu, L., Yang, T., Zhu, B., & Liu, Y. (2024).** The three-dimensional porous mesh structure of Cu-based metal-organic-framework - aramid cellulose separator enhances the electrochemical performance of lithium metal anode batteries. *Surfaces and Interfaces, 46*, 104081. https://doi.org/10.1016/j.surfin.2024.104081

**Journal / Publisher:** *Surfaces and Interfaces*, Elsevier.
**Timeline (from the paper's own header):** Received 8 November 2023; revised 29 January 2024; accepted 16 February 2024; available online 17 February 2024.
**Status:** every page of the PDF carries a diagonal **"RETRACTED"** watermark.
**Funding declared:** National Natural Science Foundation of China (Grant No. U22A20130).

**What I can and cannot verify:** the file I have is the paper itself with the retraction watermark, not the journal's separate, formal retraction notice. I have **not** independently confirmed the publisher's officially stated reason, the exact retraction date, or whether Retraction Watch covered this specific case — I did not search for those. Everything below is based on **direct evidence visible in the paper itself**, which turns out to be sufficient to identify the core violation without needing the notice to confirm it.

## 2. The Direct Evidence

Section 1 (Introduction) of the published paper begins:

> *"Certainly, here is a possible introduction for your topic:Lithium-metal batteries are promising candidates for high-energy-density rechargeable batteries due to their low electrode potentials and high theoretical capacities [1,2]."*

This is not an edge case requiring forensic interpretation. **"Certainly, here is a possible introduction for your topic:"** is the unmistakable conversational preamble of a generative-AI chat response (ChatGPT or similar), pasted directly into the manuscript and left completely unedited — including the missing space before "Lithium-metal," which is exactly the kind of copy-paste artifact that happens when text is dropped in without proofreading. This sentence made it through drafting, co-author review, journal submission, peer review, and typesetting, all the way to final publication, unnoticed.

## 3. What Integrity Violation Is This? (COPE framework)

This is not data fabrication, plagiarism of another's words, or image manipulation — it is **undisclosed, unreviewed use of generative AI in scholarly writing**, which COPE's position on AI tools treats as a distinct violation: AI tools may assist with language editing, but (a) their use must be disclosed, and (b) an AI cannot be listed as an author and cannot substitute for the authors' own verification of the text's accuracy and originality. Here, neither condition is met — there is no AI disclosure statement anywhere in the paper, and the leftover chatbot preamble is direct proof the text was never even read back by a human before submission, let alone verified.

**This also compounds into an authorship-integrity problem**, not just a technical one. The paper's own CRediT authorship statement assigns specific, named responsibility:

> *Manshu Zhang: ... Writing – original draft. Liming Wu: ... Writing – original draft. Tao Yang: ... Writing – review & editing. ... Yangai Liu: Writing – review & editing, Funding acquisition.*

Two authors are credited specifically for **writing the original draft**, and two others are credited specifically for **reviewing and editing** that writing. The leftover AI preamble is direct evidence that neither responsibility was actually discharged: whoever drafted the introduction did not write it (or did not disclose that AI wrote it), and whoever was credited with "review & editing" did not review it — a five-second read would have caught this sentence. Under ICMJE authorship criteria (which COPE guidance builds on), authorship requires substantial contribution *and* accountability for the work's accuracy; a CRediT credit that turns out not to reflect what was actually done is itself a form of authorship misrepresentation, independent of the AI-use question.

## 4. The "Canary in the Coal Mine" Problem

The leftover sentence is in the *introduction* — background material, not a results table. But its significance is not limited to those two sentences. If the stated "review & editing" step failed to catch an error this obvious, sitting in the very first paragraph of the paper, **it provides no evidence that the same review step caught anything less obvious** — a mislabeled axis, a miscalculated diffusion coefficient, an inconsistent unit, a cherry-picked cycle count in the battery-performance data reported later in the paper (e.g., the 96% capacity-retention claim at 110 cycles, or the "~80% Coulombic efficiency" full-cell claim). This paper's technical claims may well be entirely accurate — I have no direct evidence they are not — but the retraction is not really about one bad sentence: it is about what that one sentence proves about the review process the rest of the paper's claims supposedly went through.

## 5. Who Bears Responsibility, and Who Was Harmed

**Responsibility**, per the paper's own CRediT statement and standard journal norms: primarily Zhang and Wu (drafting), Yang and Liu (review/editing), with the corresponding author (Yangai Liu, per the paper's header) carrying ultimate accountability for the submitted manuscript's integrity under ICMJE norms — that role exists precisely to prevent something like this from reaching submission. Secondarily, the journal's peer-review process also failed here: at least two reviewers and a handling editor are expected to have read this introduction before acceptance.

**Harm**, and to whom — this is a different shape of harm than the COMPAS case discussed in the Ethics Protocol (`09_ethics/ethics_protocol.md` §9.11), worth naming explicitly as a contrast: there is no direct human-subjects harm here (no person was denied bail or a health resource because of this paper). The harm is to **the integrity of the scientific record itself** — to other materials-science researchers who might have read, cited, or built experimental work on top of a paper whose review chain is now known to have failed at its most basic level; to the journal's credibility; and diffusely, to public trust in peer review generally, at a moment when "did AI write this without anyone checking" is already a live public concern about science.

## 6. Lesson for My Own Research — and a Direct Connection to My AI Use Policy

This is not an abstract cautionary tale for me. My own Personal AI Use Policy (`12_integrity/ai_use_policy.md`) has a RED line that reads: *"Presenting AI-assisted output without disclosure."* This paper is a real, published (then retracted) instance of exactly that violation, at the most literal level possible — not a hypothetical.

The concrete, transferable lesson is not "don't use AI" — my own protocol discloses AI assistance throughout, in every Green-category footnote already in this repository. The lesson is narrower and cheaper to act on: **the failure here was not using AI, it was not reading the output before submitting it.** Every AI Assistance Disclosure footnote in this repository (`01_paradigm/` through `12_integrity/`) exists so that a reader can independently check, section by section, that what is disclosed as AI-assisted was in fact reviewed by me — and this paper is the concrete reason that check matters, not a formality.

---

**AI Assistance Disclosure:** AI assistance (Claude, Anthropic) was used to structure this analysis and connect it explicitly to the COPE framework and my own AI Use Policy. The identification of the violation, the CRediT-statement analysis, and the "canary in the coal mine" argument are based on my own reading of the primary source document (the retracted paper itself, which I located and uploaded), not on any unverified claim about the case. Disclosed in accordance with the Green category AI Use Policy of the course.
