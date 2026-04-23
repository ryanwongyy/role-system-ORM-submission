#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path
from textwrap import dedent


ALLOWED_DECISION_STATES = {"human_resolved", "deferred", "waived", "retain"}

GATE_ROLE_MAP = {
    "journal_choice_gate": {
        "required_human_role": "journal_strategy_editor",
        "fallback_role": "corresponding_author",
        "notes": "Confirms or changes the target journal and framing fit.",
    },
    "claim_ceiling_gate": {
        "required_human_role": "methods_editor",
        "fallback_role": "corresponding_author",
        "notes": "Confirms rhetorical ceiling and prevents evidence overreach.",
    },
    "role_ontology_freeze_gate": {
        "required_human_role": "methods_editor",
        "fallback_role": "corresponding_author",
        "notes": "Project-specific gate for changing or freezing the role ontology used in the manuscript.",
    },
    "boundary_autonomy_gate": {
        "required_human_role": "methods_editor",
        "fallback_role": "corresponding_author",
        "notes": "Project-specific gate for how autonomy-heavy cases are interpreted.",
    },
    "theory_novelty_gate": {
        "required_human_role": "methods_editor",
        "fallback_role": "corresponding_author",
        "notes": "Resolves novelty framing and theoretical positioning.",
    },
    "citation_inclusion_gate": {
        "required_human_role": "citation_steward",
        "fallback_role": "corresponding_author",
        "notes": "Approves the final citation list and section mapping.",
    },
    "disclosure_gate": {
        "required_human_role": "governance_reviewer",
        "fallback_role": "corresponding_author",
        "notes": "Approves AI-use disclosure wording and governance signoff.",
    },
    "submission_gate": {
        "required_human_role": "corresponding_author",
        "fallback_role": "",
        "notes": "Final human signoff before any external submission action.",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def join_blocks(*blocks: str) -> str:
    cleaned = [block.strip("\n") for block in blocks if block and block.strip()]
    return "\n\n".join(cleaned)


def default_input_path(paper_root: Path) -> Path:
    return paper_root / "30_reviews" / "human_gate_input_form.csv"


def gate_registry_path(paper_root: Path) -> Path:
    return paper_root / "30_reviews" / "gate_state_registry.csv"


def gate_decisions_path(paper_root: Path) -> Path:
    return paper_root / "30_reviews" / "gate_decisions.md"


def open_issues_path(paper_root: Path) -> Path:
    return paper_root / "40_runs" / "open_issues.md"


def resolution_log_path(paper_root: Path) -> Path:
    return paper_root / "30_reviews" / "human_gate_resolution_log.csv"


def instructions_path(paper_root: Path) -> Path:
    return paper_root / "30_reviews" / "human_gate_input_instructions.md"


def role_map_path(paper_root: Path) -> Path:
    return paper_root / "30_reviews" / "human_gate_role_map.csv"


def ingestion_report_path(paper_root: Path) -> Path:
    return paper_root / "40_runs" / "human_input_ingestion_report.md"


def render_gate_decisions(gate_rows: list[dict[str, str]]) -> str:
    lines = [
        "# Gate Decisions",
        "",
        "| Gate | Status | Decision state | Current decision | Next action |",
        "|---|---|---|---|---|",
    ]
    for row in gate_rows:
        lines.append(
            f"| {row['gate_label']} | {row['status']} | {row['decision_state']} | {row['current_decision']} | {row['next_action']} |"
        )
    return "\n".join(lines)


def render_open_issues(gate_rows: list[dict[str, str]]) -> str:
    unresolved = [row for row in gate_rows if row["decision_state"] != "human_resolved"]
    lines = ["# Open Issues", "", "## Remaining Protocol Tasks", ""]
    if unresolved:
        lines.extend([f"- {row['gate_label']}: {row['next_action']}" for row in unresolved])
    else:
        lines.append("- No unresolved protocol tasks remain.")
    lines.extend(
        [
            "",
            "## Current Blocker Summary",
            "",
            "- Human-only gate states are tracked directly in `30_reviews/gate_state_registry.csv`.",
            "- Submission remains blocked until all required human decisions are explicitly recorded.",
        ]
    )
    return "\n".join(lines)


def build_input_rows(gate_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in gate_rows:
        role_info = GATE_ROLE_MAP.get(row["gate_id"], {})
        rows.append(
            {
                "gate_id": row["gate_id"],
                "gate_label": row["gate_label"],
                "required_human_role": role_info.get("required_human_role", ""),
                "fallback_role": role_info.get("fallback_role", ""),
                "decision_state_options": "human_resolved|deferred|waived|retain",
                "current_decision_state": row["decision_state"],
                "ai_proposed_decision": row["current_decision"],
                "human_decision_state": "",
                "human_decision": "",
                "human_rationale": "",
                "human_reviewer_name": "",
                "human_reviewer_role": "",
                "human_decision_date": "",
                "next_action_override": "",
            }
        )
    return rows


def build_role_map_rows(gate_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in gate_rows:
        role_info = GATE_ROLE_MAP.get(row["gate_id"], {})
        rows.append(
            {
                "gate_id": row["gate_id"],
                "gate_label": row["gate_label"],
                "required_human_role": role_info.get("required_human_role", ""),
                "fallback_role": role_info.get("fallback_role", ""),
                "notes": role_info.get("notes", ""),
            }
        )
    return rows


def build_instructions(paper_root: Path, input_csv: Path, gate_rows: list[dict[str, str]]) -> str:
    bullet_lines = []
    for row in gate_rows:
        role_info = GATE_ROLE_MAP.get(row["gate_id"], {})
        role_label = role_info.get("required_human_role", "human reviewer")
        fallback = role_info.get("fallback_role", "")
        fallback_text = f"; fallback `{fallback}`" if fallback else ""
        bullet_lines.append(
            f"- `{row['gate_id']}`: {row['gate_label']}. Primary reviewer `{role_label}`{fallback_text}. Current state `{row['decision_state']}`."
        )
    bullets = "\n".join(bullet_lines)
    return join_blocks(
        "# Human Gate Input Instructions",
        dedent(
            f"""
            ## What this form is for

            This workspace contains manuscript gates that must remain human-resolved before the paper is treated as submission-ready. Fill in the CSV form at:

            `{input_csv}`
            """
        ).strip(),
        "## Gates in this session\n\n" + bullets,
        dedent(
            """
            ## How to use the CSV

            1. Open `human_gate_input_form.csv`.
            2. For each gate you want to resolve now, fill in:
               - `human_decision_state`
               - `human_decision`
               - `human_rationale`
               - `human_reviewer_name`
               - `human_reviewer_role`
               - `human_decision_date`
            3. Use `human_resolved`, `deferred`, `waived`, or `retain` for `human_decision_state`.
            4. Leave `retain` or blank for gates you are not updating yet.
            5. Optionally fill `next_action_override` if the default next action should change.
            """
        ).strip(),
        dedent(
            f"""
            ## Apply the human decisions

            Run:

            ```bash
            python3 "/Users/ryanwong/Human roles/p1_role_systems_db/09_scripts/ingest_human_gate_inputs.py" --paper-root "{paper_root}" --apply
            ```
            """
        ).strip(),
        dedent(
            """
            ## What the apply step updates

            - `30_reviews/gate_state_registry.csv`
            - `30_reviews/gate_decisions.md`
            - `30_reviews/human_gate_resolution_log.csv`
            - `40_runs/open_issues.md`
            - `40_runs/human_input_ingestion_report.md`

            ## Important rule

            This process records human decisions. It does not submit the paper, and it does not silently resolve any remaining gates.
            """
        ).strip(),
    )


def normalize_status(decision_state: str) -> str:
    if decision_state == "human_resolved":
        return "human_resolved"
    if decision_state in {"deferred", "waived"}:
        return decision_state
    return "open"


def init_template(paper_root: Path, input_csv: Path) -> None:
    gate_rows = read_csv(gate_registry_path(paper_root))
    input_rows = build_input_rows(gate_rows)
    write_csv(
        input_csv,
        [
            "gate_id",
            "gate_label",
            "required_human_role",
            "fallback_role",
            "decision_state_options",
            "current_decision_state",
            "ai_proposed_decision",
            "human_decision_state",
            "human_decision",
            "human_rationale",
            "human_reviewer_name",
            "human_reviewer_role",
            "human_decision_date",
            "next_action_override",
        ],
        input_rows,
    )
    write_csv(
        role_map_path(paper_root),
        ["gate_id", "gate_label", "required_human_role", "fallback_role", "notes"],
        build_role_map_rows(gate_rows),
    )
    write_text(instructions_path(paper_root), build_instructions(paper_root, input_csv, gate_rows))


def apply_updates(paper_root: Path, input_csv: Path) -> None:
    gate_rows = read_csv(gate_registry_path(paper_root))
    gate_lookup = {row["gate_id"]: row for row in gate_rows}
    input_rows = read_csv(input_csv)
    applied_rows: list[dict[str, str]] = []
    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")

    for row in input_rows:
        gate_id = row.get("gate_id", "").strip()
        decision_state = row.get("human_decision_state", "").strip()
        if not gate_id or gate_id not in gate_lookup:
            continue
        if not decision_state or decision_state == "retain":
            continue
        if decision_state not in ALLOWED_DECISION_STATES - {"retain"}:
            raise ValueError(f"Unsupported decision state for {gate_id}: {decision_state}")

        gate_row = gate_lookup[gate_id]
        previous_state = gate_row["decision_state"]
        gate_row["decision_state"] = decision_state
        gate_row["status"] = normalize_status(decision_state)
        if row.get("human_decision", "").strip():
            gate_row["current_decision"] = row["human_decision"].strip()
        if row.get("next_action_override", "").strip():
            gate_row["next_action"] = row["next_action_override"].strip()
        elif decision_state == "human_resolved":
            gate_row["next_action"] = "No further action required unless the manuscript changes materially."

        applied_rows.append(
            {
                "applied_at": timestamp,
                "gate_id": gate_id,
                "gate_label": gate_row["gate_label"],
                "previous_decision_state": previous_state,
                "new_decision_state": decision_state,
                "human_reviewer_name": row.get("human_reviewer_name", "").strip(),
                "human_reviewer_role": row.get("human_reviewer_role", "").strip(),
                "human_decision_date": row.get("human_decision_date", "").strip(),
                "human_decision": row.get("human_decision", "").strip(),
                "human_rationale": row.get("human_rationale", "").strip(),
            }
        )

    write_csv(
        gate_registry_path(paper_root),
        ["gate_id", "gate_label", "status", "decision_state", "current_decision", "next_action"],
        list(gate_lookup.values()),
    )
    write_text(gate_decisions_path(paper_root), render_gate_decisions(list(gate_lookup.values())))
    write_text(open_issues_path(paper_root), render_open_issues(list(gate_lookup.values())))

    log_path = resolution_log_path(paper_root)
    existing_logs = read_csv(log_path) if log_path.exists() else []
    existing_logs.extend(applied_rows)
    write_csv(
        log_path,
        [
            "applied_at",
            "gate_id",
            "gate_label",
            "previous_decision_state",
            "new_decision_state",
            "human_reviewer_name",
            "human_reviewer_role",
            "human_decision_date",
            "human_decision",
            "human_rationale",
        ],
        existing_logs,
    )

    unresolved = [row for row in gate_lookup.values() if row["decision_state"] != "human_resolved"]
    report_lines = [
        "# Human Input Ingestion Report",
        "",
        f"- Applied updates: {len(applied_rows)}",
        f"- Remaining unresolved gates: {len(unresolved)}",
        "",
        "## Updated gates",
        "",
    ]
    if applied_rows:
        report_lines.extend(
            [f"- {row['gate_label']}: {row['new_decision_state']} by {row['human_reviewer_name'] or 'unspecified reviewer'}" for row in applied_rows]
        )
    else:
        report_lines.append("- No updates were applied.")
    report_lines.extend(["", "## Still unresolved", ""])
    if unresolved:
        report_lines.extend([f"- {row['gate_label']}" for row in unresolved])
    else:
        report_lines.append("- None.")
    write_text(ingestion_report_path(paper_root), "\n".join(report_lines))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper-root", required=True)
    parser.add_argument("--input-csv", default="")
    parser.add_argument("--init", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    paper_root = Path(args.paper_root)
    input_csv = Path(args.input_csv) if args.input_csv else default_input_path(paper_root)

    if args.init or (not args.init and not args.apply):
        init_template(paper_root, input_csv)
    if args.apply:
        if not input_csv.exists():
            raise FileNotFoundError(f"Input CSV not found: {input_csv}")
        apply_updates(paper_root, input_csv)


if __name__ == "__main__":
    main()
