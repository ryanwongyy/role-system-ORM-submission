# Desk-Reject Risk Memo — Post-Editorial-Loop

**Manuscript:** `From Repository to Role System: A Comparative Typology Audit of 36 Cases`
**Target venue:** *Organizational Research Methods* (ORM)
**Final version:** `v05_post_I_personas_converged` (7,123 words, +1,251 from v02 baseline)
**Loop date:** 2026-04-23
**Convergence signal:** Iteration 3 simulated AE (I3 — editor with recent AI-in-research desk-reject history) returned **SEND-TO-REVIEW** verdict.

## Editorial-loop summary

| Iteration | Personas | Verdict-in-aggregate | Key interventions |
|---|---|---|---|
| 1 (v03) | G1 EiC / G2 multi-method AE / G3 quantitative AE / G4 copyeditor | All four: RETURN-FOR-REVISION-BEFORE-REVIEW | κ commitment tightened; case-selection protocol; typology-derivation paragraph; sparseness-robust MC p-values (seeds disclosed); paired sign test on 16 roles (p = 0.004); Cohen df-adjusted V rubric; confidence-stratified V gap widens to 0.062; merge-pressure n=2 flagged in abstract; APA mechanicals (citation commas, title case, hyphenation) |
| 2 (v04) | H1 skeptical methodologist / H2 sympathetic theorist / H3 open-science advocate | H1 MAJOR / H2 MINOR / H3 MAJOR | Role-system construct defined; Abbott frame activated in §7; allocation/specification axes paragraph; "constitutive of epistemic validity" anchor; Data & Code Availability block; Transparency and Disclosures note; Appendix B upgraded to preregistered plan; split-pressure two-criterion rule (mechanical + substantive); exemplar pilot-origin disclosure |
| 3 (v05) | I1 Hickman 2022 author / I2 Aguinis 2023 author / I3 AI-in-research desk-reject editor | I1 BELOW-BAR / I2 PARTIAL / **I3 SEND-TO-REVIEW** | Front-loaded allocation/specification axes to §1; ORM-venue-specific paragraph at §1 close citing Aguinis 2023 and Hickman 2022 as instrument-tradition precedents; Appendix C stranger-coder protocol |

## Desk-reject-risk assessment by ground

| Ground | v02 baseline | v05 converged | Evidence |
|---|---|---|---|
| **Scope fit** (is this a methods paper?) | Medium risk | **Low** | §1 opener now anchored as rubric-delivery paper; §1 close cites ORM instrument-tradition precedents; rubric on page 1 of content |
| **Methodological contribution clarity** | Medium risk | **Low** | Tripartite abstract; allocation/specification axes distinguish from Aguinis 2023, Hickman 2022, Tay 2022; six-status rubric with behavioral anchors and tie-breaker |
| **Rigor of coding scheme** | High risk | **Low-medium** | Pilot disclosed; split/merge decision rule stated; two-criterion symmetry audit; κ preregistered with committed target ≥0.60 and tie-breaker remedy; exemplar pilot-origin disclosed |
| **Statistical discipline** | High risk | **Low** | MC p-values alongside asymptotic; sign test independent of aggregate V; confidence-stratified robustness (gap widens 0.020 → 0.062); boundary-case sensitivity; Cohen df-adjusted V rubric cited |
| **Replication / open-science** | High risk | **Low** | Data & Code Availability block; repo URL / DOI / license / manifest; named analysis script; version-locked snapshot; Transparency and Disclosures note; preregistered Appendix B with drop-dead date |
| **Generalizability / claim-ceiling drift** | Medium risk | **Low** | "In this 36-case repository" bracketing at §6; Abbott-implication sentence with explicit non-generalization; "scaffold for locating" replaces "diagnostic for" in §7 |
| **Prose / house style** | Medium risk | **Low** | All in-text citations have APA commas; title-case headings; American English; em-dash / en-dash / hyphen distinguished; curly quotes |

## Residual risks — NOT blocking desk-reject but may return in reviewer reports

| Risk | Source | Severity | Status |
|---|---|---|---|
| κ point estimate and 95% CI are `[TBD]` pending second-coder pass | H3 open-science | Medium | Preregistered with 2026-06-15 drop-dead; the κ task is spawned as a parallel session chip |
| No convergence-divergence table per-role cell between V_family and V_capability (the full Hickman 2022 two-lens execution) | I1 Hickman-author POV | Low-medium | Flagged as future revision; not desk-reject-critical per I3 |
| No binary-indicator checklist paired to Table 1 (the full Aguinis 2023 instrument execution) | I2 Aguinis-author POV | Low-medium | Flagged as future revision; Appendix C protocol partially addresses |
| Per-audience differentiated deliverables for methods researchers / reviewers / institutional actors | I2 Aguinis-author POV | Low | §7 already names them; differentiated appendices deferred |
| Convergent-validity check on shrinking-status coding against within-case reported performance | I1 Hickman-author POV | Low | Flagged as future revision |
| Worked out-of-sample application in Appendix C | I2 stranger-coder | Low | Appendix C currently a stub for this worked example |
| Rubric-stability holdout never used in anchor refinement | I1 Hickman-author POV | Low | The pilot-vs-main-pass distinction partially addresses |
| Repo URL, DOI, commit hash, OSF preregistration link, funding disclosure — all bracket-placeholders | H3 open-science | Low | Must be finalized before submission (manual author step) |

## Latent commitments the editorial loop created

1. **Second-coder pass must complete by 2026-06-15** per preregistered Appendix B. Produces κ values that fill the [TBD] placeholders in Appendix B.
2. **Repository release tag `v1.0.0-ORM-submission`** must be created with the five named artifacts before submission.
3. **OSF preregistration** for the second-coder protocol must be posted *before* the second coder begins work (signed by the first author with a timestamp predating the full-coding pass).
4. **`scripts/section6_analysis.py`** referenced in §6 Data & Code Availability must be a single self-contained script reproducing every numeric value listed (χ² = 87.67, MC *p* = 0.0001, V = 0.260, V_family = 0.267, sign-test *p* = 0.004). The verification computation done during iteration 1 of this loop is the prototype; packaging it as the named script is a manuscript-prep task.
5. **Funding and COI disclosures** need concrete text before submission (currently "[to be added at submission]" and "none declared").

## Score trajectory (editorial-fitness, qualitative mean across personas)

- v02 baseline (pre-loop): ~7.0 (generic-editor loop already converged)
- v03 after G-personas: ~7.5 (all four editors moved from RETURN-FOR-REVISION to implicit SEND-TO-REVIEW)
- v04 after H-personas: ~8.0 (theorist H2 gave MINOR-REVISIONS; open-science H3 still MAJOR on disclosure placeholders)
- v05 after I-personas: ~8.5 (desk-reject-seasoned editor I3 gave SEND-TO-REVIEW; two remaining fixes applied)

**Convergence criterion met:** I3, the persona constructed to be the hardest-on-AI-in-research-papers desk-reject filter in the panel, returns SEND-TO-REVIEW. Continued iteration on I1/I2's structural asks would improve publishability (full Hickman/Aguinis template fidelity) but would not further reduce desk-reject risk.

## Recommended next steps for the author

1. **Complete the second-coder pass** (spawned task from earlier session — runs in its own session).
2. **Finalize repository tag, Zenodo DOI, OSF preregistration** and replace bracket-placeholders in §6 Data & Code Availability.
3. **Finalize the `scripts/section6_analysis.py`** file from the computation done in this loop's iteration 1.
4. **Decide on the Hickman/Aguinis full-template additions** flagged in the residual-risks table: adding the convergence-divergence table (I1) and the binary-indicator checklist (I2) would take the paper from "desk-reject-safe" to "strong-revise candidate" territory, but are not required for first submission.
5. **Submit.**
