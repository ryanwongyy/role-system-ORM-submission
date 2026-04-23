# Template vs. Manuscript — Major Differences

**Date:** 2026-04-23
**Manuscript version:** v11 (11,018 words + ~5,800 appendix words)
**Templates compared:** 5 unique papers (6 PDFs — Aguinis 2023 ships as two copies)
**Companion files:**
- [`template_candidates.md`](template_candidates.md) — ranked template analysis with "Features to borrow"
- [`transplant_specs.md`](transplant_specs.md) — specific transplants already applied

This file is the third leg of that trio. Its role is *differences*, descriptively — what the manuscript is NOT doing that the templates do, and what the manuscript does that the templates don't. It makes no recommendations; those live in the two companion files.

---

## 1. Consolidated comparison matrix

| Paper | Venue | Year | Word count | Cases / papers audited | Tables | Figures | Appendices | Claim-ceiling term | Primary evidentiary base |
|---|---|---|---:|---|---:|---:|---|---|---|
| Aguinis, Ramani & Alabduljader | *ORM* | 2023 | 17,062 | 168 methodological reviews across 42 journals | 3 | 0 | 6 (A–F) | Checklist for **producers / evaluators / users** | Content analysis; 40 observable indicators across 7 review-type typology |
| Aguinis & Solarino | *SMJ* | 2019 | 14,509 | 52 SMJ elite-interview articles | 4 | 1 | Supporting info S1–S4 | Transparency & replicability **framework** + BARS | Audit of 12-criterion transparency framework on qualitative method reporting |
| Hickman, Thapa, Tay, Cao & Srinivasan | *ORM* | 2022 | 17,739 | Two literatures (computational linguistics + organizational text-mining) | 5 | 1 | 3 (A–C) | Best-practice **decision framework** for preprocessing | Content analysis of two independent research communities; moderator-conditional recommendations |
| Aguinis, Villamor & Ramani | *JoM* | 2021 | 7,802 | 510 empirical papers in 15 journals | 3 | 0 | 8 (A–H) | **Stage-organized recommendations** (planning / implementation / reporting) | Systematic review of MTurk practice prevalence |
| Tay, Woo, Hickman, Booth & D'Mello | *AMPPS* | 2022 | 22,152 | 0 (conceptual framework, no empirical audit) | 3 | 4 | 0 | **Conceptual framework** for diagnosis and mitigation | Literature-grounded conceptual model of machine-learning measurement bias |
| **Manuscript v11** | *ORM* (target) | 2026 | 11,018 (+ ~5,800 appendix) | **36 cases × 17 roles = 612 role-coding cells** | **8** | **1** | **5 (B–F)** | **Preliminary framework** (typology audit) | Content analysis + role × status coding; second-coder LLM-agent κ = 0.289 flagged as below threshold |

Matrix reading: the manuscript is closest to Aguinis 2023 in role (both are ORM typology-audits with checklist-adjacent deliverables) but lower in word count and lower in claim ceiling; closest to Solarino 2019 in audit size (36 cases ≈ 52 articles) and BARS-like rubric; closest to Hickman 2022 in two-lens framing but with two lenses on the *same* 612 cells rather than on two independent literatures.

---

## 2. Per-template major differences

### Aguinis, Ramani & Alabduljader (2023), *ORM*

**Scope & structure.** Aguinis 2023 audits whole published papers (168 reviews) against a 7-category *review-type* typology. The manuscript audits *role × case* cells (612 rows) nested in 36 cases against a 6-status *role-status* rubric.

**Evidentiary base.** Aguinis 2023 ships 10 latent factors with 40 observable indicators derived from content analysis of 168 reviews; the manuscript ships 6 statuses with 3 behavioral indicators plus 1 counter-indicator each, derived from the rubric as designed.

**Claim ceiling.** Aguinis 2023 commits unambiguously to an actionable checklist; the manuscript downgrades to "preliminary framework" after κ failure. The word "preliminary" is the main-text marker of this contrast.

1. Aguinis 2023 treats typology as *fixed*; the manuscript treats the typology as *partially mutable* (split/merge pressure as reconfiguration axes).
2. Aguinis 2023 does not report coder confidence within the scheme; the manuscript stratifies by high (437) / medium (165) / low (10).
3. Aguinis 2023's sampling frame is peer-reviewed journal articles only; the manuscript's frame mixes published + preprint + live-project + boundary cases.
4. Aguinis 2023 does not grapple with within-paper nesting (each paper = one observation); the manuscript must handle 17-cells-per-case clustering, producing three inferential objects with divergent verdicts.

### Aguinis & Solarino (2019), *SMJ*

**Scope & structure.** Solarino 2019 audits 52 articles against a 12-criterion BARS framework; each criterion gets 5 ordinal levels. The manuscript audits 612 cells against 6 statuses with 3 behavioral indicators + 1 counter-indicator per status — flatter than Solarino's multi-level BARS.

**Evidentiary base.** Solarino 2019 audits *manuscript transparency* on qualitative reporting; the manuscript audits *role status* in research workflows. The BARS model transfers; the subject matter does not.

**Claim ceiling.** Both are auditor-facing frameworks. Solarino 2019 does not foreground a reliability-failure remedy; the manuscript does.

1. Solarino 2019's BARS has 5 ordinal levels per criterion; the manuscript's rubric has 3 parallel indicators per status. A SMJ-fidelity read would prefer graduated levels; Table 1 keeps the flatter structure to preserve readability.
2. Solarino 2019 does not report κ in main text (agreement is in supporting materials); the manuscript reports κ = 0.289 as a frame condition in §6.
3. Solarino 2019 targets journal editors and reviewers as the primary audience; the manuscript splits into three stakeholder groups (researchers, editors, institutional actors).
4. Solarino 2019 does not attach evidentiary remedies to reliability failure; the manuscript pre-commits three specific remedies (tie-breaker revision, observable-threshold tightening, claim-ceiling downgrade) in its pre-analysis plan.

### Hickman, Thapa, Tay, Cao & Srinivasan (2022), *ORM*

**Scope & structure.** Hickman 2022 compares *two literatures* (computational linguistics vs. organizational text-mining) as independent lenses on preprocessing decisions. The manuscript compares *two cuts on the same 612-cell coding* (case family vs. AI capability) — structurally parallel but evidentiarily weaker.

**Evidentiary base.** Hickman 2022's recommendations rest on cross-literature synthesis plus empirical performance comparisons on held-out corpora (their Table 7). The manuscript's rubric rests on coder reading of case files with no external-criterion validation.

**Claim ceiling.** Both claim "framework." Hickman 2022's framework is moderator-conditional ("if *X*, then *Y*"); the manuscript's framework is descriptive ("status *Z* appears in *N* cases").

1. Hickman 2022's two reviews are independent literatures; the manuscript's two lenses are strata on the same coding. The manuscript's §6 now flags this gap explicitly ("we adopt the *two-lens* label by analogy… both lenses are cuts on the same 612-cell coding rather than two independent literatures").
2. Hickman 2022 has Cohen's-et-al moderators (text type, research question, dataset characteristics); the manuscript tests case family and AI capability as post-hoc correlates, not *a priori* decision factors.
3. Hickman 2022 ships a user-facing decision tree (Figure 1 in their paper); the manuscript's Figure 1 is coder-facing (workflow schematic, not user decision aid).
4. Hickman 2022 does not face within-case clustering; the manuscript's 17-cells-per-case structure is the single largest inferential complication in §6.

### Aguinis, Villamor & Ramani (2021), *JoM*

**Scope & structure.** Aguinis-Villamor 2021 organizes recommendations along three research stages (planning / implementation / reporting); each stage has numbered actionable items. The manuscript's Table 5 (stakeholder × stage grid) transplants this structure and fills it with role-system-specific recommendations.

**Evidentiary base.** Aguinis-Villamor 2021 anchors each stage-recommendation to practice-prevalence counts from 510 papers; the manuscript anchors Table 5 cells to case IDs from the 36 (e.g., Case 3 for split pressure, Case 10 for merge pressure), not to prevalence counts. Structure transplanted; prevalence-grounding is weaker.

**Claim ceiling.** Aguinis-Villamor 2021 = "recommendations for robust MTurk research." Manuscript = "preliminary framework." Both are prescriptive but the manuscript hedges harder due to κ.

1. Aguinis-Villamor 2021's sample is 510 peer-reviewed empirical papers; the manuscript's is 36 mixed-provenance cases.
2. Aguinis-Villamor 2021 does not report case-level reliability or inter-coder agreement; the manuscript does and foregrounds its failure.
3. Aguinis-Villamor 2021 uses research-pipeline stage as the primary organizing axis; the manuscript uses role-system component as the primary axis, with stage as secondary (Table 5).

### Tay, Woo, Hickman, Booth & D'Mello (2022), *AMPPS*

**Scope & structure.** Tay 2022 is purely conceptual — a multi-level framework for measurement bias in ML assessment, with no empirical audit. The manuscript is empirical (612 coded cells); Tay 2022 is the outlier in the template set.

**Evidentiary base.** Tay 2022 is literature-grounded conceptual work; the manuscript is case-file-grounded empirical work. These are categorically different evidentiary modes.

**Claim ceiling.** Tay 2022 claims a conceptual framework for future research; the manuscript claims a preliminary framework with applied reliability evidence. Tay's ceiling is higher in ambition (general framework) but narrower in scope (ML measurement bias only).

1. Tay 2022 audits no cases; the manuscript audits 36. Tay 2022's absence of inter-coder disagreement is a consequence of this, not a methodological choice the manuscript could copy.
2. Tay 2022 ships 4 figures paired with a diagnostic-criteria table (their Figure 1 is a pipeline; Figure 4 is an expanded Brunswik lens). The manuscript ships 1 figure (coder-workflow schematic).
3. Tay 2022 is narrower in topic (measurement bias in psychological assessment); the manuscript is broader (role-system distribution across AI-embedded research workflows). Tay 2022's narrowness buys theoretical coherence; the manuscript's breadth buys empirical range.

---

## 3. Top 10 cross-template differences, ranked by stakes

1. **Claim ceiling + reliability transparency.** No template demotes its own framework in response to a reliability-failure signal. The manuscript does — "preliminary framework" after κ = 0.289 falls below the pre-committed 0.60 threshold — and pre-commits three specific remedies (§6, Appendix B). This is the manuscript's single biggest methodological departure from the template corpus, and a credibility-literature strength.

2. **Sampling frame heterogeneity.** Every template audits a homogenous corpus (peer-reviewed reviews; SMJ articles; cited papers in two established literatures; 15-journal empirical papers; conceptual literature). The manuscript mixes peer-reviewed papers + preprints + live-project repositories + autonomy-heavy boundary systems (5 of which are excluded in the Table 4 sensitivity check). Heterogeneity opens rival-explanations space the templates don't face.

3. **Typology mutability.** Aguinis 2023, Solarino 2019, Hickman 2022, and Aguinis-Villamor 2021 all use *fixed* typologies. The manuscript admits *split pressure* (39 of 612 cells) and *merge pressure* (2 of 612 cells) as reconfiguration axes, so the rubric itself is an analytic output, not only a measurement instrument. This is epistemically distinct — the manuscript is a typology-plus-revision-log, not a typology application.

4. **Nesting / clustering violates i.i.d.** Templates treat each audited paper or review as one observation. The manuscript has 17 cells per case × 36 cases = 612 observations that are *not* independent. §6 reports three inferential objects — cell-level Monte-Carlo (*p* = 0.0001), case-level Monte-Carlo (*p* = 0.57), role-level paired sign test (*p* = 0.004). The three verdicts diverge: the aggregate χ² association does not survive clustering correction; the role-level test does. Templates don't have this problem.

5. **Stakeholder framing explicitness.** Aguinis 2023 names producers / evaluators / users in its title. Aguinis-Villamor 2021 names planning / implementation / reporting stages. Solarino 2019 targets journal editors. The manuscript's original version did not name audiences up front; the §7 three-stakeholder move is a late transplant (per `transplant_specs.md` §1c).

6. **Within-scheme confidence stratification.** Templates audit presence/absence (Aguinis 2023, Aguinis-Villamor 2021) or BARS levels (Solarino 2019). The manuscript reports confidence labels on every cell: 437 high / 165 medium / 10 low. When restricted to high-confidence rows, the V_family vs. V_capability gap widens from 0.020 to 0.062 — a robustness check no template performs.

7. **Evidentiary density and source traceability.** Templates audit at the literature-count level. The manuscript requires every analytic field to trace back to source identifiers + local files, with 93 source rows + 144 evidence extracts + 612 role-coding rows. This is an order-of-magnitude denser audit trail than any template, which is both a strength (verifiability) and the origin of the inter-coder disagreement problem (what counts as an extract for this role?).

8. **LLM-agent second coder.** Aguinis 2023 and Solarino 2019 report human-coder agreement; Hickman 2022 does not report κ in the main text at all. The manuscript's second coder is a sandboxed LLM agent — explicitly "a weaker reliability test than a human second coder would provide." This is a material downgrade from templates, flagged as a pending commitment.

9. **Hypothesis pre-specification.** No template ships a pre-specification table documenting which design decisions were fixed pre-coding vs. revised post-pilot vs. added post-hoc. The manuscript includes one (lines 138–150), with H1, H2, H3 labeled as fixed pre-coding and the split/merge-pressure statuses labeled as added post-pilot.

10. **Boundary-case treatment.** Templates don't audit systems that lack pre-AI counterparts (Project APE, The AI Scientist, AgentSociety, Deep Research) because their corpora don't contain such systems. The manuscript identifies 5 such cases and reports a full sensitivity exclusion analysis (Table 4) showing headline findings survive. This is a problem templates don't face and a robustness check templates can't perform.

---

## 4. Genre-level diagnosis

The templates are **validated methodological audits** — each applies a fixed typology to a homogenous published corpus, audits completeness or quality, and ships an actionable tool (checklist, BARS, decision framework, stage-keyed recommendations). The evidentiary bar is "a reader can use this tool on a new paper without consulting the authors." Reliability is an operational detail; the typology is the deliverable.

The manuscript is a **typology-emergence audit under reliability constraint**. It audits a heterogenous corpus (published + preprint + live-project + boundary cases), with a typology that partially mutates during coding (split and merge pressure as reconfiguration axes), and reports inter-coder κ that falls below the pre-committed threshold — then treats that failure as a frame condition ("preliminary framework") with explicit pre-committed remedies. The evidentiary bar is lower per-cell ("cell-level reliability is below acceptance grade") but higher per-claim ("pattern-level hypotheses rest on aggregate distributions and the pre-specified sign test, not on cell-level reliability"). This is not a weaker paper — it is a different kind of paper. Templates say *here is how to evaluate X*; the manuscript says *here is what we found when we audited X, here is the rubric that makes it replicable, and here are the places where the rubric needs tightening*. The major differences documented above follow directly from that genre choice.
