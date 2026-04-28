# Iteration 1 Reflection — Foundation Phase

## Score trajectory

| Section | Pre-iter1 (avg of 6 reviewers) | Notes |
|---|---|---|
| Abstract | 7.6 | TR5 + structure good; weakened by κ-leading sentence |
| §1 Introduction | 7.7 | Strong; theoretical attribution gaps |
| §2 Data and Design | 7.0 | Formative declaration thin; Doty-Glick under-cashed |
| §3 Durable Roles | 7.0 | Prototype move borrowed; ex-ante motivation thin |
| §4 Shrinkage | 7.2 | **CRITICAL data error** in §4 paragraph (now fixed) |
| §5 Split Pressure | 6.8 | Rival-readings engagement weak |
| §6 Rivals & Limits | 6.7 | configural-invariance / CMV mis-applied (now fixed) |
| §7 Conclusion | 7.7 | Strong; verbatim repetition with abstract |

**Pre-iter1 overall: ~7.2.** Six reviewers converged on submission-readiness "minor revisions" verdict, with two submission-blockers and one data-integrity-critical finding.

## Iteration-1 actions applied (10)

1. **D1+D2+D3** — §4 critical data fix: re-framed asymmetry from "shrinking concentrated in 11/36 cases" to "40 shrinking codings concentrated in 3 throughput roles, zero on procedural-validity roles," with corrected counts (24/36 cases with shrinking, 12 carry zero) and corrected coverage (0.833 not 0.875) and corrected outside-gt-rich count (8 of 12 not 9 of 12). The reframe makes the asymmetry argument *substantively stronger* — zero shrinking on the §3 procedural-validity roles is a much cleaner asymmetry than the original case-level dispersion claim.
2. **E1** — AI-use disclosure (line 279): expanded one-sentence claim into three explicitly bounded uses, reconciling §6.2 LLM second-coder pass with the disclosure paragraph. Aligns with `disclosure_statement.md` packet and pre-empts the most predictable reviewer challenge.
3. **E2** — Appendix D populated with the full 17-role × 5-status sensitivity table (computed against role_coding_master.csv at the v1.0.0-ORM-submission release tag). The §6.4 cross-reference now resolves to a populated table, removing the empty-promise risk.
4. **E3** — κ disclosure stripped from abstract leading position, replaced with "Reliability is reported as a v1.0 baseline (§6.2)" — preserves TR5's v1.0-baseline framing without leading the abstract with the failure number.
5. **E4** — Missing Appendix A clarified at §Data and Code Availability: "Appendix A — the released codebook itself — is held as a versioned artifact at the release tag rather than reproduced inside this manuscript." Removes the typo-impression cheaply.
6. **A3 + abstract** — v1.1 instrument list corrected: "configural-invariance test, marker-variable CMV bound, human second-coder pass" → "case-family DIF and latent-class-invariance test, fully-blind human second-coder pass with cross-coder DIF, within-case transition-coding extension." Applied at abstract line 5 AND §6.2 line 172. The previous instruments mis-applied reflective-MGCFA invariance to a categorical formative rubric (V&L 2000) and self-report CMV (Williams et al. 2010) to coder ratings.
7. **A1 + B2 coupled** — §6.2 configural-invariance reframe: spelled out that V&L 2000 invariance is being used in a *generalized* sense (DIF + latent-class) rather than literal MGCFA; combined with §3.1 prototype theorization which converts Lord et al. (1984) from borrowed label to load-bearing diagnostic for the κ failure pattern. The two edits compose: prototype-reconstruction-failure (§3.1) explains the κ pattern, DIF/latent-class-invariance (§6.2) is the v1.1 instrument that tests the prediction.
8. **A2** — §2.4 formative measurement implications extended: explicitly stated that κ on a formative classifier indexes coder-application reliability, not indicator-trait consistency. Closes the previously-implicit gap between "formative declaration" and "construct-validity reading of the κ failure."
9. **B1** — §2.3 Doty-Glick typology-as-theory commitment made explicit: "We position the rubric as a typology in Doty & Glick's (1994) *theory-building* sense rather than in their classificatory sense" with stated empirical commitment that follows.
10. **§6.2 OSF-claim correction** — discovered during Edit 5 verification: the previous §6.2 sentence claimed the OSF pre-analysis plan committed to "CFA marker-variable test, configural-invariance test with two human coders" — but the OSF document only commits to tie-breaker revision. Honest fix: separated tie-breaker refinements (which discharge the OSF commitment) from the v1.1 instruments (which are manuscript-additional commitments beyond OSF).

## Score trajectory expected post-iter1

The data fix (item 1) and submission blockers (items 2, 3) are the most consequential. Items 4–10 strengthen the methodological footing without changing direction. Expected:

| Section | Post-iter1 (estimated) | Δ from pre-iter1 |
|---|---|---|
| Abstract | 8.5 | +0.9 (κ moved out, v1.1 list correct) |
| §2 Data and Design | 8.3 | +1.3 (formative impl. + Doty-Glick) |
| §3 Durable Roles | 8.0 | +1.0 (prototype theorization) |
| §4 Shrinkage | 8.5 | +1.3 (data fix + reframe) |
| §6 Rivals & Limits | 8.0 | +1.3 (configural-invariance reframe + v1.1 list) |
| §Transparency | 9.0 | +0.5 (AI-use disclosure) |
| Other sections | unchanged from pre-iter1 |

**Estimated post-iter1 overall: ~8.0.** Convergence threshold: 7.5 + every section ≥ 7. Both criteria likely met after iter1; the question is whether iter2 closes residual gaps to 8.5+.

## What iter2 should focus on (Argument Sharpening)

Defer items not addressed in iter1:
- **B3** — ex-ante theoretical motivation for the procedural-validity triple (procedure + calibration + accountability as the smallest closed set discharging procedural validity)
- **B4** — theoretical attribution for H1/H2/H3 (Abbott / Autor+Frey-Osborne / Barley)
- **B5** — role-system framing inoculation (task-level / workflow-level alternatives)
- **A4** — Table 1 firing rule explicitness
- **A5** — "procedure constitutes the task" softening
- **D2 (Agent D)** — §5 institutional + evolutionary rival readings
- **D4 (Agent D)** — procedural-prose density confound emphasis
- **D5 (Agent D)** — dropped-case pool size disclosure
- **C1** — verbatim "anchored deductively" repetition (abstract ↔ §7.3)
- **C2** — X-not-Y residue
- **C3** — sentence economy worst offenders
- **C4** — backticks vs italics standardization
- **C5** — paragraph transitions

## Agent performance reflection

| Agent | Iter1 verdict |
|---|---|
| **A (Methodology)** | ★★★★★ — caught the configural-invariance / CMV miscategorization. Highest-leverage agent for iter1. |
| **B (Domain Theory)** | ★★★★☆ — Doty-Glick + Lord et al. theorization moves are foundation-grade lifts. |
| **C (Prose)** | ★★★☆☆ — solid catalog of polish-tier issues; deferred to iter3. |
| **D (Comparative Methods)** | ★★★★☆ — surfaced Section-5 weakness and the cell-vs-case forward-pointer issue; some items deferred. |
| **E (Submission Process)** | ★★★★★ — caught the AI-disclosure / §6.2 contradiction (submission-blocker) and the empty Appendix D promise (submission-blocker). |
| **F (Data Auditor)** | ★★★★★ — caught the §4 critical data error that all other agents missed. Single most valuable finding of iter1. |

For iter2, drop Agent C focus (defer prose to iter3); strengthen Agent B and Agent D prompts to surface remaining argument-sharpening issues.

## Convergence status

- ❌ Convergence not yet declared (need full re-review at iter2 to compute post-iter1 scores)
- ❌ All sections ≥ 7: estimated yes after iter1, but pending re-review
- ❌ Score improvement < 0.5: not measured yet
- ❌ Word count stable: changed +574 words, not stable
- ❌ Diminishing returns: 10 actions changed in iter1, well above 3-item floor

**Decision:** Continue to iteration 2 (Argument Sharpening phase).
