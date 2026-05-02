"""Corpus cleaning pass for Strategy-5 computational text analysis (v44 / Appendix G).

Input:  04_extracted_text/<slug>/*.txt — heterogeneous-quality text files
Output: 04_extracted_text_cleaned/<slug>/*.txt — boilerplate-stripped, normalized

Strategy:
- Prefer *_pdf.txt files when available (PDF-extracted, content-rich)
- Fall back to other extracted text after stripping arxiv landing-page chrome
- Drop Cloudflare-challenge files (just "Just a moment...")
- Normalize whitespace, dedupe consecutive duplicate lines, strip URL fragments

Determinism: pure regex + string ops. No model calls. No randomness.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
SRC = ROOT / "04_extracted_text"
DST = ROOT / "04_extracted_text_cleaned"

# Boilerplate patterns observed in the v43 corpus
ARXIV_CHROME_PATTERNS = [
    r"Skip to main content",
    r"Learn about arXiv becoming an independent nonprofit\.?",
    r"We gratefully acknowledge support from.*?Donate",
    r"Help \| Advanced Search",
    r"All fields\s*Title\s*Author\s*Abstract",
    r"open search\s*GO\s*open navigation menu",
    r"quick links\s*Login\s*Help Pages\s*About",
    r"Donate\b",
    r"\barxiv author ID\b",
    r"\bORCID\b\s+(?:Help pages|arXiv author ID)",
    r"\bMSC classification\b",
    r"\bACM classification\b",
    r"\[Submitted on .*?\]",
    r"\(this version, v\d+\)",
    # Page navigation
    r"Skip to (Top|content|Bibliographic Tools)",
    r"Bibliographic and Citation Tools",
    r"Code, Data and Media Associated with this Article",
    r"Demos\b.*?Replicate \(What is Replicate\?\)",
    # Cookie / privacy banners
    r"We use cookies.*?(?:Accept|Decline|OK)",
    r"By using arxiv\.org.*?Privacy",
    # Footer
    r"Contact arXiv.*?Privacy Policy",
    r"Web Accessibility Assistance",
]

# Cloudflare/captcha challenge text (case 1, 5, 35 had only "Just a moment...")
CLOUDFLARE_PATTERNS = [
    r"Just a moment\.\.\..*?Enable JavaScript",
    r"Enable JavaScript and cookies to continue",
    r"DDoS protection by Cloudflare",
]


def is_cloudflare_challenge_file(text: str) -> bool:
    """A file is dropped if it's just a Cloudflare challenge with no actual content."""
    if len(text.strip()) < 100:
        return True
    if "Just a moment" in text and len(text.strip()) < 200:
        return True
    return False


def is_pdf_extract(filename: str) -> bool:
    """PDF extracts have *_pdf.txt suffix; they're the highest-quality source."""
    return filename.endswith("_pdf.txt")


def clean_text(text: str) -> str:
    """Apply all cleaning passes."""
    for pattern in ARXIV_CHROME_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE | re.DOTALL)
    for pattern in CLOUDFLARE_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE | re.DOTALL)

    # Strip standalone URL lines (cite URLs interleaved with content)
    text = re.sub(r"^\s*https?://\S+\s*$", "", text, flags=re.MULTILINE)

    # Strip arxiv-ID standalone lines like "arXiv:2504.01167"
    text = re.sub(r"^\s*arXiv:\d{4}\.\d{5}(?:v\d+)?\s*$", "", text, flags=re.MULTILINE)

    # Normalize whitespace: multiple blank lines → one; tabs → spaces
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Dedupe consecutive duplicate lines (common in HTML extractions)
    lines = text.split("\n")
    deduped: list[str] = []
    prev = None
    for line in lines:
        s = line.strip()
        if s and s == prev:
            continue
        deduped.append(line)
        if s:
            prev = s
    text = "\n".join(deduped)

    return text.strip()


def words(text: str) -> int:
    return len(re.findall(r"\b[A-Za-z][A-Za-z'\-]*\b", text))


def main() -> None:
    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)

    summary = []
    case_dirs = sorted(d for d in SRC.iterdir() if d.is_dir())
    for case_dir in case_dirs:
        slug = case_dir.name
        out_dir = DST / slug
        out_dir.mkdir(parents=True, exist_ok=True)

        all_files = sorted(case_dir.glob("*.txt"))
        pdf_files = [f for f in all_files if is_pdf_extract(f.name)]
        # Source-IDs we've already covered via _pdf.txt versions
        covered_stems = {f.name.replace("_pdf.txt", ".txt") for f in pdf_files}

        kept_files = []
        # Prefer PDF extracts
        for f in pdf_files:
            text = f.read_text(encoding="utf-8", errors="ignore")
            if is_cloudflare_challenge_file(text):
                continue
            cleaned = clean_text(text)
            out = out_dir / f.name
            out.write_text(cleaned, encoding="utf-8")
            kept_files.append((f.name, words(cleaned)))

        # Add HTML-extracted versions only if no PDF-extract sibling exists
        for f in all_files:
            if is_pdf_extract(f.name):
                continue
            if f.name in covered_stems:
                # Already covered by _pdf version; skip
                continue
            text = f.read_text(encoding="utf-8", errors="ignore")
            if is_cloudflare_challenge_file(text):
                continue
            cleaned = clean_text(text)
            if words(cleaned) < 100:
                # After cleaning, too thin to keep
                continue
            out = out_dir / f.name
            out.write_text(cleaned, encoding="utf-8")
            kept_files.append((f.name, words(cleaned)))

        case_total = sum(w for _, w in kept_files)
        summary.append((slug, len(kept_files), case_total))

    print(f"Cleaned corpus: 04_extracted_text_cleaned/")
    print(f"{'Case':<55} {'Files':>5} {'Tokens':>8}")
    print("-" * 75)
    for slug, n_files, n_tokens in summary:
        flag = " ⚠ THIN" if n_tokens < 1000 else ""
        print(f"{slug:<55} {n_files:>5} {n_tokens:>8,}{flag}")

    total_files = sum(n for _, n, _ in summary)
    total_tokens = sum(t for _, _, t in summary)
    print("-" * 75)
    print(f"TOTAL: {total_files} files, {total_tokens:,} tokens")
    n_thin = sum(1 for _, _, t in summary if t < 1000)
    if n_thin:
        print(f"⚠ {n_thin} cases below 1,000-token threshold; flag for re-extraction")


if __name__ == "__main__":
    main()
