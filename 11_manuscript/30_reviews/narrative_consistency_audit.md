# Manuscript Narrative-Consistency Pass

**Date:** 2026-04-21
**Target:** [10_drafts/10_manuscript.md](../10_drafts/10_manuscript.md)
**Reference:** [../../10_outputs/p1_typology_overview_table.csv](../../10_outputs/p1_typology_overview_table.csv) (post wave-2/3)

## TL;DR

Numbers and the overall argument hold together. One **real** issue (dangling
reference), two **wording-level** issues worth fixing, two **optional**
improvements. Thesis and §6 hypothesis verdicts align cleanly with §3-§5
evidence; H1/H2/H3 framing is consistent end-to-end.

## Issues — in priority order

### A1. Cox / DAISY is in the reference list but never cited in-text (real)

**Location:** [References](../10_drafts/10_manuscript.md) line 82
(`Cox, n.d.. AI Disclosure with DAISY. [C030_P1]`).

**Why it matters:** ORM and most methods journals flag orphan references at
desk review. A reader who looks for Cox via the body's Section-4 disclosure
thread won't find it.

**Fix (recommended):** add one citation in §4 where disclosure is already
named. Propose:

> "Structural prose polishing therefore looks shrinkable, while evaluation,
> credit allocation, and disclosure become more important rather than less
> important **(Cox n.d.)**."

**Alternative:** drop Cox from the reference list and also remove
`[C030_P1]` from the provenance tail. Recommendation is to keep Cox —
Case 30 is a direct source of evidence for the disclosure-side argument
you are already making.

### A2. Abstract's four-item shrinkage list doesn't match the typology's three shrinking clusters (wording)

**Location:** Abstract, line 5:
> "the cleanest shrinkage is concentrated in routine first-pass screening,
> **high-consensus coding, technical repair**, and structural prose polishing"

**Typology table** has *three* `shrinking_task_cluster` roles:
- Routine first-pass screener (13 shrinking)
- Routine coder on high-consensus, ground-truth-rich tasks (15 shrinking)
- Structural prose polisher / drafter (12 shrinking)

"Technical repair" is not a separate role cluster; it is Case 28 (code
package repair), which is coded under *Routine coder on high-consensus
tasks*. The abstract's four-item list conflates cluster-level and
case-level units.

**Fix (recommended):**

> "the cleanest shrinkage is concentrated in **three task clusters**:
> routine first-pass screening, **high-consensus coding on ground-truth-rich
> tasks (including code-package repair)**, and structural prose polishing"

### A3. §3's "27 observable-present cases" is undercounted by 5 if split/merge_pressure are treated as observable (wording)

**Location:** §3, line 29:
> "a total of 27 observable-present cases and zero shrinking"

**Typology row for Protocol and provenance architect:** 15 robust + 5
conditional + 7 transformed + 4 split_pressure + 1 merge_pressure = 32
observable-present cases out of 36 (4 are `not_applicable`).

The "27" treats only robust+conditional+transformed as observable-present.
That's a defensible reading of "stable yes-variant status," but the phrase
`observable-present` reads as broader.

**Fix (recommended):**

> "a total of **27 cases where the role is present with a stable status
> (robust, conditional, or transformed), plus 5 cases under split or merge
> pressure**, and zero shrinking"

Or simpler:

> "a total of 27 cases in robust, conditional, or transformed status and
> zero shrinking (5 further cases register split or merge pressure)"

### B1. Kang 2025 (REPRO-Bench / Case 27) cited only once, in §1 intro (optional)

**Context:** §4 has a paragraph on post-publication repair that cites
Bleier (Case 28) but not Kang (Case 27). REPRO-Bench is the reproducibility
*assessment* anchor; Bleier/Case 28 is the reproducibility *repair* anchor.
They belong together in §4.

**Fix (optional):** extend the Bleier sentence in §4:

> "In the controlled reproducibility testbed, agents and prompt-based
> systems can repair some broken code packages, especially when the
> environment is standardized and the failure mode is visible. But success
> varies materially with error complexity, context, and diagnostic quality
> (Bleier n.d.). Agentic assessment of reproducibility itself — not just
> repair — exhibits the same pattern: best current agents score only in
> the 20-37% range on full assessments, keeping humans firmly in the
> auditor role (Kang 2025)."

Keeps the paragraph anchored on two complementary Case 27/28 findings.

### B2. §3 heading says "Procedure, Boundary Setting, and Calibration" but the section covers procedure + calibration; boundary-setting is in §5 (optional)

**Location:** §3 heading line 27:
> "## 3. Durable Roles: Procedure, Boundary Setting, and Calibration"

The three paragraphs of §3 treat (i) procedure, (ii) review automation as
a variant of procedure, (iii) calibration. Construct/perspective boundary
setting as a role appears substantively in §5 (split-pressure).

**Fix (optional):**

Rename to **"§3. Durable Roles: Procedure, Review Protocol, and Calibration"**
*or* **"§3. Durable Roles: Procedure and Calibration"**.

Not worth changing if you plan to keep boundary-setting as an implicit
thread across §3 and §5.

## What passes

- **Abstract's quantitative claims match the typology table** (15/5/7 for
  Protocol; 8/10 for Calibration). Verified against
  [p1_typology_overview_table.csv](../../10_outputs/p1_typology_overview_table.csv).
- **§4 shrinkage counts match** (13/15/12; aggregate 40).
- **§4 accountability counts match** (5/8/7/6 = 26 observable + 1 merge = 27
  out of 36; consistent with Accountability row of typology).
- **Hypothesis mapping H1/H2/H3 is consistent** between §1 statement and §6
  verdict.
- **Eight family clusters** — confirmed 8: Predictive simulation & design,
  Measurement & coding, Evidence synthesis & corpus, Agenda/theory/discovery,
  Interviews/fieldwork/qualitative, Reproducibility & autonomous research,
  Governance/authorship/labor, Pedagogy & training. §2's shorter list
  ("particularly strong representation in...") is explicitly non-exhaustive
  so the mismatch with the abstract's seven-domain list is fine.
- **All other in-text citations resolve to reference list entries**:
  Abbott, Amershi, APE, Baccolini, Bleier, Gligorić, Grimmer, Ha, Hernandez,
  Kang, Keith, Larson, Li, Shneiderman, Tornberg, Xiao, Yin — all present.
- **§2 source-provenance sentence matches the refreshed database state**:
  93 source rows (57 external), all 36 cases analysis-ready, 437/165/10
  confidence distribution. Matches `data_inventory.md` exactly.
- **§2 "institutional PDF retrieval" sentence matches reality**: the four
  blocked URLs (C001_P1, C005_P1, C035_P1, C036_S1) are now all local and
  open as of today's session.
- **§5's "150 autonomous agents" figure for Case 24** matches the Case 24
  source and the wave-3 evidence-basis summary.
- **§7 conclusion** stays inside the `framework` claim ceiling; no
  overclaim relative to §6 caveats (publication bias, repository coding
  bias, benchmark artificiality).

## Suggested apply pass (3 minutes of edits)

1. **A1 fix**: insert `(Cox n.d.)` in the disclosure sentence of §4 line 43.
2. **A2 fix**: rewrite the shrinkage list in the Abstract line 5.
3. **A3 fix**: tighten the "27 observable-present cases" phrasing in §3 line 29.
4. (Optional) **B1 fix**: add one sentence citing Kang 2025 in §4 reproducibility paragraph.
5. (Optional) **B2 fix**: rename §3 heading.

Then regenerate `.docx` via the same `write_docx_from_markdown` helper used
last time (~2 seconds).

No structural rewrite, no numeric changes. Thesis intact.
