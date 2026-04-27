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

---

**To post on OSF:**
1. Create a new OSF registration (https://osf.io/registries)
2. Select the "OSF Preregistration" template
3. Paste or upload this document
4. Confirm the timestamp and copy the URL + ISO-formatted timestamp
5. Paste the URL and timestamp into the manuscript's *Transparency and Disclosures* section, replacing the current placeholder language
6. Record the URL and timestamp in `10_manuscript_versions/review_loop/convergence_report.md` under the "Author-owned commitments" list
