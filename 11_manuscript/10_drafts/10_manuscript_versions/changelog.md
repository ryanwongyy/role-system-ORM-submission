# Edit Loop Changelog

## v00 — baseline (2026-04-23)
Post-transplant post-eye-pass state. Word count: 5,763.

## v01 — post edit-loop iteration 1 (2026-04-23)
Word count: 5,872 (Δ +109).

### Agents deployed
- Agent A — Methodology reviewer (ORM register)
- Agent C — Prose editor (ORM house style)
- Agent F — Data integrity auditor (role_coding_master.csv cross-reference)

### Critical (data alignment)
1. **Keith/Case 2 role reassignment.** Agent F found that Case 2 (Keith 2026) is coded `conditional` for Protocol and provenance architect, not `robust`. However, Case 2 IS coded `robust` for Construct and perspective boundary setter. §3.0 exemplar reassigned accordingly. The Baccolini/Keith "coexistence" sentence (which asserted both on the same role) was removed as it no longer holds. First-round verification agent (pre-edit-loop) had hallucinated the robust-PPA assignment; Agent F's pandas-based audit caught it.

### High-priority (methodological)
2. Cramér's V hedging (§6 Combined verdict): aggregate 0.02 V-gap now explicitly flagged as "not claimed statistically distinguishable on its own"; per-role 14/17 check carries the inferential weight.
3. Rubric tie-breaker added below Table 1: *transformed* vs. *conditional* distinguished by changes in role content vs. changes in role scope.
4. Cohen's κ commitment added to §6 rival-explanations paragraph (points forward to Appendix B stub produced by the inter-coder task).
5. §7 "offers a diagnostic" → "offers a provisional scaffold for identifying" to stay inside the `framework` claim ceiling.

### Medium-priority (prose)
6. Abstract *Third* sentence split from compound-monster into three sentences; parallelism with *First*/*Second* restored.
7. §3.0 Exemplars paragraph broken into three paragraphs (robust/conditional/transformed — then shrinking/split/merge — then the navigational note).
8. §3.0 closing run-on split into two sentences.
9. §6 "Convergence" run-in head → "Combined verdict" to strip ML register.
10. §7 institutional-actors pivot sentence split for cadence.

### Low-priority (consistency)
11. Table 1 column header "Behavioural" → "Behavioral" for internal American-English consistency.

### Residual scan
- All 6 exemplar case IDs verified in current prose (Case 2 / 7 / 29 / 1 / 3 / 10).
- Keith cross-reference "(Keith 2026; see §3.0 Exemplars)" in §3.1 still resolves correctly.
- All six exemplar authors present in Provisional References.
- No UK spellings surviving.
- Table numbering 1 → 2 → 3a → 3b → 4 consistent.

### Remaining latent commitments
- **Cohen's κ** on double-coded 10% subsample (4 cases, 68 role × case cells) — queued to a separate session; feeds into Appendix B.
- **Supplementary joint-model table** (status ~ family × capability with interaction) — deferred until reviewer asks; the new V-hedge sentence at §127 pre-empts the objection.
- **Typography flag (backticks vs. italics)** for rubric-code references (`framework`, `transformed`, etc.) — typesetting-level decision; not a draft-level fix.

### Convergence decision
No iteration 2 required. All top 5 issues from each of the three agents addressed. Data alignment phase triggered but resolved in a single edit. Residual scan clean. Scoring trajectory (qualitative, from the three agents' section scores):

- Abstract: 7–8 → 8–9 (parallelism restored; Third sentence tightened)
- §2 Table 1: 6–8 → 8 (tie-breaker rule added; US English consistent)
- §3.0 Exemplars: 6–8 → 8 (Keith alignment fixed; paragraph split; closing de-run-on)
- §3.1 opening: 8 → 8 (no change needed; Keith cross-ref preserved)
- §6 two-lens: 6–7 → 8 (V hedge added; "Combined verdict" replaces "Convergence")
- §7 stakeholder: 7 → 8 (claim ceiling restored; pivot cadence restored)

Overall mean 6.8–7.2 → 8.0 after one iteration; convergence criterion (avg ≥ 7.5, every section ≥ 7) met.
