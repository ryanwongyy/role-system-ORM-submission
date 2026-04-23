# Inter-coder agreement — report

**Subsample coded:** Cases 2, 3, 7, 27 (17 roles × 4 cases = 68 cells).
**Date:** 2026-04-23.
**First coder:** First author (manuscript lead).
**Second coder:** Sandboxed large-language-model agent, context restricted to rubric + case files only. No access to manuscript, first-coder CSV, or hypotheses.
**Script:** `scripts/section6_analysis.py` + internal κ computation with `sklearn.metrics.cohen_kappa_score`; bootstrap CI with B = 2,000, seed 20260423.

## Headline

| Metric | Value |
|---|---|
| Raw agreement | 52.9% (36 of 68) |
| **Pooled Cohen's κ** | **0.289** |
| 95% bootstrap CI | [0.147, 0.439] |
| Pre-committed threshold | κ ≥ 0.60 |
| **Verdict** | **FAIL on threshold; pre-committed remedy invoked** |

## Per-status κ (one-vs-all)

| Status | κ | n cells (either coder) |
|---|---:|---:|
| Shrinking | 0.549 | 5 |
| Robust | 0.402 | 13 |
| Conditional | 0.009 | 21 |
| Transformed | 0.000 | 10 |
| Split pressure | 0.000 | 2 |
| Merge pressure | — | 0 |

The paired *conditional* and *transformed* rows, which dominate the observable cells (31 of 68), show essentially no above-chance agreement. This is the dominant failure mode.

## Diagnosis

Of the 32 divergent cells:

- **19** reflect disagreement on whether a role is *observable* (conditional/transformed/robust) vs. `not_applicable`. The first coder had a stricter threshold for "observable."
- **7** reflect the conditional-vs-transformed tie-breaker (both coders agreed the role was observable; disagreed on which status).
- **3** reflect disagreement on whether the case exhibits *split pressure* (first coder) vs. *transformed* or *robust* on a specific sub-role (second coder).
- **3** reflect other distinctions (shrinking vs. unclear when AI performance is sub-chance; robust vs. conditional moderator-specification).

## Remedies invoked (pre-committed)

Per the OSF preregistration (see `30_reviews/OSF_preregistration.md`):

1. **Tie-breaker revision** in Table 1 of the main manuscript: now requires an explicit quotable moderator (for *conditional*) or an explicit role-content change (for *transformed*); indeterminate cells default to *unclear*.
2. **Observable-vs-`not_applicable` threshold** tightened: requires at least one quotable sentence of direct evidence that the activity is performed or deliberately not performed; inference from adjacent discussion is not sufficient.
3. **Claim ceiling adjustment** throughout the paper: *framework* → *preliminary framework*. Applied in the abstract, §6, and §7.

## Human second-coder pass as unmet commitment

The LLM-agent pass establishes a *lower bound* for reliability. A human expert second coder is likely to achieve higher κ given richer contextual judgment, so the 0.289 value is conservative relative to what a real reliability pass would yield. This is flagged explicitly in §6 and in §Transparency and Disclosures. The human-coder pass is a pre-submission commitment (drop-dead 2026-06-15 per the OSF preregistration, extendable) but has not been completed as of this submission.

## Interpretation for the paper's claims

The low κ challenges cell-level reliability but does NOT directly threaten:

- The role-level paired sign test (H3): the sign test compares within-role V distributions aggregated over all 36 cases; the first coder's internal consistency is sufficient for this aggregate.
- The pattern-level claim (H1, H2): durable-roles and shrinking-clusters patterns aggregate across many cells each, and are visible in the distributional structure regardless of per-cell reliability.

The low κ DOES directly threaten:

- Case-level and cell-level claims: individual cell assignments and case-configuration signatures require cell-level reliability that the LLM-agent pass has not demonstrated.
- The stranger-coder protocol in Appendix C: the protocol is still specifiable, but the expected reliability achievable by a stranger coder is now bounded below 0.60 on LLM-agent evidence.

The claim ceiling adjustment to *preliminary framework* reflects these bounded implications.

## Files released

| File | Content |
|---|---|
| `06_analysis_tables/role_coding_secondcoder_subsample.csv` | 68 second-coder cells |
| `11_manuscript/30_reviews/intercoder_agreement_stats.json` | All κ statistics + bootstrap CIs |
| `11_manuscript/30_reviews/intercoder_agreement.md` | This report |
| `11_manuscript/10_drafts/appendix_B_kappa.md` | Appendix B integration with full disagreement log |
