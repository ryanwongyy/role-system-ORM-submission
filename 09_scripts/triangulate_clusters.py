"""Triangulate computational clusters against the 144 evidence extracts (Strategy 5 / Appendix G).

Reads:  06_analysis_tables/sentence_corpus.csv
        06_analysis_tables/sentence_embeddings.npy
        06_analysis_tables/sentence_clusters.csv
        06_analysis_tables/evidence_extracts_master.csv
        06_analysis_tables/role_coding_master.csv
        01_registry/cases_master.csv
Writes: 06_analysis_tables/triangulation_results.json

Method (per pre-registration §5):
1. For each of 144 evidence extracts, compute embedding via the same pipeline
2. Find the corpus-sentence with maximum cosine similarity (nearest neighbor)
3. Use that nearest sentence's cluster as the "computational assignment"
4. Cross-tabulate against the human-coded role-status from role_coding_master.csv
5. Compute per-cluster precision (% extracts in cluster sharing modal status)
6. Compute per-status recall (% extracts of status X in their modal cluster)
7. Test falsification criteria (procedural-validity vs throughput-shrinkage clusters)
"""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
EMB_PATH = ROOT / "06_analysis_tables/sentence_embeddings.npy"
CORPUS_PATH = ROOT / "06_analysis_tables/sentence_corpus.csv"
CLUSTERS_PATH = ROOT / "06_analysis_tables/sentence_clusters.csv"
EVIDENCE_PATH = ROOT / "06_analysis_tables/evidence_extracts_master.csv"
ROLE_CODING_PATH = ROOT / "06_analysis_tables/role_coding_master.csv"
CASE_REGISTRY = ROOT / "01_registry/cases_master.csv"
OUT_PATH = ROOT / "06_analysis_tables/triangulation_results.json"

PROCEDURAL_VALIDITY_ROLES = {
    "Protocol and provenance architect",
    "Calibration architect",
    "Accountability and labor allocator",
}
THROUGHPUT_ROLES = {
    "Routine first-pass screener",
    "Routine coder on high-consensus, ground-truth-rich tasks",
    "Structural prose polisher / drafter",
}

# Map informal supports_role labels (semicolon-separated, mixed case, abbreviated)
# to canonical role_label values from role_coding_master.csv
ROLE_ALIASES = {
    "protocol architect": "Protocol and provenance architect",
    "shrinking routine coder": "Routine coder on high-consensus, ground-truth-rich tasks",
    "shrinking first-pass screener": "Routine first-pass screener",
    "shrinking structural prose polisher": "Structural prose polisher / drafter",
    "shrinking routine repair labor": "Routine coder on high-consensus, ground-truth-rich tasks",
    "first-pass screener": "Routine first-pass screener",
    "routine coder": "Routine coder on high-consensus, ground-truth-rich tasks",
    "structural prose polisher": "Structural prose polisher / drafter",
}


def normalize_role(piece: str, canonical_roles: set) -> str | None:
    """Map an informal role-label piece to a canonical role_label.

    Returns None if no canonical match found.
    """
    s = piece.strip()
    # Build case-insensitive lookup
    lc_to_canonical = {r.lower(): r for r in canonical_roles}

    # 1) Exact match (case-insensitive)
    if s.lower() in lc_to_canonical:
        return lc_to_canonical[s.lower()]

    # 2) Alias map
    if s.lower() in ROLE_ALIASES:
        return ROLE_ALIASES[s.lower()]

    # 3) Substring match: piece is a substring of canonical
    s_lc = s.lower()
    for canonical_lc, canonical in lc_to_canonical.items():
        if s_lc in canonical_lc or canonical_lc in s_lc:
            return canonical

    return None


def main() -> None:
    # Load corpus + embeddings + clusters
    embeddings = np.load(EMB_PATH).astype(np.float32)
    print(f"Loaded {embeddings.shape[0]} corpus sentence embeddings")

    sentence_meta = []
    with open(CORPUS_PATH) as f:
        for row in csv.DictReader(f):
            sentence_meta.append(row)

    cluster_for_sentence = {}
    with open(CLUSTERS_PATH) as f:
        for row in csv.DictReader(f):
            cluster_for_sentence[int(row["sentence_id"])] = int(row["cluster_id"])

    # Load evidence extracts: case_id, role_label, evidence text, observable, status
    print(f"Loading evidence extracts...")
    evidence = []
    with open(EVIDENCE_PATH) as f:
        for row in csv.DictReader(f):
            evidence.append(row)
    print(f"  {len(evidence)} extracts loaded; columns: {list(evidence[0].keys())[:8]}")

    # Need to map evidence to (case_id, role_label) → role_coding row to get the human status
    coding = {}  # (case_id, role_label) → status
    with open(ROLE_CODING_PATH) as f:
        for row in csv.DictReader(f):
            coding[(row["case_id"], row["role_label"])] = row["status_in_case"]

    # v1.0' filter: exclude Case 36
    v1_0_cases = set()
    with open(CASE_REGISTRY) as f:
        for row in csv.DictReader(f):
            if row["analysis_ready"] == "yes":
                v1_0_cases.add(row["Case ID"])

    # Filter to only extracts that link to a specific role (supports_role column).
    # Drop extracts where supports_role is empty (those are general evidence, not role-specific).
    evidence = [r for r in evidence if r.get("supports_role")]
    print(f"  After filtering to role-linked extracts: {len(evidence)} extracts")

    # Embed each evidence extract using the same model.
    # The schema-correct text column is 'text_excerpt_or_paraphrase'.
    print("Embedding evidence extracts...")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    extract_texts = [r["text_excerpt_or_paraphrase"] for r in evidence]
    print(f"  Sample extract: {extract_texts[0][:120]}...")

    extract_embeddings = model.encode(
        extract_texts,
        batch_size=64,
        show_progress_bar=False,
        convert_to_numpy=True,
        normalize_embeddings=True,
    ).astype(np.float32)
    print(f"  evidence embeddings: {extract_embeddings.shape}")

    # For each evidence extract, find nearest corpus sentence
    print("Computing nearest-neighbor assignments...")
    similarities = extract_embeddings @ embeddings.T  # (144, ~10185)
    nearest_sentence_ids = similarities.argmax(axis=1)

    # Build triangulation rows: split semicolon-separated supports_role into
    # one row per canonical role match. Drop pieces that don't normalize.
    canonical_role_set = {r["role_label"] for r in csv.DictReader(open(ROLE_CODING_PATH))}
    triangulation = []
    for i, ev in enumerate(evidence):
        case_id = ev.get("case_id", "?")
        supports = ev.get("supports_role", "")
        # Get computational cluster from nearest sentence
        nearest_id = int(nearest_sentence_ids[i])
        cluster_id = cluster_for_sentence.get(nearest_id, -999)
        sim = float(similarities[i, nearest_id])
        for piece in supports.split(";"):
            canonical = normalize_role(piece, canonical_role_set)
            if canonical is None:
                continue
            human_status = coding.get((case_id, canonical), "unknown")
            triangulation.append({
                "evidence_idx": i,
                "case_id": case_id,
                "role_label_raw": piece.strip(),
                "role_label": canonical,
                "human_status": human_status,
                "nearest_sentence_id": nearest_id,
                "cluster_id": cluster_id,
                "similarity": round(sim, 4),
                "in_v1_0": case_id in v1_0_cases,
            })

    # Per-cluster role-status distribution (v1.0' only)
    cluster_to_statuses = defaultdict(Counter)
    cluster_to_roles = defaultdict(Counter)
    for t in triangulation:
        if not t["in_v1_0"]:
            continue
        cluster_to_statuses[t["cluster_id"]][t["human_status"]] += 1
        cluster_to_roles[t["cluster_id"]][t["role_label"]] += 1

    # Per-cluster precision: of evidence extracts in this cluster, what % share modal status
    cluster_precision = {}
    for cid, status_counter in cluster_to_statuses.items():
        total = sum(status_counter.values())
        if total >= 3:  # only report clusters with ≥3 evidence extracts
            modal_status, modal_count = status_counter.most_common(1)[0]
            cluster_precision[cid] = {
                "n_extracts": total,
                "modal_status": modal_status,
                "modal_share": round(modal_count / total, 4),
                "status_distribution": dict(status_counter),
                "top_roles": dict(cluster_to_roles[cid].most_common(3)),
            }

    # Per-status recall: of evidence extracts with status X, what % are in the same modal cluster
    status_to_clusters = defaultdict(Counter)
    for t in triangulation:
        if not t["in_v1_0"]:
            continue
        status_to_clusters[t["human_status"]][t["cluster_id"]] += 1

    status_recall = {}
    for status, cluster_counter in status_to_clusters.items():
        total = sum(cluster_counter.values())
        if total >= 3:
            modal_cluster, modal_count = cluster_counter.most_common(1)[0]
            status_recall[status] = {
                "n_extracts": total,
                "modal_cluster": modal_cluster,
                "modal_share": round(modal_count / total, 4),
                "cluster_distribution": dict(cluster_counter),
            }

    # Falsification: do any clusters have ≥50% procedural-validity OR ≥50% throughput-shrinkage extracts?
    proc_clusters = []
    throughput_clusters = []
    for cid, status_counter in cluster_to_statuses.items():
        total = sum(status_counter.values())
        if total < 3:
            continue
        # Need to check role + status. Get extracts in this cluster
        extracts_in = [t for t in triangulation if t["cluster_id"] == cid and t["in_v1_0"]]
        # Procedural-validity: role in PROC set AND status in {robust, transformed}
        n_proc = sum(1 for t in extracts_in
                     if t["role_label"] in PROCEDURAL_VALIDITY_ROLES
                     and t["human_status"] in ("robust", "transformed"))
        # Throughput-shrinkage: role in THROUGHPUT set AND status == 'shrinking'
        n_throughput = sum(1 for t in extracts_in
                           if t["role_label"] in THROUGHPUT_ROLES
                           and t["human_status"] == "shrinking")
        if total > 0 and n_proc / total >= 0.5:
            proc_clusters.append({"cluster_id": cid, "n_proc": n_proc, "total": total, "share": round(n_proc/total, 4)})
        if total > 0 and n_throughput / total >= 0.5:
            throughput_clusters.append({"cluster_id": cid, "n_throughput": n_throughput, "total": total, "share": round(n_throughput/total, 4)})

    # Macro-averaged precision (size-weighted)
    if cluster_precision:
        total_extracts = sum(c["n_extracts"] for c in cluster_precision.values())
        macro_precision = sum(c["modal_share"] * c["n_extracts"] for c in cluster_precision.values()) / total_extracts
    else:
        macro_precision = 0.0

    # Convergence verdict per pre-registration
    convergence_supports = (
        len(proc_clusters) >= 1
        and len(throughput_clusters) >= 1
        and macro_precision >= 0.40
    )
    falsification_fired = (
        len(proc_clusters) == 0
        or len(throughput_clusters) == 0
    )

    results = {
        "n_corpus_sentences": int(embeddings.shape[0]),
        "n_evidence_extracts": len(evidence),
        "n_evidence_extracts_v1_0": sum(1 for t in triangulation if t["in_v1_0"]),
        "n_clusters_with_3plus_extracts": len(cluster_precision),
        "macro_precision": round(macro_precision, 4),
        "convergence_supports_threshold_0_40": convergence_supports,
        "falsification_fired": falsification_fired,
        "n_procedural_validity_clusters": len(proc_clusters),
        "procedural_validity_clusters": proc_clusters,
        "n_throughput_shrinkage_clusters": len(throughput_clusters),
        "throughput_shrinkage_clusters": throughput_clusters,
        "cluster_precision_by_id": cluster_precision,
        "status_recall": status_recall,
        "triangulation_per_extract": triangulation,
    }

    OUT_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved: {OUT_PATH}")
    print(f"\nHEADLINE RESULTS:")
    print(f"  Macro precision (size-weighted): {macro_precision:.3f}")
    print(f"  Convergence (≥0.40): {convergence_supports}")
    print(f"  Falsification fired: {falsification_fired}")
    print(f"  Procedural-validity clusters (≥50%): {len(proc_clusters)}")
    print(f"  Throughput-shrinkage clusters (≥50%): {len(throughput_clusters)}")


if __name__ == "__main__":
    main()
