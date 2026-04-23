# Manuscript vs Refreshed Database — Audit

**Date:** 2026-04-21
**Target:** [10_drafts/10_manuscript.md](../10_drafts/10_manuscript.md)
**Reference:** [../../10_outputs/p1_typology_overview_table.csv](../../10_outputs/p1_typology_overview_table.csv), [../../data_inventory.md](../../data_inventory.md) (both rebuilt post wave-2/3)

## Summary

The manuscript was drafted 2026-04-08 against the pre-wave-2/3 database.
Wave-2/3 raised 559 low-confidence rows into medium/high and flipped many
`status_in_case` values, especially in the shrinking-task cluster. **Ten
numeric claims in the draft are now stale.** The directional arguments
(durable procedural roles, shrinking throughput, split-pressure findings)
still hold — the paper is not structurally wrong, it just under-counts the
evidence for its own thesis.

## Stale numeric claims (required edits)

| # | Location | Current manuscript claim | Correct count (post wave-2/3) | Severity |
|---|---|---|---|---|
| 1 | Abstract | Protocol & provenance architect: robust **16**, conditional **10** | robust **15**, conditional **5**, transformed **7** | Moderate — two numbers wrong, and 7 cases now coded as `transformed` are ignored |
| 2 | Abstract | Calibration architect: robust **12**, conditional **3** | robust **8**, conditional **10** | Moderate — direction reversed on conditional (3 → 10); robust also down |
| 3 | §2 | "98 source rows, 270 evidence extracts, 612 role-coding rows" | **91** source rows (55 external), **144** evidence extracts, 612 role rows | Moderate — first two numbers are wrong |
| 4 | §2 | "All 36 cases are currently analysis-ready" | **34 analysis-ready, 2 partial** (Cases 1 and 5) | High — directly wrong; needs "34 of 36 are fully analysis-ready; Cases 1 and 5 are partial due to journal-page access limits, with lawful fallbacks in place" |
| 5 | §3 | Protocol & provenance architect: "robust in 16 cases and conditional in 10 more" (repeats claim 1) | robust 15, conditional 5, transformed 7 | Moderate |
| 6 | §3 | Calibration architect: "robust in 12 cases and conditional in 3" (repeats claim 2) | robust 8, conditional 10 | Moderate |
| 7 | §4 | Routine first-pass screener: "shrinking in **3 cases**" | shrinking in **13 cases** | **High** — understates a core finding by ~4×, directly weakens the shrinkage argument |
| 8 | §4 | Routine coder on high-consensus tasks: "shrinking in **2**" | shrinking in **15** | **High** — understates by ~7× |
| 9 | §4 | Structural prose polisher: "shrinking in **3**" | shrinking in **12** | **High** — understates by ~4× |
| 10 | §4 | Accountability and labor allocator: "transformed in **14** cases and conditional in **11**" | transformed **7**, conditional **8** (also robust 5, split_pressure 6) | Moderate — both numbers are inflated roughly 2×; "transformed dominates" narrative weakens, but split-pressure evidence (6 cases) is new and worth mentioning |

## Directional claims that still hold

These do **not** need rewriting, but the underlying numbers have changed enough
that you may want to replace them with the stronger post wave-2/3 versions:

- **"Boundary-setting and procedure-setting roles survive more often than
  routine production tasks"** — still supported. Protocol & provenance
  architect totals 27 observable-present cases (15 robust + 5 conditional + 7
  transformed), versus routine first-pass screener where all 13 observable
  cases are shrinking. Direction is **stronger** than the draft suggests.
- **"The cleanest shrinkage is concentrated in routine first-pass screening,
  high-consensus coding, technical repair, and structural prose polishing"**
  — correct, and more strongly supported: the three shrinking-task clusters
  now account for 13+15+12 = **40 shrinking cases**, up from the 8 total the
  draft implies. This is the paper's most visible underclaim.
- **"The repository creates pressure to split several inherited roles"** —
  still correct and arguably stronger now: split_pressure totals **39 cases**
  across roles, concentrated in mechanism disciplinarian (4), construct and
  perspective boundary setter (4), accountability and labor allocator (6),
  and perspective sampler (4). The draft's specific split examples
  (construct boundary from perspective sampling; calibration from
  transportability) both appear in the data.

## New findings worth adding

Post wave-2/3, the data supports a few claims the draft omits:

- **`transformed` is a meaningful middle category.** Protocol and provenance
  architect (7 transformed) and Accountability and labor allocator (7
  transformed) both show this. The draft reads as if `transformed` is rare;
  in the refreshed data it is present across most starting roles.
- **Routine-first-pass-screener shrinkage is the most clean-cut empirical
  signal.** 13 of 13 observable cases are coded shrinking, 0 robust — a
  stronger pattern than any durability claim in the paper.
- **Role-coding confidence profile:** 437 high, 165 medium, 10 low (out of
  612 total). The draft does not currently report this but it directly
  strengthens the "source-backed" claim. Worth adding to §2.

## Recommended edit pass

- Search-replace the 10 stale counts (locations and corrections in the table
  above).
- Fix "All 36 cases are currently analysis-ready" → "34 of 36 cases are
  analysis-ready; Cases 1 and 5 are partial due to journal-page access
  limits."
- Add one sentence to §2 stating the 437/165/10 confidence distribution and
  that upgrades followed direct full-text evidence review.
- Consider strengthening §4's shrinkage section: the aggregate shrinking-task
  count (40) is substantively higher than the draft implies.
- Optionally add one sentence in §3 acknowledging `transformed` as a common
  status for procedural and accountability roles.

No structural rewrite is needed. The thesis is intact; the numbers just need
to match the refreshed data.

## How to verify after edits

Re-run a count sanity check:

```bash
python3 - <<'EOF'
import csv, re, pathlib
ms = pathlib.Path("11_manuscript/10_drafts/10_manuscript.md").read_text()
for claim in ["robust in 16", "conditional in 10 more", "robust in 12", "conditional in 3",
              "98 source rows", "270 evidence", "shrinking in 3", "shrinking in 2",
              "transformed in 14", "All 36 cases are currently analysis-ready"]:
    if claim in ms:
        print(f"STILL PRESENT: {claim}")
EOF
```

After the edit pass, that script should print nothing.
