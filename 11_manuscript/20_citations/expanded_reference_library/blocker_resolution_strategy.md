# Blocker Resolution Strategy For Remaining First-20 References

**Date:** 2026-04-23  
**Scope:** Remaining blockers from `first20_download_attempts.md` after the first-20 recovery pass.  
**Principle:** Use lawful access only: institutional login, author-deposited copies, publisher access, library e-book access, interlibrary loan, or author requests. Avoid pirate mirrors and DRM/paywall circumvention.

## Executive Plan

1. **Use an interactive browser with the author's credentials/session.** This already succeeded for A5, B6, and B7; it remains the highest-yield next step for AOM, JSTOR, ProQuest, and e-book platforms because the failed command-line attempts were mostly bot checks, app-shell redirects, or login gates rather than true absence.
2. **Authenticate once through the university/library proxy.** Start from the library discovery tool or DOI resolver after logging in, then save PDFs into `pdfs/` using the established file names below.
3. **Use Zotero Connector or browser "Save PDF" where downloads are rendered in-page.** Some publishers serve PDFs through a viewer, not a stable direct PDF URL.
4. **For books and chapters, prefer licensed e-book/library access or chapter scans.** If full-book PDF export is not licensed, save the chapter or page-range PDF permitted by the platform, or request a chapter scan/interlibrary loan.
5. **If browser access still fails, use author-request routes.** ResearchGate "Request full-text", author email, or institutional repository request forms are appropriate for B6, B7, C1, C3, and D4.

## Screen-Control Session Checklist

If screen/browser control is granted:

1. Open the project folder and keep this target folder ready:
   `11_manuscript/20_citations/expanded_reference_library/pdfs/`
2. Open a normal browser profile, not a headless scraper.
3. The user logs into institutional/library SSO, OSF, ResearchGate, or Perlego/VitalSource when prompted. Do not share passwords in chat.
4. For each download, save with the exact filename listed below.
5. After each save, run a local validation pass:
   `head -c 5 <file>` should return `%PDF-`.
6. Update `first20_download_attempts.md` and `STATUS.md` after successful recoveries.

## Reference-by-Reference Strategies

| ID | Remaining blocker | Highest-yield strategy | Target filename |
|---|---|---|---|
| A5 | Recovered. | Downloaded through a browser-authenticated ScienceDirect session as `1-s2.0-S1364661323000980-main.pdf`. The PsyArXiv/OSF route still appears stale, but the full text is now stored locally. | `A5_dillion_tandon_gu_gray_2023_ai_language_models_human_participants.pdf` |
| B6 | Recovered. | Downloaded through the browser from the ResearchGate full-text page after command-line access had failed. | `B6_short_broberg_cogliser_brigham_2010_cata.pdf` |
| B7 | Recovered. | Downloaded through a browser-authenticated Wiley session. | `B7_bluhm_harman_lee_mitchell_2011_qualitative_management.pdf` |
| C1 | AOM/JSTOR/ProQuest access controlled. | Use institutional AOM access via DOI `10.5465/amr.1994.9410210748`; if AOM fails, use JSTOR stable page `https://www.jstor.org/stable/258704` through library proxy. ProQuest is third choice because command-line probing hit redirect loops. | `C1_doty_glick_1994_typologies_theory_building.pdf` |
| C3 | AOM uploaded-file URL is stale; AOM DOI and ResearchGate are access-controlled. | Use institutional AOM access via DOI `10.5465/amr.2013.0085`. If not entitled, use ResearchGate in browser or contact Peer Fiss / Robert Delbridge for accepted manuscript. | `C3_delbridge_fiss_2013_styles_of_theorizing.pdf` |
| C4 | Commercial Sage Little Green Book. | Use library access to SAGE Research Methods or Sage e-book platform. If no PDF export is available, save the citation, table of contents, and permitted chapter/page-range export. | `C4_bailey_1994_typologies_and_taxonomies.pdf` |
| D3 | Commercial Princeton monograph; Perlego preview/subscription visible. | Prefer Princeton University Press/library e-book access. Perlego can work if the user has a subscription, but it may not permit archival PDF export; if export is restricted, save notes/citation only and request library e-book or scan. | `D3_brint_1994_age_of_experts.pdf` |
| D4 | Routledge edited-volume chapter; no OA chapter found. | A lawful 29-page Routledge/PagePlace preview is already stored at `previews/D4_fournier_2000_boundary_work_unmaking_professions_preview.pdf`. For full text, use Taylor & Francis eBooks through institutional access and export chapter 4/page range 67-86 if licensed. If no entitlement, request a chapter scan via library/interlibrary loan. | `D4_fournier_2000_boundary_work_unmaking_professions.pdf` |
| D5 | Commercial OUP monograph; no lawful full book PDF found. | A lawful 37-page OUP/PagePlace preview is already stored at `previews/D5_susskind_susskind_2015_future_professions_preview.pdf`. For full text, use OUP/library e-book access. A direct APS PDF route looked promising but is currently Cloudflare-challenged from shell/browser automation, so treat it as a secondary manual browser check rather than a dependable download route. | `D5_susskind_susskind_2015_future_professions.pdf` |

## Triage Order

1. **A5, B6, C3** — most likely to succeed with browser login and simple download.
2. **B7, C1** — likely institutional-access wins.
3. **D4** — likely chapter export/ILL rather than OA.
4. **C4, D3, D5** — book-platform or library workflows; decide whether full text is necessary or whether an authorized preview/supplementary article is enough.

## Legal Substitutes If Full Text Remains Unavailable

- **D5 Susskind & Susskind:** The stored OUP/PagePlace preview can support contents/front-matter checking. If a supplemental OA article is still desired, manually test the American Philosophical Society route in a normal browser session; shell and automation requests hit Cloudflare challenge pages.
- **D4 Fournier:** If the chapter cannot be retrieved, the boundary-work concept is summarized and applied in several OA healthcare/professions articles; these can support the general point, but the original chapter should remain in the bibliography if directly invoked.
- **C4 Bailey:** Sage's publisher page and SAGE Research Methods metadata are enough for citation metadata, but not enough for direct page-specific claims. For page-specific typology/taxonomy methods, obtain the book through library access.

## What Not To Do

- Do not use Z-Library, Scribd uploads of entire books, or random textbook-PDF sites for commercial monographs.
- Do not strip DRM or bypass a publisher paywall.
- Do not store HTML pages as `.pdf` unless the browser's print/save workflow creates a legitimate PDF of an accessible page and the file is clearly labeled as such.
