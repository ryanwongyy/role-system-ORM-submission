"""Assemble per-case cleaned text into a sentence-level corpus.

Reads:  04_extracted_text_cleaned/<slug>/*.txt
Writes: 06_analysis_tables/sentence_corpus.csv with columns:
        sentence_id, case_id, source_file, sentence_index, text

Sentence segmentation rule (pre-registered):
- Split on [.!?]+\\s+ followed by a capital letter
- Drop sentences shorter than 30 characters
- Preserve original casing (sentence-transformers handles this)

Determinism: pure regex + string ops. No model calls.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
SRC = ROOT / "04_extracted_text_cleaned"
OUT = ROOT / "06_analysis_tables/sentence_corpus.csv"

# Map slugs to case_id (per case_slug column in cases_master.csv)
CASE_REGISTRY = ROOT / "01_registry/cases_master.csv"

SENTENCE_SPLIT = re.compile(r"(?<=[\.!?])\s+(?=[A-Z\(])")


def split_sentences(text: str) -> list[str]:
    """Split text into sentences via the pre-registered rule."""
    # Replace newlines with spaces inside paragraphs so sentence boundaries
    # are punctuation-driven, not line-driven
    text = re.sub(r"\n+", " ", text)
    raw = SENTENCE_SPLIT.split(text)
    return [s.strip() for s in raw if len(s.strip()) >= 30]


def main() -> None:
    # Load registry slug → case_id mapping
    slug_to_case = {}
    with open(CASE_REGISTRY) as f:
        for row in csv.DictReader(f):
            slug_to_case[row["case_slug"]] = row["Case ID"]

    sentence_id = 0
    rows = []
    case_dirs = sorted(d for d in SRC.iterdir() if d.is_dir())
    for case_dir in case_dirs:
        slug = case_dir.name
        case_id = slug_to_case.get(slug, "?")
        for txt_file in sorted(case_dir.glob("*.txt")):
            text = txt_file.read_text(encoding="utf-8", errors="ignore")
            for sent_idx, sentence in enumerate(split_sentences(text)):
                rows.append({
                    "sentence_id": sentence_id,
                    "case_id": case_id,
                    "source_file": txt_file.name,
                    "sentence_index": sent_idx,
                    "text": sentence,
                })
                sentence_id += 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["sentence_id", "case_id", "source_file", "sentence_index", "text"])
        w.writeheader()
        for r in rows:
            w.writerow(r)

    # Per-case sentence counts
    from collections import Counter
    per_case = Counter(r["case_id"] for r in rows)
    print(f"Sentence corpus: {len(rows):,} sentences across {len(per_case)} cases")
    print(f"  min={min(per_case.values())}, max={max(per_case.values())}, median={sorted(per_case.values())[len(per_case)//2]}")
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
