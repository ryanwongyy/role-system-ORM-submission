#!/usr/bin/env python3
"""
Analysis script for §6 of "From Repository to Role System" (ORM submission).

Reproduces every numeric value reported in §6:
  * Cell-level Monte-Carlo permutation p-values (family = 0.0001, capability = 0.0011)
  * Case-level Monte-Carlo permutation p-values (family = 0.57, capability = 0.31)
  * Cramér's V point estimates (V_family = 0.260, V_capability = 0.240)
  * Case-cluster bootstrap 95% CIs on V and on V_gap
  * Paired sign test on per-role V gaps (14 positive / 16 defined, p = 0.004)
  * Wilcoxon signed-rank on defined roles (W = 7, p = 0.0006)
  * High-confidence-only V gap (V_family = 0.267, V_capability = 0.205; gap = 0.062)
  * Pilot hold-out sign test (13 positive / 15 defined, p = 0.007)
  * Case-configuration count for durable-on-all-three H1 roles (12 of 36)
  * Consistency/coverage for ground-truth-rich × has-shrinking (0.857 / 0.500)
  * Holm-adjusted p-values across the six confirmatory/robustness tests

Dependencies (see requirements.txt):
  python >= 3.9
  pandas >= 2.0
  numpy >= 1.23
  scipy >= 1.10

Seeds are fixed:
  20260423 — cell-level MC permutation (family)
  20260424 — cell-level MC permutation (capability)
  20260423 — case-level MC permutation (reused seed; preserved from development)
  20260425 — case-cluster bootstrap V CIs

Inputs:
  role_coding_master.csv (612 rows; role × case coding)
  cases_master.csv       (36 cases; registry with family and capability columns)

Expected runtime: ~60 s on a 2023 laptop.

Usage:
  python scripts/section6_analysis.py \\
      --coding data/role_coding_master.csv \\
      --registry data/cases_master.csv \\
      --output analysis_output.json

Or, with default paths:
  python scripts/section6_analysis.py

Output:
  analysis_output.json — machine-readable record of every statistic reported in §6.
  Also writes a human-readable table to stdout.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

DEFAULT_CODING = Path("/Users/ryanwong/Human roles/p1_role_systems_db/06_analysis_tables/role_coding_master.csv")
DEFAULT_REGISTRY = Path("/Users/ryanwong/Human roles/p1_role_systems_db/01_registry/cases_master.csv")

# Seeds — load-bearing; do not change without updating the manuscript.
SEED_MC_CELL_FAMILY = 20260423
SEED_MC_CELL_CAPABILITY = 20260424
SEED_MC_CASE = 20260423
SEED_BOOTSTRAP = 20260425

# Inference parameters
N_PERM_CELL = 10_000
N_PERM_CASE = 5_000
N_BOOTSTRAP = 2_000

OBSERVABLE_STATUSES = {
    "robust", "conditional", "transformed", "shrinking",
    "split_pressure", "merge_pressure",
}

# For case-configuration and consistency/coverage analyses
H1_DURABLE_ROLES = [
    "Protocol and provenance architect",
    "Calibration architect",
    "Accountability and labor allocator",
]
GROUND_TRUTH_RICH_FAMILIES = {
    "Measurement & coding",
    "Evidence synthesis & corpus",
    "Reproducibility & autonomous research",
}

# Pilot cases (per manuscript §2 typology-derivation paragraph)
PILOT_CASE_IDS = {1, 2, 7, 21}


def load_data(coding_path: Path, registry_path: Path) -> pd.DataFrame:
    """Load and merge the coding and registry tables."""
    coding = pd.read_csv(coding_path)
    registry = pd.read_csv(registry_path)[
        ["Case ID", "Case family", "Primary AI capability"]
    ].rename(
        columns={
            "Case ID": "case_id",
            "Case family": "family",
            "Primary AI capability": "capability",
        }
    )
    merged = coding.merge(registry, on="case_id", how="left")
    return merged


def chi2_V(crosstab: pd.DataFrame) -> tuple[float | None, float | None]:
    """Return (chi2, Cramér's V). Returns (None, None) on a degenerate table."""
    if crosstab.size == 0 or min(crosstab.shape) < 2:
        return None, None
    try:
        chi2, _, _, _ = stats.chi2_contingency(crosstab)
    except (ValueError, ZeroDivisionError):
        return None, None
    n = crosstab.values.sum()
    if n == 0:
        return None, None
    V = float(np.sqrt(chi2 / (n * (min(crosstab.shape) - 1))))
    return float(chi2), V


def headline_stats(obs: pd.DataFrame) -> dict:
    """Cell-level χ², V, and sparseness diagnostics for family and capability."""
    ct_fam = pd.crosstab(obs["status_in_case"], obs["family"])
    ct_cap = pd.crosstab(obs["status_in_case"], obs["capability"])

    def _diag(ct):
        chi2, _, dof, expected = stats.chi2_contingency(ct)
        n = ct.values.sum()
        V = float(np.sqrt(chi2 / (n * (min(ct.shape) - 1))))
        cells_lt5 = int((expected < 5).sum())
        return {
            "chi2": round(float(chi2), 2),
            "df": int(dof),
            "V": round(V, 3),
            "n_cells_total": int(expected.size),
            "n_cells_exp_lt_5": cells_lt5,
            "pct_cells_exp_lt_5": round(100 * cells_lt5 / expected.size, 1),
        }

    return {"family": _diag(ct_fam), "capability": _diag(ct_cap)}


def mc_cell_level(obs: pd.DataFrame, grouping: str, seed: int, n_perm: int) -> float:
    """Monte-Carlo p-value at the cell level (shuffle status across all cells)."""
    ct_obs = pd.crosstab(obs["status_in_case"], obs[grouping])
    chi2_obs, _, _, _ = stats.chi2_contingency(ct_obs)
    rng = np.random.default_rng(seed)
    null_chi2 = np.zeros(n_perm)
    statuses = obs["status_in_case"].to_numpy()
    groups = obs[grouping].to_numpy()
    for i in range(n_perm):
        permuted = rng.permutation(statuses)
        ct_perm = pd.crosstab(pd.Series(permuted), pd.Series(groups))
        c, _, _, _ = stats.chi2_contingency(ct_perm)
        null_chi2[i] = c
    p = ((null_chi2 >= chi2_obs).sum() + 1) / (n_perm + 1)
    return float(p)


def mc_case_level(obs: pd.DataFrame, grouping: str, seed: int, n_perm: int) -> float:
    """Monte-Carlo p-value at the CASE level (preserves 17-cell-per-case structure;
    permutes the mapping from case_id → group label across the 36 cases).

    This is the clustering-aware version of the permutation test."""
    ct_obs = pd.crosstab(obs["status_in_case"], obs[grouping])
    chi2_obs, _, _, _ = stats.chi2_contingency(ct_obs)
    case_to_group = (
        obs.drop_duplicates("case_id").set_index("case_id")[grouping]
    )
    rng = np.random.default_rng(seed)
    null_chi2 = np.zeros(n_perm)
    for i in range(n_perm):
        perm_groups = rng.permutation(case_to_group.values)
        cid_to_group_perm = dict(zip(case_to_group.index, perm_groups))
        perm_col = obs["case_id"].map(cid_to_group_perm)
        ct_perm = pd.crosstab(obs["status_in_case"], perm_col)
        c, _, _, _ = stats.chi2_contingency(ct_perm)
        null_chi2[i] = c
    p = ((null_chi2 >= chi2_obs).sum() + 1) / (n_perm + 1)
    return float(p)


def bootstrap_V_CIs(obs: pd.DataFrame, seed: int, B: int) -> dict:
    """Case-cluster bootstrap 95% CIs for V_family, V_capability, and V_gap.

    Resamples the 36 cases with replacement (cluster bootstrap)."""
    case_ids = obs["case_id"].unique()
    by_case = {cid: obs[obs["case_id"] == cid] for cid in case_ids}
    rng = np.random.default_rng(seed)
    Vs_f, Vs_c = [], []
    for _ in range(B):
        sampled = rng.choice(case_ids, size=len(case_ids), replace=True)
        sub = pd.concat([by_case[cid] for cid in sampled], ignore_index=True)
        _, V_f = chi2_V(pd.crosstab(sub["status_in_case"], sub["family"]))
        _, V_c = chi2_V(pd.crosstab(sub["status_in_case"], sub["capability"]))
        if V_f is not None and V_c is not None and np.isfinite(V_f) and np.isfinite(V_c):
            Vs_f.append(V_f)
            Vs_c.append(V_c)
    Vs_f = np.array(Vs_f)
    Vs_c = np.array(Vs_c)
    gaps = Vs_f - Vs_c
    return {
        "V_family_CI95": [round(float(np.percentile(Vs_f, 2.5)), 3),
                          round(float(np.percentile(Vs_f, 97.5)), 3)],
        "V_capability_CI95": [round(float(np.percentile(Vs_c, 2.5)), 3),
                              round(float(np.percentile(Vs_c, 97.5)), 3)],
        "V_gap_CI95": [round(float(np.percentile(gaps, 2.5)), 3),
                       round(float(np.percentile(gaps, 97.5)), 3)],
        "P_gap_positive": round(float((gaps > 0).mean()), 3),
        "B": B,
        "successful_reps": int(len(Vs_f)),
    }


def per_role_V_table(obs: pd.DataFrame) -> pd.DataFrame:
    """V_family and V_capability for each role; rows where V is undefined are dropped."""
    rows = []
    for role, sub in obs.groupby("role_label"):
        _, V_f = chi2_V(pd.crosstab(sub["status_in_case"], sub["family"]))
        _, V_c = chi2_V(pd.crosstab(sub["status_in_case"], sub["capability"]))
        if V_f is not None and V_c is not None and np.isfinite(V_f) and np.isfinite(V_c):
            rows.append({"role": role, "V_family": V_f, "V_capability": V_c,
                         "diff": V_f - V_c})
    return pd.DataFrame(rows)


def paired_tests(per_role: pd.DataFrame) -> dict:
    """Paired sign test and Wilcoxon signed-rank on per-role V gaps."""
    pos = int((per_role["diff"] > 0).sum())
    neg = int((per_role["diff"] < 0).sum())
    n = pos + neg
    p_sign = 2 * min(stats.binom.cdf(min(pos, neg), n, 0.5),
                     1 - stats.binom.cdf(min(pos, neg) - 1, n, 0.5))
    W, p_w = stats.wilcoxon(per_role["V_family"], per_role["V_capability"],
                             alternative="two-sided")
    return {
        "n_roles_defined": len(per_role),
        "n_positive": pos,
        "n_negative": neg,
        "sign_test_p_two_sided": round(float(p_sign), 4),
        "wilcoxon_W": round(float(W), 2),
        "wilcoxon_p_two_sided": round(float(p_w), 4),
        "median_V_family": round(float(per_role["V_family"].median()), 3),
        "median_V_capability": round(float(per_role["V_capability"].median()), 3),
    }


def high_confidence_Vs(merged: pd.DataFrame) -> dict:
    """V_family and V_capability restricted to confidence == 'high'."""
    hi = merged[(merged["confidence"] == "high")
                & (merged["status_in_case"].isin(OBSERVABLE_STATUSES))]
    _, V_f = chi2_V(pd.crosstab(hi["status_in_case"], hi["family"]))
    _, V_c = chi2_V(pd.crosstab(hi["status_in_case"], hi["capability"]))
    return {
        "n_rows": int(len(hi)),
        "V_family": round(V_f, 3) if V_f is not None else None,
        "V_capability": round(V_c, 3) if V_c is not None else None,
        "V_gap": round(V_f - V_c, 3) if (V_f is not None and V_c is not None) else None,
    }


def pilot_holdout(merged: pd.DataFrame) -> dict:
    """Sign test and aggregate Vs on the 32 non-pilot cases."""
    holdout = merged[~merged["case_id"].isin(PILOT_CASE_IDS)]
    obs_h = holdout[holdout["status_in_case"].isin(OBSERVABLE_STATUSES)]
    per_role = per_role_V_table(obs_h)
    pt = paired_tests(per_role)
    ct_fam = pd.crosstab(obs_h["status_in_case"], obs_h["family"])
    ct_cap = pd.crosstab(obs_h["status_in_case"], obs_h["capability"])
    _, V_f = chi2_V(ct_fam)
    _, V_c = chi2_V(ct_cap)
    return {
        "n_cases": 36 - len(PILOT_CASE_IDS),
        "n_obs_rows": int(len(obs_h)),
        "V_family": round(V_f, 3),
        "V_capability": round(V_c, 3),
        "V_gap": round(V_f - V_c, 3),
        "paired_tests": pt,
    }


def case_configuration_analysis(merged: pd.DataFrame) -> dict:
    """Case-level configuration on the three H1 durable roles."""
    sub = merged[merged["role_label"].isin(H1_DURABLE_ROLES)]
    pivot = sub.pivot_table(
        index="case_id", columns="role_label", values="status_in_case",
        aggfunc="first",
    )

    def collapse(s):
        if pd.isna(s):
            return "na"
        if s in ("robust", "conditional", "transformed"):
            return "durable"
        if s == "shrinking":
            return "shrink"
        if s in ("split_pressure", "merge_pressure"):
            return "pressure"
        return "na"

    pc = pivot.map(collapse)
    config_series = pc.apply(lambda row: "|".join(row.values), axis=1)
    counts = config_series.value_counts().to_dict()
    all_durable = int(((pc == "durable").all(axis=1)).sum())
    two_durable = int(((pc == "durable").sum(axis=1) >= 2).sum())
    return {
        "all_three_durable": all_durable,
        "at_least_two_durable": two_durable,
        "top_configurations": {k: int(v) for k, v in list(counts.items())[:5]},
    }


def consistency_coverage(merged: pd.DataFrame) -> dict:
    """QCA-style set-theoretic measures for ground-truth-rich → shrinking."""
    gt_rich_cases = set(
        merged[merged["family"].isin(GROUND_TRUTH_RICH_FAMILIES)]["case_id"]
    )
    shrink_cases = set(
        merged[(merged["role_group"] == "shrinking_task_cluster")
               & (merged["status_in_case"] == "shrinking")]["case_id"]
    )
    gt_and_shrink = len(gt_rich_cases & shrink_cases)
    return {
        "n_ground_truth_rich_cases": len(gt_rich_cases),
        "n_shrinking_cases": len(shrink_cases),
        "n_both": gt_and_shrink,
        "sufficiency_gt_for_shrink": round(gt_and_shrink / len(gt_rich_cases), 3),
        "necessity_gt_for_shrink": round(gt_and_shrink / len(shrink_cases), 3),
    }


def holm_correction(p_values: dict) -> dict:
    """Holm step-down correction across the family-wise p-values in §6."""
    sorted_ps = sorted(p_values.items(), key=lambda kv: kv[1])
    m = len(sorted_ps)
    adjusted = {}
    for i, (name, p) in enumerate(sorted_ps):
        adj = min(1.0, p * (m - i))
        adjusted[name] = round(adj, 4)
    return adjusted


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--coding", type=Path, default=DEFAULT_CODING)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--output", type=Path, default=Path("analysis_output.json"))
    parser.add_argument("--n-perm-cell", type=int, default=N_PERM_CELL)
    parser.add_argument("--n-perm-case", type=int, default=N_PERM_CASE)
    parser.add_argument("--n-bootstrap", type=int, default=N_BOOTSTRAP)
    args = parser.parse_args()

    print(f"Loading {args.coding}", file=sys.stderr)
    merged = load_data(args.coding, args.registry)
    obs = merged[merged["status_in_case"].isin(OBSERVABLE_STATUSES)].copy()
    print(f"  Merged rows: {len(merged)}   Observable-status rows: {len(obs)}",
          file=sys.stderr)

    results = {}

    print("Computing headline χ² and V …", file=sys.stderr)
    results["headline"] = headline_stats(obs)

    print(f"Cell-level MC permutation (n={args.n_perm_cell}, seeds={SEED_MC_CELL_FAMILY}/{SEED_MC_CELL_CAPABILITY}) …", file=sys.stderr)
    results["mc_cell_level"] = {
        "family_p": round(mc_cell_level(obs, "family",
                                        SEED_MC_CELL_FAMILY, args.n_perm_cell), 5),
        "capability_p": round(mc_cell_level(obs, "capability",
                                            SEED_MC_CELL_CAPABILITY, args.n_perm_cell), 5),
        "n_perm": args.n_perm_cell,
    }

    print(f"Case-level MC permutation (n={args.n_perm_case}, seed={SEED_MC_CASE}) …", file=sys.stderr)
    results["mc_case_level"] = {
        "family_p": round(mc_case_level(obs, "family",
                                        SEED_MC_CASE, args.n_perm_case), 4),
        "capability_p": round(mc_case_level(obs, "capability",
                                            SEED_MC_CASE + 1, args.n_perm_case), 4),
        "n_perm": args.n_perm_case,
    }

    print(f"Case-cluster bootstrap V CIs (B={args.n_bootstrap}, seed={SEED_BOOTSTRAP}) …", file=sys.stderr)
    results["bootstrap_V_CIs"] = bootstrap_V_CIs(obs, SEED_BOOTSTRAP, args.n_bootstrap)

    print("Per-role V table and paired tests …", file=sys.stderr)
    per_role = per_role_V_table(obs)
    results["per_role_V_table"] = [
        {"role": r["role"],
         "V_family": round(r["V_family"], 3),
         "V_capability": round(r["V_capability"], 3),
         "diff": round(r["diff"], 3)}
        for _, r in per_role.iterrows()
    ]
    results["paired_tests"] = paired_tests(per_role)

    print("High-confidence-only Vs …", file=sys.stderr)
    results["high_confidence_Vs"] = high_confidence_Vs(merged)

    print("Pilot hold-out (excluding cases 1/2/7/21) …", file=sys.stderr)
    results["pilot_holdout"] = pilot_holdout(merged)

    print("Case-configuration on H1 durable roles …", file=sys.stderr)
    results["case_configuration"] = case_configuration_analysis(merged)

    print("Consistency / coverage for H2 ground-truth claim …", file=sys.stderr)
    results["consistency_coverage"] = consistency_coverage(merged)

    print("Holm adjustment across family-wise p-values …", file=sys.stderr)
    p_values = {
        "mc_cell_family": results["mc_cell_level"]["family_p"],
        "mc_cell_capability": results["mc_cell_level"]["capability_p"],
        "mc_case_family": results["mc_case_level"]["family_p"],
        "mc_case_capability": results["mc_case_level"]["capability_p"],
        "sign_test": results["paired_tests"]["sign_test_p_two_sided"],
        "wilcoxon": results["paired_tests"]["wilcoxon_p_two_sided"],
    }
    results["holm_adjusted_p"] = holm_correction(p_values)

    results["seeds"] = {
        "mc_cell_family": SEED_MC_CELL_FAMILY,
        "mc_cell_capability": SEED_MC_CELL_CAPABILITY,
        "mc_case": SEED_MC_CASE,
        "bootstrap": SEED_BOOTSTRAP,
    }

    args.output.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nWrote {args.output}", file=sys.stderr)

    # Human-readable summary to stdout
    print("\n=== §6 ANALYSIS OUTPUT ===\n")
    print(f"Cell-level χ²: family = {results['headline']['family']['chi2']:.2f} "
          f"(df={results['headline']['family']['df']}, V={results['headline']['family']['V']:.3f})")
    print(f"                capability = {results['headline']['capability']['chi2']:.2f} "
          f"(df={results['headline']['capability']['df']}, V={results['headline']['capability']['V']:.3f})")
    print(f"Sparse cells (expected < 5): family {results['headline']['family']['n_cells_exp_lt_5']}/{results['headline']['family']['n_cells_total']}, "
          f"capability {results['headline']['capability']['n_cells_exp_lt_5']}/{results['headline']['capability']['n_cells_total']}")
    print()
    print(f"Cell-level MC p:  family = {results['mc_cell_level']['family_p']:.5f}  "
          f"capability = {results['mc_cell_level']['capability_p']:.5f}")
    print(f"Case-level MC p:  family = {results['mc_case_level']['family_p']:.4f}  "
          f"capability = {results['mc_case_level']['capability_p']:.4f}  [NULL]")
    print()
    print(f"Bootstrap V_family 95% CI: {results['bootstrap_V_CIs']['V_family_CI95']}")
    print(f"Bootstrap V_capability 95% CI: {results['bootstrap_V_CIs']['V_capability_CI95']}")
    print(f"Bootstrap V_gap 95% CI: {results['bootstrap_V_CIs']['V_gap_CI95']}  "
          f"P(gap > 0) = {results['bootstrap_V_CIs']['P_gap_positive']}")
    print()
    pt = results["paired_tests"]
    print(f"Paired sign test (n={pt['n_roles_defined']}): {pt['n_positive']} positive / "
          f"{pt['n_negative']} negative; p = {pt['sign_test_p_two_sided']:.4f}")
    print(f"Wilcoxon signed-rank: W = {pt['wilcoxon_W']:.1f}, p = {pt['wilcoxon_p_two_sided']:.4f}")
    print(f"Median V_family = {pt['median_V_family']:.3f}, median V_capability = {pt['median_V_capability']:.3f}")
    print()
    hc = results["high_confidence_Vs"]
    print(f"High-confidence-only (n={hc['n_rows']}): V_family = {hc['V_family']}, "
          f"V_capability = {hc['V_capability']}, gap = {hc['V_gap']}")
    print()
    ph = results["pilot_holdout"]
    print(f"Pilot hold-out ({ph['n_cases']} cases, {ph['n_obs_rows']} obs): "
          f"{ph['paired_tests']['n_positive']}/{ph['paired_tests']['n_roles_defined']} positive, "
          f"sign-test p = {ph['paired_tests']['sign_test_p_two_sided']:.4f}")
    print(f"  V_family = {ph['V_family']}, V_capability = {ph['V_capability']}, gap = {ph['V_gap']}")
    print()
    cc = results["case_configuration"]
    print(f"Case configuration: {cc['all_three_durable']} cases durable on all three H1 roles; "
          f"{cc['at_least_two_durable']} cases durable on ≥2")
    print()
    conco = results["consistency_coverage"]
    print(f"Ground-truth-rich × shrinking: sufficiency = {conco['sufficiency_gt_for_shrink']:.3f}, "
          f"necessity = {conco['necessity_gt_for_shrink']:.3f}")
    print()
    print("Holm-adjusted p-values (family of 6 tests):")
    for name, p in sorted(results["holm_adjusted_p"].items(), key=lambda kv: kv[1]):
        print(f"  {name}: {p}")


if __name__ == "__main__":
    main()
