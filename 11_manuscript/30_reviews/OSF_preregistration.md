# Pre-analysis plan (OSF-ready) — Inter-coder Reliability Pass for "From Repository to Role System"

**Study:** *From Repository to Role System: A Comparative Typology Audit of 36 Cases*
**Target venue:** *Organizational Research Methods* (ORM)
**Document status at v1.0.0-ORM-submission:** **pre-analysis plan**. An independent OSF registration was not posted before the second-coder pass; this document is OSF-ready but not OSF-timestamped, and the manuscript labels it accordingly. OSF registration is a recommended post-submission step; the document may then be uploaded as-is.
**Plan purpose:** Pre-commit the second-coder protocol for computing Cohen's κ on a stratified 10% subsample of the role-status coding, and pre-commit the remedy for per-status κ values below the acceptance threshold.

---

## 1. Background and hypotheses

The main manuscript proposes a six-status role-status rubric (*robust, conditional, transformed, shrinking, split pressure, merge pressure*) with behavioral anchors and a conditional-vs-transformed tie-breaker. The four allocation statuses are deductively anchored to the automation-augmentation paradox literature (Raisch & Krakowski, 2021; Autor, 2015); the two specification operations (split / merge pressure) emerged inductively from constant comparison across cases. All role × case cells (n = 612) were coded by the first author against this rubric. This preregistration covers a stratified 10% subsample to be independently re-coded by a second coder for reliability assessment.

The hypotheses H1–H3 and the statistical analysis plan (including the sign test as single pre-registered confirmatory test, the Holm correction across robustness checks, and the case-cluster bootstrap for V confidence intervals) were fixed before the full-coding pass per the manuscript's Transparency and Disclosures pre-specification table. This preregistration is therefore an addition to — not a replacement for — that earlier commitment.

## 2. Subsample (pre-specified)

Four cases, stratified to span the four largest case-family clusters and to include at least one case from each primary AI capability:

| Case ID | Author/year | Case family | Primary AI capability |
|---|---|---|---|
| 2 | Keith, 2026 | Measurement & coding | Generative |
| 7 | Baccolini, 2026 | Evidence synthesis & corpus | Generative |
| 3 | Gligorić, n.d. | Interviews, fieldwork & qualitative interpretation | Generative |
| 27 | Kang, 2025 | Reproducibility & autonomous research | Agentic |

Total cells to re-code: **4 cases × 17 roles = 68 cells.**

The subsample was selected before the second coder was contacted. A rationale document for the stratification is released with this preregistration.

## 3. Second-coder protocol (pre-specified)

1. The second coder is provided exclusively with:
   - The rubric (Table 1 of the main manuscript, including the conditional-vs-transformed tie-breaker stated below the table);
   - The six role-status labels plus `unclear` and `not_applicable`;
   - The four case files (primary-source PDFs).
2. The second coder is **blind** to: (a) the first coder's status assignments, (b) the first coder's evidence-summary column, (c) the manuscript's hypotheses H1–H3, (d) the exemplar case-to-status mapping in §3.0.
3. The second coder assigns one of eight labels (six observable statuses plus `unclear`, `not_applicable`) to each of the 68 cells, independently.
4. Second-coder assignments are recorded in `/06_analysis_tables/role_coding_secondcoder_subsample.csv`. This file is NOT merged into the master table.

## 4. Reliability computation (pre-specified)

- **Pooled Cohen's κ** is computed over all 68 cells using the six-status rubric, with `unclear` and `not_applicable` pooled into a single "not-observable" category to match how the main manuscript's χ² analyses treat them.
- **Per-status Cohen's κ** (one-vs-all) is computed for each of the six observable statuses.
- **95% confidence intervals** are computed via 2,000-iteration bootstrap over the 68 cells.
- Every divergent cell is recorded in a disagreement log with a one-line diagnosis of which behavioral indicator was read differently.

## 5. Pre-committed acceptance criteria and remedies

- **Pooled κ ≥ 0.60** is the submission target for acceptance-grade reliability.
- **Pooled κ < 0.60**: authors acknowledge the rubric has not met acceptance-grade reliability and flag this as a limitation in §6. The manuscript's claim ceiling is adjusted downward from "framework" to "preliminary framework."
- **Per-status κ < 0.60 on any single status**: authors pre-commit to revising the Table 1 tie-breaker text for that status and documenting the revision in the disagreement log before resubmission. No status is re-coded in the main pass based on post-hoc information.
- **Merge pressure** (n = 2 cells in the full database, both on Case 10 Hajishirzi): not included in the 68-cell subsample by construction. Per-status κ for merge pressure is not estimable and is disclosed as a limitation.

## 6. Drop-dead date

Second-coder pass must complete by **2026-06-15.** If complete before the manuscript is submitted for review, the κ values are inserted into Appendix B. If not complete before submission, the manuscript is resubmitted with Appendix B marked as "forthcoming" and the κ is provided as a conditional-acceptance artifact.

## 7. Release and access

The second-coder CSV (`role_coding_secondcoder_subsample.csv`), the disagreement log, and this preregistration document are released at the same commit as the computed κ, under release tag `v1.0.0-ORM-submission` at `[repository URL]`, mirrored at DOI `[Zenodo DOI to be minted on acceptance]`, under CC-BY-4.0 for data and MIT for code.

## 8. What this preregistration does NOT cover

- The rubric itself (frozen at codebook v0.3 after the four-case pilot).
- The main-coding pass (n = 612 cells) — already complete; first-coder non-blindness disclosed as a limitation in the manuscript.
- The statistical analysis plan for H1–H3 (already pre-registered; see Transparency and Disclosures pre-specification table in the manuscript).
- HARKing risk from pilot cases (addressed by the hold-out analysis reported in the manuscript, not by this preregistration).

## 9. Conflict of interest and authorship

The first author of the manuscript and the first coder are the same individual. The second coder is independent and has no financial or academic stake in the outcome. No generative AI system is used in the second-coder pass.

## 10. Versioning

Version 1.0 (YYYY-MM-DD UTC). Any change after posting is tracked in an OSF registration update.

## 11. v1.1 redesign blueprint (pre-registered)

This section pre-registers the v1.1 redesign that addresses the v1.0 reliability shortfall at the source rather than after the fact. The redesign will be executed against the 2027 hold-out described below; this section is timestamped before any v1.1 coding pass.

### 11.1 Coding-scheme redesign

The v1.0 rubric anchors deductively to the automation-augmentation paradox literature (Raisch & Krakowski, 2021; Autor, 2015). v1.1 replaces this single anchor with a peer-reviewed AI-work-design taxonomy as the deductive starting point. Two candidate taxonomies are pre-specified, with the choice made before pilot coding:

- Brynjolfsson & Mitchell (2017) Suitable-for-Machine-Learning rubric — applied at the activity-level role rather than the task level, with explicit operationalization documented in the v1.1 codebook.
- Daugherty & Wilson (2018) "missing middle" 6-band human-machine collaboration spectrum — applied at the activity-level role with documented mapping to the rubric's status-cell schema.

One inductive specification operation is added if and only if the calibration pilot (§11.2) surfaces a pattern the borrowed taxonomy cannot accommodate. The locked codebook is released alongside the OSF timestamp.

### 11.2 Two-coder calibration protocol

A 4-case calibration pilot is coded independently by two coders. Both coders complete pre-coding calibration sessions on the locked codebook. The instrument is locked for main coding only after pooled Cohen's κ ≥ 0.70 is reached on the pilot. The κ ≥ 0.60 v1.0 threshold is raised to κ ≥ 0.70 because the v1.0 κ failure was diagnostic of insufficient pre-coding calibration rather than of an unmeasurable construct. If κ ≥ 0.70 is not reached after two calibration rounds, the v1.1 instrument is sent back for redesign before any main coding; the released disagreement log documents the redesign trigger explicitly.

### 11.3 External instrument review

A 3-person expert panel of ORM-published methods scholars reviews the locked instrument before main coding (lightweight Delphi). Panel selection criteria are pre-specified: at least one scholar with published work on (a) construct validity / measurement, (b) configurational / typological theorizing, and (c) AI-organizing or AI-in-research methods. Panel feedback is released as an annex alongside the locked codebook; substantive panel objections trigger a documented instrument revision pass before main coding.

### 11.4 Main coding pass

The v1.1 main coding pass operates on the 2027 hold-out at N = 60 cases (a target sampling frame independent of the v1.0 36-case base, drawn from a parallel preprint-and-published-article window 2026-05 to 2027-04). Both coders code all 60 cases independently, blind to (a) the other coder's status assignments, (b) the manuscript's hypotheses, (c) the v1.0 case-status mapping. Disagreement adjudication follows the §3 protocol of this preregistration applied to the new instrument.

### 11.5 Triangulated analysis plan

Three analytical lenses are pre-committed; each carries pre-specified hypotheses and acceptance thresholds.

- **Lens 1 — categorical-association (preserves v1.0 structure).** Cell-level χ² and Cramér's V on status × case-family and status × AI capability; cell-level Monte-Carlo permutation; case-cluster bootstrap on V; clustering-aware case-level Monte-Carlo. Pre-committed primary confirmatory test: per-role paired sign test on V_family vs. V_capability, with a two-sided binomial p-value.
- **Lens 2 — latent-class derivation.** Latent class analysis on the six-status responses across roles within case. Pre-specified model selection: BIC + bootstrap likelihood ratio. Tests whether the borrowed taxonomy's class structure holds against the data.
- **Lens 3 — configurational (QCA).** Fuzzy-set QCA (Ragin, 2008; Fiss, 2011) on the focal sufficient-condition claim: (ground-truth-rich ∨ clean-post-hoc-auditability) → has-shrinking. Consistency threshold pre-committed at ≥ 0.80; coverage threshold pre-committed at ≥ 0.50.

### 11.6 Convergence criterion

The v1.1 H3 verdict is supported only if all three lenses converge on the same direction (V_family > V_capability) at their pre-committed thresholds. Partial convergence (1 or 2 of 3 lenses) is reported as a partial-support verdict with the divergent lens(es) named explicitly. No single lens overrides the others.

### 11.7 Drop-dead date and release schedule

The v1.1 main coding pass completes by 2027-12-31. The v1.1 results, codebook, panel-feedback annex, and disagreement log are released within 90 days of pass completion under a v1.1.0-OSF release tag. Any deviation from this preregistration is logged as a deviation note in the released package; substantive deviations trigger a re-registration with explicit comparison to this v1.1 preregistration.

---

**To post on OSF:**
1. Create a new OSF registration (https://osf.io/registries)
2. Select the "OSF Preregistration" template
3. Paste or upload this document
4. Confirm the timestamp and copy the URL + ISO-formatted timestamp
5. Paste the URL and timestamp into the manuscript's *Transparency and Disclosures* section, replacing the current placeholder language
6. Record the URL and timestamp in `10_manuscript_versions/review_loop/convergence_report.md` under the "Author-owned commitments" list
