#!/usr/bin/env python3
"""Wave-3 role-coding confidence upgrades for the remaining 31 cases.

Reads per-case CSV proposals from /tmp/wave3_csvs/, writes them to the per-case
role_coding.csv files, then rebuilds role_coding_master.csv,
role_confidence_report.csv, data_inventory.md, and known_gaps.md.
"""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
STAGING_DIR = Path("/tmp/wave3_csvs")

ROLE_FIELDS = [
    "case_id",
    "role_label",
    "role_group",
    "role_observable_in_case",
    "status_in_case",
    "confidence",
    "evidence_basis_summary",
    "main_supporting_source_ids",
    "main_contrary_source_ids",
    "notes",
]

CASE_SLUGS: dict[int, str] = {}
for path in sorted((PROJECT_ROOT / "02_cases").iterdir()):
    if path.is_dir():
        cid = int(path.name.split("_", 1)[0])
        CASE_SLUGS[cid] = path.name


WAVE3_CASES = [1, 2, 4, 5, 6, 7, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21,
               22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]


def read_csv_file(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv_file(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def apply_case_updates() -> None:
    for case_id in WAVE3_CASES:
        slug = CASE_SLUGS[case_id]
        staged = STAGING_DIR / f"case_{case_id:02d}.csv"
        if not staged.exists():
            raise FileNotFoundError(staged)
        rows = read_csv_file(staged)
        assert len(rows) == 17, f"Case {case_id} has {len(rows)} rows, expected 17"
        target = PROJECT_ROOT / "02_cases" / slug / "role_coding.csv"
        write_csv_file(target, ROLE_FIELDS, rows)
        print(f"Wrote {target} ({len(rows)} rows)")


def rebuild_master() -> list[dict[str, str]]:
    all_rows: list[dict[str, str]] = []
    for case_id in sorted(CASE_SLUGS):
        slug = CASE_SLUGS[case_id]
        path = PROJECT_ROOT / "02_cases" / slug / "role_coding.csv"
        if not path.exists():
            continue
        all_rows.extend(read_csv_file(path))
    out = PROJECT_ROOT / "06_analysis_tables" / "role_coding_master.csv"
    write_csv_file(out, ROLE_FIELDS, all_rows)
    print(f"Rebuilt {out} ({len(all_rows)} rows)")
    return all_rows


def rebuild_confidence_report(role_master: list[dict[str, str]]) -> None:
    cases_master = read_csv_file(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    sources_master = read_csv_file(PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv")

    source_by_case: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sources_master:
        if row.get("source_role") == "registry":
            continue
        source_by_case[row["case_id"]].append(row)

    confidence_by_case: dict[str, Counter] = defaultdict(Counter)
    for row in role_master:
        confidence_by_case[row["case_id"]][row.get("confidence", "")] += 1

    out_fields = [
        "case_id", "case_slug", "case_title", "analysis_ready",
        "low_confidence_rows", "medium_confidence_rows", "high_confidence_rows",
        "open_external_sources", "non_open_external_sources",
        "uses_open_fallback_or_companion_source", "next_review_priority",
    ]
    rows = []
    for case in cases_master:
        case_id = case["Case ID"]
        sources = source_by_case.get(case_id, [])
        counts = confidence_by_case.get(case_id, Counter())
        open_count = sum(1 for r in sources if r.get("access_status") == "open")
        non_open_count = sum(1 for r in sources if r.get("access_status") != "open")
        uses_fallback = "yes" if open_count and non_open_count else "no"
        low = counts.get("low", 0)
        priority = "high" if low >= 15 or non_open_count else "medium" if low else "low"
        rows.append(
            {
                "case_id": case_id,
                "case_slug": case["case_slug"],
                "case_title": case["Case title"],
                "analysis_ready": case["analysis_ready"],
                "low_confidence_rows": str(low),
                "medium_confidence_rows": str(counts.get("medium", 0)),
                "high_confidence_rows": str(counts.get("high", 0)),
                "open_external_sources": str(open_count),
                "non_open_external_sources": str(non_open_count),
                "uses_open_fallback_or_companion_source": uses_fallback,
                "next_review_priority": priority,
            }
        )
    out = PROJECT_ROOT / "08_logs" / "role_confidence_report.csv"
    write_csv_file(out, out_fields, rows)
    print(f"Rebuilt {out} ({len(rows)} rows)")


def rebuild_data_inventory(role_master: list[dict[str, str]]) -> None:
    cases_master = read_csv_file(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    sources_master = read_csv_file(PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv")

    ar_counts = Counter(row["analysis_ready"] for row in cases_master)
    src_counts = Counter(
        row["access_status"] for row in sources_master if row.get("source_role") != "registry"
    )
    conf_counts = Counter(row.get("confidence", "") for row in role_master)

    by_case: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sources_master:
        if row.get("source_role") == "registry":
            continue
        by_case[row["case_id"]].append(row)
    fallback_supported = sum(
        1
        for rows in by_case.values()
        if any(r.get("access_status") == "open" for r in rows)
        and any(r.get("access_status") != "open" for r in rows)
    )

    lines = [
        "# Data Inventory",
        "",
        f"- Cases in registry: {len(cases_master)}",
        f"- Analysis-ready `yes`: {ar_counts.get('yes', 0)}",
        f"- Analysis-ready `partial`: {ar_counts.get('partial', 0)}",
        f"- Analysis-ready `no`: {ar_counts.get('no', 0)}",
        f"- Open external sources: {src_counts.get('open', 0)}",
        f"- Paywalled external sources: {src_counts.get('paywalled', 0)}",
        f"- Inaccessible external sources: {src_counts.get('inaccessible', 0)}",
        f"- Cases with open fallback or companion-source coverage: {fallback_supported}",
        f"- Role-coding rows at `high` confidence: {conf_counts.get('high', 0)}",
        f"- Role-coding rows at `medium` confidence: {conf_counts.get('medium', 0)}",
        f"- Role-coding rows at `low` confidence: {conf_counts.get('low', 0)}",
    ]
    out = PROJECT_ROOT / "data_inventory.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Rebuilt {out}")


def rebuild_known_gaps(role_master: list[dict[str, str]]) -> None:
    cases_master = read_csv_file(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    sources_master = read_csv_file(PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv")

    weak_cases = [row for row in cases_master if row["analysis_ready"] != "yes"]
    title_lookup = {row["Case ID"]: row["Case title"] for row in cases_master}

    lines = ["# Known Gaps", ""]
    if weak_cases:
        lines.append("## Case-level gaps")
        lines.append("")
        for row in weak_cases:
            lines.append(
                f"- Case {row['Case ID']} ({row['Case title']}): {row['analysis_ready']} / {row['collection_status']} - {row['main_limitations']}"
            )
    else:
        lines.append("- No case-level analysis gaps remain.")

    non_open = [
        row for row in sources_master
        if row.get("source_role") != "registry" and row.get("access_status") != "open"
    ]
    if non_open:
        lines.extend(["", "## Residual source-access limits", ""])
        for row in non_open:
            lines.append(
                f"- Case {row['case_id']} source {row['source_id']} ({row['access_status']}): {row['URL']}"
            )
        lines.append(
            "- These remaining journal-original URL failures do not block analysis where a lawful local fallback or companion full text is already stored; the unresolved part is journal-page retrieval, often due to anti-bot or landing-page access friction."
        )

    conf_counts = Counter(row.get("confidence", "") for row in role_master)
    low_by_case: Counter = Counter(
        row["case_id"] for row in role_master if row.get("confidence") == "low"
    )
    lines.extend(["", "## Residual role-coding confidence limits", ""])
    lines.append(f"- Low-confidence role rows: {conf_counts.get('low', 0)} of {len(role_master)} total.")
    lines.append(f"- Medium-confidence role rows: {conf_counts.get('medium', 0)}; high-confidence role rows: {conf_counts.get('high', 0)}.")
    if conf_counts.get('low', 0):
        top_cases = ", ".join(
            f"Case {case_id} ({title_lookup.get(case_id, case_id)}: {count})"
            for case_id, count in low_by_case.most_common(5)
        )
        lines.append(f"- Cases with the densest low-confidence coding: {top_cases}.")
        lines.append("- These rows remain traceable, but many still rely on workbook-driven initialization or limited direct role evidence.")

    out = PROJECT_ROOT / "known_gaps.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Rebuilt {out}")


def main() -> int:
    apply_case_updates()
    role_master = rebuild_master()
    rebuild_confidence_report(role_master)
    rebuild_data_inventory(role_master)
    rebuild_known_gaps(role_master)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
