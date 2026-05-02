"""UMAP + HDBSCAN clustering on sentence embeddings (Strategy 5 / Appendix G primary method).

Reads:  06_analysis_tables/sentence_embeddings.npy
        06_analysis_tables/sentence_corpus.csv
Writes: 06_analysis_tables/sentence_clusters.csv (sentence_id → cluster_id)
        06_analysis_tables/case_topic_distributions.csv (case_id × cluster_id counts)
        06_analysis_tables/umap_2d_for_viz.npy (2D UMAP for figure)

Pipeline (v0.2, per pre-registration §3):
1. UMAP reduce 384 → 10 dim (n_neighbors=15, min_dist=0.0, metric=cosine, seed=20260502)
2. HDBSCAN cluster on reduced (min_cluster_size=30, min_samples=5, eom)
3. Also produce a 2D UMAP for visualization in Appendix G figure

Calibration baseline (v0.1, for reference): HDBSCAN(min_cluster_size=5, min_samples=3,
no UMAP) on the 384-dim space produced 345 clusters / 64.7% noise — the v0.2
parameters address this calibration gap.
"""
from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
import umap
from sklearn.cluster import HDBSCAN

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
EMB_PATH = ROOT / "06_analysis_tables/sentence_embeddings.npy"
CORPUS_PATH = ROOT / "06_analysis_tables/sentence_corpus.csv"
OUT_CLUSTERS = ROOT / "06_analysis_tables/sentence_clusters.csv"
OUT_CASE_DIST = ROOT / "06_analysis_tables/case_topic_distributions.csv"
OUT_UMAP_2D = ROOT / "06_analysis_tables/umap_2d_for_viz.npy"

SEED = 20260502


def main() -> None:
    np.random.seed(SEED)

    embeddings = np.load(EMB_PATH)
    print(f"Loaded embeddings: {embeddings.shape}")

    sentence_meta = []
    with open(CORPUS_PATH) as f:
        for row in csv.DictReader(f):
            sentence_meta.append({
                "sentence_id": int(row["sentence_id"]),
                "case_id": row["case_id"],
                "source_file": row["source_file"],
                "text": row["text"],
            })
    assert len(sentence_meta) == embeddings.shape[0]

    print("Running UMAP (384 → 10 dim, n_neighbors=15, min_dist=0.0, cosine, seed=20260502)...")
    reducer = umap.UMAP(
        n_components=10,
        n_neighbors=15,
        min_dist=0.0,
        metric="cosine",
        random_state=SEED,
    )
    reduced = reducer.fit_transform(embeddings)
    print(f"UMAP-reduced: {reduced.shape}")

    # Also compute 2D UMAP for figure
    print("Computing 2D UMAP for visualization...")
    reducer_2d = umap.UMAP(
        n_components=2,
        n_neighbors=15,
        min_dist=0.1,
        metric="cosine",
        random_state=SEED,
    )
    reduced_2d = reducer_2d.fit_transform(embeddings)
    np.save(OUT_UMAP_2D, reduced_2d.astype(np.float32))
    print(f"Saved 2D UMAP: {OUT_UMAP_2D}")

    print("Running HDBSCAN (min_cluster_size=30, min_samples=5, eom)...")
    clusterer = HDBSCAN(
        min_cluster_size=30,
        min_samples=5,
        cluster_selection_method="eom",
        metric="euclidean",
        alpha=1.0,
    )
    labels = clusterer.fit_predict(reduced)
    probs = clusterer.probabilities_

    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise = int((labels == -1).sum())
    print(f"\nClusters discovered: {n_clusters}")
    print(f"Noise points (label=-1): {n_noise} ({n_noise/len(labels)*100:.1f}%)")

    cluster_sizes = Counter(labels)
    print(f"\nCluster sizes (sorted descending):")
    for cid, n in sorted(cluster_sizes.items(), key=lambda x: -x[1]):
        print(f"  cluster {cid:>3}: {n:>4} sentences")

    # Save sentence-level cluster assignments
    with open(OUT_CLUSTERS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["sentence_id", "case_id", "cluster_id", "membership_prob", "text"])
        w.writeheader()
        for i, meta in enumerate(sentence_meta):
            w.writerow({
                "sentence_id": meta["sentence_id"],
                "case_id": meta["case_id"],
                "cluster_id": int(labels[i]),
                "membership_prob": round(float(probs[i]), 4),
                "text": meta["text"][:300],
            })
    print(f"\nSaved: {OUT_CLUSTERS}")

    # Per-case topic distribution
    case_dist = defaultdict(Counter)
    for i, meta in enumerate(sentence_meta):
        case_dist[meta["case_id"]][int(labels[i])] += 1

    sorted_cluster_ids = sorted(set(labels))
    with open(OUT_CASE_DIST, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["case_id"] + [f"cluster_{cid}" for cid in sorted_cluster_ids]
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for case_id in sorted(case_dist.keys(), key=lambda x: int(x) if x.isdigit() else 999):
            row = {"case_id": case_id}
            for cid in sorted_cluster_ids:
                row[f"cluster_{cid}"] = case_dist[case_id][cid]
            w.writerow(row)
    print(f"Saved: {OUT_CASE_DIST}")


if __name__ == "__main__":
    main()
