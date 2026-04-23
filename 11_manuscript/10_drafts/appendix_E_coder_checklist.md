# Appendix E — Coder Protocol (Pending Second-Coder Reliability Upgrade)

**Companion artifact.** The reviewer-audit checklist in Appendix F is the downstream counterpart of this protocol: Appendix E tells a coder how to assign a status; Appendix F tells a reviewer what to look for in the resulting coding. Items E1.2, E3.2, E3.3, and E4.1 each record a quoted sentence that Appendix F items F2.1, F2.3, and F3.5 then audit.

**Purpose.** This protocol operationalizes the rubric in Table 1 of the main manuscript as a numbered sequence of binary decisions, so a new coder can apply the rubric to a new case without consulting the authors. Each item is yes/no. The protocol is used once per (role × case) cell — 17 cells per case.

**Status and ceiling.** This protocol is released as the **v0.3 coder protocol** for the role-system rubric. It is *not* an instrument at acceptance-grade reliability: the current LLM-agent second-coder pass yields Cohen's κ = 0.289 (95% CI [0.147, 0.439]), below the 0.60 pre-committed threshold (see §6 and Appendix B). The protocol is what a pending human second-coder pass will be asked to apply, and the v1.1 release will carry the resulting κ and any tie-breaker revisions. Adopting this protocol for a new coding pass is therefore appropriate only under the "preliminary framework" claim ceiling stated in the abstract.

**How to use.** For each role observable in the case, answer items E1 through E4 in order. The branching path through the questions terminates at one of the eight status labels. If at any point the item is truly ambiguous, default to *unclear* rather than forcing a status.

---

## E1. Observability gate

E1.1 Does the case file contain at least one quotable sentence of direct evidence that this role is performed (or deliberately not performed) in the case's research workflow?
- Yes → continue to E2.
- No → assign **not_applicable**; stop.

E1.2 If yes, record the quoted sentence and its source-file location (page or section pointer) in the evidence-summary column.

---

## E2. Reconfiguration gate

E2.1 Does the case describe the role as performed by humans in a way that is jurisdictionally stable (no explicit reconfiguration under AI involvement)?
- Yes → continue to E3 (allocation-stable path).
- No → continue to E2.2.

E2.2 Does the case reveal that the starting role conflates two distinct activities that should be coded separately?
- Yes → assign **split pressure**; confirm the second-criterion substantive check (§2 of the main manuscript) before finalizing; stop.
- No → continue to E2.3.

E2.3 Does the case report that the evidence for this role is inseparable from the evidence for another role within this case?
- Yes → assign **merge pressure**; note the paired role in the evidence-summary; stop.
- No → continue to E3 (allocation-revised path).

---

## E3. Allocation-stable path — Robust vs. Conditional

E3.1 Does the case treat the role as methodologically load-bearing for the study's inferences (named in methods/abstract/limitations as load-bearing)?
- Yes → continue to E3.2.
- No → go to E4 (shrinking / transformed check).

E3.2 Does the case specify that AI substitution would not preserve validity, or does the role appear in reported limitations as load-bearing?
- Yes → assign **robust** with high confidence; stop.
- No → assign **robust** with medium confidence; record the partial-evidence basis; stop.

E3.3 (Conditional sub-check.) Does the case name at least one explicit moderator variable — a specific task feature, data property, or institutional setting — under which human performance is required?
- Yes → assign **conditional**; record the moderator; stop.
- No → return to E4.

---

## E4. Allocation-revised path — Transformed vs. Shrinking vs. Unclear

E4.1 Does the case describe a qualitative shift in what humans do at this step, using before/after language or a verb swap (e.g., "write" → "review"), or name a new sub-task as new?
- Yes → assign **transformed**; record the content-change sentence; stop.
- No → continue to E4.2.

E4.2 Does the case report public ground truth or a high-consensus target for this activity, AND does the case report AI matching or exceeding human performance on a defined subset?
- Yes → continue to E4.3.
- No → continue to E4.4.

E4.3 Is residual human labor characterized as audit, exception handling, rescue, triage, or verification?
- Yes → assign **shrinking**; stop.
- No → assign **conditional** (the task has partial AI substitution but human labor is still primary); stop.

E4.4 Final fallback: is the evidence contradictory or thin?
- Yes → assign **unclear** with low confidence; record the thin-evidence basis; stop.
- No → reconsider E3.1 with looser interpretation; if still no status fits, assign **unclear**.

---

## E5. Confidence recording

After the status is assigned:

- **High** confidence: all three of the status's behavioral indicators in Table 1 fire cleanly; no counter-indicator is present; the evidence is based on a direct quote.
- **Medium** confidence: two of three indicators fire, or one indicator is partial; evidence is based on a quote plus inference.
- **Low** confidence: one indicator fires or indicators are contradictory; evidence is inferential only.

---

## E6. CSV row log

Append one row to `role_coding_master.csv` (or to a new-case-submissions file) with the columns:

```
case_id, role_label, role_group, role_observable_in_case, status_in_case,
confidence, evidence_basis_summary, main_supporting_source_ids,
main_contrary_source_ids, notes
```

Always record:
- The quoted sentence from E1.2 in the `evidence_basis_summary` column
- Any moderator named in E3.3 or before/after phrase from E4.1 in `notes`
- Any tie-breaker invocation (E3 to E4 jump, or E4.3 vs. E4.4) in `notes`

---

## E7. Reporting and release

When all 17 roles have been coded for the case:

- Attach the quoted evidence to each row
- Record the rubric version used (current: v0.3)
- If the case triggers a split or merge pressure, propose the role revision as a candidate for codebook v1.1 and release the proposal alongside the coding CSV

---

**Design notes.** This protocol is a decision-tree operationalization of Table 1. The Aguinis, Ramani & Alabduljader (2023) *ORM* checklist is 40 indicators across 10 latent factors, derived from a content analysis of 168 reviews; this protocol is 18 yes/no items plus 6 status-specific sub-items, derived from the rubric as designed. That evidentiary-base difference is real: their indicators are *empirically observed* in a 168-review corpus, ours are *operationally defined* from a six-status rubric. The v1.1 human second-coder pass is the first step toward closing the evidentiary gap; a content-analytic expansion against a larger case pool is the second step. The protocol is released under MIT license; improvements are welcome as pull requests against the GitHub repository.
