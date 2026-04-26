# First 20 Previously Undownloaded References — Attempt Log

**Date:** 2026-04-23  
**Target folders:** [`pdfs/`](pdfs/) for full-text PDFs; [`previews/`](previews/) for lawful publisher previews

This pass retried the first 20 undownloaded references from `links_for_first_20_undownloaded.md`, prioritizing publisher/DOI routes first, then author or institutional open-access mirrors. Only files that validated with a `%PDF-` header were stored. Full-text OA PDFs went to `pdfs/`; lawful preview-only files went to `previews/`.

## Result Summary

**Full-text PDFs downloaded:** 14 / 20  
**Preview-only PDFs stored:** 2 / 20  
**Still not recovered as full text:** 4 / 20

| ID | Reference | Outcome | Local file / note | Successful route or main blocker |
|---|---|---|---|---|
| A1 | Bail 2024, PNAS | Downloaded | `pdfs/A1_bail_2024_generative_ai_social_science.pdf` | PMC PDF at `https://pmc.ncbi.nlm.nih.gov/articles/PMC11127003/pdf/pnas.202314021.pdf`. The supplied PMC ID `PMC11126981` resolves to a different article; `PMC11127003` is the correct PMC record for Bail 2024. |
| A5 | Dillion et al. 2023, TiCS | Downloaded | `pdfs/A5_dillion_tandon_gu_gray_2023_ai_language_models_human_participants.pdf` | Browser-authenticated ScienceDirect PDF: `1-s2.0-S1364661323000980-main.pdf`, confirming the corrected PII `S1364661323000980`. |
| B1 | Aguinis et al. 2018, AOM Annals | Downloaded | `pdfs/B1_aguinis_ramani_alabduljader_2018_methodological_transparency.pdf` | Current Aguinis author PDF: `https://www.hermanaguinis.com/pdf/AOMAtransparency.pdf`. |
| B2 | Aguinis et al. 2011, JoM | Downloaded | `pdfs/B2_aguinis_boyd_pierce_short_2011_micro_macro.pdf` | Current Aguinis author PDF: `https://hermanaguinis.com/pdf/JOMmicromacro.pdf`. |
| B3 | Bergh et al. 2017, Strategic Organization | Downloaded | `pdfs/B3_bergh_sharp_aguinis_li_2017_credibility_crisis.pdf` | Current Aguinis author PDF: `https://www.hermanaguinis.com/pdf/SOcredibility.pdf`. |
| B4 | Aguinis et al. 2009, ORM | Downloaded | `pdfs/B4_aguinis_pierce_bosco_muslin_2009_orm_first_decade.pdf` | Current Aguinis author PDF: `https://www.hermanaguinis.com/pdf/ORMfirstdecade.pdf`. |
| B5 | Edwards 2001, ORM | Downloaded | `pdfs/B5_edwards_2001_multidimensional_constructs.pdf` | Current Edwards author PDF: `https://tarheels.live/jeffreyedwardswebsite/wp-content/uploads/sites/5503/2024/03/Edwards2001a.pdf`. |
| B6 | Short et al. 2010, ORM | Downloaded | `pdfs/B6_short_broberg_cogliser_brigham_2010_cata.pdf` | Browser-authenticated PDF download from the ResearchGate record. |
| B7 | Bluhm et al. 2011, JMS | Downloaded | `pdfs/B7_bluhm_harman_lee_mitchell_2011_qualitative_management.pdf` | Browser-authenticated Wiley PDF: `J Management Studies - 2011 - Bluhm - Qualitative Research in Management  A Decade of Progress.pdf`. |
| C1 | Doty & Glick 1994, AMR | Not downloaded | AOM/JSTOR/ProQuest access controlled | AOM and JSTOR PDF routes returned access-control HTML; ProQuest PDF route hit redirect/access loops. |
| C2 | Fiss 2011, AMJ | Downloaded | `pdfs/C2_fiss_2011_building_better_causal_theories.pdf` | USC author/faculty file: `https://msbfile03.usc.edu/digitalmeasures/fiss/intellcont/Fiss%20AMJ%202011-1.pdf`. |
| C3 | Delbridge & Fiss 2013, AMR | Not downloaded | AOM upload stale / access controlled | AOM uploaded-file URL returned 404; AOM DOI/PDF route returned access-control HTML; ResearchGate returned `error code: 1020`. |
| C4 | Bailey 1994 book | Not downloaded | Commercial monograph | No lawful full-text PDF route found; library/purchase route remains appropriate. |
| C5 | Cornelissen 2017, AMR | Downloaded | `pdfs/C5_cornelissen_2017_developing_propositions_process_model_typology.pdf` | Erasmus repository PDF: `https://pure.eur.nl/ws/files/47698929/REPUB_108698.pdf`. |
| C6 | Kraatz & Block 2008 handbook chapter | Downloaded | `pdfs/C6_kraatz_block_2008_institutional_pluralism.pdf` | Author-hosted PDF: `https://www.profemilyblock.com/uploads/3/2/0/2/32024349/kraatz_and_block_-_institutional_pluralism.pdf`. |
| D1 | Abbott 2005, Sociological Theory | Downloaded | `pdfs/D1_abbott_2005_linked_ecologies.pdf` | The supplied UChicago author URL returned 404; a university mirror worked: `https://pics.unison.mx/wp-content/uploads/2012/03/Abbott_2005.pdf`. |
| D2 | Eyal 2013, AJS | Downloaded | `pdfs/D2_eyal_2013_sociology_of_expertise_autism.pdf` | Columbia Academic Commons asset download: `https://academiccommons.columbia.edu/doi/10.7916/D81J9NHV/download`, discovered from the `D8H70F1X` landing record. |
| D3 | Brint 1994 book | Not downloaded | Commercial monograph | No lawful full-text PDF route found; library/purchase route remains appropriate. |
| D4 | Fournier 2000 chapter | Preview stored | `previews/D4_fournier_2000_boundary_work_unmaking_professions_preview.pdf` | Lawful Routledge/PagePlace preview PDF recovered from `https://api.pageplace.de/preview/DT0400.9781134651603_A23780673/preview-9781134651603_A23780673.pdf`. This is a 29-page publisher preview, not the full chapter. |
| D5 | Susskind & Susskind 2015 book | Preview stored | `previews/D5_susskind_susskind_2015_future_professions_preview.pdf` | Lawful OUP/PagePlace preview PDF recovered from `https://api.pageplace.de/preview/DT0400.9780191022401_A25657212/preview-9780191022401_A25657212.pdf`. This is a 37-page publisher preview, not the full book. |

## Notes For Later Citation Work

- Treat D1 as an OA mirror rather than the author homepage copy; if exact pagination matters, verify against the Wiley/Sociological Theory version.
- A1's supplied PMC fallback was misidentified in the handoff. The downloaded file is from the correct PMC record for the PNAS article.
- A5 may still be obtainable interactively from ScienceDirect through institutional access, but the supplied PsyArXiv/OSF route now behaves like a stale or access-gated record rather than a straightforward OA download.
- D4 and D5 now have lawful preview PDFs stored under `previews/`; those are useful for contents, front matter, and limited quotation checking, but they are not substitutes for the full Routledge/OUP texts.
- The browser session also downloaded `Typology_as_a_Theory_Building_Tool_in_Management.pdf`, but that file is a different 2020 article by Arabi and Rahimi rather than Delbridge & Fiss (2013), so it was not ingested as `C3`.
- The ResearchGate-only items may be accessible to the author through a browser session, but they were not stored because the command-line responses were not PDFs.
