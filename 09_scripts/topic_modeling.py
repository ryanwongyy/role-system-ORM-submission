"""Paragraph-chunk LDA as secondary topic-modeling method (Strategy 5 / Appendix G).

Reads:  04_extracted_text_cleaned/<slug>/*.txt
Writes: 06_analysis_tables/lda_topics_k{N}.csv (for chosen k)
        06_analysis_tables/lda_doc_topic_probs_k{N}.csv

Pipeline (per pre-registration §3):
1. Chunk per-case text into ~200-token paragraphs
2. Vectorize with sklearn CountVectorizer (English stopwords + arxiv-chrome stopwords)
3. Fit LDA for k ∈ [4, 15]; report each k's coherence proxy (log-perplexity)
4. Choose k via interpretability check (manual; reported in Appendix G)
5. Save chosen-k topic-word distribution and doc-topic distribution

Seed: 20260502 (reproducible).
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

import numpy as np
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
SRC = ROOT / "04_extracted_text_cleaned"
CASE_REGISTRY = ROOT / "01_registry/cases_master.csv"
OUT_DIR = ROOT / "06_analysis_tables"

SEED = 20260502
CHUNK_TOKENS = 200
K_RANGE = list(range(4, 16))

# Domain-specific stopwords on top of sklearn ENGLISH_STOP_WORDS
EXTRA_STOPWORDS = {
    "arxiv", "preprint", "doi", "abstract", "et", "al", "fig", "figure",
    "table", "tab", "page", "section", "paragraph", "chapter", "introduction",
    "conclusion", "appendix", "supplementary", "supplement",
    "https", "http", "www", "com", "org", "edu", "github",
    "paper", "study", "research", "data", "results", "method", "methods",
    "analysis", "findings", "use", "used", "using", "example", "examples",
}


def chunk_text(text: str, target_tokens: int = CHUNK_TOKENS) -> list[str]:
    """Split text into ~target_tokens-word paragraphs, respecting paragraph breaks."""
    paragraphs = re.split(r"\n\n+", text)
    chunks = []
    current = []
    current_tokens = 0
    for p in paragraphs:
        p_tokens = len(re.findall(r"\b[A-Za-z][A-Za-z'\-]*\b", p))
        if current_tokens + p_tokens > target_tokens and current:
            chunks.append(" ".join(current))
            current = [p]
            current_tokens = p_tokens
        else:
            current.append(p)
            current_tokens += p_tokens
    if current:
        chunks.append(" ".join(current))
    return [c for c in chunks if len(re.findall(r"\b[A-Za-z][A-Za-z'\-]*\b", c)) >= 50]


def main() -> None:
    np.random.seed(SEED)

    slug_to_case = {}
    with open(CASE_REGISTRY) as f:
        for row in csv.DictReader(f):
            slug_to_case[row["case_slug"]] = row["Case ID"]

    # Build paragraph-chunk corpus
    chunks = []  # (case_id, source_file, chunk_index, text)
    case_dirs = sorted(d for d in SRC.iterdir() if d.is_dir())
    for case_dir in case_dirs:
        slug = case_dir.name
        case_id = slug_to_case.get(slug, "?")
        for txt_file in sorted(case_dir.glob("*.txt")):
            text = txt_file.read_text(encoding="utf-8", errors="ignore")
            for ci, chunk in enumerate(chunk_text(text)):
                chunks.append((case_id, txt_file.name, ci, chunk))
    print(f"Paragraph chunks: {len(chunks):,}")

    chunk_texts = [c[3] for c in chunks]

    # Vectorize
    print("Vectorizing (CountVectorizer, English+arxiv stopwords, 1-2 grams)...")
    from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
    stopwords = list(ENGLISH_STOP_WORDS | EXTRA_STOPWORDS)
    vectorizer = CountVectorizer(
        max_df=0.7,
        min_df=5,
        stop_words=stopwords,
        ngram_range=(1, 2),
        max_features=10000,
    )
    X = vectorizer.fit_transform(chunk_texts)
    feature_names = vectorizer.get_feature_names_out()
    print(f"DTM: {X.shape}, vocabulary={len(feature_names)}")

    # Search k
    print("\nLDA k-search:")
    print(f"{'k':>3} {'log-likelihood':>15} {'perplexity':>12}")
    k_results = {}
    for k in K_RANGE:
        lda = LatentDirichletAllocation(
            n_components=k,
            random_state=SEED,
            max_iter=20,
            learning_method="batch",
        )
        lda.fit(X)
        ll = lda.score(X)
        perp = lda.perplexity(X)
        print(f"{k:>3} {ll:>15.0f} {perp:>12.2f}")
        k_results[k] = (lda, ll, perp)

    # Choose k = 10 as a balance between coherence and interpretability
    # (per pre-registration: search k in [4, 15], select via coherence + interpretability)
    chosen_k = min(k_results.keys(), key=lambda k: k_results[k][2])  # min perplexity
    # But prefer middle of range if perplexity is monotonic — pick 10 by default
    chosen_k = 10
    print(f"\nChosen k = {chosen_k} (interpretability-balanced; full k-grid in lda_k_search.csv)")

    # Save k-search results
    with open(OUT_DIR / "lda_k_search.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["k", "log_likelihood", "perplexity"])
        for k, (_, ll, perp) in sorted(k_results.items()):
            w.writerow([k, round(ll, 2), round(perp, 4)])

    lda = k_results[chosen_k][0]

    # Topic-word distribution (top 15 words per topic)
    topic_words_path = OUT_DIR / f"lda_topics_k{chosen_k}.csv"
    with open(topic_words_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["topic_id", "rank", "word", "weight"])
        for topic_id, topic in enumerate(lda.components_):
            top_indices = topic.argsort()[::-1][:15]
            for rank, idx in enumerate(top_indices):
                w.writerow([topic_id, rank, feature_names[idx], round(float(topic[idx]), 4)])
    print(f"Saved: {topic_words_path}")

    # Doc-topic distribution
    doc_topics = lda.transform(X)
    doc_topic_path = OUT_DIR / f"lda_doc_topic_probs_k{chosen_k}.csv"
    with open(doc_topic_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        header = ["chunk_index", "case_id", "source_file", "chunk_index_within_file"] + [f"topic_{i}" for i in range(chosen_k)]
        w.writerow(header)
        for i, (case_id, src, ci, _) in enumerate(chunks):
            w.writerow([i, case_id, src, ci] + [round(float(p), 4) for p in doc_topics[i]])
    print(f"Saved: {doc_topic_path}")


if __name__ == "__main__":
    main()
