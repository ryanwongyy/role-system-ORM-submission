# Appendix G — Computational text-analysis triangulation of the role-coding rubric

This appendix reports a computational text-analysis pass that runs unsupervised topic / sentence-cluster discovery on the case-file corpus and asks whether the clusters that emerge inductively converge with the human-coded role-status rubric used in the main manuscript. The analysis is **convergent-validity evidence only** — the rubric remains the primary inferential apparatus; the computational layer is corroborative.

## G.1 Method

**Corpus.** Cleaned per-case text from `04_extracted_text_cleaned/<slug>/*.txt`, produced by the deterministic boilerplate-cleaning pass in `09_scripts/clean_extracted_text.py` (strips arxiv landing-page chrome, Cloudflare-challenge text, standalone URLs/IDs) and (for thin cases) the BeautifulSoup re-extraction pass in `09_scripts/reextract_thin_cases.py`. Final cleaned-corpus size: 60 files, ~258,000 tokens, distributed across 36 cases. One case (Case 23) remains thin at ~570 tokens because only the arxiv abstract page was retrievable at build time; this thinness is flagged in the pre-registration. The two duplicate-primary-URL pairs (Cases 11/12 and 23/36) are stratified — not deduped — so that the C3 analytical-framing-distinctness criterion (manuscript §2.1) is preserved at the corpus level.

**Sentence segmentation.** Split on `[.!?]+\s+` followed by a capital letter; minimum 30 characters per retained sentence. Total: **10,185 sentences**.

**Embedding model.** `sentence-transformers/all-MiniLM-L6-v2`, 384-dim, L2-normalized. Locally runnable, deterministic; seed = 20260502 throughout.

**Clustering pipeline.** Following the BERTopic-lineage practice (Hannigan et al., 2019; Berente et al., 2019), embeddings are first reduced via UMAP (384 → 10 dim, n_neighbors = 15, min_dist = 0.0, cosine metric) and then clustered via HDBSCAN (min_cluster_size = 30, min_samples = 5, excess-of-mass selection). These v0.2 parameters are pre-committed in `30_reviews/OSF_preregistration_computational.md` §3 with explicit documentation of the v0.1 calibration baseline (HDBSCAN-on-raw-embeddings produced 345 clusters / 64.7% noise, motivating the v0.2 UMAP step). Both v0.1 and v0.2 outputs are committed to the release artifacts.

**Secondary topic-modeling method.** Paragraph-chunk Latent Dirichlet Allocation (CountVectorizer with English + arxiv stopwords, 1–2 grams, max_df=0.7, min_df=5; LDA k searched in [4, 15] with k=10 chosen per the pre-registered interpretability-balanced rule). 567 paragraph chunks; topics in `06_analysis_tables/lda_topics_k10.csv`.

**Triangulation against the human-coded gold standard.** Each of the 144 evidence extracts in `evidence_extracts_master.csv` is independently embedded via the same model; its corpus-nearest-neighbor sentence's cluster assignment is taken as the "computational role-status proposal." Cross-tabulation against the human-assigned `status_in_case` from `role_coding_master.csv` (joined by case_id × normalized role_label) produces the convergence contingency. Role-label normalization handles the informal-to-canonical mapping documented in `09_scripts/triangulate_clusters.py`. Of the 144 extracts, 72 carry an explicit `supports_role`; after canonical-role normalization and v1.0' filter, **70 evidence extracts** form the gold-standard-triangulation set (Case 36 is excluded because it is held back as v1.1 hold-out per the manuscript §2.1 C2 criterion).

**Convergence and falsification thresholds (pre-registered).** Convergent-validity is reported as "supports" if (a) ≥1 cluster has ≥50% of its mapped evidence-extracts coded as procedural-validity-relevant (PV: protocol-and-provenance, calibration, or accountability roles in robust/transformed status), AND (b) ≥1 cluster has ≥50% of its mapped extracts coded as throughput-shrinkage (any of the three throughput roles in shrinking status), AND (c) macro-averaged precision (size-weighted modal-status share) ≥ 0.40. Failure on (a) OR (b) OR macro precision < 0.40 fires the falsification criterion and the convergent-validity claim does not stand.

## G.2 Results

**Cluster yield.** UMAP+HDBSCAN produced **93 clusters** with **2,833 noise points (27.8%)**. Cluster sizes range 30–149 sentences. Of these, 7 clusters had ≥3 evidence-extract neighbors after triangulation.

**Convergence outcome.** **The convergence test supports.** Specifically:

| Criterion | Threshold | Observed | Verdict |
|---|---|---|---|
| Procedural-validity clusters (≥50% PV) | ≥1 | **8** | ✓ |
| Throughput-shrinkage clusters (≥50% shrinking) | ≥1 | **1** | ✓ |
| Macro-averaged precision (size-weighted) | ≥0.40 | **0.539** | ✓ |
| Falsification fired | — | No | ✓ |

**The 8 procedural-validity clusters and 1 throughput-shrinkage cluster** (with one cluster — Cluster 66 — counting toward both the procedural-validity and throughput-shrinkage criteria due to its mixed evidence-extract loading) are documented with inductive names in `30_reviews/computational_cluster_interpretation_log.md`:

| Cluster | Name (inductive) | n extracts | PV-share | Cases anchored |
|---|---|---|---|---|
| 33 | AI disclosure / authorship protocols | 10 | 60% | 30 (DAISY), 29 (lab co-writing) |
| 38 | Systematic-review screening protocols | 4 | 50% | 7, 8, 27 |
| 55 | Qualitative research methodology references | 3 | 67% | 6, 16, 19, 20 |
| 79 | AI conversational interviewing | 4 | 50% | 16, 17 |
| 1 | Open-source literature-synthesis pipelines | 3 | 67% | 9, 33 |
| 8 | Tournament-style autonomous policy evaluation | 4 | 50% | 25, 26 (APE), 24 |
| 69 | Generative social simulation systems | 4 | 50% | 34 (AgentSociety), 22 |
| 66 | **Reproducibility / code-repair workflows (throughput-shrinkage)** | 4 | 50% (shrinking) | 28 (code repair), 27 |

The cluster names emerged from inductive close-reading of the top-10 most-representative sentences per cluster *before* consulting the manuscript's typology or the antecedent literature (per the pre-registration §4 protocol). After the names were committed, the post-hoc check confirmed each procedural-validity cluster's substantive content matches the rubric's protocol/calibration/accountability grouping and the throughput-shrinkage cluster matches the routine-coder shrinkage pattern §4 describes.

## G.3 Triangulation reading

The 0.539 macro precision means that, on average, when a cluster contains evidence extracts mapped to it via embedding nearest-neighbor, ~54% of those extracts share the same human-coded role-status. This is meaningfully above chance (12.5% under uniform 8-status assumptions) and above the pre-committed 0.40 convergence threshold, but is not unanimous — the rubric distinguishes role × case status pairings at finer granularity than embeddings of free text from case files can recover.

**Where computational and human codings converge.** Each of the manuscript's three procedural-validity roles (protocol-and-provenance, calibration, accountability) has at least one PV-cluster anchored on it; the throughput-shrinkage signature §4 documents (concentrated in three throughput-task roles) is mirrored by Cluster 66's reproducibility / code-repair theme. The convergence is real but coarser-grained than the rubric: clusters tend to track *case-family-by-substantive-theme* (e.g., "AI conversational interviewing across Cases 16 and 17") rather than *role-status* directly.

**Where they diverge.** The 27.8% noise rate and the 86 clusters that did not reach the ≥3-extract triangulation threshold mean that most case-file sentences are not assigned a substantive cluster; this is a known small-corpus limitation. Cluster 1's residual license-boilerplate contamination shows that the cleaning pass, while substantially reducing arxiv chrome, did not fully strip CC-license / metadata language from PDF-extracted files. A v1.1 cleaning pass with more aggressive license-language stripping is pre-committed.

## G.4 Limitations

- **Small corpus.** 10,185 sentences is on the low end for unsupervised embedding clustering; many of the 93 clusters carry few sentences and could collapse or merge under different parameter choices. The v0.2 parameters (UMAP n_components = 10, HDBSCAN min_cluster_size = 30) are pre-committed and not tuned post-hoc to maximize convergence.
- **English-only.** All cases are English-language. Non-English handling is out of scope for v1.0.
- **Embedding-model-specific.** Results depend on `sentence-transformers/all-MiniLM-L6-v2`'s induced geometry; replication with a different model (e.g., `mxbai-embed-large-v1`, `text-embedding-3-small`) is a v1.1 robustness commitment.
- **Case 23 is thin** (~570 tokens) because only the arxiv abstract page was retrievable; its cluster assignments rest on a smaller evidentiary base than other cases.
- **No human inter-rater check on the inductive cluster naming.** The naming protocol was followed by the first author alone; the pre-registration commits to a v1.1 second-rater pass on cluster naming.
- **Reverse-mapping not symmetric.** Triangulation maps evidence-extract → cluster via embedding nearest neighbor, not cluster → evidence-extract via cluster-membership probability. The asymmetry is documented in the released triangulation script.

## G.5 Reading of the result

The convergent-validity finding **supports the rubric's procedural-validity / throughput-shrinkage structural distinction at the corpus-text level**, independent of the rubric-codings used to derive that distinction. This is the strongest claim Appendix G can make: an unsupervised method, run on the case files without seeing the human codings, surfaces themes that match the manuscript's primary structural finding. It does **not** validate the κ = 0.289 inter-coder reliability (the κ failure remains a v1.0 baseline as §6.2 reports), and it does **not** elevate the rubric's claim ceiling — the §6.5 H3-bounded conclusions are unchanged. Appendix G is convergent-validity evidence; it is not a replacement for the v1.1 instrument commitments.

The manuscript's §6 will cross-reference this finding briefly; reviewers wanting to inspect the per-cluster details should consult `30_reviews/computational_cluster_interpretation_log.md` and `06_analysis_tables/triangulation_results.json` in the released artifacts.
