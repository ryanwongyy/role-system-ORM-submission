# Browser-Assisted Download Queue

Use a normal Chrome session. When a page requires login, complete it in the browser and use the site's normal `PDF`, `Download`, or export control. The watcher script will capture new PDFs from `~/Downloads`.

## Batch 2A — Highest-Leverage Paywalled Articles

| ID | URL | Save target |
|---|---|---|
| C1 | https://doi.org/10.5465/amr.1994.9410210748 | `C1_doty_glick_1994_typologies_theory_building.pdf` |

## Batch 2B — Secondary Journal Targets

| ID | URL | Save target |
|---|---|---|
| H1 | https://doi.org/10.1177/001316446002000104 | `H1_cohen_1960_agreement_nominal_scales.pdf` |
| I3 | https://doi.org/10.1177/1065912912468269 | `I3_fiss_sharapov_cronqvist_2013_large_n_qca_econometric.pdf` |
| K4 | https://citeseerx.ist.psu.edu/document?doi=f7637823a9588424cf138088419dc8aee412db99&repid=rep1&type=pdf | `K4_short_2009_art_writing_review_article.pdf` |
| O6 | https://doi.org/10.1002/smj.2338 | `O6_bergh_etal_2016_mase_strategic_management.pdf` |

## Book / Chapter / Preview Cases

Keep these separate from journal retrieval and treat them as preview-only, licensed-export, or metadata-only items unless a lawful full-text export is available.

| ID | URL | Save target |
|---|---|---|
| C4 | https://us.sagepub.com/en-us/nam/book/typologies-and-taxonomies | `C4_bailey_1994_typologies_and_taxonomies.pdf` |
| D3 | https://www.perlego.com/book/1440220/in-an-age-of-experts-the-changing-roles-of-professionals-in-politics-and-public-life-pdf | `D3_brint_1994_age_of_experts.pdf` |
| D4 | https://www.routledge.com/Professionalism-Boundaries-and-the-Workplace/Malin/p/book/9780415192637 | `D4_fournier_2000_boundary_work_unmaking_professions.pdf` |
| D5 | https://global.oup.com/academic/product/the-future-of-the-professions-9780198713951 | `D5_susskind_susskind_2015_future_professions.pdf` |

## Notes

- `K1` is already stored from the parallel open PLOS version; no browser action needed unless the BMJ version is specifically desired.
- `O2` has now been recovered from the browser-assisted pass.
- Recovered in the latest browser-assisted, bibliography-alignment, article-first shell, and browser-ingest passes: `C3`, `D6`, `E1`, `E4`, `F1`-`F6`, `G3`, `G5`, `H3`, `H5`, `H6`, `I4`, `I5`, `J2`, `J3`, `J5`, `K2`, `K3`, `K5`, `L3`, `L4`, `L5`, `N2`, `N3`, `N4`, `N5`, `O2`.
- Still outstanding from the highest-leverage wave: `C1`.
- If the browser downloads a generic filename such as `download.pdf`, leave it alone; the watcher can still map it from PDF text when the title is extractable.
