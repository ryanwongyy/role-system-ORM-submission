# Reference Style Guide — ORM Submission

**Source:** Synthesized from `11_manuscript/30_reviews/template_inventory_v30.md` (v30-era; 10-template comparative analysis), with template PDFs available at `11_manuscript/30_reviews/template_pdfs/` for direct grounding.

**Target venue:** *Organizational Research Methods* (ORM)

---

## ORM register (binding)

- **Active first-person plural** for contribution claims: "We categorized," "We develop," "We offer," "We find."
- **Conditional-confident hedging vocabulary** (Hickman 2022 / Pratt-Kaplan-Whittington 2020): "candidate framework," "best-practice recommendation," "deviations will be appropriate," "decoupleable goals."
- **No double-disclaimers.** "Comparative typology audit, not validated theory" ❌ — single positive descriptor preferred.
- **Hedge with vocabulary, not parentheticals.** Strip "in our view" / "we suggest" type softeners from main claims.
- **κ disclosure**: report once in §Method/§6.2, with cross-references elsewhere. Do not lead the abstract with the reliability-failure number.

## Structural moves the manuscript has already adopted

- Tripartite "First… Second… Third…" contribution structure in abstract (Aguinis 2023)
- Stakeholder-named conclusion register: "Methods researchers receive… Reviewers and editors receive… Institutional actors…" (Aguinis 2023 / Aguinis-Villamor 2021)
- Stage-organised recommendations table (Aguinis-Villamor 2021)
- Numbered-close at §7 final: "(1) the rubric… (2) the applied-use pipeline… (3) the disconfirmation apparatus…" (Ziems et al. 2024)
- Catalyst-style abstract closer: "we hope this serves as a catalyst for…" (Aguinis & Solarino 2019)
- §1 paradigm declaration ("Before describing the audit, we clarify…") (Aguinis & Solarino 2019)
- Reliability-as-opportunity sentence (TR5, just applied 2026-04-28): "we treat this rubric and its κ as the v1.0 baseline for future development." (Bergh et al. 2017 / Pratt-Kaplan-Whittington 2020)
- Decoupling-positioning move on transparency vs. replication (Pratt-Kaplan-Whittington 2020)

## ORM submission requirements (general — verify against current author guidelines)

- **Word count target:** ORM standard articles run 8,000–12,000 words; methodological-reviews up to 14,000. Current manuscript at 10,984 — within range.
- **Abstract:** 200–250 words. Current at 218 — fine.
- **Title:** Specific, instrument-or-finding-led. Current title is finding-led ("Evidence from 36 Cases").
- **Reference style:** APA 7. Verify alphabetical order and that every in-text citation has a list entry.
- **Statistical reporting:** APA standards — italicize *N*, *p*, *V*, *χ²*, *df*; Cohen's κ italicized; CIs in square brackets with comma separators.
- **Tables/figures:** Numbered consecutively; introduced in text before first appearance; standalone interpretable.
- **Open materials:** ORM increasingly expects deposited data + analysis scripts. Manuscript already commits to this via the v1.0.0-ORM-submission release tag.
- **Pre-registration:** Where applicable, OSF or equivalent. Manuscript names a pre-analysis plan in `30_reviews/OSF_preregistration.md`.
- **Inter-coder reliability:** ORM strongly expects κ ≥ 0.60 for accepted methods-coding work. The manuscript reports κ = 0.289 below threshold and frames it as v1.0 baseline (the rhetorical work TR5 just reinforced). This is a known submission risk — handle the disclosure with discipline, not concealment.

## What to watch for (binding for reviewers)

- **Cross-section consistency on shared statistics.** Numbers cited in the abstract must match §6 exactly: χ² = 87.67 (family) / 29.80 (capability); Cramér's V = 0.260 / 0.240; cell-level MC p = 0.0002 / 0.0012; case-level MC p = 0.58 / 0.33; bootstrap CI for V_family = [0.261, 0.43]; bootstrap CI for V_capability = [0.193, 0.451]; per-role Wilcoxon W = 7, p = 0.0006; sign-test p = 0.004; n = 612 codings; n = 36 cases; 12/36 = durable epistemic-guardian configuration; 1.52× lift over independence; 40 throughput-shrinkage observations; κ = 0.289 [0.147, 0.439].
- **Reference list integrity.** Every in-text citation should have a list entry; list should not contain orphans.
- **Table/figure references.** Every "Table N" and "Figure N" mention should resolve to an actual table/figure.
- **Appendix references.** Appendices A–F are referenced; each should exist and be cross-referenced consistently.
- **§3.0 vs §3.1 numbering** — TR4 stakeholder paragraph (line 250 in v39+TR5) refers to "§3.1 exemplar index"; verify §3.1 is the right cross-ref against the current section structure.
- **Tense consistency** in methods (past tense for completed work) and results (past tense for findings).
- **US English** throughout (already established convention).
- **Backticks vs. italics for rubric codes** (`robust`, *robust*) — currently mixed; minor typesetting question, low priority unless agents flag.

## Risks the manuscript carries into submission

1. **κ = 0.289 below pre-committed threshold.** Mitigation in place: structural failure framed as construct-validity-relevant + diagnostic of where the field needs new instruments + treated as v1.0 baseline for future development (TR5).
2. **N = 36 case-level inference** does not reach significance under clustering-aware null (p = 0.58 family, p = 0.33 capability); cell-level p < 0.001 supported. Manuscript already discloses this honestly; reviewers should verify it is foregrounded, not buried.
3. **Single-coder primary pass.** Mitigated by sandboxed-LLM second-coder pass on 10% subsample + pre-committed v1.1 human second-coder.
4. **Ostensive-only coding** (no performative aspect). Mitigation: scope-condition declared in §2.

## Reviewer-feedback bar

Reviewers should:
- Score each section 1–10 on submission-readiness for ORM.
- Surface specific issues with section/paragraph/line references.
- Cap at 5 prioritized action items per agent.
- Provide replacement text for each action.
- **Not** re-litigate transplants TR1, TR2a, TR2c, TR4, TR5, TR6, TR7 (already applied and verified in this loop's pre-flight).
- **Not** propose changes to the title (just shipped at v39 after deliberate revision; out of scope for this loop).
- **Not** propose statistical reanalysis (numbers locked to `06_analysis_tables/section6_analysis_output.json`).
