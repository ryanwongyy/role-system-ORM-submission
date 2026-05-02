# Computational Cluster Interpretation Log (Strategy 5 / Appendix G)

**Date:** 2026-05-02
**Pre-registration:** `30_reviews/OSF_preregistration_computational.md` (committed at d4e870e, before pipeline execution)
**Pipeline outputs:** `06_analysis_tables/sentence_clusters.csv`, `triangulation_results.json`
**Interpretation protocol:** Per pre-registration §4 — read top-10 most-representative sentences per cluster, name the cluster from what those sentences share substantively, do NOT consult the manuscript's typology or anchors literature (Abbott / Faraj-Pachidi / Autor / Raisch-Krakowski) until all clusters are named.

This log documents only the clusters that triangulated against ≥3 role-linked evidence extracts (n=7 procedural-validity-relevant clusters + 2 additional themed clusters that surfaced ≥3 hits). The full HDBSCAN run produced 93 clusters from 10,185 sentences with 27.8% noise; the 86 clusters not documented here either had <3 role-linked extracts mapped to them or contained boilerplate-residue / general methods-paper text.

---

## Cluster 33 — AI disclosure / authorship protocols (10 extracts; 60% PV-coded)

**Top sentences:**
- "While relatively little design research has directly examined AI disclosure as an author-facing task, several adjacent strands of work have explored how structured disclosure artefacts shape author behavior..."
- "We discuss three types of AI disclosure challenges (i.e., social, cognitive, and emotional) identified in prior HCI and related interdisciplinary work."
- "Participants often saw AI disclosure as operating as a trust-based 'honour' system because there were no verification mechanisms."
- "To investigate the questions of how structuring the AI disclosure process shapes what authors report..."

**Inductive name.** *AI disclosure / authorship protocols.*
**Substance:** the cluster is about how authors report and disclose their use of AI in research workflows; mechanisms range from honour-system trust to structured forms (DAISY-style); covers both the disclosure design problem and the social-cognitive challenges authors face in practice. Strongly mapped to Cases 30 (DAISY) and 29 (lab manuscript co-writing).

## Cluster 38 — Systematic-review screening protocols (4 extracts; 50% PV-coded)

**Top sentences:**
- "Visual example of the inclusion decision process for a single record within each systematic review."
- "Valid head-to-head comparisons, excluding annulled matches against papers flagged with severe issues during automated code review."
- "These additional instances stemmed from previous systematic reviews conducted by our group."
- "The three systematic reviews had 8.6% (VL), 7.3% (AB), and 14.3% (COVID-19) records with a missing abstract."

**Inductive name.** *Systematic-review screening protocols.*
**Substance:** cluster captures the mechanics of inclusion/exclusion decisions in systematic reviews — admissibility rules, head-to-head comparisons, missing-data handling. Procedural and provenance-related: methodological venues' screening machinery. Mapped to Cases 7 (Baccolini), 8 (study-type triage), 27 (REPRO-Bench).

## Cluster 55 — Qualitative research methodology references (3 extracts; 67% PV-coded)

**Top sentences:**
- "Using thematic analysis in psychology."
- "The qualitative research interview."
- "The choice of a qualitative research approach by researchers depends on the theoretical tradition and research paradigm that they adhere to."

**Inductive name.** *Qualitative research methodology references.*
**Substance:** citations and citations-adjacent prose for qualitative-tradition methodology (Braun & Clarke, qualitative interviewing, paradigm choice). The cluster is heavy in reference-list-like content from cases that use qualitative methods (interviews, fieldnotes, memoing). Mapped to Cases 6 (maternal health), 16 (AI conversational interviewing), 19 (memoing), 20 (reflexive content analysis).

## Cluster 79 — AI conversational interviewing (4 extracts; 50% PV-coded)

**Top sentences:**
- "Yet, critical questions regarding the implementation remain unresolved and little is known about the relative performance compared with human-led interviews."
- "While this latency may reflect similar reaction times in human-to-human chat interactions, participants appeared to prefer shorter waiting times when they were aware they were in [conversation with an AI]."
- "While error rates of human and AI interviewers were at similar levels, the nature of the errors differed."
- "While emphasizing that a satisfactory interview hinges on a flawless technical implementation..."

**Inductive name.** *AI conversational interviewing.*
**Substance:** the cluster is specifically about AI-conducted interviews (latency, error patterns, participant perception, technical implementation). Mapped primarily to Case 16 (AI conversational interviewing on welfare stigma) and Case 17 (Dynamic Surveys with AI follow-ups).

## Cluster 1 — Open-source synthesis pipelines (3 extracts; 67% PV-coded)

**Top sentences:**
- "To view a copy of this licence, visit creativecommons.org/licenses/by-nc-nd/4.0/."
- "To isolate retrieval, we use our 8B LM without self-feedback or citation verification and rerank to the top 15 with OpenScholar reranker."
- (license boilerplate from the OpenScholar paper)

**Inductive name.** *Open-source literature-synthesis pipelines.*
**Substance:** OpenScholar / multi-paper-synthesis-system descriptions, including license/copyright matter and component descriptions (LM, reranker). Mapped primarily to Case 9 (citation-grounded synthesis) and Case 33 (Deep Research). The cluster is partially contaminated by license-boilerplate that survived cleaning; the substantive content is about retrieval-augmented synthesis pipelines.

## Cluster 8 — Tournament-style autonomous policy evaluation (4 extracts; 50% PV-coded)

**Top sentences:**
- "We run an automated tournament evaluating the papers against human benchmarks from top journals."
- "Tournament Leaderboard • About • GitHub Repository Project APE a Social Catalyst Lab project"
- (Project APE site material)

**Inductive name.** *Tournament-style autonomous policy evaluation (Project APE).*
**Substance:** cluster is dominated by Project APE site content describing tournament-style evaluation of autonomous policy-evaluation systems. Mapped to Cases 25 and 26 (Project APE) and 24 (multiverse-nonstandard errors).

## Cluster 69 — Generative social simulation systems (4 extracts; 50% PV-coded)

**Top sentences:**
- "While these efforts in specific areas have shown the human-level intelligence of LLMs, creating LLM-driven social generative agents capable of simulating a comprehensive social being remains largely underexplored."
- "While past literature mainly focused on agent-based social simulation, there is an increasing trend to adopt LLMs as simulation tools."
- "We first focus on the most basic element of the simulator, i.e., LLM-driven social generative agents."
- "To address the above gaps, we propose AgentSociety, a large-scale social generative simulator..."

**Inductive name.** *Generative social simulation systems.*
**Substance:** AgentSociety-and-similar cluster about LLM-driven social-simulation platforms. Mapped to Case 34 (AgentSociety) and Case 22 (SocSci210 simulators).

## Cluster 66 — Reproducibility / code-repair workflows (4 extracts; 50% shrinking — THROUGHPUT-CLUSTER)

**Top sentences:**
- "Whereas Not Reproduced means the script either failed to run or outputs differed from the ground truth."
- "When execution failed, the failing script and associated error logs were collected and used to construct a prompt for the selected model."
- "We selected Qwen3-Coder-480B-A35B due to its strong performance on real-world coding benchmarks, particularly SWE-bench1..."
- "We evaluated three models, GPT-4o (release 2024-06-08), Gemini 2.5 Pro (release preview-06-05), and Qwen3-Coder-480B-A35B using the same repair loop..."

**Inductive name.** *Reproducibility / code-repair workflows.*
**Substance:** AI-assisted code-repair pipelines (prompt construction from failing scripts, model selection, repair-loop evaluation). Mapped to Cases 28 (agent-based code repair) and 27 (REPRO-Bench). **This is the throughput-shrinkage cluster** — routine code-repair labor shrinks when models can run the repair loop end-to-end.

---

## Notes on the un-documented 86 clusters

- 64 small clusters (3–10 sentences each) that contain mostly methods-paper introductions, definitions, or transitional prose. None reached the ≥3-extract threshold for triangulation reporting.
- 22 medium clusters (10–50 sentences) that contain mixed-topic content — citations, footnotes, license matter, table captions — without a clean substantive theme.
- The HDBSCAN noise label (cluster_id = -1) holds 2,833 sentences (27.8% of corpus). These are sentences whose neighborhood density was below HDBSCAN's threshold; mostly short methods-prose fragments distributed across the embedding space.

## Anchor-literature comparison (post-hoc, after all 9 names committed above)

After naming the 9 documented clusters above, the manuscript's typology framework was consulted to check post-hoc fit. The 8 procedural-validity clusters all contain sentences that the manuscript's rubric would code as protocol/provenance, calibration, or accountability work — supporting the rubric's procedural-validity grouping. The single throughput-shrinkage cluster (Cluster 66) maps cleanly to the rubric's "routine coder on high-consensus, ground-truth-rich tasks" being shrinking under AI substitution. **This convergence is the Appendix G headline finding.**

The non-convergent observations are also informative:
- Some clusters (e.g., Cluster 33 AI disclosure) span both procedural-validity and accountability-allocator role-codings; the rubric distinguishes these but the embedding does not; this is a reasonable convergence given the substantive overlap.
- Many small clusters surface domain-specific themes (qualitative methodology citations, simulation systems, conversational interviewing) that the rubric handles via the case-family lens (§6.4, Lens 1) rather than the role-status lens — also consistent.
- Cluster 1's license-boilerplate contamination is a known limitation; future cleaning passes could strip license language more aggressively.
