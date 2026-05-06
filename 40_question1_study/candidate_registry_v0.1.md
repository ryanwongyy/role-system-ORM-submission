# Question-1 Study: Candidate Case Registry (v0.1)

**Question:** Which functions in scientific work are constitutive of research validity — cannot be delegated to AI without losing the validity claim — and which are throughput labor whose delegation does not affect what the research can claim?

**Sample design:** Theoretically-sampled, purposive; not statistically representative. Stratified across research stages × AI capabilities × evaluability conditions.

**Status:** v0.1 — initial candidate sample, pre-coding-calibration. Subject to revision after manual C1–C4 verification of CHECK cases and OSF pre-registration of the coding scheme.

---

## Cases adopted from existing 36-case corpus

After applying C1–C6 + E1–E10 + C7 to the existing 36 cases (audit performed earlier), the following are adopted into Question-1's candidate sample:

### Direct PASS (10 cases — verified C1–C4 via pattern + manual review)

| ID | Slug | Stage | Capability |
|---|---|---|---|
| 1 | objective_party_annotation (Tornberg) | coding | generative |
| 4 | party_cue_perturbation | coding | generative |
| 9 | citation_grounded_synthesis | synthesis | agentic |
| 10 | citation_hallucination_checks | synthesis | agentic |
| 18 | qda_delegation_preferences | qualitative coding | generative |
| 19 | ai_assisted_fieldnote_memoing | qualitative interpretation | generative |
| 24 | ai_multiverse_nonstandard_errors | analysis | agentic |
| 30 | structured_ai_disclosure_daisy | disclosure / governance | generative |
| 33 | deep_research_policy_reconnaissance | synthesis | agentic |
| 7 | agentic_screening (Baccolini) — RESCUED | screening | agentic |
| 22 | socsci210_simulators — RESCUED | data generation | predictive |

### CHECK (17 cases — likely PASS post manual C4 review)

Cases 2, 3, 5, 6, 8, 11, 13, 14, 15, 16, 17, 20, 21, 27, 28, 29, 32, 35.
Manual review of C4 rationale-language remains pending.

### Conditional PASS pending re-extraction

| ID | Action |
|---|---|
| 23 (Forecasting) | Re-extract from arxiv full PDF (cleaned text was landing-page only) |

### Adopted under C7 boundary-condition admittance

| ID | Reason |
|---|---|
| 31 (Project Rachel) | Action research on AI scholarly identity; institutional adaptation question; capped within C7 boundary set |

### Excluded under new criteria

| ID | Reason |
|---|---|
| 12 (Funding-pipeline) | E10 Pair-A duplicate with Case 11 |
| 25 (Project APE tournament) | C1 fail — no peer-reviewed methods documentation |
| 26 (Project APE autonomy) | Same as 25 |
| 34 (AgentSociety) | C1 fail — alignment claim asserted, not substantiated in paper |
| 36 (Methods-course design) | E5 — proposed pedagogical configuration |

---

## NEW cases adopted (verified C1–C4 via web search)

### NEW Case A — Detecting LLM-generated peer reviews

| Field | Value |
|---|---|
| Citation | (Authors TBD) PLOS One, 2025 |
| Primary URL | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0331871 (PLOS One) |
| Mirror | https://pmc.ncbi.nlm.nih.gov/articles/PMC12453209/ |
| Stage | Peer review (NEW STAGE — fills gap) |
| Capability | Generative (LLMs generating reviews) + detection / statistical methods |
| Evidence status | Peer-reviewed article |
| Year | 2025 |

**C1 (commitments):**
- "Random citation watermark...appearing in 98.6% of LLM-generated reviews on average"
- "94%+ of watermarked reviews retain the watermark even after being paraphrased"
- "Zero false positives even when applied to over ten thousand reviews"
- "Higher statistical power than standard corrections such as Bonferroni"
- "Up to 89% watermark embedding" on NSF grant proposals

**C2 (function decomposition):**
1. Watermark candidate selection (humans: surnames, technical terms, citation formats)
2. Statistical detection algorithm design (humans: Algorithms 1–3)
3. PDF font-embedding (humans via Glyphr Studio + Adobe Acrobat)
4. Dataset curation (humans: ICLR 2024, NSF proposals, PeerRead)
5. Cryptic prompt injection optimization (humans + Greedy Coordinate Gradient)
6. Review generation (AI: ChatGPT 4o, Gemini 2.0 Flash, Claude 3.5 Sonnet)
7. Watermark embedding (AI: same models)
8. Paraphrasing defense simulations (AI)

**C3 (AI disclosure):** ChatGPT 4o, o1-mini, Gemini 2.0 Flash, Claude 3.5 Sonnet, LLaMA 2, Vicuna 1.5 — all named. API vs WebApp distinction made.

**C4 (rationale):** Watermark must be "exogenous to the entire review-writing process" for FWER bounds; Bonferroni rejected because "can severely reduce statistical power"; cryptic injection chosen because "such jailbreaking techniques have been used in broader LLM safety literature."

---

### NEW Case B — Automated survey collection with LLM-based conversational agents

| Field | Value |
|---|---|
| Primary URL | https://pmc.ncbi.nlm.nih.gov/articles/PMC12574787/ |
| Stage | Data collection / survey methodology (NEW STAGE — fills gap) |
| Capability | Generative (GPT-4o) + agentic (BlandAI) |
| Evidence status | Peer-reviewed open-access |
| Year | 2025 |

**C1 (commitments):**
- "GPT-4o extracted responses to survey questions with an average accuracy of 98%"
- "Average WER across all participants was 7.7%"
- "Correlation between [transcription errors and response accuracy failures] was calculated to be r=−0.25, with a P-value of .12"
- Comparison: "slightly trailing the 99.55% human accuracy reported for telephone-based health data collection"

**C2 (function decomposition):**
1. Survey design + persona spec (humans)
2. Call initiation + conversational survey administration + transcription (BlandAI agent)
3. Response extraction from transcripts (GPT-4o, 5-pass self-consistency voting)
4. REDCap upload (automated via API)
5. Manual review of 40 audio recordings for ground-truth labeling (humans)

**C3 (AI disclosure):** BlandAI agent (specific company); GPT-4o version 2024-11-20; REDCap (specific system).

**C4 (rationale):** Cost efficiency stated explicitly ($30.15 total / $0.75 per survey); 5-pass self-consistency voting "for established-technique value"; human review limited to ground-truth labeling not operational.

---

### NEW Case C — Quantifying LLM usage in scientific papers

| Field | Value |
|---|---|
| Citation | Liang et al. (2025) Nature Human Behaviour |
| Primary URL | https://www.nature.com/articles/s41562-025-02273-8 |
| Mirror | https://nlp.stanford.edu/~manning/papers/Liang_et_al-2025-Nature_Human_Behaviour.pdf |
| Stage | Scholarly meta-research / institutional adoption tracking |
| Capability | Predictive (population-level word-frequency framework) |
| Evidence status | Peer-reviewed article |
| Year | 2025 |
| **Admitted under** | **C7 boundary-condition** |

**C1 (commitments):**
- "Largest and fastest growth estimated for computer science papers (up to 22%)"
- "Mathematics papers and the Nature portfolio showed lower evidence of LLM modification (up to 9%)"
- LLM modification estimates "higher among papers from first authors who post preprints more frequently, papers in more crowded research areas and papers of shorter lengths"
- Sample: 1,121,912 preprints/papers from arXiv, bioRxiv, 15 Nature portfolio journals, Jan 2020 to Sep 2024

**C2 (function decomposition):** Population-level statistical framework analysis (humans designed framework, ran corpus analysis); no LLM-augmented step in the analysis pipeline itself.

**C3 (AI disclosure):** The LLMs are the *object of study*, not the *method of analysis*. The analysis is human-statistical.

**C4 (rationale):** Population-level framework chosen over individual-paper detection (which has higher per-paper uncertainty); stratification by discipline + venue + year for cross-domain comparison.

---

### NEW Case D — Can LLMs Provide Useful Feedback on Research Papers?

| Field | Value |
|---|---|
| Citation | Liang et al. (2024) NEJM AI |
| Primary URL | https://ai.nejm.org/doi/abs/10.1056/AIoa2400196 |
| Arxiv preprint | https://arxiv.org/abs/2310.01783 |
| Stage | Peer review (workflow case, distinct from Case A's detection angle) |
| Capability | Generative (GPT-4 as reviewer) |
| Evidence status | Peer-reviewed article |
| Year | 2024 |

**C1 (commitments):**
- "Overlap in the points raised by GPT-4 and by human reviewers (average overlap 30.85% for Nature journals, 39.23% for ICLR)"
- Overlap "comparable to the overlap between two human reviewers (average overlap 28.58% for Nature journals, 35.25% for ICLR)"
- "More than half (57.4%) of the users found GPT-4 generated feedback helpful/very helpful"

**C2 (function decomposition):**
1. Paper-author authorship (humans)
2. Automated pipeline using GPT-4 to provide comments on full PDFs (AI)
3. User evaluation prospective study (humans)

**C3 (AI disclosure):** GPT-4 only model deployed.

**C4 (rationale):** "High-quality peer reviews are increasingly difficult to obtain"; "junior or from under-resourced settings" researchers face delays. Delegation addresses capacity constraints rather than comparative advantage.

---

### NEW Case E — Academic journals' AI policies fail to curb AI-assisted writing

| Field | Value |
|---|---|
| Citation | He & Bu (2026) PNAS 123(9) |
| Primary URL | https://www.pnas.org/doi/10.1073/pnas.2526734123 |
| Arxiv preprint | https://arxiv.org/abs/2512.06705 |
| Stage | Institutional/policy adaptation tracking |
| Capability | Predictive (LLM-detection methodology applied at scale) |
| Evidence status | Peer-reviewed article |
| Year | 2026 |
| **Admitted under** | **C7 boundary-condition** |

**C1 (commitments):**
- 5.2 million papers analyzed across 5,114 journals (2021-2025)
- 70% of journals adopted AI policies; "no significant difference between journals with or without policies"
- Full-text analysis on 164k publications: "of the 75k papers published since 2023, only 76 (~0.1%) explicitly disclosed AI use"
- Authors: Yongyuan He and Yi Bu, Department of Information Management, Peking University

**C2 (function decomposition):** Population-level analysis; humans designed framework, ran corpus analysis on 5.2M papers.

**C3 (AI disclosure):** LLMs studied, not LLM-augmented analysis pipeline.

**C4 (rationale):** Study tests whether journal policies actually shift author behavior; comparative analysis with vs. without policy controls for journal-policy effect.

---

### NEW Case G — Widespread adoption of LLM-assisted writing across society

| Field | Value |
|---|---|
| Citation | Liang, Zhang, Codreanu, Wang, Cao, Zou (2025) Patterns 6 |
| Primary URL | https://www.cell.com/patterns/fulltext/S2666-3899(25)00214-4 |
| Arxiv preprint | https://arxiv.org/abs/2502.09747 |
| Stage | Cross-domain societal adoption tracking |
| Capability | Predictive (same population-level mixture-model framework as Case C) |
| Evidence status | Peer-reviewed article |
| Year | 2025 |
| **Admitted under** | **C7 boundary-condition** |
| **E10 status** | **Pair C with Case C** — same author team, distinct corpora; admitted with disclosure |

**C1 (commitments):**
- "By late 2024, roughly 18% of financial consumer complaints, 24% of corporate press releases, nearly 10% of job postings in small firms, and 14% of UN press releases involve LLM-assisted writing"
- Datasets: 687,241 consumer complaints, 537,413 corporate releases, 304.3M job postings, 15,919 UN press releases
- Coverage: January 2022 to September 2024

**C2 (function decomposition):** Same population-level framework as Case C; applied to 4 different non-academic corpora; humans designed/ran the analysis.

**C3 (AI disclosure):** LLMs as object of study; analysis is human-statistical.

**C4 (rationale):** Domain selection covers regulator, corporate, labor, and international-governance text — chosen for cross-domain comparison; "robust population-level statistical framework" justified by avoiding per-document false-positive concerns.

---

## E10 decision for Cases C and G

**Decision: ADMIT BOTH** with explicit Pair-C disclosure.

**Rationale:**
- Same author team (Weixin Liang et al., Stanford NLP)
- Same methodological framework (population-level mixture model)
- **But materially distinct framings:**
  - Case C: scientific papers from arxiv/bioRxiv/Nature portfolio (1.1M papers, single domain — academia)
  - Case G: 4 different non-academic corpora (consumer complaints + corporate PR + job postings + UN press releases — 953M+ documents)
- Different research questions: Case C asks about academic adoption; Case G asks about cross-society adoption
- Different findings (per-discipline academic estimates vs. per-domain societal estimates)
- Different primary URLs and venues (Nature Human Behaviour vs. Patterns)
- ≥30% disjoint role-cell coverage criterion (per v43 §2.1 C3 / new C5) is satisfied — the cases anchor different functions of the same methodological framework

**Treatment:** Both included in Question-1 sample; cited as **Pair C** with explicit shared-team-and-framework disclosure in §2.1 of the eventual manuscript. Coded independently. The pair operates as a within-pair sensitivity check: if both cases produce convergent constitutive/throughput verdicts despite different corpora, the typology travels across domains.

---

## Pending verifications (lower priority)

| Case | Notes |
|---|---|
| F (Wiley Learned Publishing — Wang 2026 cross-disciplinary AI policies in peer review across 439 journals) | URL returned 403; alternative routes (arxiv preprint, ResearchGate) not yet exhausted; would be 2nd C7 case on policy effectiveness if verified |

If Case F is verified, the C7 boundary-condition cap (5 cases) would be hit: Cases 31, C, E, F, G.

---

## Updated sample composition

| Partition | Count | Cases |
|---|---|---|
| Direct PASS from existing corpus | 10 | 1, 4, 7, 9, 10, 18, 19, 22, 24, 30, 33 |
| CHECK pending manual C4 review (likely PASS) | 17 | 2, 3, 5, 6, 8, 11, 13, 14, 15, 16, 17, 20, 21, 27, 28, 29, 32, 35 |
| Conditional PASS pending re-extraction | 1 | 23 |
| **NEW main-sample cases (verified)** | **2** | **A (peer-review detection), B (survey collection)** |
| C7 boundary cases | 1 + 3 + (F if verified) | 31 (existing); C, E, G (new); F pending |
| **Total estimated sample** | **~33–34** | (if all CHECK resolve PASS and Case 23 re-extracts) |

The new cases meaningfully fill prior gaps:
- Peer review (A from detection angle, D from feedback-usefulness angle, G from policy-effectiveness angle)
- Survey methodology / data collection (B)
- Scholarly meta-research / institutional adaptation (C, E, F-pending)

---

## Next steps (per the new I/E criteria's pre-registration commitment)

1. Manual C4 review of the 17 CHECK cases (1–2 hours per case)
2. Re-extract Case 23 from arxiv full PDF
3. Pursue Case F via alternative routes; finalize C7 cap
4. Lock the candidate sample
5. Pre-register on OSF: this candidate registry + the inferential-commitment-extraction protocol + the methodological-detail decomposition rubric + the constitutive/throughput coding protocol (still to be drafted)
6. Begin two-coder calibration on a 20% subsample

---

# v0.2 update — 4 additional cases verified (2026-05-03)

## NEW Case H — LLM hypothesis generation in breast cancer treatment

| Field | Value |
|---|---|
| Citation | (Authors TBD) Royal Society Interface 2025 |
| Primary URL | https://royalsocietypublishing.org/rsif/article/22/227/20240674/235871 |
| Mirror | https://pmc.ncbi.nlm.nih.gov/articles/PMC12134935/ |
| Stage | Hypothesis generation (NEW STAGE — gap-filler) |
| Capability | Generative (GPT-4) + experimental wet-lab validation |
| Evidence status | Peer-reviewed article |
| Year | 2025 |

**C1 (commitments):** 3/12 drug combinations validated with synergy scores above positive controls in round 1; 3/4 in round 2; HSA score 10.58 for disulfiram + simvastatin; MCF7 specificity demonstrated; ANOVA + IC50 + n≥3 replicates.

**C2 (function decomposition):**
- GPT-4: 12 initial hypotheses, mechanistic rationales, controls, iterative refinement, third-iteration suggestions
- Humans + wet-lab: prompt engineering, cell-line selection (MCF7 vs MCF10A), experimental execution, statistical analysis, literature cross-reference

**C3 (AI disclosure):** GPT-4 named primary; Gemini + PubMedGPT secondary comparison; biological error documented (itraconazole false claim about ergosterol/mammalian membranes).

**C4 (rationale):** "Explore regions of hypothesis space humans may miss"; "make expertise in drug design more accessible to non-specialists."

---

## NEW Case I — Medical Data Cleaning AI-Assisted vs Traditional (Octozi platform)

| Field | Value |
|---|---|
| Primary URL | https://arxiv.org/abs/2508.05519 |
| Stage | Data cleaning (NEW STAGE — gap-filler) |
| Capability | Generative (LLMs) + heuristic |
| Evidence status | Preprint |
| Year | 2025 |

**C1 (commitments):** Throughput 6.03×; cleaning errors 54.67% → 8.48% (6.44× improvement); false positives reduced 15.48×; database-lock 33% acceleration; $5.1M cost savings in Phase III oncology trials.

**C2 (function decomposition):** Hybrid delegation (LLM + domain-specific heuristics); 10 human reviewers; granular step-by-step weak (full paper review needed).

**C3 (AI disclosure):** Octozi platform named; specific LLMs powering it not disclosed (C3 weakness flagged).

**C4 (rationale):** Efficiency under regulatory constraints ("critical bottleneck", "exponentially increasing data volumes"); "maintaining regulatory compliance" as guardrail.

---

## NEW Case J — AI-Based Screening of Cancer Research Publications (paper-mill detection) — **C7 BOUNDARY**

| Field | Value |
|---|---|
| Citation | Scancar, Byrne, Causeur, Barnett (2025) bioRxiv |
| Primary URL | https://www.biorxiv.org/content/10.1101/2025.08.29.673016v2.full |
| Coverage | Nature 2025 article (d41586-025-02906-y) |
| Stage | Scientific integrity / paper-mill detection |
| Capability | Predictive (BERT-based text classification) |
| Evidence status | Preprint (bioRxiv) |
| Year | 2025 |
| **Admitted under** | **C7 boundary-condition (slot 5/5 — cap reached)** |

**C1 (commitments):** Trained on 2,202 retracted paper-mill papers; screened 2.6M cancer research papers; 9.87% flagged for paper-mill similarities; **prediction accuracy 0.91** (titles + abstracts only).

**C2 (function decomposition):** Humans designed BERT classifier + curated training set; ML model performs at-scale screening; image integrity experts validated independently.

**C3 (AI disclosure):** BERT-based text classification model; specific architecture documented; predictive (not generative) AI.

**C4 (rationale):** At-scale detection (2.6M papers) cannot be done manually; "reveal the iceberg" of paper-mill prevalence as system-level integrity question.

---

## NEW Case K — AI-assisted protocol information extraction in clinical trial workflows

| Field | Value |
|---|---|
| Primary URL | https://arxiv.org/abs/2602.00052 |
| Stage | Protocol / preregistration / extraction |
| Capability | Generative + agentic (RAG) |
| Evidence status | Preprint |
| Year | 2026 |

**C1 (commitments):** Clinical-trial-specific RAG extraction accuracy **89.0%** vs standalone LLMs 62.6%; AI-assisted tasks completed **≥40% faster**; tasks "rated as less cognitively demanding."

**C2 (function decomposition):** Three modes contrasted — (i) clinical-trial-specific RAG, (ii) standalone LLMs with fine-tuned prompts, (iii) Clinical Research Coordinators (human baseline). Comparison across modes is the core methodology.

**C3 (AI disclosure):** "Generative LLMs" generic; specific models not named (C3 weakness flagged).

**C4 (rationale):** Burden reduction under "protocol complexity, amendments, and challenges around knowledge management"; "expert oversight remains essential" as guardrail.

---

## C7 boundary cap status: CLOSED at 5/5

| Slot | Case | Angle |
|---|---|---|
| 1 | Case 31 — Project Rachel | Identity governance / action research |
| 2 | Case C — Liang Nature Human Behaviour | Academic LLM adoption tracking |
| 3 | Case E — He & Bu PNAS | Policy effectiveness |
| 4 | Case G — Liang Patterns (Pair-C with C) | Cross-society LLM adoption |
| 5 | **Case J — Scancar bioRxiv** | **Paper-mill detection / integrity** |

**Case F (Wiley Learned Publishing 439 journals) DROPPED** — would have been a 6th C7 case; held in reserve as fallback if any C7 case fails final coding.

---

## v0.2 sample composition

| Partition | Count |
|---|---|
| Direct PASS from existing | 11 |
| CHECK pending manual C4 review (likely PASS) | 17 |
| Conditional PASS pending re-extraction (Case 23) | 1 |
| **NEW main-sample cases** | **6 (A, B, D, H, I, K)** |
| C7 boundary cases | 5 (31, C, E, G, J) |
| **Total estimated sample** | **~40** |

## v0.2 stage coverage

All major stages now covered:

| Stage | Cases |
|---|---|
| Coding / measurement | 1, 2, 4, 5, 6, 8 (+ CHECK) |
| Synthesis / literature review | 9, 10, 33 |
| Qualitative coding | 18, 19, 20 |
| Survey / data collection | NEW B |
| **Data cleaning** | **NEW I** |
| Hypothesis generation | 13, 14, 15 + **NEW H (lab-validated)** |
| **Protocol / preregistration** | **NEW K** |
| Statistical analysis assistance | Case 24 (still soft-gap; defer to v0.3) |
| Reproducibility / replication | 27, 28 |
| Manuscript writing | 29 |
| **Peer review** | **NEW A + NEW D** |
| Disclosure / governance | 30, 31, C, E, G, J |
| Pedagogy / training | Case 35 |

Soft gap remaining: statistical analysis assistance / methods choice. Could be filled in v0.3 if a strong candidate surfaces.

---

## Total v0.2 cases (final list for the candidate sample)

**Main sample (~35 cases after CHECK resolution):**
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 (conditional), 24, 27, 28, 29, 30, 32, 33, 35, **A, B, D, H, I, K**

**C7 boundary (5 cases):**
31, **C, E, G, J**

**Excluded (5 cases):** 12 (E10), 25, 26, 34, 36
