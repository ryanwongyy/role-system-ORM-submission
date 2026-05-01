# Appendix D — Full 17-role sensitivity table (exclusion of boundary / live-project cases)

Companion to Table 4 in the main manuscript, which shows the six H1 / H2 roles only. This appendix reports Δ for all 17 roles under the five-case exclusion (Cases 25 and 26 Project APE, 32 The AI Scientist, 33 Deep Research, 34 AgentSociety) computed against the v1.0' inferential base (35 cases, 595 codings — Case 36 held back as a v1.1 design entry).

**Columns:** *all* = the v1.0' inferential base of 35 cases; *excl* = 30 cases after boundary-case exclusion; *Δ* = excl − all. Status columns report **R** (robust) / **C** (conditional) / **T** (transformed) / **S** (shrinking) / **SP** (split pressure). Computed against `role_coding_master.csv` at release tag `v1.0.0-ORM-submission` filtered to `cases_master.analysis_ready == "yes"`.

| Role | Role group | R (all/excl/Δ) | C (all/excl/Δ) | T (all/excl/Δ) | S (all/excl/Δ) | SP (all/excl/Δ) |
|---|---|---|---|---|---|---|
| Relevance adjudicator | starting_role | 0/0/+0 | 8/6/−2 | 3/2/−1 | 0/0/+0 | 1/1/+0 |
| Mechanism disciplinarian | starting_role | 2/2/+0 | 5/4/−1 | 2/1/−1 | 0/0/+0 | 4/3/−1 |
| Construct and perspective boundary setter | starting_role | 3/3/+0 | 3/3/+0 | 2/2/+0 | 0/0/+0 | 4/4/+0 |
| Corpus pluralist | starting_role | 2/1/−1 | 7/7/+0 | 2/2/+0 | 0/0/+0 | 0/0/+0 |
| Protocol and provenance architect | starting_role | 14/11/−3 | 5/5/+0 | 8/7/−1 | 0/0/+0 | 4/4/+0 |
| Counterfactual and transportability judge | starting_role | 2/2/+0 | 10/8/−2 | 2/1/−1 | 0/0/+0 | 3/2/−1 |
| Situated interlocutor / context witness | starting_role | 3/3/+0 | 2/2/+0 | 1/1/+0 | 0/0/+0 | 2/2/+0 |
| Accountability and labor allocator | starting_role | 5/4/−1 | 8/7/−1 | 8/7/−1 | 0/0/+0 | 5/4/−1 |
| Construct boundary setter | split_candidate | 5/5/+0 | 4/4/+0 | 1/1/+0 | 0/0/+0 | 2/2/+0 |
| Perspective sampler | split_candidate | 1/1/+0 | 2/2/+0 | 0/0/+0 | 0/0/+0 | 4/4/+0 |
| Counterfactual / transportability judge | split_candidate | 0/0/+0 | 11/9/−2 | 0/0/+0 | 0/0/+0 | 3/2/−1 |
| Calibration architect | split_candidate | 7/5/−2 | 10/9/−1 | 1/1/+0 | 0/0/+0 | 2/2/+0 |
| Situated interlocutor | split_candidate | 2/2/+0 | 3/3/+0 | 0/0/+0 | 0/0/+0 | 2/2/+0 |
| Context witness | split_candidate | 4/4/+0 | 5/5/+0 | 1/1/+0 | 0/0/+0 | 1/1/+0 |
| Routine first-pass screener | shrinking_task_cluster | 0/0/+0 | 0/0/+0 | 0/0/+0 | 12/8/−4 | 0/0/+0 |
| Routine coder on high-consensus, ground-truth-rich tasks | shrinking_task_cluster | 0/0/+0 | 1/1/+0 | 0/0/+0 | 14/11/−3 | 1/1/+0 |
| Structural prose polisher / drafter | shrinking_task_cluster | 0/0/+0 | 2/2/+0 | 1/1/+0 | 12/8/−4 | 0/0/+0 |
| **Column totals** | — | **50/43/−7** | **86/77/−9** | **32/27/−5** | **38/27/−11** | **38/34/−4** |

**Reading the table.** Computed on the v1.0' inferential base of 35 cases (Case 36, the proposed pedagogical configuration, is held back for v1.1 hold-out adjudication and is therefore not included in the *all* totals here). The five autonomy-heavy boundary cases contribute disproportionately to *shrinking* (11 of 38 = 28.9%) and to *conditional* (9 of 86 = 10.5%); the *robust* and *transformed* totals decline by 14.0% and 15.6% respectively. The directional pattern of H1 (procedural-validity roles more robust than throughput task roles) is preserved under the exclusion: the six procedural-validity / boundary-setting roles still dominate the *robust* count (28 of 43 in the exclusion sample, 65%), while the three throughput clusters retain all 27 remaining *shrinking* codings. The headline *V* values (family 0.286, capability 0.266) and the H3 paired-rank verdicts in the main text are computed on the full v1.0' base; the sensitivity here documents that excluding the five boundary cases moves counts but not directions.

## Stricter-cell exclusion variant

The K-persona review (see `10_manuscript_versions/review_loop/convergence_report.md`) asked for a stricter sensitivity: not excluding all five boundary cases, but excluding only the `edge_case=no_pre_AI_counterpart`-flagged *cells* within those cases (roughly 60 of 85 observable rows on those five cases). This variant is pre-specified for the v1.1 instrument and is reported in the release-tag artifact rather than reproduced here.

Expected finding: shrinking and durable-role counts closer to the full-sample pattern than under the five-case exclusion. Direction of H3 paired sign test unchanged.
