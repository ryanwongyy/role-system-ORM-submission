# Appendix B — Inter-coder agreement on a double-coded subsample

**Pre-analysis plan.** The second-coder protocol is specified in `30_reviews/OSF_preregistration.md`, released with the database at tag `v1.0.0-ORM-submission` (commit `7f0a816`). The plan documents the four-case stratified subsample, the coder-blindness protocol, the κ ≥ 0.60 acceptance threshold, and the tie-breaker-revision remedy. The temporal-precedence standard is the git commit history rather than an OSF timestamp: an independent OSF registration was not posted before the second-coder pass, and we flag OSF registration as a recommended follow-up rather than claim it retrospectively. All acceptance thresholds and tie-breaker remedies were drafted before the second-coder pass was run within the same development session.

## Subsample (pre-specified)

Four cases, stratified across the four largest case-family clusters:

| Case ID | Author/year | Case family | Primary AI capability |
|---|---|---|---|
| 2 | Keith, 2026 | Measurement & coding | Generative |
| 7 | Baccolini, 2026 | Evidence synthesis & corpus | Generative |
| 3 | Gligorić, n.d. | Interviews, fieldwork & qualitative interpretation | Generative |
| 27 | Kang, 2025 | Reproducibility & autonomous research | Agentic |

Total cells: **4 cases × 17 roles = 68 cells.**

## Second coder

The second-coder pass was performed by a sandboxed large-language-model agent (general-purpose Anthropic Claude agent), with context explicitly restricted to: (a) the Table 1 rubric reproduced verbatim, (b) the 17 role labels, (c) the primary-source extracts for the four cases, and (d) the output-CSV schema. The agent was blind to: the manuscript, the first-coder evidence summaries, the hypotheses H1–H3, the exemplar case-to-status mapping, and the first-coder CSV. The second-coder session log is released with the database.

**This is a weaker reliability test than a human independent second coder would provide**, and we flag it as such in §6 of the main manuscript. A human second-coder pass remains a recommended follow-up for the final reliability number; the LLM-agent κ reported below is a lower-bound conservative estimate that a human second coder is likely to exceed given richer contextual judgment. The LLM-as-second-coder disclosure is added to §Transparency and Disclosures.

## Results

**Raw agreement:** 36 of 68 cells (52.9%) — well above chance but short of the pre-committed threshold.

**Pooled Cohen's κ (7 categories: six observable statuses + not_observable):**

> **κ = 0.289, 95% bootstrap CI [0.147, 0.439]** (B = 2,000; seed 20260423).

This **fails** the pre-committed acceptance threshold of κ ≥ 0.60.

**Per-status κ (one-vs-all):**

| Status | κ | Cells where either coder used this label |
|---|---:|---:|
| Robust | +0.402 | 13 |
| Shrinking | +0.549 | 5 |
| Conditional | +0.009 | 21 |
| Transformed | +0.000 | 10 |
| Split pressure | +0.000 | 2 |
| Merge pressure | — | 0 (neither coder used it in subsample) |

The per-status pattern is diagnostic: *robust* and *shrinking* show moderate-to-substantial agreement; *conditional* and *transformed* show effectively no above-chance agreement; *split pressure* showed one case of disagreement, neither cell was picked up as merge pressure by either coder. The dominant disagreement axis is whether a role is *observable* (i.e., coded as `conditional`/`transformed`/`robust`) or `not_observable` (i.e., coded as `not_applicable` or `unclear`).

## Pre-committed remedies — invoked

Per the pre-analysis plan, failure on κ triggers three remedies. All three are applied in the revision:

1. **Rubric tie-breaker revision (Table 1).** The conditional-vs-transformed tie-breaker has been extended to name the two most common failure modes observed: (a) inferring `transformed` from the mere presence of AI in the workflow, rather than from an explicit before/after change; and (b) coding `conditional` when no moderator analysis is in the case. The revised tie-breaker requires the coder to identify at least one *explicit* moderator variable (for `conditional`) or at least one *explicit* role-content change (for `transformed`). Indeterminate cells default to `unclear`.

2. **Observable-vs-not-applicable threshold.** The rubric's implicit boundary between "observable" and `not_applicable` is tightened. A role counts as observable only if the case file contains at least one sentence that could be quoted as evidence of that activity being performed (or deliberately not performed) in the case's research workflow. Inference from adjacent activity does not establish observability.

3. **Claim ceiling adjustment.** The abstract, §1, §6, and §7 are updated to describe the contribution as a **preliminary framework** rather than a validated framework, pending a human second-coder pass at acceptance-grade reliability.

## Full disagreement log (32 divergent cells)

Format: [case_id | role | first coder | second coder | diagnosis].

| Case | Role | Coder 1 | Coder 2 | Diagnosis |
|---|---|---|---|---|
| 2 | Accountability and labor allocator | conditional | transformed | Tie-breaker: second coder read "behavioral tests" as new AI-specific sub-task. Remedy #1 applies. |
| 2 | Calibration architect | not_applicable | transformed | Observable-vs-NA: second coder inferred calibration activity from adjacent validation steps. Remedy #2 applies. |
| 2 | Construct boundary setter | conditional | robust | Conditional-vs-robust: moderator specification unclear in case text. |
| 2 | Corpus pluralist | not_applicable | conditional | Observable-vs-NA. Remedy #2 applies. |
| 2 | Protocol and provenance architect | conditional | transformed | Tie-breaker. Remedy #1 applies. |
| 2 | Routine coder on high-consensus, ground-truth-rich tasks | conditional | shrinking | Rubric clarity: does the case shrink this task or make it conditional on LLM performance? |
| 3 | Accountability and labor allocator | not_applicable | transformed | Observable-vs-NA. Remedy #2 applies. |
| 3 | Calibration architect | not_applicable | transformed | Observable-vs-NA. Remedy #2 applies. |
| 3 | Construct and perspective boundary setter | split_pressure | robust | Split-pressure recognition: second coder did not see two conflated sub-activities. Diagnostic of split-pressure under-specification. |
| 3 | Construct boundary setter | robust | conditional | Moderator specification mismatch. |
| 3 | Context witness | not_applicable | robust | Observable-vs-NA. Remedy #2 applies. |
| 3 | Counterfactual / transportability judge | not_applicable | conditional | Observable-vs-NA. Remedy #2 applies. |
| 3 | Counterfactual and transportability judge | not_applicable | conditional | Observable-vs-NA. Remedy #2 applies. |
| 3 | Protocol and provenance architect | split_pressure | transformed | Split-pressure vs. single-role content change. |
| 3 | Routine coder on high-consensus, ground-truth-rich tasks | unclear | not_applicable | Agreement on non-observability; labeling differs. |
| 3 | Situated interlocutor | not_applicable | robust | Observable-vs-NA. Remedy #2 applies. |
| 3 | Situated interlocutor / context witness | not_applicable | robust | Observable-vs-NA. Remedy #2 applies. |
| 7 | Accountability and labor allocator | unclear | transformed | Observable-vs-NA + tie-breaker. Remedies #1 + #2 apply. |
| 7 | Calibration architect | conditional | transformed | Tie-breaker. Remedy #1 applies. |
| 7 | Counterfactual / transportability judge | unclear | conditional | Observable-vs-NA. Remedy #2 applies. |
| 7 | Counterfactual and transportability judge | not_applicable | conditional | Observable-vs-NA. Remedy #2 applies. |
| 7 | Protocol and provenance architect | conditional | transformed | Tie-breaker. Remedy #1 applies. |
| 7 | Relevance adjudicator | unclear | shrinking | Ambiguous — first coder's uncertainty vs. second coder's shrinking call on title-abstract triage. |
| 27 | Calibration architect | robust | transformed | Robust-vs-transformed: rubric currently has no tie-breaker for this pairing. Potential remedy #1 extension. |
| 27 | Construct and perspective boundary setter | conditional | robust | Conditional-vs-robust. |
| 27 | Construct boundary setter | conditional | robust | Conditional-vs-robust. |
| 27 | Context witness | conditional | not_applicable | Observable-vs-NA in reverse. |
| 27 | Counterfactual / transportability judge | not_applicable | conditional | Observable-vs-NA. Remedy #2 applies. |
| 27 | Counterfactual and transportability judge | not_applicable | conditional | Observable-vs-NA. Remedy #2 applies. |
| 27 | Mechanism disciplinarian | conditional | not_applicable | Observable-vs-NA in reverse. |
| 27 | Relevance adjudicator | conditional | not_applicable | Observable-vs-NA in reverse. |
| 27 | Routine coder on high-consensus, ground-truth-rich tasks | shrinking | unclear | First coder confident shrinkage; second coder flagged evidence of sub-random AI performance as contradicting shrinkage indicator. Diagnostic: the shrinking rubric row needs language for "target exists but AI does not yet reach human performance." |

## Summary

The LLM-agent second-coder pass returned κ = 0.289, below the pre-committed 0.60 threshold. The pre-analysis plan's three-part remedy is invoked in the revision. The paper's claim ceiling is adjusted from *framework* to *preliminary framework*. The rubric's tie-breaker and observable-vs-NA threshold are revised. A human second-coder pass is recommended as a follow-up and is named in §6 as an unmet commitment; until then, the rubric's reliability is characterized by the LLM-agent lower bound reported here.

**Pass/fail verdict:** FAIL on pre-committed threshold; remedies fully invoked.

## Artifacts

- `/Users/ryanwong/Human roles/p1_role_systems_db/06_analysis_tables/role_coding_secondcoder_subsample.csv` — 68 rows, second-coder codings
- `/Users/ryanwong/Human roles/p1_role_systems_db/11_manuscript/30_reviews/intercoder_agreement_stats.json` — all κ values + bootstrap CIs + per-status κ
- This appendix file
