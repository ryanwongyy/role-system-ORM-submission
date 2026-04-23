#!/usr/bin/env python3
"""Generate the four manuscript tables requested by the narrative-critique
pass (items 1 and 3):

  Table 1        - role × status counts (17 roles × 6 status columns)
  Table 2a       - status distribution by Case family (8 rows)
  Table 2b       - status distribution by Primary AI capability (3 rows)
  Table 3 (sens) - headline role counts with 5 boundary cases excluded

Outputs:
  10_outputs/p1_manuscript_tables.md       - compiled markdown, paste-ready
  10_outputs/p1_manuscript_table_1.csv     - Table 1 backing data
  10_outputs/p1_manuscript_table_2a.csv    - Table 2a backing data
  10_outputs/p1_manuscript_table_2b.csv    - Table 2b backing data
  10_outputs/p1_manuscript_table_sensitivity.csv - Table 3 backing data

Reads only:
  01_registry/cases_master.csv
  06_analysis_tables/role_coding_master.csv
  09_scripts/build_p1_db.py (for ROLE_UNIVERSE order)
"""
from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
sys.path.insert(0, str(PROJECT_ROOT / "09_scripts"))
from build_p1_db import ROLE_UNIVERSE  # noqa: E402

STATUSES = [
    "robust", "conditional", "transformed",
    "shrinking", "split_pressure", "merge_pressure",
    "unclear", "not_applicable",
]

# Codebook §"Live-project and benchmark cases"
BOUNDARY_CASE_IDS = {"25", "26", "32", "33", "34"}

# Roles whose counts the paper's argument hinges on (for Table 3)
HEADLINE_ROLES = [
    "Protocol and provenance architect",
    "Calibration architect",
    "Accountability and labor allocator",
    "Routine first-pass screener",
    "Routine coder on high-consensus, ground-truth-rich tasks",
    "Structural prose polisher / drafter",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as h:
        return list(csv.DictReader(h))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as h:
        w = csv.DictWriter(h, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


def md_table(headers: list[str], rows: list[list]) -> str:
    """Emit a GitHub-flavoured markdown table."""
    col_widths = [len(h) for h in headers]
    str_rows = [[str(cell) for cell in row] for row in rows]
    for r in str_rows:
        for i, cell in enumerate(r):
            col_widths[i] = max(col_widths[i], len(cell))
    head = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
    sep = "|" + "|".join("-" * (w + 2) for w in col_widths) + "|"
    body = "\n".join(
        "| " + " | ".join(c.ljust(col_widths[i]) for i, c in enumerate(r)) + " |"
        for r in str_rows
    )
    return "\n".join([head, sep, body])


def build_table_1(role_master: list[dict]) -> tuple[list[list], list[str]]:
    """Role × status counts."""
    counts: dict[str, Counter] = defaultdict(Counter)
    for row in role_master:
        counts[row["role_label"]][row["status_in_case"]] += 1
    headers = ["role_label", "role_group"] + STATUSES
    data_rows = []
    for role_label, role_group in ROLE_UNIVERSE:
        row = [role_label, role_group] + [counts[role_label].get(s, 0) for s in STATUSES]
        data_rows.append(row)
    return data_rows, headers


def build_table_2(
    role_master: list[dict],
    cases_master: list[dict],
    group_field: str,
    group_label: str,
) -> tuple[list[list], list[str]]:
    """Status distribution by a case-level grouping field."""
    case_field = {c["Case ID"]: c[group_field] for c in cases_master}
    case_by_id_counter: Counter = Counter(case_field.values())
    counts: dict[str, Counter] = defaultdict(Counter)
    for row in role_master:
        group = case_field.get(row["case_id"], "UNKNOWN")
        counts[group][row["status_in_case"]] += 1
    headers = [group_label, "n_cases"] + STATUSES
    # Sort rows by number of cases descending, break ties alphabetically
    sorted_groups = sorted(
        case_by_id_counter.keys(),
        key=lambda g: (-case_by_id_counter[g], g),
    )
    data_rows = []
    for group in sorted_groups:
        n_cases = case_by_id_counter[group]
        row = [group, n_cases] + [counts[group].get(s, 0) for s in STATUSES]
        data_rows.append(row)
    # TOTAL row
    total_cases = len(cases_master)
    total_status = Counter()
    for c in counts.values():
        total_status.update(c)
    data_rows.append(["TOTAL", total_cases] + [total_status.get(s, 0) for s in STATUSES])
    return data_rows, headers


def build_sensitivity(
    role_master: list[dict],
    cases_master: list[dict],
) -> tuple[list[list], list[str]]:
    """Headline role counts: full 36 cases vs 31 cases (boundary-excluded)."""
    full = defaultdict(Counter)
    exc = defaultdict(Counter)
    for row in role_master:
        full[row["role_label"]][row["status_in_case"]] += 1
        if row["case_id"] not in BOUNDARY_CASE_IDS:
            exc[row["role_label"]][row["status_in_case"]] += 1
    # For each headline role show robust/conditional/transformed/shrinking/split
    display_statuses = ["robust", "conditional", "transformed", "shrinking", "split_pressure"]
    headers = ["role_label", "cases_in_scope"] + [
        h for s in display_statuses for h in (f"{s}_all", f"{s}_excl", f"{s}_Δ")
    ]
    data_rows = []
    for role in HEADLINE_ROLES:
        row = [role, "36 → 31"]
        for s in display_statuses:
            a = full[role].get(s, 0)
            e = exc[role].get(s, 0)
            row.extend([a, e, e - a])
        data_rows.append(row)
    return data_rows, headers


def compose_markdown(
    t1: tuple[list[list], list[str]],
    t2a: tuple[list[list], list[str]],
    t2b: tuple[list[list], list[str]],
    t3: tuple[list[list], list[str]],
) -> str:
    parts = ["# Manuscript Tables", ""]
    parts += ["## Table 1. Role × status counts (all 36 cases)", "", md_table(t1[1], t1[0]), ""]
    parts += [
        "## Table 2a. Status distribution by Case family",
        "",
        "Each cell is the count of role-rows with that status across all cases "
        "in the family (17 role rows per case × `n_cases`).",
        "",
        md_table(t2a[1], t2a[0]),
        "",
    ]
    parts += [
        "## Table 2b. Status distribution by Primary AI capability",
        "",
        "Same aggregation as Table 2a, grouped by AI-capability label instead "
        "of case family. H3 predicts more variation here across rows of "
        "Table 2a than across rows of Table 2b.",
        "",
        md_table(t2b[1], t2b[0]),
        "",
    ]
    parts += [
        "## Table 3. Sensitivity to exclusion of boundary / live-project cases",
        "",
        "Boundary cases excluded: 25 (Project APE), 26 (Project APE autonomy "
        "gradient), 32 (AI Scientist), 33 (Deep Research), 34 (AgentSociety). "
        "Columns: `_all` = full 36 cases; `_excl` = 31 cases; `_Δ` = "
        "`_excl` minus `_all`.",
        "",
        md_table(t3[1], t3[0]),
        "",
    ]
    return "\n".join(parts) + "\n"


def main() -> int:
    cases_master = read_csv(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    role_master = read_csv(PROJECT_ROOT / "06_analysis_tables" / "role_coding_master.csv")

    t1 = build_table_1(role_master)
    t2a = build_table_2(role_master, cases_master, "Case family", "case_family")
    t2b = build_table_2(role_master, cases_master, "Primary AI capability", "primary_ai_capability")
    t3 = build_sensitivity(role_master, cases_master)

    outputs_dir = PROJECT_ROOT / "10_outputs"

    # CSV backups
    for name, (rows, headers) in [
        ("p1_manuscript_table_1.csv", t1),
        ("p1_manuscript_table_2a.csv", t2a),
        ("p1_manuscript_table_2b.csv", t2b),
        ("p1_manuscript_table_sensitivity.csv", t3),
    ]:
        path = outputs_dir / name
        with path.open("w", newline="", encoding="utf-8") as h:
            writer = csv.writer(h)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"wrote {path.relative_to(PROJECT_ROOT)}")

    # Compiled markdown
    md_path = outputs_dir / "p1_manuscript_tables.md"
    md_path.write_text(compose_markdown(t1, t2a, t2b, t3), encoding="utf-8")
    print(f"wrote {md_path.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
