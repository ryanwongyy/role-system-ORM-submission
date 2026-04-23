#!/usr/bin/env python3
"""Rebuild the five 10_outputs/ files from on-disk master tables.

Sidesteps build_p1_db.py's monolithic main() which re-initialises per-case
role_coding.csv files from hardcoded defaults, destroying wave-2/3 upgrades.
This script reads the already-up-to-date master tables and uses the modular
generator functions from build_p1_db.py (which are themselves fine; only
main()'s data-ingestion path is destructive).
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
sys.path.insert(0, str(PROJECT_ROOT / "09_scripts"))

from build_p1_db import (  # noqa: E402
    ROLE_UNIVERSE,
    build_anchor_cases,
    build_casebook_row,
    build_collection_summary,
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def build_typology_overview(
    role_master: list[dict[str, str]],
    repo_by_id: dict[int, dict[str, str]],
) -> list[dict[str, str]]:
    role_counts: dict[str, Counter[str]] = defaultdict(Counter)
    role_families: dict[str, Counter[str]] = defaultdict(Counter)
    role_caps: dict[str, Counter[str]] = defaultdict(Counter)
    for row in role_master:
        role_counts[row["role_label"]][row["status_in_case"]] += 1
        case = repo_by_id[int(row["case_id"])]
        role_families[row["role_label"]][case["Case family"]] += 1
        role_caps[row["role_label"]][case["Primary AI capability"]] += 1

    overview_rows = []
    for role_label, _role_group in ROLE_UNIVERSE:
        counter = role_counts[role_label]
        families = role_families[role_label].most_common(2)
        caps = role_caps[role_label].most_common(2)
        overview_rows.append(
            {
                "role_label": role_label,
                "number_of_cases_robust": counter.get("robust", 0),
                "number_of_cases_conditional": counter.get("conditional", 0),
                "number_of_cases_transformed": counter.get("transformed", 0),
                "number_of_cases_shrinking": counter.get("shrinking", 0),
                "number_of_cases_split_pressure": counter.get("split_pressure", 0),
                "number_of_cases_merge_pressure": counter.get("merge_pressure", 0),
                "most_common_case_families": "; ".join(f"{name} ({count})" for name, count in families),
                "most_common_ai_capabilities": "; ".join(f"{name} ({count})" for name, count in caps),
                "notes": "Counts generated from role_coding_master.csv",
            }
        )
    return overview_rows


def build_comparison_matrix(
    cases_master: list[dict[str, str]],
    case_features_rows: list[dict[str, str]],
    hypotheses_rows: list[dict[str, str]],
) -> list[dict[str, str]]:
    features_by_id = {row["Case ID"]: row for row in case_features_rows}
    hypotheses_by_id = {row["case_id"]: row for row in hypotheses_rows}
    comparison_rows = []
    for case in cases_master:
        cid = case["Case ID"]
        features = features_by_id[cid]
        hypothesis = hypotheses_by_id[cid]
        comparison_rows.append(
            {
                "case_id": cid,
                "case_slug": case["case_slug"],
                "case_title": case["Case title"],
                "case_family": case["Case family"],
                "primary_ai_capability": case["Primary AI capability"],
                "primary_research_stage": case["Primary research stage"],
                "institutional_setting": case["Institutional setting"],
                "task_ground_truth_level": features["task_ground_truth_level"],
                "post_hoc_auditability": features["post_hoc_auditability"],
                "evidence_strength_overall": features["evidence_strength_overall"],
                "autonomy_pressure": features["autonomy_pressure"],
                "analysis_ready": case["analysis_ready"],
                "dominant_role_pattern": hypothesis["dominant_role_pattern"],
                "portfolio_group": case["Portfolio group"],
                "program_priority": case["Program priority"],
            }
        )
    return comparison_rows


def main() -> int:
    cases_master = read_csv(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    sources_master = read_csv(PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv")
    role_master = read_csv(PROJECT_ROOT / "06_analysis_tables" / "role_coding_master.csv")
    case_features_rows = read_csv(PROJECT_ROOT / "06_analysis_tables" / "case_features.csv")
    hypotheses_rows = read_csv(PROJECT_ROOT / "06_analysis_tables" / "hypotheses_prep.csv")

    repo_by_id: dict[int, dict[str, str]] = {int(c["Case ID"]): c for c in cases_master}

    # p1_casebook.md — per-case narrative
    casebook_sections = []
    for case in cases_master:
        case_role_rows = [r for r in role_master if r["case_id"] == case["Case ID"]]
        casebook_sections.append(build_casebook_row(case, case, case_role_rows))
    write_text(PROJECT_ROOT / "10_outputs" / "p1_casebook.md", "\n".join(casebook_sections))

    # p1_anchor_cases.md — hardcoded case-ID groups
    write_text(
        PROJECT_ROOT / "10_outputs" / "p1_anchor_cases.md",
        build_anchor_cases(repo_by_id),
    )

    # p1_typology_overview_table.csv — role × status counts, top families/caps
    overview_rows = build_typology_overview(role_master, repo_by_id)
    write_csv(
        PROJECT_ROOT / "10_outputs" / "p1_typology_overview_table.csv",
        [
            "role_label",
            "number_of_cases_robust",
            "number_of_cases_conditional",
            "number_of_cases_transformed",
            "number_of_cases_shrinking",
            "number_of_cases_split_pressure",
            "number_of_cases_merge_pressure",
            "most_common_case_families",
            "most_common_ai_capabilities",
            "notes",
        ],
        overview_rows,
    )

    # p1_case_comparison_matrix.csv — wide case-level table
    comparison_rows = build_comparison_matrix(cases_master, case_features_rows, hypotheses_rows)
    write_csv(
        PROJECT_ROOT / "10_outputs" / "p1_case_comparison_matrix.csv",
        [
            "case_id",
            "case_slug",
            "case_title",
            "case_family",
            "primary_ai_capability",
            "primary_research_stage",
            "institutional_setting",
            "task_ground_truth_level",
            "post_hoc_auditability",
            "evidence_strength_overall",
            "autonomy_pressure",
            "analysis_ready",
            "dominant_role_pattern",
            "portfolio_group",
            "program_priority",
        ],
        comparison_rows,
    )

    # p1_collection_summary.md — overview narrative
    write_text(
        PROJECT_ROOT / "10_outputs" / "p1_collection_summary.md",
        build_collection_summary(cases_master, sources_master, role_master),
    )

    print("Rebuilt 5 files in 10_outputs/:")
    for name in (
        "p1_casebook.md",
        "p1_anchor_cases.md",
        "p1_typology_overview_table.csv",
        "p1_case_comparison_matrix.csv",
        "p1_collection_summary.md",
    ):
        print(f"  - {PROJECT_ROOT / '10_outputs' / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
