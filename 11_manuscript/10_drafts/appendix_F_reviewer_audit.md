# Appendix F — Reviewer-Audit Checklist

**Companion artifact.** This checklist is the downstream audit of coder output produced via the Appendix E protocol. Items F2.1, F2.3, and F3.5 here audit for the quoted-evidence artifacts recorded at Appendix E steps E1.2, E3.2, E3.3, and E4.1. A reviewer using F on a submission that did not use E can still apply it — the items are portable — but the evidentiary standard becomes "quoted sentence or not," not "protocol-compliant evidence record."

**Purpose.** This checklist is designed for **peer reviewers and editors** evaluating an AI-embedded research manuscript under review. It does not replace domain-specific review criteria; it locates *where* the manuscript's automation claims sit in the role × status space (Table 1 of the main paper) and flags whether the claims are supported by the evidence the paper contains. It is a one-page adjunct to existing reviewer evaluation forms, designed to take 10–15 minutes to complete.

**How to use.** Read the manuscript once for content. Then work through F1 through F4 in order, marking each item yes / no / unclear. The summary at F5 aggregates the answers into a recommended reviewer disposition (accept / minor / major / reject on automation claims alone).

---

## F1. Scope and claim identification (6 items)

F1.1 Does the manuscript name at least one *durable* (robust or conditional) research role that remains human-performed?
- [ ] Yes [ ] No [ ] Unclear

F1.2 Does the manuscript name at least one *shrinking* task-cluster where AI substitutes for human labor?
- [ ] Yes [ ] No [ ] Unclear

F1.3 Does the manuscript explicitly distinguish the *task-cluster* layer (where shrinkage is defensible) from the *role* layer (where disappearance requires stronger evidence)?
- [ ] Yes [ ] No [ ] Unclear

F1.4 Are the automation claims situated within a named methodological frame (e.g., measurement, screening, reproducibility, authorship), not as generic "AI helps research" statements?
- [ ] Yes [ ] No [ ] Unclear

F1.5 If the paper claims role *transformation* (role content has changed), does it use before/after language or a verb swap?
- [ ] Yes [ ] No [ ] Not claimed

F1.6 If the paper claims role *shrinkage*, is a public ground truth or high-consensus target named?
- [ ] Yes [ ] No [ ] Not claimed

---

## F2. Evidence quality (6 items)

F2.1 For each durable role named, is there a quoted methods or limitations sentence that supports the claim?
- [ ] Yes [ ] No [ ] Partial (some but not all)

F2.2 For each shrinkage claim, is the human-AI performance gap reported numerically, or only qualitatively?
- [ ] Numerically [ ] Qualitatively [ ] Not reported

F2.3 For each *conditional* claim (AI works except under X), is the moderator variable X explicitly named?
- [ ] Yes [ ] No [ ] No conditional claims

F2.4 If coding or annotation is the object of the shrinkage claim, is the ground-truth distribution (inter-rater agreement, consensus rate, or similar) reported?
- [ ] Yes [ ] No [ ] Not applicable

F2.5 Are edge cases or task conditions where AI fails reported alongside the successful cases?
- [ ] Yes [ ] No [ ] Unclear

F2.6 Does the paper report any inter-coder or inter-annotator agreement statistic (Cohen's κ, Krippendorff's α, or equivalent) for its own coding pass?
- [ ] Yes [ ] No [ ] Not applicable (no coding pass)

---

## F3. Transparency and reproducibility (6 items)

F3.1 Are the data (coding CSV, case files, or pipeline outputs) released under an open license?
- [ ] Yes [ ] No [ ] Partial

F3.2 Is a reproducibility script provided that regenerates the reported statistics?
- [ ] Yes [ ] No [ ] Not applicable

F3.3 Are software version, random seeds, and dependencies pinned?
- [ ] Yes [ ] No [ ] Partial

F3.4 Is an OSF preregistration or a published pre-analysis plan cited, and does its timestamp predate the result it claims to constrain?
- [ ] Yes, predates [ ] Yes, post-hoc [ ] No

F3.5 Is the first-coder / first-author blindness disclosed (non-blind to hypotheses is acceptable if flagged)?
- [ ] Flagged and disclosed [ ] Implicit [ ] Not addressed

F3.6 Is at least one LLM or AI tool's role in the research workflow disclosed (per ORM 2025 standard)?
- [ ] Yes [ ] No [ ] Not applicable

---

## F4. Role-layer vs. task-layer claim alignment (4 items)

F4.1 Where the paper reports AI matching or exceeding human performance, is the claim restricted to the task-cluster level (not extended to the role)?
- [ ] Yes [ ] No (extended to role) [ ] Unclear

F4.2 Where the paper reports human labor persisting, is the role clearly named (not just "oversight" or "checking") and tied to a methodological function (protocol, provenance, calibration, accountability, boundary setting)?
- [ ] Yes [ ] No [ ] Partial

F4.3 Where the paper reports *split pressure* — two sub-activities the original role confused — does the revised typology preserve substantive information?
- [ ] Yes [ ] No split claimed [ ] Unclear

F4.4 Where the paper reports *merge pressure* — two roles inseparable in practice — is the joint object defended as the right unit?
- [ ] Yes [ ] No merge claimed [ ] Unclear

---

## F5. Summary and disposition

**Positive answers (Yes + Flagged-and-disclosed + Partial-counts-as-half):** tally.

- **≥ 18 of 22 applicable items:** claims are well-supported at the role-system level. Recommend accept / minor revision on automation claims.
- **12–17 applicable items:** claims are mostly supported but some are extended beyond the evidence base. Recommend major revision keyed to the specific items that failed.
- **< 12 applicable items:** claims are inadequately supported at the role-system level. Recommend major revision or reject-with-invitation-to-resubmit. Attach this checklist to the decision letter so the author sees which items need strengthening.

**Items that should never be missing (any "No" here is a likely rejection trigger):**

- F1.1 (at least one durable role named)
- F2.1 (evidence for durable roles)
- F3.4 (preregistration / pre-analysis status)
- F4.1 (task-cluster vs. role alignment)

---

**Scope.** This checklist does not cover: statistical-method correctness; domain-specific construct validity; theoretical contribution beyond the role-system frame; or writing quality. Those remain the reviewer's responsibility under the journal's existing criteria. This checklist adds a shared vocabulary for adjudicating automation claims, not a replacement for substantive review.

**License.** CC-BY-4.0. Released with the role-system database at `v1.0.0-ORM-submission`. Adapt freely to journal-specific evaluation forms.
