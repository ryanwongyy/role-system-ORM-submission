# Transplant Specs — Three Priority Structural Moves

**Date:** 2026-04-22
**Target manuscript:** [`../10_drafts/10_manuscript.md`](../10_drafts/10_manuscript.md) — *From Repository to Role System: A Comparative Typology Audit of 36 Cases* (154 lines)
**Source templates:** Aguinis, Ramani & Alabduljader (2023, *ORM*); Aguinis & Solarino (2019, *SMJ*); Hickman, Thapa, Tay, Cao & Srinivasan (2022, *ORM*). See [`template_candidates.md`](template_candidates.md) for full ranking and [`template_pdfs/`](template_pdfs/) for local PDFs.

This document fixes the exact structural moves to transplant into the manuscript before the full rewrite pass, so that each move has a named edit site, a named before/after shape, and target prose you can paste, edit, and approve (or reject) without re-deriving the design decision.

It is deliberately narrow. It covers only the three highest-leverage transplants identified in [`template_candidates.md`](template_candidates.md) §Recommendation. Lower-priority moves (stage-organised recommendations table from Aguinis et al. 2021; diagnostic-criteria figure from Tay et al. 2022) are out of scope and should only be picked up if a reviewer asks.

---

## Transplant 1 — Aguinis, Ramani & Alabduljader (2023): tripartite abstract + Exemplars + stakeholder-named conclusion

This is the highest-leverage single move. Aguinis 2023 is the closest template (same journal, same genre, same "categorise + content-analyse + recommend" scale) and their three-part contribution frame is the one ORM reviewers will recognise as a well-formed methodological-review paper. The transplant has three parts that should land together, because the frame opens in the abstract, lands in the findings, and closes in the conclusion. Doing one without the others creates structural asymmetry.

### 1a. Abstract — rewrite as "three contributions"

**Edit site.** `10_manuscript.md` lines 3–5 (the Abstract block, currently a single ~250-word thesis-first paragraph).

**Before shape.** Problem → approach → finding → claim ceiling, with the three-part structure implicit. The reader has to infer that the paper is doing three things (building the database, auditing the typology, producing a cautious framework).

**After shape.** Same word count. First sentence: framing problem (unchanged in spirit). Second sentence: explicit "This paper makes three contributions." Third through fifth sentences: "First… Second… Third…" — each sentence naming one deliverable. Remaining sentences: core comparative finding + claim ceiling (largely preserved from the current abstract). The headline numbers (15 robust for protocol and provenance architect; 8 robust / 10 conditional for calibration architect; 40 shrinking observations) stay in the Third contribution sentence, not earlier, so they read as evidence of the typology rather than as the paper's thesis.

**Target prose (ready to paste).**

> Debate about AI in research is still often framed as a contest between humans and models. That framing is too coarse for the current evidence. **This paper makes three contributions.** *First*, it recasts a source-backed repository of 36 cases — spanning measurement, evidence synthesis, qualitative interpretation, simulation, reproducibility, governance, and autonomy-heavy boundary systems — as a **role-system dataset**, with 93 source rows, 144 evidence extracts, and 612 role-coding rows traced to local full-text PDFs. *Second*, it develops a **comparative typology** that distinguishes durable, transformed, shrinking, and split-pressure role statuses, and specifies behavioural anchors that make each status externally auditable. *Third*, it applies the typology to the 36 cases and reports the resulting pattern: protocol and provenance architect is robust in 15 cases, conditional in 5, and transformed in 7; calibration architect is robust in 8 and conditional in 10; by contrast, cleanly shrinking work is concentrated in three throughput clusters — routine first-pass screening, high-consensus coding on ground-truth-rich tasks (including code-package repair), and structural prose polishing — which together account for 40 shrinking observations. Autonomy-heavy systems such as Project APE and The AI Scientist remain useful boundary-pressure cases but do not license claims that human research roles have broadly disappeared. The paper's claim ceiling is therefore deliberately set at *comparative typology audit* with a `framework` rather than *validated theory of automated science*.

**Drafting notes.**
- Word count ≈ 240, within the current 250-word envelope and ORM's ~250–300 abstract guideline.
- Bold "This paper makes three contributions" is for the spec; remove the bold before submission (ORM does not use bold in abstracts).
- Italicised "First / Second / Third" mirrors Aguinis et al. 2023 pp. 47–48 exactly.
- The database accounting sentence (93 source rows / 144 evidence extracts / 612 role-coding rows) is kept in the abstract because Aguinis 2023's abstract carries its headline counts (168 reviews, 42 journals) up front — it is genre-appropriate.

**Risk.** The current abstract's opening claim — that human-vs-AI framing is too coarse — is the manuscript's signature rhetorical move and must not be diluted. Kept verbatim in the new draft.

---

### 1b. Findings — add an Exemplars subsection at the top of §3

**Edit site.** Insert between `10_manuscript.md` line 51 (heading `## 3. Durable Roles…`) and line 53 (current opening paragraph).

**Before shape.** §3 jumps straight into a prose exposition that implicitly uses Keith 2026, Baccolini 2026, and Larson 2024 as exemplars without labelling them as such. A reviewer who wants to know "which case is the canonical instance of robust protocol-and-provenance architect?" has to infer the answer from the third sentence of paragraph 1.

**After shape.** A compact **§3.0 Exemplars** paragraph (≈120 words) or a six-row inset box that names one exemplar case per role status, with a case ID and a one-line reason. Serves as an index into the findings. Aguinis et al. 2023 do this in their Table 2 and the paragraph immediately preceding it (pp. 54–55), naming exemplar reviews for each of their 7 typology categories.

**Target prose (ready to paste as §3.0).**

> **3.0 Exemplars.** Before turning to the durable-role pattern, we name one exemplar case per status to index the argument. For **robust** roles, Keith (2026; Case 2) exemplifies *protocol and provenance architect*: the measurement workflow is explicit about preparation, behavioural testing, labelled evaluation, and error analysis before any model is treated as a measurement instrument. For **conditional** roles, Larson (2024; Case 21) exemplifies *calibration architect*: synthetic personas are usable for means and simple descriptives but require human calibration on variance, sign stability, prompt sensitivity, and higher-order relationships. For **transformed** roles, Cox (n.d.; Case 30) exemplifies *accountability and labor allocator*: the role does not disappear but is redefined around disclosure, credit allocation, and human-legible labour traces. For **shrinking** task clusters, Tornberg (2025; Case 1) exemplifies the *routine coder on high-consensus, ground-truth-rich tasks*: GPT-4 outperforms supervised classifiers and human coders on objective party-affiliation annotation, yet the surrounding interpretive role is not removed. For **split pressure**, Gligorić (n.d.; Case 3) exemplifies *construct-vs-perspective boundary setting*: disagreement across subgroups is the quantity of interest, so a single correction target collapses the inferential object. For **merge pressure**, Yin (n.d.; Case 29) is the clearest instance: authorship and labor-allocation signals tangle once prose polishing is outsourced. These exemplars are referenced by case ID throughout §§3–5.

**Drafting notes.**
- Case selections are first-pass; they correspond to the cases already carrying the most narrative weight in §§3–5. Swap any that have moved in the latest coding pass.
- The six statuses (robust / conditional / transformed / shrinking / split_pressure / merge_pressure) map one-to-one onto the BARS table in Transplant 2. Keep the exemplar case IDs consistent across the two tables.
- If the Exemplars paragraph reads too dense as prose, migrate to a six-row inset box with columns [Status | Exemplar case | One-line reason]. Either form works; prose is easier to typeset in ORM's two-column layout.

**Risk.** Fixing a single exemplar per status freezes an editorial call that the codebook currently leaves open — a case can be the exemplar of *robust protocol-and-provenance architect* and of *split pressure on counterfactual-and-transportability judge* simultaneously. State this explicitly in the Exemplars paragraph ("cases are named as exemplars of one status each for expositional economy; the full status profile for every case is in the released database") so a reviewer does not over-read the selection.

---

### 1c. Conclusion — name the stakeholder audiences and the delivered artifact

**Edit site.** `10_manuscript.md` lines 129–133 (§7 Conclusion, currently two paragraphs).

**Before shape.** The conclusion ends with "not from human research to machine research, but from one research role system to another" — a strong rhetorical close that makes no address to specific reader groups and does not foreground the repository + codebook as the shippable artifact. Aguinis et al. 2023 pp. 68–70 close by naming three stakeholder audiences (producers, evaluators, users) and stating what each gets from the framework.

**After shape.** Keep paragraph 1 of the current conclusion (the "durable question" recap). Replace the final paragraph with a three-sentence stakeholder close — one sentence each for methods researchers, reviewers/editors, and institutional actors (PhD programmes, journal methods policy, replication archives) — plus one sentence naming the released repository and codebook as the paired deliverable.

**Target prose (ready to paste as the new final paragraph of §7).**

> The framework is built to be used by three audiences. For **methods researchers**, it offers a role-first vocabulary for designing future studies — one that distinguishes *which* role is changing rather than asking whether "AI" helps overall — and six behaviourally-anchored status categories that can be applied to a new case without opening the underlying database. For **reviewers and editors**, it offers an audit scaffold: the role × status table and the exemplar index make it straightforward to check whether a manuscript's automation claims are located at the task-cluster layer (where shrinkage is defensible) or at the role layer (where the evidence in this repository does not support disappearance). For **institutional actors** — PhD training, methods-policy committees, and replication archives — it offers a diagnostic for the roles that remain constitutive of valid research and therefore warrant curricular, editorial, and provenance investment even as throughput tasks migrate. The paired deliverable is not the manuscript alone but the released 36-case database, codebook, and status rubric; the comparative typology audit is their analytic expression, and readers are invited to apply, contest, and extend the coding on the released case files.

**Drafting notes.**
- Three stakeholders chosen to mirror Aguinis et al. 2023's "producers / evaluators / users" while re-specifying for the P1 audience. *Methods researchers* ≈ producers; *reviewers and editors* ≈ evaluators; *institutional actors* ≈ users.
- "Paired deliverable" language forecloses the ambiguity in §2 line 21 about whether the paper or the database is the artifact. ORM's data-availability norms make this an asset.
- Keeps the current closing sentiment ("from one research role system to another") alive in paragraph 1, which stays unchanged.

**Risk.** Naming institutional actors introduces an implicit policy claim. Keep the verb "offers a diagnostic" — not "recommends" — to stay inside the `framework` claim ceiling.

---

## Transplant 2 — Aguinis & Solarino (2019): BARS table for role statuses

This addresses the single most likely reviewer objection: that role-status coding is insufficiently specified for a single-coder audit. Solarino's paper audited 52 *SMJ* articles against a 12-criterion framework and shipped a behaviourally-anchored rating scale (BARS) that made every criterion replicable without consulting the authors. A one-page BARS table for the six P1 statuses materially closes that objection.

### 2. Add Table 1.5: Role-Status Rubric with Behavioural Anchors

**Edit site.** Insert between `10_manuscript.md` line 25 (end of the "live-project / autonomy-heavy systems" paragraph) and line 27 (current "Table 1 summarises…" paragraph). New table should be numbered **Table 1** (current Table 1 becomes Table 2; downstream Tables 2a/2b/3 become 3a/3b/4). Alternatively, number it **Table 1 continued** or call it **Box 1** to avoid downstream renumbering; style choice.

**Before shape.** The six statuses are defined prosaically in §2 line 23: "Some starting roles may split… Some roles may merge… some recurring activities may be better described not as durable roles but as shrinking task-clusters." A reader cannot tell from the manuscript text alone what observable evidence would distinguish *robust* from *conditional*, or *shrinking* from *transformed*.

**After shape.** A six-row × four-column table. Columns: **Status** (one of the six) | **Operational definition** (prose, one sentence) | **Behavioural indicator: what would count as evidence** (two or three observable signals) | **Counter-indicator: what would rule this out** (one signal). This is the Solarino 2019 BARS pattern compressed from their 12-criterion × 5-level grid onto a 6-status × 3-column grid appropriate for the P1 status set.

**Target prose (ready to paste as Table 1).**

> **Table 1. Role-status rubric with behavioural anchors.** Each status is defined by observable features of the case so that a second coder can apply the rubric without consulting the authors. Rows are mutually exclusive within a (role × case) cell but not across cells of the same role (a single role may be *robust* in one case and *shrinking* in another).
>
> | Status | Operational definition | Behavioural indicators (evidence *for*) | Counter-indicator (evidence *against*) |
> |---|---|---|---|
> | **Robust** | The role is performed by humans in the case and its performance is constitutive of the study's validity. | (a) Case explicitly treats the role as methodologically load-bearing; (b) authors specify human labour at this step and describe why AI substitution would not preserve validity; (c) role appears in the reported limitations if omitted. | Case reports AI performing the role without human checking and reports no validity loss. |
> | **Conditional** | The role is performed by humans contingent on specified moderators (task features, data quality, institutional setting); AI can partially substitute outside those moderators. | (a) Case specifies the conditions under which human performance is needed; (b) reports empirical variation in AI adequacy across those conditions; (c) retains a human-in-the-loop step for edge cases. | Case reports blanket human or blanket AI performance with no moderator analysis. |
> | **Transformed** | The role persists but its content has been redefined around AI involvement (e.g., from drafting to reviewing, from coding to auditing, from authoring to disclosing). | (a) Case describes a qualitative shift in what humans do at this step; (b) new sub-tasks (disclosure, credit allocation, calibration audit) are introduced; (c) the pre-AI role description no longer fits. | Case reports the role as unchanged, or reports it as absent. |
> | **Shrinking** | The task-cluster is increasingly performed by AI with human labour reduced to audit or exception handling; the role label is retained but its scope has contracted. | (a) Public ground truth or high-consensus targets exist; (b) case reports AI matching or exceeding human performance on a defined subset; (c) residual human labour is characterised as rescue, triage, or verification. | No public ground truth; disagreement across coders is the inferential object. |
> | **Split pressure** | The case reveals that the starting role conflates two distinct activities that should be coded separately (e.g., *construct boundary setting* and *perspective sampling*). | (a) AI performance differs systematically across the conflated sub-activities; (b) the case's own analysis distinguishes them; (c) collapsing them back into one role loses substantive information. | Case treats the role as indivisible and the evidence supports that treatment. |
> | **Merge pressure** | The case reveals that two starting roles are entangled in practice and cannot be cleanly separated without losing information (e.g., *authorship* and *labor allocation* in LLM-assisted drafting). | (a) The case's evidence for one role is inseparable from evidence for the other; (b) attempting to code them independently produces arbitrary splits; (c) the case authors themselves treat the two as a joint object. | The two roles are coded independently with no loss of information. |

**Drafting notes.**
- Six rows, one per status. No empty or "reserved" rows.
- Column 3 is the BARS anchor — three observable signals, (a)/(b)/(c) — mirroring Solarino 2019 Table 3 (p. 1303). Column 4 is the anti-anchor, which Solarino does not include but which improves usability for a single new coder and handles the question "how would I know it *isn't* this?"
- Table should fit on one ORM manuscript page. At roughly 30 words per cell × 4 columns × 6 rows = 720 words, it is close to that limit; trim column 2 to one sentence per row if needed.
- Keeping this as Table 1 (and renumbering downstream tables) puts the rubric *before* the role × status counts, so the reader sees the measurement instrument before the measurement. Renumbering cost: three Find/Replace operations in the draft.

**Risk.** A BARS table invites reviewers to test it by re-coding a sample case. That is a feature, not a bug — but expect at least one reviewer to ask for an inter-coder agreement statistic on a subsample. Pre-empt by adding one sentence after the table: "Inter-coder agreement on a random 10% subsample (3–4 cases, double-coded by a second rater) is reported in Appendix B; Cohen's κ = [TBD] across the six statuses." Generating that κ is a post-submission task, not part of this transplant; flag it on the submission checklist.

---

## Transplant 3 — Hickman, Thapa, Tay, Cao & Srinivasan (2022): two complementary lenses framing for Tables 2a/2b

Hickman et al. 2022 organise their text-preprocessing review around two complementary reviews — computational linguistics and organisational text mining — and frame their joint findings as *triangulated* across the two. The P1 manuscript has structurally identical material (Table 2a by case family, Table 2b by AI capability) but currently presents them as two independent tables with a pieced-together verdict. Reframing as two lenses converging on H3 is a structural move with minimal prose cost and a large clarity gain.

### 3. Reframe Tables 2a/2b as two complementary lenses on H3

**Edit site.** Two edits:
- `10_manuscript.md` line 83 — the sentence introducing Table 2a ("Tables 2a and 2b give the simplest repository-level test of H3").
- `10_manuscript.md` line 108 — the "Read together, the two tables support H3 only partially" paragraph.

**Before shape.** Line 83 sets up the two tables flatly ("simplest repository-level test"); the two tables appear in sequence; line 108 synthesises them with "Read together…" — correct but under-structured. A reviewer reading quickly cannot tell which conclusions come from lens 1 alone, lens 2 alone, or their triangulation.

**After shape.** Explicit two-lens framing. Lens 1 (case family) asks: *does what the research is doing predict role status?* Lens 2 (AI capability) asks: *does the tool modality predict role status?* Paragraph after 2b is reorganised as **lens-1 verdict → lens-2 verdict → convergence**, so the H3 conclusion is licensed by the triangulation rather than being asserted over two loosely linked tables.

**Target prose 1 — replace line 83.**

> We test H3 through two complementary lenses on the same 612 role-coding observations. **Lens 1** (Table 2a) asks whether *research kind* — what the study is methodologically doing — predicts role status, pooling across AI capability. **Lens 2** (Table 2b) asks whether *AI-capability modality* — generative, agentic, or predictive — predicts role status, pooling across research kind. H3 is supported as a repository pattern only if the lens-1 association is consistently larger than the lens-2 association; a comparable or weaker lens-1 effect would indicate that capability modality, not research kind, is doing the work.

**Target prose 2 — replace the paragraph at line 108.**

> **Lens 1 verdict.** Case family clearly matters. Measurement & coding is robust-heavy (18 robust / 21 conditional / 5 shrinking); Evidence synthesis & corpus is shrinking-heavy (10 shrinking / 6 robust); Agenda, theory & discovery is conditional-heavy (18 conditional / 2 robust); Interviews, fieldwork & qualitative interpretation is split-pressure-heavy (12 split pressure). These are differences of kind, not only of degree. **Lens 2 verdict.** AI capability also matters. Generative cases lean conditional; agentic cases carry most of the shrinkage (22 of 40 observations) and the highest split-pressure density per case; predictive cases are relatively robust but concentrate transportability-related split pressure. **Convergence.** A formal test sharpens the comparison. Restricting to observable-present statuses (robust, conditional, transformed, shrinking, split-pressure, merge-pressure) and pooling across all 17 roles, a χ² test of independence yields χ² = 87.67 (df = 35, *p* < 10⁻⁵, Cramér's V = 0.260) for status against case family and χ² = 29.80 (df = 10, *p* < 10⁻³, Cramér's V = 0.240) for status against AI capability. Both associations are statistically significant — capability is not a residual variable — but case family is the stronger associate, and the per-role robustness check is sharper still: for 14 of 17 roles Cramér's V is larger across case family than across AI capability (median V_family = 0.587 versus median V_capability = 0.442), so the aggregate difference is not being carried by a handful of atypical roles. The two lenses converge on the same verdict. H3 is supported as a repository pattern: research kind is the dominant predictor of role status, with AI capability as a meaningful but secondary dimension that the typology does not explain away.

**Drafting notes.**
- Three bold subheads (Lens 1 verdict / Lens 2 verdict / Convergence) are for the spec; delete the bold before submission — ORM uses italicised run-in heads for this kind of tripartite argument structure (Aguinis et al. 2023 p. 58 does exactly this). The word "Convergence" may or may not survive stylistic editing; the *structure* is the transplant.
- All the statistics in Target prose 2 are preserved verbatim from the current draft (line 108). The transplant is *organisational*, not analytical; no numbers change.
- Hickman et al. 2022 §3 pp. 119–122 is the specific template; two lenses, a one-sentence setup for each, and a convergence paragraph.

**Risk.** The two-lens framing forecloses an alternative reading in which the two tables show *distinct* effects that should be modelled jointly rather than triangulated. If a reviewer pushes for a joint model (e.g., status ~ family + capability, with family × capability interaction), the convergence framing makes that extension natural rather than defensive. Note for the submission checklist: be ready to add a supplementary joint-model table if asked.

---

## Summary — three transplants in sequence

| # | Transplant | Edit site(s) | Net new prose | Net restructuring | Reviewer risk if skipped |
|---|---|---|---|---|---|
| 1a | Tripartite abstract | Lines 3–5 | ~0 words (rewrite) | Paragraph restructured | High — current abstract reads as thesis-first, not methods-review-first |
| 1b | Exemplars §3.0 | After line 51 | ~200 words | New subsection | Medium — reviewer can infer exemplars but must do work |
| 1c | Stakeholder-named conclusion | Lines 129–133 | ~180 words (replaces 2 paragraphs) | Replace final paragraph | Medium — current close is strong but audience-silent |
| 2 | BARS role-status table | After line 25 | ~720 words (table) | New table + 3 renumbers | **High** — single-coder objection is the likeliest desk-reject trigger |
| 3 | Two-lens framing Tables 2a/2b | Lines 83 + 108 | ~0 words (rewrite) | Restructure paragraph | Low — clarity gain, not evidentiary gain |

Estimated total edit surface: ~1,100 words rewritten or added, one new table, three table renumberings. No changes to §§4, 5, 6 narrative paragraphs. No changes to the reference list.

**Ordering.** Apply in the order 2 → 1a → 1b → 1c → 3. Transplant 2 (BARS) is first because it sets the measurement instrument on which Transplant 1b (Exemplars) depends. Transplants 1a and 1c bracket the paper and should land together. Transplant 3 is last because it is the cheapest and carries the lowest reviewer risk.

## What this spec does *not* fix

- **Case-ID stability.** Transplants 1b and parts of 2 assume Case 1 = Tornberg 2025, Case 2 = Keith 2026, etc. Confirm against the current case registry before pasting.
- **Inter-coder κ.** Transplant 2 creates the commitment to report Cohen's κ on a double-coded 10% subsample; generating that statistic is a separate task.
- **Supplementary joint-model table.** Transplant 3 creates a latent commitment to be able to produce status ~ family × capability if asked; not required for the transplant itself.
- **Figure.** None of the three transplants require a figure. If a figure is added (e.g., a one-page role × status workflow diagram per Tay et al. 2022), it is an additional transplant, not a dependency.

## Next action

Review this spec. Approve, amend, or reject the three target-prose blocks. Once approved, the rewrite pass applies them in the order above, then runs the full `/edit` or `/rolemanuscript` loop for polish on the modified sections only.
