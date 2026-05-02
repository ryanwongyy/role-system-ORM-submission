# OSF Preregistration — Computational text-analysis triangulation (Strategy 5; Appendix G)

**Companion to:** `OSF_preregistration.md` (the v1.0 second-coder κ pre-analysis plan)
**Manuscript section:** Appendix G — Computational triangulation of the human role-coding rubric
**Document status at v1.0.0-ORM-submission:** **pre-analysis plan**. This document is OSF-ready and is intended to be timestamped via OSF posting **before** any computational pipeline scripts execute. The git commit history serves as the in-repository ordering proof.

---

## 1. Purpose

Strategy 5 is a computational text-analysis layer that triangulates with the manuscript's human-coded role-status rubric. The goal is convergent-validity evidence: do unsupervised topic clusters or sentence-embedding clusters extracted from the case files independently surface themes that map onto the procedural-validity / throughput-shrinkage / specification-pressure structure the rubric documents? The analysis is reported as **Appendix G** with a one-paragraph cross-reference in §6 of the main manuscript. The rubric remains the manuscript's primary inferential apparatus; the computational layer is corroborative only.

This pre-analysis plan is filed before the pipeline executes to forestall the methodological objection that computational outputs were post-hoc rationalized to fit the human-coded rubric.

## 2. Corpus construction protocol

**Source.** `04_extracted_text_cleaned/<slug>/*.txt` produced by `09_scripts/clean_extracted_text.py` and (for thin cases only) `09_scripts/reextract_thin_cases.py`. Both scripts are deterministic regex/HTML-parsing operations with no model calls.

**Boilerplate cleaning rules.** Strip arxiv landing-page chrome (navigation menus, "Skip to main content", "Donate", "Help Pages", ORCID/MSC/ACM classification labels), Cloudflare-challenge text ("Just a moment…"), standalone URL lines, standalone arxiv-ID lines. Normalize whitespace; dedupe consecutive duplicate lines. PDF-extracted files (`*_pdf.txt`) are preferred; HTML-extracted siblings are only retained when no PDF version exists.

**Re-extraction policy (thin cases).** Cases with <1,000 cleaned tokens after the primary cleaning pass are re-extracted from `03_raw_sources/<slug>/*.html` via BeautifulSoup with proper HTML parsing. Re-extracted output is saved with `_v2.txt` suffix only when the new extraction yields more tokens than the original cleaned output (otherwise the original is retained).

**Stratify-by-pair handling for duplicate primary URLs.** Cases 11/12 share `arxiv.org/abs/2601.15485`; Cases 23/36 share `arxiv.org/abs/2504.01167`. Per v43 §2.1 criterion C3 (analytical-framing distinctness), the two cases in each pair represent analytically distinct framings. **The computational pipeline preserves both copies** — we do not collapse, dedupe, or merge. Each case-level topic distribution is computed independently. Convergent computational topic profiles for paired cases would itself be a finding (the rubric over-distinguishes); divergent profiles would corroborate the C3 analytical-framing-distinctness claim.

**Non-English handling.** The current corpus is English-only. Non-English cases would require a separate embedding model and are out of scope for v1.0.

**v1.0' inferential base.** The computational pipeline operates on all 36 cases (all 595 v1.0 codings + 17 v1.1-design codings for Case 36). Triangulation against role codings is reported separately for the v1.0' base (35 cases) and the v1.1-design entry (Case 36) so that Appendix G's convergent-validity claim is not contaminated by the design-time-projection codings.

**Case 23 thinness disclosure.** Case 23 has only ~570 cleaned tokens (landing-page abstract only; full paper PDF was not retrievable at build time). The case is retained in the corpus but flagged. We pre-commit to reporting its sentence count and noting that any cluster assignment for Case 23 rests on a substantially smaller evidentiary base than other cases.

## 3. Embedding model and clustering parameters

**Sentence embedding model.** `sentence-transformers/all-MiniLM-L6-v2`, version pinned in `requirements.txt`. Locally runnable; no API key needed; deterministic output for fixed inputs and fixed model weights.

**Tokenization.** Sentence-level: split on `[\.!?]+\s+` followed by a capital letter; minimum 30 characters per retained sentence; sentences are not lowercased prior to embedding (the model handles casing).

**Random seed.** All clustering and dimensionality-reduction operations use seed `20260502`.

**Pipeline (v0.2 amendment, documented below).** Sentence embeddings → UMAP dimensionality reduction → HDBSCAN clustering on the reduced space. UMAP is the standard preprocessing step for sentence-embedding clustering (BERTopic, Top2Vec, and the Hannigan et al. 2019 / Berente et al. 2019 lineage all use this pattern). The v0.1 of this pre-registration omitted UMAP and used `min_cluster_size = 5`; an initial calibration run on the actual corpus (10,185 sentences) under v0.1 parameters produced 345 clusters with 64.7% noise — symptomatic of the well-known curse-of-dimensionality problem when running density-based clustering directly on 384-dim sentence embeddings. The v0.2 parameters below are calibrated to the realized corpus size and are committed before the v0.2 results are observed.

**UMAP parameters (v0.2):**
- `n_components = 10` (reduce 384 → 10)
- `n_neighbors = 15`
- `min_dist = 0.0`
- `metric = 'cosine'` (on the un-normalized embeddings; UMAP handles the geometry)
- `random_state = 20260502`

**HDBSCAN parameters (v0.2 amendment):**
- `min_cluster_size = 30` (≈0.3% of corpus; produces interpretable cluster counts in the 10–30 range expected for ORM-style methodological reviews)
- `min_samples = 5`
- `cluster_selection_method = 'eom'` (excess-of-mass)
- `metric = 'euclidean'` (on UMAP-reduced space)
- `alpha = 1.0`

**v0.1 parameters retained for reproducibility documentation:**
- HDBSCAN(min_cluster_size=5, min_samples=3, no UMAP) produced 345 clusters / 64.7% noise. Reported in Appendix G as the "calibration baseline" — evidence that the v0.2 parameters are not cherry-picked to give pretty results on the actual corpus.

**Secondary topic-modeling method.** Paragraph-chunk **Latent Dirichlet Allocation** via `sklearn.decomposition.LatentDirichletAllocation`. Chunks are ~200-token paragraph windows. Topic count `k` is searched in the integer range [4, 15]; the chosen k is the integer that maximizes UMass coherence subject to the interpretability check below. The chosen k is reported in Appendix G alongside the second-best k as a sensitivity check.

## 4. Inductive interpretation protocol

**Pre-commitment to inductive interpretation.** For each cluster (or LDA topic), the interpretation procedure is:

1. Identify the top-10 sentences (or paragraph chunks) by cluster-membership probability or topic-loading.
2. Read those 10 sentences in isolation (without consulting the rubric, the manuscript, or the prior literature on Abbott / Faraj-Pachidi / Autor / Raisch-Krakowski).
3. Name the cluster from what the 10 sentences share substantively. Names should be 3–7 words, descriptive rather than theoretical.
4. Record the name, the 10 sentence excerpts, and the interpretation rationale in `30_reviews/computational_cluster_interpretation_log.md`.
5. **Only after all clusters are named** consult the manuscript's typology and the antecedent literature. Anchors-literature framing in Appendix G is post-hoc; pre-existing names are NOT revised to better match Abbott/Faraj-Pachidi/Autor categories after the fact.

**HDBSCAN noise label.** Sentences assigned to cluster `-1` (HDBSCAN's noise label) are reported as a count and percentage; they are not interpreted as a "noise theme."

## 5. Triangulation against the 144 evidence extracts

**Gold standard.** `06_analysis_tables/evidence_extracts_master.csv` contains 144 evidence extracts with role-status assignments (one per quotable sentence linked to a coded (role × case) cell).

**Mapping protocol.** For each of the 144 evidence extracts, compute its sentence embedding and find the cluster (or topic) of its embedding-nearest-neighbor in the corpus. This produces a contingency table: cluster-id × role-status, with cell counts.

**Convergence metric.** For each cluster, compute the mode role-status of the evidence-extract neighbors that fall in it. Report:
- **Precision** per cluster: of evidence extracts mapped to cluster X, what fraction are coded with the modal role-status?
- **Recall** per role-status: of evidence extracts coded `robust` (or `conditional`, etc.), what fraction map to the same cluster?
- **Macro-averaged convergence score**: mean per-cluster precision weighted by cluster size.

**Falsification criteria.** The convergent-validity claim **fails** if either:
- (a) ZERO clusters have ≥50% of their evidence-extract neighbors coded with procedural-validity-related statuses (`robust` or `transformed` on protocol-and-provenance, calibration architect, or accountability-and-labor allocator), OR
- (b) ZERO clusters have ≥50% of their evidence-extract neighbors coded `shrinking` on any of the three throughput-task roles (routine first-pass screener, routine coder on high-consensus tasks, structural prose polisher).

If either falsification fires, Appendix G reports "computational analysis does not converge with the human-coded rubric" as the headline finding and the manuscript's §6 cross-reference acknowledges this honestly. The rubric is not adjusted post-hoc to chase convergence.

**Macro-averaged convergence threshold for "supports".** A macro-precision ≥ 0.40 is reported as "computational and human codings converge meaningfully." Below 0.40 is reported as "weak/no convergence."

## 6. Replication path

The full pipeline is reproducible via:

```bash
python3 09_scripts/clean_extracted_text.py
python3 09_scripts/reextract_thin_cases.py
python3 09_scripts/build_corpus.py
python3 09_scripts/embed_corpus.py
python3 09_scripts/cluster_embeddings.py
python3 09_scripts/topic_modeling.py
python3 09_scripts/triangulate_clusters.py
```

All scripts are deterministic given the pinned sentence-transformers model weights and the seed `20260502`. Outputs are committed to `06_analysis_tables/`. The cleaned corpus is committed to `04_extracted_text_cleaned/`.

## 7. Pre-registration ordering proof

The git commit history shows the pre-registration commit precedes the pipeline-execution commits. Specifically:
- This document committed at the pre-registration commit (immediately before pipeline scripts run for the first time)
- `clean_extracted_text.py`, `reextract_thin_cases.py` may be committed in the same pre-registration commit (they produced the cleaned corpus and re-extracted the thin cases — these are inputs to the pipeline)
- `build_corpus.py`, `embed_corpus.py`, `cluster_embeddings.py`, `topic_modeling.py`, `triangulate_clusters.py` and their first run-outputs are committed in a subsequent commit

The pre-registration thus precedes the analytic results commit. OSF timestamping is a recommended follow-up step for stronger external proof.

## 8. Disclosure

The first author conducted the corpus cleaning, re-extraction, and pre-registration drafting. The pipeline executes deterministically from the pre-registration's pre-committed parameters; no human-in-the-loop tuning is performed between pre-registration and Appendix G drafting.

Generative AI was used for prose editing of this preregistration document and may be used for prose editing of Appendix G itself, under the same disclosure standard adopted in §Transparency of the main manuscript. No generative AI is used to interpret cluster contents (the inductive interpretation protocol in Section 4 is human-only).

Funding: none. Competing interests: none declared.
