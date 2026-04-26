# Manifest Continuation Attempts

**Date:** 2026-04-26
**Scope:** post-first-20 continuation pass for `manifest.md`

## Library Integrity Cleanup

| ID | Result | Action | Notes |
|---|---|---|---|
| A8 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |
| A9 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |
| A11 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |
| A12 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |
| A13 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |
| A14 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |
| A15 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |
| K6 | quarantined | moved to `quarantine/` | known misfiled PDF; excluded from active use |

## Phase 1 — Narrative-Critical OA Sweep

| ID | Result | Local file | Source route | Notes |
|---|---|---|---|---|
| F2 | stored full text | `F2_cronbach_meehl_1955_construct_validity_psychological_tests.pdf` | University of Minnesota Conservancy | 1956 reprint of the 1955 paper; first page explicitly says reprinted with permission |
| G4 | stored full text | `G4_stemler_2001_overview_content_analysis.pdf` | UMass open journal PDF | Article page labels the piece as 2000; manifest kept as 2001-style slot for continuity |
| H2 | stored full text | `H2_krippendorff_2011_computing_alpha_reliability.pdf` | public mirror of UPenn ScholarlyCommons postprint | official UPenn bitstream intermittently served dynamic HTML to shell requests; mirrored PDF clearly identifies the UPenn postprint source |
| K1 | stored full text | `K1_page_2021_prisma_2020_statement.pdf` | PLOS Medicine parallel OA version | BMJ PDF route was Cloudflare-blocked from shell; stored parallel open version of the same PRISMA 2020 statement |
| L1 | stored full text | `L1_lazer_2009_computational_social_science.pdf` | Human Nature Lab-hosted PDF | JSTOR-formatted scan hosted on a lab site |
| N1 | stored full text | `N1_autor_2015_why_are_there_still_so_many_jobs.pdf` | MIT-hosted PDF | clean author/institutional copy |
| O1 | stored full text | `O1_nosek_2015_promoting_open_research_culture.pdf` | BITSS-hosted PDF | validated as the correct Science article |
| O3 | stored full text | `O3_gelman_loken_2014_statistical_crisis_science.pdf` | rendered from open American Scientist HTML article | stored as a PDF capture of the openly accessible full-text web article because no clean publisher PDF route surfaced |
| O4 | stored full text | `O4_open_science_collaboration_2015_reproducibility_psychological_science.pdf` | University of Alabama / LSE accepted manuscript route | validated accepted manuscript with matching title and DOI |
| O2 | blocked | — | official OA routes tested: PMC, university mirror | official routes were Cloudflare/reCAPTCHA-blocked from shell; a public mirror exists but was not stored pending a cleaner route |
| L2 | metadata only | — | `bitbybitbook.com` | author site is available, but no clean full-book PDF surfaced in shell probing |

## Phase 2 — Browser-Assisted Targets

Queue expanded in [`browser_assisted_download_queue.md`](browser_assisted_download_queue.md).

Watcher expanded in [`watch_browser_pdfs.py`](watch_browser_pdfs.py).

Results from the first priority browser wave and bibliography-alignment follow-up:

- `C3` — stored full text
- `E1` — stored full text
- `E4` — stored full text
- `F1` — stored full text
- `G5` — stored full text
- `K2` — stored full text
- `L4` — stored full text
- `L5` — stored full text
- `N3` — stored full text
- `N5` — stored full text
- `O2` — stored full text

Still priority browser targets:

- `C1`

Additional route notes:

- `E1` — stored full text from a Web Archive capture of a faculty-posted PDF (`RoleTheory-Biddle-1986.pdf`); first-page text matches Biddle (1986).
- `F1` — stored full text from a public mirror PDF; first-page text matches Messick (1995), *American Psychologist*, 50(9), 741-749.
- `D6` — initially stalled from shell probing via Harvard Scholar discovery routes, but later recovered from the author-hosted PDF on Michel Anteby's site.

## Article-First Follow-Up Sweep

| ID | Result | Local file | Source route | Notes |
|---|---|---|---|---|
| D6 | stored full text | `D6_anteby_chan_dibenigno_2016_occupations_professions_organizations.pdf` | Michel Anteby author site | first-page text matches the Annals review article |
| F3 | stored full text | `F3_borsboom_mellenbergh_van_heerden_2004_concept_validity.pdf` | Denny Borsboom author site | clean publisher-formatted PDF hosted on the author site |
| H3 | stored full text | `H3_hayes_krippendorff_2007_standard_reliability_measure.pdf` | Andrew Hayes public PDF page | first-page citation line explicitly matches the target article |
| H6 | stored full text | `H6_landis_koch_1977_observer_agreement_categorical_data.pdf` | public course-repository mirror | JSTOR-style scan; first-page text matches the Biometrics article |
| I4 | blocked | — | ResearchGate direct PDF route and repository mirror | ResearchGate served 403; alternate repository PDF resolved to a different article |
| I5 | blocked | — | UPV repository mirror | downloaded PDF was a different QCA paper, so it was rejected |
| J2 | stored full text | `J2_eisenhardt_1989_building_theories_case_study_research.pdf` | QualQuant open JSTOR scan mirror | first-page text matches the AMR article |
| J3 | stored full text | `J3_eisenhardt_2021_eisenhardt_method_really.pdf` | Mackenzie institutional mirror | author-accepted/hosted PDF with matching DOI and title |
| K4 | blocked | — | CiteseerX direct PDF route | shell retrieval stalled or failed SSL verification; no validated file stored |
| K5 | blocked | — | Annual Reviews PDF routes | shell and headless-browser attempts were Cloudflare-blocked |
| L3 | blocked | — | CACM public article page | curl and headless Chrome both produced Cloudflare block pages rather than article text |
| N2 | stored full text | `N2_frey_osborne_2017_future_employment_computerisation.pdf` | UCL Gatsby mirror | working-paper PDF with matching title used as the local full-text version |
| N4 | stored full text | `N4_acemoglu_restrepo_2020_robots_jobs_us_labor_markets.pdf` | MIT economics author-hosted PDF | first-page text matches the article title; local copy is a preprint/author version |

## Browser-Ingest Follow-Up Sweep

| ID | Result | Local file | Source route | Notes |
|---|---|---|---|---|
| F4 | stored full text | `F4_edwards_2011_formative_measurement_fallacy.pdf` | browser-downloaded PDF | first-page text matches the ORM article title |
| F5 | stored full text | `F5_bagozzi_yi_phillips_1991_construct_validity_organizational_research.pdf` | browser-downloaded PDF | ProQuest-formatted full text matching the ASQ article |
| F6 | stored full text | `F6_diamantopoulos_riefler_roth_2008_formative_measurement_models.pdf` | browser-downloaded PDF | Elsevier PDF with matching title and authors |
| G3 | stored full text | `G3_hruschka_etal_2004_reliability_coding_open_ended_data.pdf` | browser-downloaded PDF | first-page text matches the Field Methods article |
| H5 | stored full text | `H5_lombard_snyder_duch_bracken_2002_intercoder_reliability.pdf` | browser-downloaded institutional repository copy | first-page text matches the Human Communication Research article |
| I3 | blocked | — | browser-downloaded PDF | downloaded file was a different PRQ mini-symposium article (`QCA 25 years after The Comparative Method`), so it was rejected |
| I4 | stored full text | `I4_kraus_ribeiro_soriano_schussler_2018_fsQCA_entrepreneurship_innovation.pdf` | browser-downloaded PDF | first-page text matches the fsQCA entrepreneurship and innovation review |
| I5 | stored full text | `I5_greckhamer_furnari_fiss_aguilera_2018_qca_best_practices.pdf` | browser-downloaded PDF | first-page text matches the Strategic Organization best-practices article |
| J5 | stored full text | `J5_langley_1999_theorizing_process_data.pdf` | browser-downloaded PDF | ProQuest-formatted full text matching the AMR article |
| K3 | stored full text | `K3_rousseau_manning_denyer_2008_evidence_management_organizational_science.pdf` | browser-downloaded SSRN/AIM working-paper PDF | local full-text copy matches the evidence-synthesis article family, though the working-paper title carries an extended subtitle |
| K5 | stored full text | `K5_siddaway_wood_hedges_2019_how_to_do_systematic_review.pdf` | browser-downloaded Annual Reviews PDF | browser-authenticated PDF succeeded after shell and headless attempts were blocked |
| L3 | stored full text | `L3_wallach_2018_css_not_cs_plus_social_data.pdf` | browser-downloaded CACM PDF | first-page text matches the Wallach CACM viewpoint article |
| C1 | blocked | — | browser pass not yet recovered | still outstanding from the high-leverage wave |
| H1 | blocked | — | browser pass not yet recovered | no validated local PDF landed in this round |
| K4 | blocked | — | browser pass not yet recovered | no validated local PDF landed in this round |
| O6 | blocked | — | browser pass not yet recovered | no validated local PDF landed in this round |

## Phase 3 — Books / Chapters / Preview Cleanup

Already present as lawful previews:

- `D4_fournier_2000_boundary_work_unmaking_professions_preview.pdf`
- `D5_susskind_susskind_2015_future_professions_preview.pdf`

Still to assess for preview-only or metadata-only handling:

- `C4`, `D3`
- `E2`, `E3`, `E5`
- `G1`, `G2`
- `H4`
- `I1`, `I2`
- `J1`
