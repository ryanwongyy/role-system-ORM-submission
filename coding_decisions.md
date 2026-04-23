# Coding Decisions

1. The workbook repository is treated as an internal curation source for provenance, especially for case descriptions, leverage notes, falsification criteria, and confounds.
2. External source collection prioritizes the workbook primary URL, then the workbook secondary URL. Additional supporting sources are not added unless already supplied in the workbook companion sheets.
3. When a full text cannot be fetched legally, the landing page snapshot is preserved and the access limit is logged as paywalled or inaccessible.
4. Role coding is initialized from the workbook's candidate-role field plus case-family heuristics. Low-confidence rows are explicitly flagged where direct source confirmation is limited.
5. Analysis-ready status is conservative: `yes` requires at least one usable external source plus completed case files; `partial` indicates a working case folder with explicit evidence limits; `no` is reserved for missing or unusable external source capture.
6. When an original workbook URL remains challenge-blocked or paywalled but a lawful repository copy or preprint is available, the case may still be marked analysis-ready while the original access limit remains logged.
