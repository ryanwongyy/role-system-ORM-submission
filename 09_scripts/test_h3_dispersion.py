#!/usr/bin/env python3
"""Formal test for H3: does role status depend more on Case family than on
Primary AI capability?

Computes χ² tests of independence and Cramér's V effect sizes for two
contingency tables:

  T_family     status × Case family (8 cols × 8 statuses)
  T_capability status × Primary AI capability (3 cols × 8 statuses)

Restricts to cases where the role is observable-present (status ∉
{not_applicable, unclear}), on the grounds that the H3 claim is about how
role *status among present roles* varies — the paper does not claim that
cases where a role is not applicable are evidence for or against H3.

Also reports per-role Cramér's V as a robustness check, with a warning on
the well-known sparse-contingency-table issue for per-role subtables.

Outputs:
  stdout  - readable summary
  10_outputs/p1_h3_dispersion.csv           - per-role Cramér's V
  10_outputs/p1_h3_dispersion_summary.md    - markdown summary for the paper

Reads only:
  01_registry/cases_master.csv
  06_analysis_tables/role_coding_master.csv
"""
from __future__ import annotations

import csv
import math
import sys
from collections import Counter, defaultdict
from pathlib import Path

from scipy.stats import chi2_contingency  # type: ignore

PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
sys.path.insert(0, str(PROJECT_ROOT / "09_scripts"))
from build_p1_db import ROLE_UNIVERSE  # noqa: E402

# Observable-present statuses (exclude not_applicable and unclear so the
# test is about how active statuses are distributed, not about role scope)
OBSERVABLE_STATUSES = [
    "robust", "conditional", "transformed",
    "shrinking", "split_pressure", "merge_pressure",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as h:
        return list(csv.DictReader(h))


def cramers_v(chi2: float, n: int, r: int, c: int) -> float:
    denom = n * (min(r, c) - 1)
    if denom <= 0:
        return float("nan")
    return math.sqrt(chi2 / denom)


def build_contingency(
    role_master: list[dict],
    cases_master: list[dict],
    group_field: str,
    role_filter: str | None = None,
) -> tuple[list[str], list[str], list[list[int]]]:
    case_group = {c["Case ID"]: c[group_field] for c in cases_master}
    groups = sorted(set(case_group.values()))
    statuses = OBSERVABLE_STATUSES
    table = [[0 for _ in statuses] for _ in groups]
    for r in role_master:
        if role_filter is not None and r["role_label"] != role_filter:
            continue
        status = r["status_in_case"]
        if status not in OBSERVABLE_STATUSES:
            continue
        group = case_group.get(r["case_id"])
        if group is None:
            continue
        i = groups.index(group)
        j = statuses.index(status)
        table[i][j] += 1
    return groups, statuses, table


def summarise(label: str, table: list[list[int]]) -> dict:
    # drop empty rows or columns to keep chi2_contingency happy
    row_sums = [sum(r) for r in table]
    col_sums = [sum(table[i][j] for i in range(len(table))) for j in range(len(table[0]))]
    keep_rows = [i for i, s in enumerate(row_sums) if s > 0]
    keep_cols = [j for j, s in enumerate(col_sums) if s > 0]
    if not keep_rows or not keep_cols:
        return {"label": label, "n": 0, "chi2": float("nan"), "p": float("nan"),
                "dof": 0, "cramers_v": float("nan"), "rows": 0, "cols": 0}
    compact = [[table[i][j] for j in keep_cols] for i in keep_rows]
    n = sum(sum(r) for r in compact)
    chi2, p, dof, _expected = chi2_contingency(compact)
    v = cramers_v(chi2, n, len(compact), len(compact[0]))
    return {"label": label, "n": n, "chi2": chi2, "p": p, "dof": dof,
            "cramers_v": v, "rows": len(compact), "cols": len(compact[0])}


def main() -> int:
    cases_master = read_csv(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    role_master = read_csv(PROJECT_ROOT / "06_analysis_tables" / "role_coding_master.csv")

    # ---- Aggregate tests ----
    _, _, t_family = build_contingency(role_master, cases_master, "Case family")
    _, _, t_cap = build_contingency(role_master, cases_master, "Primary AI capability")

    agg_family = summarise("case family", t_family)
    agg_cap = summarise("AI capability", t_cap)

    print("=== Aggregate χ² tests (all 17 roles, observable-present statuses only) ===")
    for s in (agg_family, agg_cap):
        print(f"  vs {s['label']:>16s}: χ²={s['chi2']:.2f}, df={s['dof']}, "
              f"p={s['p']:.2e}, Cramér's V={s['cramers_v']:.3f} "
              f"(n={s['n']}, table {s['rows']}×{s['cols']})")

    verdict = (
        f"V_family={agg_family['cramers_v']:.3f} vs "
        f"V_capability={agg_cap['cramers_v']:.3f} → "
        f"case family "
        f"{'more strongly' if agg_family['cramers_v'] > agg_cap['cramers_v'] else 'less strongly'} "
        f"associated with status."
    )
    print(f"  Verdict: {verdict}")

    # ---- Per-role Cramér's V (warn about sparsity) ----
    per_role_rows = []
    for role_label, role_group in ROLE_UNIVERSE:
        _, _, tf = build_contingency(role_master, cases_master, "Case family", role_filter=role_label)
        _, _, tc = build_contingency(role_master, cases_master, "Primary AI capability", role_filter=role_label)
        sf = summarise(f"{role_label}|family", tf)
        sc = summarise(f"{role_label}|capability", tc)
        per_role_rows.append(
            {
                "role_label": role_label,
                "role_group": role_group,
                "n_observations": sf["n"],
                "family_chi2": round(sf["chi2"], 2) if not math.isnan(sf["chi2"]) else "",
                "family_dof": sf["dof"],
                "family_cramers_v": round(sf["cramers_v"], 3) if not math.isnan(sf["cramers_v"]) else "",
                "capability_chi2": round(sc["chi2"], 2) if not math.isnan(sc["chi2"]) else "",
                "capability_dof": sc["dof"],
                "capability_cramers_v": round(sc["cramers_v"], 3) if not math.isnan(sc["cramers_v"]) else "",
            }
        )

    # Summaries across roles
    vf_values = [r["family_cramers_v"] for r in per_role_rows if isinstance(r["family_cramers_v"], float)]
    vc_values = [r["capability_cramers_v"] for r in per_role_rows if isinstance(r["capability_cramers_v"], float)]

    def median(xs: list[float]) -> float:
        xs = sorted(xs)
        n = len(xs)
        return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2

    def mean(xs: list[float]) -> float:
        return sum(xs) / len(xs) if xs else float("nan")

    stronger_family = sum(1 for r in per_role_rows
                          if isinstance(r["family_cramers_v"], float)
                          and isinstance(r["capability_cramers_v"], float)
                          and r["family_cramers_v"] > r["capability_cramers_v"])
    stronger_cap = sum(1 for r in per_role_rows
                       if isinstance(r["family_cramers_v"], float)
                       and isinstance(r["capability_cramers_v"], float)
                       and r["family_cramers_v"] < r["capability_cramers_v"])

    print()
    print("=== Per-role Cramér's V (warning: some per-role subtables are sparse) ===")
    print(f"  n roles with computable V: {len(vf_values)} of {len(per_role_rows)}")
    print(f"  V_family       median={median(vf_values):.3f}  mean={mean(vf_values):.3f}  "
          f"min={min(vf_values):.3f}  max={max(vf_values):.3f}")
    print(f"  V_capability   median={median(vc_values):.3f}  mean={mean(vc_values):.3f}  "
          f"min={min(vc_values):.3f}  max={max(vc_values):.3f}")
    print(f"  Roles where V_family > V_capability: {stronger_family} of {len(per_role_rows)}")
    print(f"  Roles where V_family < V_capability: {stronger_cap} of {len(per_role_rows)}")

    # ---- Outputs ----
    outputs = PROJECT_ROOT / "10_outputs"
    per_role_csv = outputs / "p1_h3_dispersion.csv"
    with per_role_csv.open("w", newline="", encoding="utf-8") as h:
        fields = ["role_label", "role_group", "n_observations",
                  "family_chi2", "family_dof", "family_cramers_v",
                  "capability_chi2", "capability_dof", "capability_cramers_v"]
        w = csv.DictWriter(h, fieldnames=fields)
        w.writeheader()
        for r in per_role_rows:
            w.writerow(r)
    print(f"wrote {per_role_csv.relative_to(PROJECT_ROOT)}")

    summary_md = outputs / "p1_h3_dispersion_summary.md"
    summary_md.write_text(
        f"""# H3 dispersion — formal test

Contingency tables built from `role_coding_master.csv` × `cases_master.csv`,
restricted to observable-present statuses (`robust`, `conditional`,
`transformed`, `shrinking`, `split_pressure`, `merge_pressure`). Statuses
`not_applicable` and `unclear` are excluded so the test is about how
active role statuses distribute, not about scope.

## Aggregate χ² tests (all 17 roles pooled)

| Grouping | χ² | df | p | Cramér's V | n |
|---|---:|---:|---:|---:|---:|
| Case family | {agg_family['chi2']:.2f} | {agg_family['dof']} | {agg_family['p']:.2e} | **{agg_family['cramers_v']:.3f}** | {agg_family['n']} |
| AI capability | {agg_cap['chi2']:.2f} | {agg_cap['dof']} | {agg_cap['p']:.2e} | **{agg_cap['cramers_v']:.3f}** | {agg_cap['n']} |

**Verdict:** {verdict}

## Per-role Cramér's V (descriptive)

- Roles with computable V on both groupings: {len(vf_values)} of {len(per_role_rows)}
- V_family: median {median(vf_values):.3f}, mean {mean(vf_values):.3f}, range [{min(vf_values):.3f}, {max(vf_values):.3f}]
- V_capability: median {median(vc_values):.3f}, mean {mean(vc_values):.3f}, range [{min(vc_values):.3f}, {max(vc_values):.3f}]
- V_family > V_capability in **{stronger_family}** of 17 roles; V_family < V_capability in **{stronger_cap}**.

Per-role χ² p-values are unreliable because of sparse cells (expected
counts below 5 in many cells of the per-role subtables). Treat per-role
V as a robustness descriptive only; rely on the aggregate test above for
the H3 verdict.
""",
        encoding="utf-8",
    )
    print(f"wrote {summary_md.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
