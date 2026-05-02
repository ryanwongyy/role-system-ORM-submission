"""Compute sentence embeddings for the cleaned corpus (Strategy 5 / Appendix G).

Reads:  06_analysis_tables/sentence_corpus.csv
Writes: 06_analysis_tables/sentence_embeddings.npy

Model:  sentence-transformers/all-MiniLM-L6-v2 (per pre-registration §3)
Seed:   20260502
Output: L2-normalized 384-dim embeddings, dtype float32

The embeddings are deterministic given fixed model weights and inputs.
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
CORPUS = ROOT / "06_analysis_tables/sentence_corpus.csv"
OUT_EMB = ROOT / "06_analysis_tables/sentence_embeddings.npy"

SEED = 20260502
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def main() -> None:
    np.random.seed(SEED)

    # Load corpus
    sentences = []
    with open(CORPUS) as f:
        for row in csv.DictReader(f):
            sentences.append(row["text"])
    print(f"Loaded {len(sentences):,} sentences from {CORPUS.name}")

    # Compute embeddings
    print(f"Loading model: {MODEL_NAME}")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(MODEL_NAME)
    print(f"Encoding... (this takes a few minutes for 10k sentences on CPU)")
    embeddings = model.encode(
        sentences,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,  # L2-normalize for cosine-equivalent euclidean
    )
    embeddings = embeddings.astype(np.float32)

    print(f"Embedding matrix: {embeddings.shape}, dtype={embeddings.dtype}")
    np.save(OUT_EMB, embeddings)
    print(f"Saved: {OUT_EMB}")


if __name__ == "__main__":
    main()
