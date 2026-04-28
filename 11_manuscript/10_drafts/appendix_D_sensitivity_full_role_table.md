# Appendix D — Full 17-role sensitivity table (exclusion of boundary / live-project cases)

Companion to Table 4 in the main manuscript, which shows the six H1 / H2 roles only. This appendix reports Δ for all 17 roles under the five-case exclusion (Cases 25 and 26 Project APE, 32 The AI Scientist, 33 Deep Research, 34 AgentSociety).

**Columns:** *all* = full 36 cases; *excl* = 31 cases after boundary-case exclusion; *Δ* = excl − all. Status columns report **R** (robust) / **C** (conditional) / **T** (transformed) / **S** (shrinking) / **SP** (split pressure). Computed against `role_coding_master.csv` at release tag `v1.0.0-ORM-submission`.

| Role | Role group | R (all/excl/Δ) | C (all/excl/Δ) | T (all/excl/Δ) | S (all/excl/Δ) | SP (all/excl/Δ) |
|---|---|---|---|---|---|---|
| Relevance adjudicator | starting_role | 1/1/+0 | 8/6/−2 | 3/2/−1 | 0/0/+0 | 1/1/+0 |
| Mechanism disciplinarian | starting_role | 2/2/+0 | 6/5/−1 | 2/1/−1 | 0/0/+0 | 4/3/−1 |
| Construct and perspective boundary setter | starting_role | 3/3/+0 | 4/4/+0 | 2/2/+0 | 0/0/+0 | 4/4/+0 |
| Corpus pluralist | starting_role | 2/1/−1 | 7/7/+0 | 2/2/+0 | 0/0/+0 | 0/0/+0 |
| Protocol and provenance architect | starting_role | 15/12/−3 | 5/5/+0 | 7/6/−1 | 0/0/+0 | 4/4/+0 |
| Counterfactual and transportability judge | starting_role | 2/2/+0 | 11/9/−2 | 2/1/−1 | 0/0/+0 | 3/2/−1 |
| Situated interlocutor / context witness | starting_role | 4/4/+0 | 2/2/+0 | 1/1/+0 | 0/0/+0 | 2/2/+0 |
| Accountability and labor allocator | starting_role | 5/4/−1 | 8/7/−1 | 7/6/−1 | 0/0/+0 | 6/5/−1 |
| Construct boundary setter | split_candidate | 5/5/+0 | 5/5/+0 | 1/1/+0 | 0/0/+0 | 2/2/+0 |
| Perspective sampler | split_candidate | 2/2/+0 | 2/2/+0 | 0/0/+0 | 0/0/+0 | 4/4/+0 |
| Counterfactual / transportability judge | split_candidate | 0/0/+0 | 12/10/−2 | 0/0/+0 | 0/0/+0 | 3/2/−1 |
| Calibration architect | split_candidate | 8/6/−2 | 10/9/−1 | 1/1/+0 | 0/0/+0 | 2/2/+0 |
| Situated interlocutor | split_candidate | 3/3/+0 | 3/3/+0 | 0/0/+0 | 0/0/+0 | 2/2/+0 |
| Context witness | split_candidate | 4/4/+0 | 6/6/+0 | 1/1/+0 | 0/0/+0 | 1/1/+0 |
| Routine first-pass screener | shrinking_task_cluster | 0/0/+0 | 0/0/+0 | 0/0/+0 | 13/9/−4 | 0/0/+0 |
| Routine coder on high-consensus, ground-truth-rich tasks | shrinking_task_cluster | 0/0/+0 | 1/1/+0 | 0/0/+0 | 15/12/−3 | 1/1/+0 |
| Structural prose polisher / drafter | shrinking_task_cluster | 0/0/+0 | 2/2/+0 | 1/1/+0 | 12/8/−4 | 0/0/+0 |
| **Column totals** | — | **56/49/−7** | **92/83/−9** | **30/25/−5** | **40/29/−11** | **39/35/−4** |

**Reading the table.** The five autonomy-heavy boundary cases contribute disproportionately to *shrinking* (11 of 40 = 27.5%) and to *conditional* (9 of 92 = 9.8%); the *robust* and *transformed* totals decline by 12.5% and 16.7% respectively. The directional pattern of H1 (procedural-validity roles more robust than throughput task roles) is preserved under the exclusion: the six procedural-validity / boundary-setting roles still dominate the *robust* count (29 of 49 in the exclusion sample, 59%), while the three throughput clusters retain all 29 remaining *shrinking* codings. The headline *V* values (family 0.260, capability 0.240) and the H3 paired-rank verdicts in the main text are computed on the full 36-case sample; the sensitivity here documents that excluding the five boundary cases moves counts but not directions.

## Stricter-cell exclusion variant

The K-persona review (see `10_manuscript_versions/review_loop/convergence_report.md`) asked for a stricter sensitivity: not excluding all five boundary cases, but excluding only the `edge_case=no_pre_AI_counterpart`-flagged *cells* within those cases (roughly 60 of 85 observable rows on those five cases). This variant is pre-specified for the v1.1 instrument and is reported in the release-tag artifact rather than reproduced here.

Expected finding: shrinking and durable-role counts closer to the full-sample pattern than under the five-case exclusion. Direction of H3 paired sign test unchanged.
