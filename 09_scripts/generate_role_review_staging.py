#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
STAGING_ROOT = PROJECT_ROOT / ".codex" / "research-staging" / "role-review-wave-1"
WAVE_GROUPS = {
    "anchor_cases": [2, 7, 21, 27],
    "split_pressure_cases": [3, 19, 24, 34],
    "shrinkage_cases": [1, 7, 28, 29],
    "autonomy_boundary_cases": [25, 26, 32],
}
WAVE_ORDER = []
for case_ids in WAVE_GROUPS.values():
    for case_id in case_ids:
        if case_id not in WAVE_ORDER:
            WAVE_ORDER.append(case_id)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_queue_reason(group_names: list[str]) -> str:
    label_map = {
        "anchor_cases": "anchor completeness",
        "split_pressure_cases": "split-pressure review",
        "shrinkage_cases": "shrinkage validation",
        "autonomy_boundary_cases": "autonomy-boundary caution",
    }
    return "; ".join(label_map[name] for name in group_names)


def main() -> int:
    cases_master = read_csv(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    confidence_rows = read_csv(PROJECT_ROOT / "08_logs" / "role_confidence_report.csv")
    case_lookup = {int(row["Case ID"]): row for row in cases_master}
    confidence_lookup = {int(row["case_id"]): row for row in confidence_rows}

    group_lookup: dict[int, list[str]] = defaultdict(list)
    for group_name, case_ids in WAVE_GROUPS.items():
        for case_id in case_ids:
            group_lookup[case_id].append(group_name)

    queue_rows: list[dict[str, str]] = []
    root_lines = [
        "# Role Review Wave 1",
        "",
        "This staging area contains draft scaffolds only. Nothing here is production evidence, source-of-truth coding, or a final adjudication.",
        "",
        "Use these packs to run the next manual or assisted review wave on the highest-leverage P1 cases.",
        "",
        "## Included groups",
        "",
    ]
    for group_name, case_ids in WAVE_GROUPS.items():
        formatted = ", ".join(f"Case {case_id}" for case_id in case_ids)
        root_lines.append(f"- `{group_name}`: {formatted}")

    root_lines.extend(
        [
            "",
            "## Pack contents",
            "",
            "- `input.draft.md`: case context, live file paths, and currently collected source anchors",
            "- `expected-output.draft.md`: exact local artifacts that should change after review",
            "- `review.draft.md`: stepwise review instructions for the case",
            "- `missing-input-checklist.md`: concrete missing evidence or access items to seek next",
            "",
            "## Regeneration",
            "",
            "- Recommended project-local command after syncing the generator into `09_scripts/`: `python3 09_scripts/generate_role_review_staging.py`",
        ]
    )

    for case_id in WAVE_ORDER:
        case = case_lookup[case_id]
        conf = confidence_lookup[case_id]
        case_slug = case["case_slug"]
        groups = group_lookup[case_id]
        case_dir = PROJECT_ROOT / "02_cases" / case_slug
        manifest_rows = read_csv(case_dir / "source_manifest.csv")
        external_rows = [row for row in manifest_rows if row["source_role"] != "registry"]
        open_rows = [row for row in external_rows if row["access_status"] == "open"]
        blocked_rows = [row for row in external_rows if row["access_status"] != "open"]

        queue_rows.append(
            {
                "case_id": str(case_id),
                "case_slug": case_slug,
                "case_title": case["Case title"],
                "priority_groups": "; ".join(groups),
                "why_prioritized": build_queue_reason(groups),
                "analysis_ready": case["analysis_ready"],
                "low_confidence_rows": conf["low_confidence_rows"],
                "medium_confidence_rows": conf["medium_confidence_rows"],
                "high_confidence_rows": conf["high_confidence_rows"],
                "non_open_external_sources": conf["non_open_external_sources"],
                "staging_pack_dir": str(STAGING_ROOT / case_slug),
            }
        )

        source_lines = []
        for row in external_rows:
            source_lines.append(
                f"- `{row['source_id']}` | {row['evidence_tier']} | {row['access_status']} | {row['URL']}"
            )
        blocked_lines = [
            f"- `{row['source_id']}` remains `{row['access_status']}` at the original URL: {row['URL']}"
            for row in blocked_rows
        ] or ["- No currently known source-access blocker for this case."]

        pack_root = STAGING_ROOT / case_slug
        write_text(
            pack_root / "input.draft.md",
            "\n".join(
                [
                    f"# Input Draft: Case {case_id}",
                    "",
                    "Draft scaffold only. This file is not production evidence or final coding.",
                    "",
                    f"- Case title: {case['Case title']}",
                    f"- Priority groups: {', '.join(groups)}",
                    f"- Current analysis-ready status: {case['analysis_ready']}",
                    f"- Role-confidence profile: low {conf['low_confidence_rows']}, medium {conf['medium_confidence_rows']}, high {conf['high_confidence_rows']}",
                    f"- Case folder: {case_dir}",
                    f"- Notes file: {case_dir / 'notes.md'}",
                    f"- Source manifest: {case_dir / 'source_manifest.csv'}",
                    f"- Evidence extracts: {case_dir / 'evidence_extracts.csv'}",
                    f"- Role coding: {case_dir / 'role_coding.csv'}",
                    "",
                    "## Collected sources",
                    "",
                    *source_lines,
                ]
            ),
        )

        write_text(
            pack_root / "expected-output.draft.md",
            "\n".join(
                [
                    f"# Expected Output Draft: Case {case_id}",
                    "",
                    "Draft scaffold only. Do not treat this as completed review output.",
                    "",
                    "The next review pass should aim to update these live artifacts:",
                    "",
                    f"- {case_dir / 'evidence_extracts.csv'} with stronger direct role-support and contrary-evidence extracts",
                    f"- {case_dir / 'role_coding.csv'} with revised confidence levels and source-linked justifications where warranted",
                    f"- {case_dir / 'qa.md'} with any resolved ambiguity or remaining unresolved disputes",
                    "",
                    "The review should not create new cases or silently remove access-limit history.",
                ]
            ),
        )

        write_text(
            pack_root / "review.draft.md",
            "\n".join(
                [
                    f"# Review Draft: Case {case_id}",
                    "",
                    "Draft scaffold only. This is a checklist for the next human or assisted review wave.",
                    "",
                    "1. Read the open full-text or methodology sources already collected for this case.",
                    "2. Verify whether the currently marked robust, conditional, transformed, shrinking, or split-pressure roles are explicitly visible in source text.",
                    "3. Add at least one direct supportive extract and one limiting or rival extract if the current evidence file is still mostly workbook-seeded.",
                    "4. Re-score confidence in role_coding.csv only where source-linked justification materially improves.",
                    "5. Leave an explicit note if any remaining claim still depends mainly on repository curation rather than direct source language.",
                ]
            ),
        )

        write_text(
            pack_root / "missing-input-checklist.md",
            "\n".join(
                [
                    f"# Missing Input Checklist: Case {case_id}",
                    "",
                    "Draft scaffold only. Use this to request or collect the next lawful inputs if needed.",
                    "",
                    "## Source-access items",
                    "",
                    *blocked_lines,
                    "",
                    "## Review upgrades to look for",
                    "",
                    "- Direct language naming role responsibilities, adjudication logic, or division of labor",
                    "- Supplementary materials, appendices, benchmark cards, repo docs, or methodology notes",
                    "- Explicit caveats, failures, disclaimers, or boundary conditions",
                    "- Evidence that would raise or lower confidence in the current role status labels",
                ]
            ),
        )

    write_text(STAGING_ROOT / "README.md", "\n".join(root_lines))
    write_csv(
        STAGING_ROOT / "queue.csv",
        [
            "case_id",
            "case_slug",
            "case_title",
            "priority_groups",
            "why_prioritized",
            "analysis_ready",
            "low_confidence_rows",
            "medium_confidence_rows",
            "high_confidence_rows",
            "non_open_external_sources",
            "staging_pack_dir",
        ],
        queue_rows,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
