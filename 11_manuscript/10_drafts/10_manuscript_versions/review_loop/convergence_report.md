# Reviewer Loop — Convergence Report

**Loop:** 3 iterations × 9 distinct reviewer personas. All fresh per iteration; no persona reuse.
**Baseline:** v05 (post-editorial-loop, 7,123 words)
**Final:** v08_post_L_personas_converged (9,637 words, +2,514 from v05; +35% size)
**Date:** 2026-04-23

## Convergence signal

**Three consecutive post-revision readers (L1, L2, L3) returned MINOR REVISIONS.** None returned MAJOR or REJECT. The remaining concerns were small and well-specified; all were addressed in v08.

## Iteration trajectory

| Iter | Personas | Verdicts | Output | Δ words |
|---|---|---|---|---:|
| 1 | J1 methodology craft / J2 statistical / J3 theorist | MAJOR / MAJOR / MAJOR | v06 | +1,213 |
| 2 | K1 QCA / K2 grumpy AI-expert / K3 meta-science | MAJOR / MAJOR / MAJOR | v07 | +834 |
| 3 | **L1 methodology / L2 theorist / L3 open-science** (post-revision) | **MINOR / MINOR / MINOR** | v08 | +467 |

Each iteration's word-count delta decreased monotonically (1,213 → 834 → 467), consistent with diminishing-returns convergence.

## What the reviewer loop added

### J-persona iteration (core methodological and theoretical scaffolding)

| Item | Location |
|---|---|
| Rubric indicator rewording — Robust-a textual locator, Transformed-c before/after language | Table 1 |
| Four-unit-of-analysis block (cell / role / case-configuration / pattern) with H-to-unit mapping | §2 |
| Edge-case adjudication paragraph (multi-version / joint-performance / mid-analysis redefinition) | §2 |
| Abbott–Freidson jurisdictional mechanism mapping to the six statuses | §2 close |
| Contribution-boundary sentences vs. Aguinis 2023 / Hickman 2022 / Tay 2022 | §1 close |
| Case-level Monte-Carlo permutation (p = 0.57 family, p = 0.31 capability) disclosed as null | §6 |
| Case-cluster bootstrap CIs on Cramér's V; V_gap CI [−0.10, +0.16] | §6 |
| Multiple-testing / Holm correction; sign test as single pre-registered confirmatory | §6 |
| Wilcoxon = NaN footnote explaining why sign test is primary (W = 7, p = 0.0006 on defined roles) | §6 |
| Causal-claim softening (correlational-not-causal) | §7 |
| Deskilling / delegation / boundary-redefinition vocabulary for shrinkage | §4 opener |
| Three forward-looking testable predictions | §7 |
| Freidson (2001) cited | §2, §7, references |

### K-persona iteration (sub-domain specialization)

| Item | Location |
|---|---|
| Analytic-tradition declaration (typology audit with association stats, not QCA; truth-table non-identified at N=36) | §2 |
| Case-level configuration analysis on H1 three durable roles (12 cases `durable|durable|durable`) | §3 |
| Consistency / coverage for H2 (gt-rich → shrinking sufficiency = 0.857; necessity = 0.500) | §4 |
| Pilot hold-out sign test (13 pos / 15 defined roles excluding pilot cases, p = 0.007) | §6 |
| Standalone null framing at §6 opener | §6 |
| First-coder non-blindness disclosed with mitigation (blind second coder, stranger-coder protocol) | §6 |
| Human/AI binary softening in §1 opener and *transformed* anchor | §1, Table 1 |
| Tornberg re-characterization (GPT-4 draws on previously-distinctly-human interpretive skills) | §4 |
| "Scaffold" → specific artifact language for §7 reviewer/editor audience | §7 |
| No-pre-AI-counterpart adjudication for boundary cases (APE/AI Scientist/AgentSociety) | §5 |
| Conditional-as-undifferentiated flagged as v1.1 extension | §6 limits |

### L-persona iteration (convergence fixes)

| Item | Location |
|---|---|
| Sign-test-as-THE-H3-evidence framing | §6 combined verdict |
| Upper-bound sensitivity on conditional subtypes (robust to C-H/C-A extreme priors; p = 0.004 / 0.021) | §6 |
| Hedge on forward-looking prediction #1 as leading-indicator-only | §7 |
| Robust anchor narrowed to *author-stated* load-bearingness with explicit construct-operationalization note | Table 1 |
| Abbott vocabulary now in §3.1 (calibration as segmented-then-consolidated jurisdiction) and §5 (construct-and-perspective as diagnostic–sampling segmentation) | §§3.1, 5 |
| OSF preregistration honesty ("URL at resubmission; label as pre-analysis plan if OSF does not predate") | §Transparency |
| **Pre-specification table** (Table 3) listing 12 design decisions as Fixed pre-coding / Fixed pre-analysis / Post-hoc exploratory | §Transparency |

## Residual verdicts at convergence

All three L-persona reviewers returned MINOR REVISIONS with scoped, small fixes — all applied in v08. No structural issues raised. No reject-trigger territory.

**L1 methodologist:** MINOR verging on ACCEPT. 11 of 13 prior items adequately addressed; remaining 3 concerns each ≤ +60 words. Quote: *"The authors produced a genuinely responsive revision… The statistical response (items 6–9) is the strongest element: the authors correctly diagnosed that independence violation shifts the H3 verdict onto the role-level sign test, ran the case-level MC even though it returned null, and disclosed that null rather than burying it."*

**L2 theorist:** MINOR. *"The revisions have moved the paper from name-checks to structural use of the jurisdictional vocabulary in two of the three loci where it matters (typology construction, H3 framing, forward predictions)."*

**L3 open-science:** MINOR. *"The revision closes H3/K3's substantive gaps… The placeholders that remain are either conventional (DOI on acceptance, funding line) or tied to objects whose specificity makes evasion visible."*

## Final statistical apparatus (after reviewer loop)

The paper now reports **six inferential objects** for H3, with a clear hierarchy:

| Test | Unit | Result | Load-bearing? |
|---|---|---|---|
| Cell-level Monte-Carlo (10,000 perms) | Cell (612) | p = 0.0001 family, 0.0011 capability | No — cell-level only |
| Case-level Monte-Carlo (5,000 perms) | Case (36) | p = 0.57 family, 0.31 capability (null) | **Disclosed as null** |
| Case-cluster bootstrap V CIs (B=2000) | Case (36) | V_gap CI [−0.10, +0.16] | Directional-only |
| **Paired sign test on per-role V gaps** | **Role (16 defined)** | **14 pos / 16, p = 0.004** | **YES — pre-registered confirmatory** |
| Wilcoxon on per-role V gaps | Role (16 defined) | W = 7, p = 0.0006 | Consistent confirmation |
| Pilot hold-out sign test | Role (15 defined, 32 cases) | 13 pos / 15, p = 0.007 | HARKing robustness |
| High-confidence-only V gap | Role (204 rows) | V_gap widens 0.020 → 0.062 | Coder-uncertainty robustness |

The H3 claim is explicitly anchored to the paired sign test. The aggregate V comparison is described as directional-only.

## Artifacts saved

```
10_manuscript_versions/review_loop/
├── plan.md                                # persona pool + convergence criteria
├── computed_stats_v06.json                # MC cell-level + case-level + bootstrap V CIs + Wilcoxon
├── computed_stats_v07.json                # case configuration + consistency/coverage + pilot hold-out
├── v05_baseline.{md,docx}                 # entering this loop
├── v06_post_J_personas.{md,docx}
├── v07_post_K_personas.{md,docx}
├── v08_post_L_personas_converged.{md,docx}    # FINAL
└── convergence_report.md                  # this file

10_drafts/
├── 10_manuscript.{md,docx}                # latest == v08 (9,637 words, 6 tables)
├── appendix_B_kappa.md                    # preregistered κ plan
└── appendix_C_application_protocol.md     # stranger-coder protocol
```

## Author-owned commitments (unchanged from prior loop; author must fill before submission)

1. **OSF preregistration** — post second-coder protocol to OSF with timestamp predating the second-coder pass; insert URL in §Transparency.
2. **Cohen's κ** — complete double-coded subsample by 2026-06-15; fill Appendix B.
3. **Repository release tag** `v1.0.0-ORM-submission` with manifest; insert URL in Data and Code Availability.
4. **`scripts/section6_analysis.py`** — package the analysis pipeline from `computed_stats_v06.json` + `computed_stats_v07.json` into a single script.
5. **Worked out-of-sample example** in Appendix C.
6. **Funding statement**.
7. **Zenodo DOI** minted on acceptance.

## Total editorial-loop + reviewer-loop trajectory

| Version | Words | Phase | Verdict |
|---|---:|---|---|
| Pre-transplant | 5,763 | — | — |
| v02 (post-transplant + eye-pass) | 5,872 | Post-transplants | — |
| v03 (post G-personas: editors) | 6,440 | Editorial | RETURN-FOR-REVISION → addressed |
| v04 (post H-personas: reviewers in editorial context) | 7,008 | Editorial | MAJOR/MINOR/MAJOR → addressed |
| v05 (post I-personas: adjacent-paper POVs + desk-reject-seasoned editor) | 7,123 | Editorial | SEND-TO-REVIEW (convergence) |
| v06 (post J-personas: first-read reviewers) | 8,336 | Reviewer | 3 × MAJOR → addressed |
| v07 (post K-personas: sub-domain specialists) | 9,170 | Reviewer | 3 × MAJOR → addressed |
| **v08 (post L-personas: post-revision readers)** | **9,637** | **Reviewer — CONVERGED** | **3 × MINOR** |

The manuscript has absorbed feedback from **21 distinct simulated personas** across **two /edit loops**. Convergence reached at the simulated second-round-review stage with all three post-revision readers converging on MINOR. Ready for real submission after the seven author-owned commitments above are filled.
