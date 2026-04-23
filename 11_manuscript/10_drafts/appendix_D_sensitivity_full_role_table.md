# Appendix D — Full 17-role sensitivity table (exclusion of boundary / live-project cases)

Companion to Table 4 in the main manuscript, which shows the six H1 / H2 roles only. This appendix reports Δ for all 17 roles under the five-case exclusion (Cases 25 and 26 Project APE, 32 The AI Scientist, 33 Deep Research, 34 AgentSociety).

**Columns:** *all* = full 36 cases; *excl* = 31 cases after boundary-case exclusion; *Δ* = excl − all. Status columns report (robust / conditional / transformed / shrinking / split pressure).

To be populated by running `scripts/section6_analysis.py --sensitivity-full --output appendix_D_output.json` against `role_coding_master.csv` at release tag `v1.0.0-ORM-submission`. The script is pre-specified; the output table will fill this appendix at submission.

**Expected structure:**

| Role | Role group | R (all / excl / Δ) | C | T | S | SP |
|---|---|---|---|---|---|---|
| Relevance adjudicator | starting_role | … | … | … | … | … |
| Mechanism disciplinarian | starting_role | … | … | … | … | … |
| Construct and perspective boundary setter | starting_role | … | … | … | … | … |
| Corpus pluralist | starting_role | … | … | … | … | … |
| Protocol and provenance architect | starting_role | (see Table 4) | | | | |
| Counterfactual and transportability judge | starting_role | … | … | … | … | … |
| Situated interlocutor / context witness | starting_role | … | … | … | … | … |
| Accountability and labor allocator | starting_role | (see Table 4) | | | | |
| Construct boundary setter | split_candidate | … | … | … | … | … |
| Perspective sampler | split_candidate | … | … | … | … | … |
| Counterfactual / transportability judge | split_candidate | … | … | … | … | … |
| Calibration architect | split_candidate | (see Table 4) | | | | |
| Situated interlocutor | split_candidate | … | … | … | … | … |
| Context witness | split_candidate | … | … | … | … | … |
| Routine first-pass screener | shrinking_task_cluster | (see Table 4) | | | | |
| Routine coder on high-consensus, ground-truth-rich tasks | shrinking_task_cluster | (see Table 4) | | | | |
| Structural prose polisher / drafter | shrinking_task_cluster | (see Table 4) | | | | |

## Stricter-cell exclusion variant

The K-persona review (see `10_manuscript_versions/review_loop/convergence_report.md`) asked for a stricter sensitivity: not excluding all five boundary cases, but excluding only the `edge_case=no_pre_AI_counterpart`-flagged *cells* within those cases (roughly 60 of 85 observable rows on those five cases). This variant is pre-specified and will be produced by the same script with the flag `--sensitivity-cells-only`.

Expected finding: shrinking and durable-role counts closer to the full-sample pattern than under the five-case exclusion. Direction of H3 paired sign test unchanged.
