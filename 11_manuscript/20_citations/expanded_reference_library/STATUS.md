# Expanded Reference Library — Status

**Date:** 2026-04-26
**Scope:** `manifest.md` continuation pass, browser follow-up, and active-library integrity cleanup.

## Snapshot

- `manifest.md` candidate references: **84**
- Active full-text coverage of manifest refs: **65 / 84**
- Active full-text PDF files in `pdfs/`: **70**
- Lawful preview coverage of manifest refs: **2 / 84**
- Lawful preview PDFs in `previews/`: **2**
- Quarantined misfiled/suspect PDFs in `quarantine/`: **8**
- Manifest refs still lacking any local full text or preview: **17**

Why `70` PDF files but only `65` manifest refs covered:
- `J4b` is an alternate repository copy of `J4`
- `M6`-`M9` are useful supporting PDFs stored locally but **not part of the current manifest**

## 2026-04-25 Continuation Pass

### Integrity cleanup completed

Moved known misfiled files out of active use and into `quarantine/`:

- `A8`
- `A9`
- `A11`
- `A12`
- `A13`
- `A14`
- `A15`
- `K6`

### New full-text recoveries added in this pass

- `F2` — Cronbach & Meehl (1955), stored from the University of Minnesota reprint of the same paper
- `G4` — Stemler (2001/2000), open journal PDF
- `H2` — Krippendorff (2011), public mirror of the UPenn ScholarlyCommons postprint
- `K1` — Page et al. (2021), stored from the parallel open PLOS Medicine version of the PRISMA 2020 statement
- `L1` — Lazer et al. (2009), Human Nature Lab-hosted PDF
- `N1` — Autor (2015), MIT-hosted PDF
- `O1` — Nosek et al. (2015), BITSS-hosted PDF
- `O3` — Gelman & Loken (2014), rendered to PDF from the openly accessible American Scientist HTML article
- `O4` — Open Science Collaboration (2015), accepted manuscript from an institutional repository

### Browser-authenticated and follow-up recoveries added in this pass

- `C3` — Delbridge & Fiss (2013)
- `E1` — Biddle (1986)
- `E4` — Merton (1957)
- `F1` — Messick (1995)
- `G5` — Duriau, Reger, & Pfarrer (2007)
- `K2` — Tranfield, Denyer, & Smart (2003)
- `L4` — Edelmann, Wolff, Montagne, & Bail (2020)
- `L5` — Lazer et al. (2020)
- `N3` — Brynjolfsson & Mitchell (2017)
- `N5` — Raisch & Krakowski (2021)
- `O2` — Nosek, Ebersole, DeHaven, & Mellor (2018)

### Additional article-first recoveries added in this pass

- `D6` — Anteby, Chan, & DiBenigno (2016), author-hosted PDF
- `F3` — Borsboom, Mellenbergh, & van Heerden (2004), author-hosted PDF
- `H3` — Hayes & Krippendorff (2007), author-hosted PDF
- `H6` — Landis & Koch (1977), course-repository/JSTOR scan mirror
- `J2` — Eisenhardt (1989), open JSTOR scan mirror
- `J3` — Eisenhardt (2021), institutional mirror PDF
- `N2` — Frey & Osborne (2017), open working-paper PDF matching the article title
- `N4` — Acemoglu & Restrepo (2020), author-hosted PDF with matching title

### Additional browser-authenticated article recoveries added in this pass

- `F4` — Edwards (2011), browser-downloaded PDF
- `F5` — Bagozzi, Yi, & Phillips (1991), browser-downloaded PDF
- `F6` — Diamantopoulos, Riefler, & Roth (2008), browser-downloaded PDF
- `G3` — Hruschka et al. (2004), browser-downloaded PDF
- `H5` — Lombard, Snyder-Duch, & Bracken (2002), browser-downloaded PDF
- `I4` — Kraus, Ribeiro-Soriano, & Schüssler (2018), browser-downloaded PDF
- `I5` — Greckhamer, Furnari, Fiss, & Aguilera (2018), browser-downloaded PDF
- `J5` — Langley (1999), browser-downloaded PDF
- `K3` — Rousseau, Manning, & Denyer (2008), browser-downloaded working-paper PDF
- `K5` — Siddaway, Wood, & Hedges (2019), browser-downloaded Annual Review PDF
- `L3` — Wallach (2018), browser-downloaded CACM PDF

Detailed route notes are in [`manifest_continuation_attempts.md`](manifest_continuation_attempts.md).

## Active Manifest Coverage

### Full text recovered

- `A1`-`A7`
- `B1`-`B7`
- `C2`, `C3`, `C5`, `C6`
- `D1`, `D2`, `D6`
- `E1`, `E4`
- `F1`-`F6`
- `G3`, `G4`, `G5`
- `H2`, `H3`, `H5`, `H6`
- `I4`, `I5`
- `J2`, `J3`, `J4`, `J5`
- `K1`, `K2`, `K3`, `K5`
- `L1`, `L3`, `L4`, `L5`
- `M1`-`M5`
- `N1`, `N2`, `N3`, `N4`, `N5`
- `O1`, `O2`, `O3`, `O4`, `O5`

### Preview only

- `D4`
- `D5`

### Still missing from the manifest set

- `C1`, `C4`
- `D3`
- `E2`, `E3`, `E5`
- `G1`, `G2`
- `H1`, `H4`
- `I1`, `I2`, `I3`
- `J1`
- `K4`
- `L2`
- `O6`

## Non-Manifest Supporting PDFs Kept Active

These remain in `pdfs/` because they are useful for the broader AI/LLM framing, but they are **not** counted toward manifest coverage:

- `J4b`
- `M6`
- `M7`
- `M8`
- `M9`

## Storage Rules

- `pdfs/` = validated, correctly matched full texts only
- `previews/` = lawful preview-only PDFs
- `quarantine/` = misfiled or suspect items removed from active use
- HTML, login pages, and challenge pages are not stored as `.pdf`

## Next Pass

1. Browser-assisted paywalled retrieval using the expanded queue in [`browser_assisted_download_queue.md`](browser_assisted_download_queue.md)
2. Watcher-assisted ingest using [`watch_browser_pdfs.py`](watch_browser_pdfs.py)
3. Book/chapter cleanup for lawful previews and metadata-only cases
