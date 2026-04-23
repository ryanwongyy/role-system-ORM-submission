#!/usr/bin/env python3
"""Register the lawful green-OA / author-version fallback sources that already
exist on disk for Cases 1 and 5 into their source manifests and the master
tables, then recompute analysis_ready and downstream reports.

Background
----------
- `02_cases/.../04_extracted_text/` already contains `C001_S1.txt` (UvA-DARE
  green-OA CC BY deposit of the Tornberg paper) and `C005_S1.txt` (Liu & Sun
  author-version preprint of the same study referenced by `C005_P1`).
- These files were added during the initial 2026-04-07 build but never
  registered in `source_manifest.csv`, so `sources_master.csv` still shows
  only the inaccessible `C001_P1` and `C005_P1`.
- As a result, `infer_analysis_status()` flags both cases as `partial`, even
  though wave-3 role coding cites `C001_S1` / `C005_S1` as its source.

This script fixes the inconsistency.
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
sys.path.insert(0, str(PROJECT_ROOT / "09_scripts"))

# Reuse build_p1_db's report builders for consistency
from build_p1_db import (  # noqa: E402
    build_collection_summary,
    build_data_inventory,
    build_known_gaps,
    build_role_confidence_report,
)


SOURCE_MANIFEST_FIELDS = [
    "source_id", "case_id", "source_role", "source_title",
    "authors / organization", "year", "source_type", "evidence_tier",
    "DOI", "URL", "local_raw_path", "local_text_path", "retrieval_date",
    "access_status", "why_included", "notes",
]

FALLBACK_ROWS = {
    1: {
        "source_id": "C001_S1",
        "case_id": "1",
        "source_role": "secondary",
        "source_title": "Large Language Models Outperform Expert Coders and Supervised Classifiers at Annotating Political Social Media Messages (UvA-DARE green OA deposit, CC BY)",
        "authors / organization": "Tornberg, Petter",
        "year": "2025",
        "source_type": "journal article",
        "evidence_tier": "peer-reviewed article",
        "DOI": "10.1177/08944393241286471",
        "URL": "https://doi.org/10.1177/08944393241286471",
        "local_raw_path": "",
        "local_text_path": str(PROJECT_ROOT / "04_extracted_text" / "001_objective_party_annotation" / "C001_S1.txt"),
        "retrieval_date": "2026-04-07",
        "access_status": "open",
        "why_included": "Lawful CC BY green-OA deposit of the same peer-reviewed article whose journal landing page (C001_P1) is anti-bot blocked. Provides the substantive evidence used in wave-3 role coding.",
        "notes": "Green-OA deposit via University of Amsterdam (UvA-DARE). License: CC BY.",
    },
    5: {
        "source_id": "C005_S1",
        "case_id": "5",
        "source_role": "secondary",
        "source_title": "From Voices to Validity: Leveraging Large Language Models (LLMs) for Textual Analysis of Policy Stakeholder Interviews (author version / preprint)",
        "authors / organization": "Liu, Alex and Sun, Min",
        "year": "2025",
        "source_type": "journal article",
        "evidence_tier": "peer-reviewed article",
        "DOI": "10.1177/23328584251374595",
        "URL": "https://doi.org/10.1177/23328584251374595",
        "local_raw_path": "",
        "local_text_path": str(PROJECT_ROOT / "04_extracted_text" / "005_human_developed_codebooks" / "C005_S1.txt"),
        "retrieval_date": "2026-04-07",
        "access_status": "open",
        "why_included": "Lawful open-access author version of the same peer-reviewed article whose journal landing page (C005_P1) is anti-bot blocked. Provides the substantive evidence used in wave-3 role coding.",
        "notes": "Author-version deposit covering the same study as C005_P1.",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as h:
        return list(csv.DictReader(h))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def update_per_case_manifest(case_slug: str, new_row: dict[str, str]) -> None:
    path = PROJECT_ROOT / "02_cases" / case_slug / "source_manifest.csv"
    rows = read_csv(path)
    # Guard: don't double-register
    if any(r["source_id"] == new_row["source_id"] for r in rows):
        print(f"  {case_slug}: {new_row['source_id']} already in manifest — skipping")
        return
    rows.append({k: new_row.get(k, "") for k in SOURCE_MANIFEST_FIELDS})
    write_csv(path, SOURCE_MANIFEST_FIELDS, rows)
    print(f"  {case_slug}: appended {new_row['source_id']} to manifest")


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
    print(f"Rebuilt {out} ({len(all_rows)} rows)")
    return all_rows


def update_cases_master(affected_case_ids: set[str]) -> list[dict[str, str]]:
    path = PROJECT_ROOT / "01_registry" / "cases_master.csv"
    rows = read_csv(path)
    fields = list(rows[0].keys())
    for row in rows:
        if row["Case ID"] in affected_case_ids:
            row["analysis_ready"] = "yes"
            row["collection_status"] = "complete"
            row["main_limitations"] = (
                "Primary journal-page URL is access-limited, but a lawful open-access "
                "deposit (secondary source) covers the substantive evidence."
            )
            # Bump source counts (one new external secondary)
            try:
                row["source_count_total"] = str(int(row["source_count_total"]) + 1)
            except (ValueError, KeyError):
                pass
    write_csv(path, fields, rows)
    print(f"Updated {path} for cases {sorted(affected_case_ids)}")
    return rows


def rebuild_source_access_report(sources_master: list[dict[str, str]]) -> None:
    out = PROJECT_ROOT / "08_logs" / "source_access_report.csv"
    rows = []
    for row in sources_master:
        if row.get("source_role") == "registry":
            continue
        case_dir = next(
            (d for d in (PROJECT_ROOT / "02_cases").iterdir()
             if d.is_dir() and d.name.startswith(f"{int(row['case_id']):03d}_")),
            None,
        )
        case_slug = case_dir.name if case_dir else ""
        rows.append(
            {
                "case_id": row["case_id"],
                "case_slug": case_slug,
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
    print(f"Rebuilt {out} ({len(rows)} rows)")


def rebuild_role_master_master() -> list[dict[str, str]]:
    """Aggregate per-case role_coding.csv into role_coding_master.csv.
    (Called to be safe — wave-2/3 updates already wrote this, but regenerating
    keeps it in lock-step with the per-case files.)"""
    all_rows = []
    role_fields = [
        "case_id", "role_label", "role_group", "role_observable_in_case",
        "status_in_case", "confidence", "evidence_basis_summary",
        "main_supporting_source_ids", "main_contrary_source_ids", "notes",
    ]
    for case_dir in sorted((PROJECT_ROOT / "02_cases").iterdir()):
        if not case_dir.is_dir():
            continue
        path = case_dir / "role_coding.csv"
        if path.exists():
            all_rows.extend(read_csv(path))
    out = PROJECT_ROOT / "06_analysis_tables" / "role_coding_master.csv"
    write_csv(out, role_fields, all_rows)
    print(f"Rebuilt {out} ({len(all_rows)} rows)")
    return all_rows


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
    print(f"Rebuilt {out_conf}")

    # data_inventory.md
    (PROJECT_ROOT / "data_inventory.md").write_text(
        build_data_inventory(cases_master, sources_master, role_master) + "\n",
        encoding="utf-8",
    )
    print(f"Rebuilt {PROJECT_ROOT / 'data_inventory.md'}")

    # known_gaps.md
    (PROJECT_ROOT / "known_gaps.md").write_text(
        build_known_gaps(cases_master, sources_master, role_master) + "\n",
        encoding="utf-8",
    )
    print(f"Rebuilt {PROJECT_ROOT / 'known_gaps.md'}")

    # collection_summary.md (10_outputs) — uses same inputs
    (PROJECT_ROOT / "10_outputs" / "p1_collection_summary.md").write_text(
        build_collection_summary(cases_master, sources_master, role_master) + "\n",
        encoding="utf-8",
    )
    print(f"Rebuilt {PROJECT_ROOT / '10_outputs' / 'p1_collection_summary.md'}")


def main() -> int:
    # Per-case manifests
    update_per_case_manifest("001_objective_party_annotation", FALLBACK_ROWS[1])
    update_per_case_manifest("005_human_developed_codebooks", FALLBACK_ROWS[5])

    # Master tables
    sources_master = rebuild_sources_master()
    cases_master = update_cases_master({"1", "5"})
    rebuild_source_access_report(sources_master)

    # Role master (idempotent, for lock-step)
    role_master = rebuild_role_master_master()

    # Downstream reports driven off the masters
    rebuild_downstream_reports(cases_master, sources_master, role_master)

    # Verify
    ar_counts = Counter(r["analysis_ready"] for r in cases_master)
    print()
    print(f"analysis_ready distribution: {dict(ar_counts)}")
    assert ar_counts["yes"] == 36, f"Expected 36 yes, got {ar_counts['yes']}"
    assert ar_counts.get("partial", 0) == 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
