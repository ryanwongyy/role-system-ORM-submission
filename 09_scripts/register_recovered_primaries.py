#!/usr/bin/env python3
"""Register the four full-text PDFs the user placed at
/Users/ryanwong/Human roles/*.pdf into the project folder.

For each of C001_P1, C005_P1, C035_P1, C036_S1:
  1. Move the user's PDF into 03_raw_sources/{slug}/{source_id}.pdf (overwriting
     the broken 2026-04-08 anti-bot snapshot).
  2. Extract full text (all pages) to 04_extracted_text/{slug}/{source_id}_pdf.txt.
  3. Flip access_status in the per-case source_manifest.csv from
     inaccessible/paywalled to open; update local paths and notes.

Then rebuild the master tables, the logs, the 10_outputs/ artefacts, and
leave the manuscript untouched (updated separately).

Does NOT modify per-case role_coding.csv — wave-2/3 upgrades are preserved.
"""
from __future__ import annotations

import csv
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
USER_ROOT = Path("/Users/ryanwong/Human roles")

sys.path.insert(0, str(PROJECT_ROOT / "09_scripts"))

from build_p1_db import (  # noqa: E402
    TODAY,
    WORKBOOK_COPY_PATH,
    build_collection_log,
    build_collection_summary,
    build_data_inventory,
    build_known_gaps,
    build_role_confidence_report,
    clean_text,
    fallback_supported_case_ids,
    non_open_external_sources,
    supplemental_enrichment_case_ids,
)

try:
    from pypdf import PdfReader  # type: ignore
except Exception:  # pragma: no cover
    PdfReader = None

try:
    import pdfplumber  # type: ignore
except Exception:  # pragma: no cover
    pdfplumber = None


SOURCE_MANIFEST_FIELDS = [
    "source_id", "case_id", "source_role", "source_title",
    "authors / organization", "year", "source_type", "evidence_tier",
    "DOI", "URL", "local_raw_path", "local_text_path", "retrieval_date",
    "access_status", "why_included", "notes",
]

# Ordered: (user_filename, case_slug, source_id, prior_access_status)
RECOVERIES = [
    (
        "törnberg-2024-large-language-models-outperform-expert-coders-and-supervised-classifiers-at-annotating-political-social.pdf",
        "001_objective_party_annotation",
        "C001_P1",
        "inaccessible",
    ),
    (
        "liu-sun-2025-from-voices-to-validity-leveraging-large-language-models-(llms)-for-textual-analysis-of-policy-stakeholder.pdf",
        "005_human_developed_codebooks",
        "C005_P1",
        "inaccessible",
    ),
    (
        "Use of artificial intelligence tools by doctoral students  a mixed-methods explanatory-sequential investigation (1).pdf",
        "035_doctoral_student_ai_use",
        "C035_P1",
        "inaccessible",
    ),
    (
        "Use of artificial intelligence tools by doctoral students  a mixed-methods explanatory-sequential investigation.pdf",
        "036_predictive_design_course",
        "C036_S1",
        "paywalled",
    ),
]

RECOVERY_NOTE = (
    f"Full-text PDF obtained via institutional access and stored locally on {TODAY}."
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as h:
        return list(csv.DictReader(h))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def extract_full_pdf_text(pdf_path: Path) -> str:
    """Extract text from all pages of the PDF. pypdf primary, pdfplumber
    fallback per-page for pages pypdf returns empty on."""
    pages: list[str] = []
    reader = None
    if PdfReader is not None:
        try:
            reader = PdfReader(str(pdf_path))
        except Exception:
            reader = None
    if reader is not None:
        for i, page in enumerate(reader.pages):
            text = ""
            try:
                text = page.extract_text() or ""
            except Exception:
                text = ""
            if not text.strip() and pdfplumber is not None:
                try:
                    with pdfplumber.open(str(pdf_path)) as pdf:
                        if i < len(pdf.pages):
                            text = pdf.pages[i].extract_text() or ""
                except Exception:
                    pass
            cleaned = clean_text(text)
            if cleaned:
                pages.append(cleaned)
        if pages:
            return "\n\n".join(pages).strip()
    # Fallback: pdfplumber only
    if pdfplumber is not None:
        try:
            with pdfplumber.open(str(pdf_path)) as pdf:
                for page in pdf.pages:
                    cleaned = clean_text(page.extract_text() or "")
                    if cleaned:
                        pages.append(cleaned)
        except Exception:
            pass
    return "\n\n".join(pages).strip()


def move_pdf(src_name: str, case_slug: str, source_id: str) -> Path:
    src = USER_ROOT / src_name
    if not src.exists():
        raise FileNotFoundError(f"User file not found: {src}")
    dest = PROJECT_ROOT / "03_raw_sources" / case_slug / f"{source_id}.pdf"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    shutil.move(str(src), str(dest))
    print(f"  moved {src_name} -> {dest}")
    return dest


def extract_text(case_slug: str, source_id: str, pdf_path: Path) -> Path:
    text = extract_full_pdf_text(pdf_path)
    if not text:
        raise RuntimeError(f"Empty text extracted for {pdf_path}")
    dest = PROJECT_ROOT / "04_extracted_text" / case_slug / f"{source_id}_pdf.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text + "\n", encoding="utf-8")
    line_count = len(text.splitlines()) + 1
    print(f"  extracted text -> {dest} ({line_count} lines, {len(text):,} chars)")
    return dest


def update_manifest(
    case_slug: str, source_id: str, pdf_path: Path, text_path: Path
) -> None:
    path = PROJECT_ROOT / "02_cases" / case_slug / "source_manifest.csv"
    rows = read_csv(path)
    found = False
    for row in rows:
        if row["source_id"] == source_id:
            row["access_status"] = "open"
            row["local_raw_path"] = str(pdf_path)
            row["local_text_path"] = str(text_path)
            row["retrieval_date"] = TODAY
            # Improve the degenerate source_title "Just a moment..." from the
            # original anti-bot snapshot, if still present.
            if row.get("source_title", "").strip().startswith("Just a moment"):
                row["source_title"] = _infer_title_from_text(text_path)
            row["notes"] = RECOVERY_NOTE
            found = True
            break
    if not found:
        raise RuntimeError(f"{source_id} not found in {path}")
    write_csv(path, SOURCE_MANIFEST_FIELDS, rows)
    print(f"  manifest updated: {path.relative_to(PROJECT_ROOT)}")


def _infer_title_from_text(text_path: Path) -> str:
    """Best-effort: first non-empty line usually approximates the paper title."""
    for line in text_path.read_text(encoding="utf-8").splitlines():
        cleaned = line.strip()
        if len(cleaned) > 20:
            return cleaned[:300]
    return text_path.stem


def rebuild_sources_master() -> list[dict[str, str]]:
    all_rows: list[dict[str, str]] = []
    for case_dir in sorted((PROJECT_ROOT / "02_cases").iterdir()):
        if not case_dir.is_dir():
            continue
        path = case_dir / "source_manifest.csv"
        if path.exists():
            all_rows.extend(read_csv(path))
    out = PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv"
    write_csv(out, SOURCE_MANIFEST_FIELDS, all_rows)
    print(f"rebuilt {out.relative_to(PROJECT_ROOT)} ({len(all_rows)} rows)")
    return all_rows


def rebuild_source_access_report(sources_master: list[dict[str, str]]) -> None:
    out = PROJECT_ROOT / "08_logs" / "source_access_report.csv"
    slug_by_cid: dict[str, str] = {}
    for d in (PROJECT_ROOT / "02_cases").iterdir():
        if d.is_dir():
            slug_by_cid[str(int(d.name.split("_", 1)[0]))] = d.name
    rows = []
    for row in sources_master:
        if row.get("source_role") == "registry":
            continue
        rows.append(
            {
                "case_id": row["case_id"],
                "case_slug": slug_by_cid.get(row["case_id"], ""),
                "source_id": row["source_id"],
                "url": row.get("URL", ""),
                "access_status": row.get("access_status", ""),
                "local_raw_path": row.get("local_raw_path", ""),
                "local_text_path": row.get("local_text_path", ""),
            }
        )
    write_csv(
        out,
        ["case_id", "case_slug", "source_id", "url", "access_status",
         "local_raw_path", "local_text_path"],
        rows,
    )
    print(f"rebuilt {out.relative_to(PROJECT_ROOT)} ({len(rows)} rows)")


def load_role_master() -> list[dict[str, str]]:
    return read_csv(PROJECT_ROOT / "06_analysis_tables" / "role_coding_master.csv")


def load_cases_master() -> list[dict[str, str]]:
    return read_csv(PROJECT_ROOT / "01_registry" / "cases_master.csv")


def rebuild_downstream_reports(
    cases_master: list[dict[str, str]],
    sources_master: list[dict[str, str]],
    role_master: list[dict[str, str]],
) -> None:
    # role_confidence_report.csv
    out_conf = PROJECT_ROOT / "08_logs" / "role_confidence_report.csv"
    conf_rows = build_role_confidence_report(cases_master, sources_master, role_master)
    write_csv(
        out_conf,
        ["case_id", "case_slug", "case_title", "analysis_ready",
         "low_confidence_rows", "medium_confidence_rows", "high_confidence_rows",
         "open_external_sources", "non_open_external_sources",
         "uses_open_fallback_or_companion_source", "next_review_priority"],
        conf_rows,
    )
    print(f"rebuilt {out_conf.relative_to(PROJECT_ROOT)}")

    (PROJECT_ROOT / "data_inventory.md").write_text(
        build_data_inventory(cases_master, sources_master, role_master) + "\n",
        encoding="utf-8",
    )
    print("rebuilt data_inventory.md")

    (PROJECT_ROOT / "known_gaps.md").write_text(
        build_known_gaps(cases_master, sources_master, role_master) + "\n",
        encoding="utf-8",
    )
    print("rebuilt known_gaps.md")

    (PROJECT_ROOT / "10_outputs" / "p1_collection_summary.md").write_text(
        build_collection_summary(cases_master, sources_master, role_master) + "\n",
        encoding="utf-8",
    )
    print("rebuilt 10_outputs/p1_collection_summary.md")

    # collection_log.md
    external = [r for r in sources_master if r.get("source_role") != "registry"]
    status_counter = Counter(r.get("access_status", "") for r in external)
    summary = {
        "case_count": len(cases_master),
        "external_sources_attempted": len(external),
        "external_sources_open": status_counter.get("open", 0),
        "external_sources_paywalled": status_counter.get("paywalled", 0),
        "external_sources_inaccessible": status_counter.get("inaccessible", 0),
        "fallback_supported_cases": len(fallback_supported_case_ids(sources_master)),
        "role_coding_high_confidence_rows": sum(
            1 for r in role_master if r.get("confidence") == "high"
        ),
        "role_coding_medium_confidence_rows": sum(
            1 for r in role_master if r.get("confidence") == "medium"
        ),
        "role_coding_low_confidence_rows": sum(
            1 for r in role_master if r.get("confidence") == "low"
        ),
    }
    (PROJECT_ROOT / "collection_log.md").write_text(
        build_collection_log(summary) + "\n", encoding="utf-8"
    )
    print("rebuilt collection_log.md")


def run_rebuild_10_outputs() -> None:
    """Refresh casebook, anchor cases, typology overview, comparison matrix."""
    import importlib
    import rebuild_10_outputs  # type: ignore
    importlib.reload(rebuild_10_outputs)
    rebuild_10_outputs.main()


def main() -> int:
    print("=== Phase 1/2: move PDFs and extract text ===")
    for src_name, case_slug, source_id, _prior in RECOVERIES:
        print(f"[{source_id}]")
        pdf_path = move_pdf(src_name, case_slug, source_id)
        text_path = extract_text(case_slug, source_id, pdf_path)
        update_manifest(case_slug, source_id, pdf_path, text_path)
    print()
    print("=== Phase 3: rebuild masters ===")
    sources_master = rebuild_sources_master()
    rebuild_source_access_report(sources_master)
    cases_master = load_cases_master()
    role_master = load_role_master()
    print()
    print("=== Phase 4: rebuild reports ===")
    rebuild_downstream_reports(cases_master, sources_master, role_master)
    print()
    print("=== Phase 5: rebuild 10_outputs/ ===")
    run_rebuild_10_outputs()
    print()
    # Post-checks
    external_counter = Counter(
        r.get("access_status", "")
        for r in sources_master
        if r.get("source_role") != "registry"
    )
    print(f"external source access distribution: {dict(external_counter)}")
    assert external_counter.get("inaccessible", 0) == 0
    assert external_counter.get("paywalled", 0) == 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
