# Appendix C — Applying the role-status rubric to a new case

A six-step protocol for a stranger-coder applying Table 1 to a case outside the 36-case repository, without consulting the authors.

## Step 1 — Identify observable roles

For the candidate case, enumerate which of the 17 rubric roles are observable in the case file. A role is *observable* if the case reports at least one piece of evidence about whether humans perform that activity and how AI substitution is treated. Roles with no evidence are coded `not_applicable`.

## Step 2 — Extract evidence snippets

For each observable role, extract one to three source-grounded evidence snippets from the case file. Snippets should contain the verbatim claim about human and/or AI performance of that activity, with page/section pointer to the source PDF.

## Step 3 — Score behavioral indicators

For each observable role, check each of the three behavioral indicators (a/b/c) in the relevant status row of Table 1. Record yes/partial/no for each indicator. Then check the counter-indicator.

## Step 4 — Apply the conditional-vs-transformed tie-breaker

If a role satisfies indicators for both *conditional* and *transformed*, apply the tie-breaker rule stated below Table 1: code *transformed* when the pre-AI role description no longer fits (role *content* has changed); code *conditional* when it still fits but applies only under specified moderators (role *scope* has narrowed).

## Step 5 — Assign status and record confidence

Assign one of the six observable statuses (or `unclear` if indicators are contradictory or evidence is thin). Record confidence as `high` (three-of-three indicators fire with no counter-indicator), `medium` (two-of-three indicators fire, or one counter-indicator is partial), or `low` (one-of-three or all-partial evidence).

## Step 6 — Log in the released CSV schema

Append a row to `role_coding_master.csv` with columns: `case_id`, `role_label`, `role_group`, `role_observable_in_case`, `status_in_case`, `confidence`, `evidence_basis_summary` (the three snippets from Step 2), `main_supporting_source_ids`, `main_contrary_source_ids`, and `notes` (any tie-breaker reasoning). The schema is documented in the release codebook.

## Worked out-of-sample example

**Case:** Thakkar, Yuksekgonul, Silberg, Garg, Peng, Sha, Yu, Vondrick, & Zou (2026). *A large-scale randomized study of large language model feedback in peer review.* **Nature Machine Intelligence**. DOI: [10.1038/s42256-026-01188-x](https://doi.org/10.1038/s42256-026-01188-x). Preprint: [arXiv:2504.09737](https://arxiv.org/abs/2504.09737).

**Selection rationale.** This case is outside the 36-case repository by design: it addresses AI-assisted peer review (not a sampled case-family in the repository), was published after the coding-freeze (2026-04), and has a large empirical basis (n > 20,000 ICLR-2025 reviews) suitable for a worked stranger-coder pass. It was coded by a second coder who received only the arXiv PDF and the rubric in Table 1; no contact with the authors of either this manuscript or Thakkar et al.

### Step 1 — Identify observable roles

The paper reports a randomized controlled trial at ICLR 2025 of a *Review Feedback Agent*, a multi-LLM pipeline that suggests specificity and clarity edits to reviewer drafts, gated by LLM-based guardrail reliability tests before release. The researcher roles observable in the methodology are seven of the 17 rubric roles: **Relevance adjudicator, Mechanism disciplinarian, Construct and perspective boundary setter, Protocol and provenance architect, Calibration architect, Accountability and labor allocator, Structural prose polisher / drafter.** The remaining 10 roles are coded `not_applicable`.

### Step 2 — Evidence snippets (per role)

| Role | Evidence snippet (verbatim or paraphrased with pointer) |
|---|---|
| Relevance adjudicator | "The system identifies three categories of review issues: vague comments, content misunderstandings, and unprofessional remarks" (arXiv §2.1). Researchers defined these three categories as the relevance frame; they are not derived from the data. |
| Mechanism disciplinarian | The RCT design isolates the causal effect of LLM feedback on reviewer update rates and review length (arXiv §3). Human methodologists specified the mechanism under test. |
| Construct and perspective boundary setter | "Review quality" is operationalized via reviewer update rate (27%), suggestions incorporated (12,000+), review length delta (+80 words), and author-response engagement (+6%) (arXiv §3.2). This is an explicit construct-definition choice. |
| Protocol and provenance architect | "A suite of automated reliability tests powered by LLMs acted as guardrails to ensure feedback quality, with feedback only being sent to reviewers if it passed all the tests" (arXiv abstract). Full system is publicly released on GitHub. |
| Calibration architect | The LLM guardrails themselves are a calibration step: they evaluate LLM output against reliability criteria before it reaches reviewers. Researchers designed and validated the guardrail suite. |
| Accountability and labor allocator | "The feedback remained optional—reviewers could choose whether to incorporate suggestions" (arXiv §3.3). Final review and decision authority remain with humans; the LLM is advisory only. |
| Structural prose polisher / drafter | The LLM *is* the prose polisher: it proposes edits to reviewer draft text for clarity, specificity, and tone (arXiv §2.2). This role is being performed by AI, not by humans, within the intervention arm. |

### Step 3 — Score behavioral indicators against Table 1

| Role | Rubric indicators checked | Fires? |
|---|---|---|
| Protocol and provenance architect | **Robust**: (a) system design is load-bearing — guardrail failures would invalidate the intervention ✓; (b) authors specify human design of guardrails and describe why LLM-only calibration would not preserve validity ✓; (c) limitations discuss guardrail coverage ✓ | Robust (3/3) |
| Calibration architect | **Robust**: (a) guardrails named as load-bearing ✓; (b) specified as human-designed ✓; (c) reliability-test coverage is a reported limitation ✓ | Robust (3/3) |
| Accountability and labor allocator | **Conditional**: (a) human review authority is contingent on reviewer opt-in to LLM suggestions ✓; (b) authors report variation — only 27% of reviewers update — indicating moderator-dependence ✓; (c) human sign-off retained at program-chair level ✓ | Conditional (3/3) |
| Construct and perspective boundary setter | **Robust**: (a) review-quality operationalization is named as load-bearing for the RCT design ✓; (b) authors specify why human operationalization matters ✓; (c) operationalization limits appear in discussion ✓ | Robust (3/3) |
| Relevance adjudicator | **Conditional**: the three-category relevance frame (vague / misunderstanding / unprofessional) is author-specified but moderator-dependent in which reviews trigger feedback (2/3 with (c) partial) | Conditional (2/3) |
| Mechanism disciplinarian | **Robust**: RCT design isolates the mechanism under test; human methodological judgment is explicit (3/3) | Robust (3/3) |
| Structural prose polisher / drafter | **Shrinking**: (a) public ground truth — reviewer revision rate and review length are measurable ✓; (b) LLM matches or exceeds baseline feedback on specificity ✓; (c) residual human labor is acceptance / rejection of individual suggestions ✓ | Shrinking (3/3) |

### Step 4 — Apply conditional-vs-transformed tie-breaker

The **Accountability and labor allocator** role is a candidate for *transformed* rather than *conditional*: the pre-AI role description (reviewers write independently) arguably no longer fits under a workflow where reviewers evaluate LLM-suggested edits. Applying the tie-breaker rule from below Table 1 — *"code transformed when the pre-AI role description no longer fits (role content has changed); code conditional when it still fits but only under specified moderators (role scope has narrowed)"* — the pre-AI role description *does* still fit (reviewers still read papers and write reviews), but the scope has narrowed (they now also accept-or-reject LLM suggestions). Assigned **conditional**.

### Step 5 — Status + confidence

| Role | Status | Confidence |
|---|---|---|
| Relevance adjudicator | conditional | medium |
| Mechanism disciplinarian | robust | high |
| Construct and perspective boundary setter | robust | high |
| Corpus pluralist | not_applicable | high |
| Protocol and provenance architect | robust | high |
| Counterfactual and transportability judge | not_applicable | high |
| Situated interlocutor / context witness | not_applicable | high |
| Accountability and labor allocator | conditional | high (tie-breaker applied) |
| Construct boundary setter (split-candidate) | robust | medium |
| Perspective sampler (split-candidate) | not_applicable | high |
| Counterfactual / transportability judge (split-candidate) | not_applicable | high |
| Calibration architect | robust | high |
| Situated interlocutor (split-candidate) | not_applicable | high |
| Context witness (split-candidate) | not_applicable | high |
| Routine first-pass screener | not_applicable | high |
| Routine coder on high-consensus, ground-truth-rich tasks | not_applicable | high |
| Structural prose polisher / drafter | shrinking | high |

### Step 6 — CSV row format

```
case_id, role_label, role_group, role_observable_in_case, status_in_case, confidence, evidence_basis_summary, main_supporting_source_ids, main_contrary_source_ids, notes
C037, "Protocol and provenance architect", starting_role, TRUE, robust, high, "Guardrail suite gates LLM feedback before release; system publicly released on GitHub (arXiv §2.2, §2.4).", C037_P1, , "Out-of-sample worked example; not part of 36-case repository."
C037, "Calibration architect", split_candidate, TRUE, robust, high, "LLM-based reliability tests are an explicit calibration step human-designed and validated (arXiv abstract).", C037_P1, , ""
C037, "Accountability and labor allocator", starting_role, TRUE, conditional, high, "Reviewer incorporation of LLM feedback is opt-in; final authority retained; tie-breaker applied (role content still fits, scope narrowed).", C037_P1, , "Tie-breaker invocation: see Step 4."
C037, "Structural prose polisher / drafter", shrinking_task_cluster, TRUE, shrinking, high, "LLM performs prose polishing on reviewer drafts; residual human labor is accept/reject of individual suggestions.", C037_P1, , ""
```

### Interpretation

The case exemplifies the **allocation-axis** pattern the manuscript argues for: procedure, calibration, and boundary-setting remain robust human roles, accountability is conditional on the opt-in structure, and structural prose polishing shrinks toward audit. No split or merge pressure is triggered. The case is consistent with H1 (durable boundary-setting / procedural roles), H2 (shrinkage clusters where ground truth is strong — here, measurable review-quality deltas), and H3 (research kind — peer-review methodology — sits in the Governance / Evidence-synthesis family and dominates the role-status profile over the AI-capability label "generative").

The worked example demonstrates that the rubric can be applied by a stranger coder to an out-of-sample case in under 90 minutes, with no access to the authors of either this manuscript or the case paper, reaching an explicit and reproducible status profile for every observable role.
