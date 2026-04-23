# From Repository to Role System — Replication Archive

**Paper:** *From Repository to Role System: A Comparative Typology Audit of 36 Cases*
**Target venue:** *Organizational Research Methods*
**Release tag:** `v1.0.0-ORM-submission`
**License:** CC-BY-4.0 for data; MIT for code

## What's in this repository

| Folder / file | Contents | License |
|---|---|---|
| `01_registry/cases_master.csv` | 36-case registry: IDs, titles, family, capability, DOI/URL pointers | CC-BY-4.0 |
| `02_cases/` | Per-case metadata, role codings, paraphrased evidence extracts, and QA notes | CC-BY-4.0 |
| `06_analysis_tables/role_coding_master.csv` | First-coder role-status coding (612 rows = 17 roles × 36 cases) | CC-BY-4.0 |
| `06_analysis_tables/role_coding_secondcoder_subsample.csv` | Independent-second-coder reliability subsample (68 cells) | CC-BY-4.0 |
| `07_codebook/` | Rubric, codebook version history, tie-breaker documentation | CC-BY-4.0 |
| `09_scripts/section6_analysis.py` | Self-contained script reproducing every §6 manuscript statistic | MIT |
| `09_scripts/requirements.txt` | Pinned Python dependencies | MIT |
| `11_manuscript/10_drafts/10_manuscript.md` + `.docx` | Submission manuscript | CC-BY-4.0 |
| `11_manuscript/10_drafts/appendix_B_kappa.md` | Inter-coder agreement full report | CC-BY-4.0 |
| `11_manuscript/10_drafts/appendix_C_application_protocol.md` | Stranger-coder protocol + worked out-of-sample example | CC-BY-4.0 |
| `11_manuscript/10_drafts/appendix_D_sensitivity_full_role_table.md` | Full 17-role sensitivity stub | CC-BY-4.0 |
| `11_manuscript/30_reviews/OSF_preregistration.md` | OSF preregistration document (also posted on OSF) | CC-BY-4.0 |

## What is NOT in this repository (and why)

- **Primary-source PDFs and extracted text** (`03_raw_sources/`, `04_extracted_text/`). Each of the 36 cases references a published paper, preprint, or system release with its own distribution rules. We do not redistribute those texts. `01_registry/cases_master.csv` provides DOIs and URLs for reader retrieval from original rightsholders.
- **Template PDFs** used as editorial-design references during manuscript development (`11_manuscript/30_reviews/template_pdfs/`). These are published ORM / SMJ / JoM / AMPPS papers, cited by DOI in the manuscript, not redistributable here.
- **Private researcher case notes** (`05_case_notes/`). Unstructured working notes not needed for reproducibility.
- **Scratch outputs and logs** (`10_outputs/`, `08_logs/`).
- **Intermediate manuscript versions** from the editorial and review loops — only the convergence reports and the final submission version are released.

## Reproducing the §6 statistics

```bash
cd p1_role_systems_db
pip install -r 09_scripts/requirements.txt
python3 09_scripts/section6_analysis.py --output analysis_output.json
```

Expected runtime: ≤ 60 s. Reproduces every numeric value reported in the manuscript's §6 (cell-level and case-level Monte-Carlo permutation p-values, Cramér's V point estimates, case-cluster bootstrap 95% CIs, per-role paired sign test and Wilcoxon, high-confidence-only robustness, pilot hold-out, case-configuration on H1 durable roles, QCA-style consistency/coverage for the H2 ground-truth claim).

Seeds are fixed in the script docstring. Running against `role_coding_master.csv` at this release tag reproduces the manuscript numbers to within rounding.

## Inter-coder reliability — summary

Pooled Cohen's κ = 0.289 on the preregistered 68-cell subsample (95% bootstrap CI [0.147, 0.439]), from a sandboxed LLM-agent second coder. This **fails** the preregistered κ ≥ 0.60 threshold. The preregistered remedy has been invoked: Table 1's tie-breaker is revised, the observable-vs-`not_applicable` threshold is tightened, and the claim ceiling is adjusted from *framework* to *preliminary framework*. A human second-coder pass is recommended as a follow-up. See `11_manuscript/10_drafts/appendix_B_kappa.md` for the full disagreement log and remedy details.

## OSF preregistration

The second-coder protocol is preregistered on OSF. See `11_manuscript/30_reviews/OSF_preregistration.md` for the registered document; the live OSF URL and ISO timestamp are inserted in the manuscript's Transparency and Disclosures section at final submission.

## Citation

If you use this database, please cite:

> [Author]. (2026). From Repository to Role System: A Comparative Typology Audit of 36 Cases. *Organizational Research Methods* [under review]. Database: [Zenodo DOI to be minted on acceptance].

## Provenance notes (from original database construction)

- Repository workbook rows are preserved exactly in the seed export and propagated into metadata.
- External source collection followed the workbook primary and secondary URLs first.
- Missingness is recorded explicitly rather than silently filled.
- Live-project and autonomy-heavy cases are coded as boundary-pressure evidence unless full, stable methodology is available.
- Generated: 2026-04-07; reliability subsample added 2026-04-23.

## Contact

For questions, corrections, or an independent human second-coder pass contribution, see the contact information in the submitted manuscript.
