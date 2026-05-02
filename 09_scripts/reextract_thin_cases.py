"""Re-extract content from HTML sources for thin cases (gap 2).

Identifies cases with <2,000 cleaned tokens after clean_extracted_text.py runs,
then re-extracts from 03_raw_sources/<slug>/*.html using BeautifulSoup with proper
HTML parsing (vs. the original raw text-extraction that produced boilerplate).

Output: appends _v2.txt files into 04_extracted_text_cleaned/<slug>/
preserving the cleaning-script's existing outputs for thicker cases.

Determinism: pure HTML parsing + regex cleanup. No model calls. No randomness.
"""
from __future__ import annotations

import re
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
RAW = ROOT / "03_raw_sources"
CLEANED = ROOT / "04_extracted_text_cleaned"

THIN_CASES = [
    "006_maternal_health_interview_coding",
    "023_forecasting_before_field_experiments",
    "031_project_rachel_authorship_boundary",
]


def html_to_text(html: str) -> str:
    """Strip HTML to text, preserving paragraph structure."""
    soup = BeautifulSoup(html, "html.parser")

    # Drop noise tags
    for tag in soup(["script", "style", "nav", "header", "footer",
                     "form", "button", "noscript", "svg", "iframe"]):
        tag.decompose()

    # Prefer the abstract / main content sections on arxiv pages
    main = soup.find("main") or soup.find("article") or soup.body or soup
    text = main.get_text(separator="\n", strip=True)
    return text


def clean_arxiv_chrome(text: str) -> str:
    """Strip residual arxiv chrome that survives HTML parsing."""
    patterns = [
        r"Skip to main content.*?(?=Title:|Abstract|Authors:)",
        r"Donate\s*",
        r"open navigation menu.*?(?=\n)",
        r"open search\s*GO\s*",
        r"All fields\s*Title\s*Author\s*Abstract.*?(?=\n)",
        r"quick links\s*Login.*?(?=\n)",
        r"Help \| Advanced Search",
        r"Web Accessibility Assistance.*?(?=\n)",
        r"Bibliographic and Citation Tools.*?(?=\n)",
        r"Code, Data and Media Associated with this Article.*?(?=\n)",
        r"Recommenders and Search Tools.*?(?=\n)",
        r"Demos\s*",
        r"Related Papers.*?(?=\n)",
        r"BibTeX formatted citation.*?(?=\n)",
        r"Bookmark\s*",
        r"Connected Papers.*?(?=\n)",
        r"Litmaps\s*",
        r"scite\.ai\s*",
        r"Replicate\s*\(What is Replicate\?\)",
        r"\barXiv author ID\b",
        r"\bORCID\b",
        r"\bMSC classification\b",
        r"\bACM classification\b",
        r"DBLP \(What is DBLP\?\)",
        r"Semantic Scholar.*?(?=\n)",
        r"Privacy and Cookies.*?(?=\n)",
        r"Help Pages.*?(?=\n)",
        r"Contact arXiv.*?(?=\n)",
        # Cloudflare residue
        r"Just a moment\.\.\..*?(?=\n)",
        r"Enable JavaScript and cookies.*?(?=\n)",
        # Standalone URLs
        r"^\s*https?://\S+\s*$",
    ]
    for p in patterns:
        text = re.sub(p, "", text, flags=re.IGNORECASE | re.DOTALL | re.MULTILINE)

    # Whitespace normalization
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Drop very short residual lines (navigation artifacts)
    lines = []
    for line in text.split("\n"):
        s = line.strip()
        if s and len(s) >= 20 or s == "":
            lines.append(line)
    text = "\n".join(lines)

    return text.strip()


def words(text: str) -> int:
    return len(re.findall(r"\b[A-Za-z][A-Za-z'\-]*\b", text))


def main() -> None:
    print(f"{'Case':<55} {'File':<25} {'Orig':>6} {'New':>6} {'Δ':>6}")
    print("-" * 105)
    for slug in THIN_CASES:
        raw_dir = RAW / slug
        cleaned_dir = CLEANED / slug
        cleaned_dir.mkdir(parents=True, exist_ok=True)

        html_files = sorted(raw_dir.glob("*.html"))
        for html_file in html_files:
            html = html_file.read_text(encoding="utf-8", errors="ignore")
            extracted = html_to_text(html)
            cleaned = clean_arxiv_chrome(extracted)

            # Determine output filename
            stem = html_file.stem  # C023_P1
            out_path = cleaned_dir / f"{stem}_v2.txt"

            # Check existing output for comparison
            old_path = cleaned_dir / f"{stem}.txt"
            old_words = words(old_path.read_text(encoding="utf-8")) if old_path.exists() else 0
            new_words = words(cleaned)

            if new_words >= 200:  # threshold for "useful" re-extraction
                out_path.write_text(cleaned, encoding="utf-8")
                print(f"{slug:<55} {html_file.name:<25} {old_words:>6} {new_words:>6} {new_words-old_words:>+6}")
            else:
                print(f"{slug:<55} {html_file.name:<25} {old_words:>6} {new_words:>6}  SKIP (too thin)")


if __name__ == "__main__":
    main()
