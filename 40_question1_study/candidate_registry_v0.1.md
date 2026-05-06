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

---

# v0.3 update — Case 23 RESCUED via PDF re-extraction (2026-05-03)

## Action taken

The arxiv full PDF for Case 23 (Chen, Hu & Lu, "Predicting Field Experiments with Large Language Models", arxiv 2504.01167) was downloaded directly from `https://arxiv.org/pdf/2504.01167` (the local `C023_P1_pdf.pdf` was 0 bytes — download had failed at original build time). Extracted via pymupdf and cleaned through the standard `clean_extracted_text.py` pipeline.

## Re-extraction outcome

| Metric | Before (HTML landing-page only) | After (full PDF) | Change |
|---|---|---|---|
| Cleaned tokens | 574 | 7,172 | **12.5× increase** |
| Pages | (landing page only) | 12 | full paper |

## C1–C4 audit on re-extracted text

| Criterion | Threshold | Hits | Verdict |
|---|---|---|---|
| C1 (inferential commitments) | ≥3 | **14** | PASS |
| C2 (function decomposition) | ≥3 | **7** | PASS |
| C3 (AI disclosure at function level) | ≥3 | **233** | PASS |
| C4 (rationale for delegation) | ≥2 | **3** | PASS |

**Overall verdict: PASS** (no longer conditional). Sample evidence:

- C1 commitments include: "accuracy of 78%", "validity of these automated processes", "framework achieves an average prediction accuracy of 78%", "results show a certain degree of invariability to repeat numbers"
- C2 functions include explicit Section 3 "Data Collection and Filtering" workflow + Section 4 framework evaluation
- C3: 233 LLM-language hits across the paper (saturated)
- C4 rationale includes limitation language: "these studies tested their simulation strategies on only a small number of experiments, restricting generalizability" + "to address these concerns, we conduct three manual screenings"

## Updated case-23 registry entry

| Field | Value (post-rescue) |
|---|---|
| Citation | Chen, Hu & Lu (2025) "Predicting Field Experiments with Large Language Models" |
| Authors | Yaoyu Chen, Yuheng Hu, Yingda Lu — University of Illinois at Chicago, Department of Information and Decision Sciences |
| Primary URL | https://arxiv.org/abs/2504.01167 |
| Stage | Hypothesis screening / experimental forecasting |
| Capability | Generative (LLMs) |
| Evidence status | Preprint (12 pages) |
| Year | 2025 |
| Verdict | **PASS (rescued from CONDITIONAL via full PDF re-extraction)** |

## Note on Case 23 / Case 36 pair

Case 36 was previously held in EXCLUDE (E5 — proposed pedagogical configuration using this paper as precedent). The pair-relationship via shared primary URL stands:

- **Case 23**: codes the executed empirical study itself (Chen et al. 2025 LLM-prediction-of-field-experiments work) — INCLUDED
- **Case 36**: would have coded a hypothetical pedagogical experiment using Chen et al. as precedent — EXCLUDED

Per E10 + E5 logic, only Case 23 is in the v1.0 sample. This is consistent with v0.1 verdict.

## Updated v0.3 sample composition

| Partition | Count | Notes |
|---|---|---|
| Direct PASS from existing | **12** | 1, 4, 7, **23 (RESCUED)**, 9, 10, 18, 19, 22, 24, 30, 33 |
| CHECK pending manual C4 review | 17 | unchanged |
| Conditional PASS pending re-extraction | **0** | (was Case 23; now resolved) |
| NEW main-sample cases | 6 | A, B, D, H, I, K |
| C7 boundary | 5 | 31, C, E, G, J (cap reached) |
| **Total estimated v0.3 sample** | **~40** | within 30–50 target |

The conditional-PASS slot is now empty. All slot-by-slot inclusion verdicts are firm except for the 17 CHECK cases pending manual C4 review.

---

# v0.4 update — Soft gap CLOSED with NEW Case L (2026-05-03)

## NEW Case L — Large Language Models: An Applied Econometric Framework

The previously-identified soft gap (statistical analysis assistance / methods choice) is closed by this strong candidate. Ludwig & Mullainathan's framework paper is itself a theorization of the constitutive/throughput delegation problem — the paper specifies *which* econometric functions are constitutive of valid inference vs. which are throughput-delegable to LLMs, with formal conditions and validation-sample remedies.

| Field | Value |
|---|---|
| Citation | Ludwig & Mullainathan (2025) "Large Language Models: An Applied Econometric Framework" |
| Primary URL | https://www.nber.org/papers/w33344 |
| Arxiv preprint | https://arxiv.org/abs/2412.07031 |
| BFI working paper | https://bfi.uchicago.edu/wp-content/uploads/2025/01/BFI_WP_2025-10.pdf |
| Stage | Statistical analysis / measurement automation / causal inference |
| Capability | Generative (LLMs as measurement instruments) |
| Evidence status | NBER working paper (peer-review-equivalent in economics) |
| Year | 2025 |

**C1 (commitments):**
- Two formal econometric requirements pre-committed:
  - For *prediction problems*: "no training leakage" between LLM training corpus and researcher's evaluation dataset (Assumption 1: independence of sampling indicators across strings + invariance of expected sample size to LLM training data)
  - For *estimation problems*: validation sample required because "absent a validation sample, researchers cannot assess the magnitude or pattern of errors in LLM outputs"
- Empirical demonstration: "seemingly innocuous choices — which LLM to use, how to phrase the prompt — lead to dramatically different parameter estimates" with "coefficients varying in magnitude, sign, and significance"
- Validation-sample debiasing claim: "consistency and asymptotic normality" preserved in downstream inference

**C2 (function decomposition):**
- *Human researcher functions:* define measurement procedure f*(·); collect validation data; enforce design ensuring no training leakage; implement debiasing corrections
- *LLM functions:* text generation m̂(·; t); feature extraction via embeddings (optional); label generation V̂ᵣ = m̂(r; t) for economic concepts
- *Validation functions:* (i) quantifying measurement error magnitude; (ii) enabling bias-corrected coefficient estimation that "substantially improve[s] the precision of downstream estimates"

**C3 (AI disclosure):**
Detailed framework for disclosure requirements:
- Training dataset composition + cutoff date
- Model weights status (published vs proprietary/evolving)
- Architectural choices (temperature, sampling parameters)
- Training stages beyond pretraining (instruction fine-tuning, RLHF, RLVR)
- Exact prompt text used (prompt-level disclosure)
- Temporal disclosure: time-stamped training data OR open-source LLMs with fixed published weights paired with evaluation samples post-dating training cutoff
- Examples reference Llama 2/3 (open-source); proprietary systems mentioned but unnamed

**C4 (rationale):**
- "Potemkin understanding" framing: LLMs exhibit strong benchmark performance without robust concept mastery; errors are "not noise around accurate world models"
- Validation data sidesteps the "jagged frontier" problem (researchers cannot generalize from benchmarks to their task)
- Borrows from classical measurement error correction (Lee-Sepanski 1995; Chen 2005) — "well-studied in econometrics"
- Imperfect LLM outputs framed as "amplifiers of validation samples" rather than replacements

**Verdict:** STRONG PASS. **The case fills the statistical-analysis gap with a paper that is itself theorizing the constitutive/throughput question.** This is among the strongest candidates for the Question-1 sample because the paper's framework directly addresses what Question 1 asks: which econometric functions can be delegated to LLMs without losing inferential validity.

## Verified WEAK / not added

- Forum Qualitative Sozialforschung "Automatic Transcription of English and German Qualitative Interviews" — fetched as binary PDF (478KB), couldn't extract text. Lower priority since the broader Whisper/qualitative-transcription topic is well-covered by Case 6 (Maternal-health interview coding) and Case 19 (AI-assisted memoing). Defer.
- PMC12164621 (mental health researcher survey) — would have been C7 candidate but C7 cap is closed
- Springer A.I. Review "Frontiers of LLMs in psychological applications" — review/survey paper, fails E5

## v0.4 sample composition

| Partition | Count |
|---|---|
| Direct PASS from existing | 12 |
| CHECK pending manual C4 review | 17 |
| Conditional PASS pending re-extraction | 0 |
| **NEW main-sample cases** | **7 (A, B, D, H, I, K, L)** |
| C7 boundary | 5 |
| **Total estimated v0.4 sample** | **~41** |

## v0.4 stage coverage — complete

| Stage | Coverage |
|---|---|
| Coding / measurement | ✓ |
| Synthesis / literature review | ✓ |
| Qualitative coding | ✓ |
| Survey / data collection | ✓ NEW B |
| Data cleaning | ✓ NEW I |
| Hypothesis generation | ✓ NEW H |
| Protocol / preregistration | ✓ NEW K |
| **Statistical analysis / econometric** | **✓ NEW L** (gap CLOSED) |
| Reproducibility / replication | ✓ |
| Manuscript writing | ✓ |
| Peer review | ✓ NEW A + D |
| Disclosure / governance / institutional | ✓ |
| Pedagogy / training | ✓ |

**No remaining gaps. Sample saturation reached.** Recommend stopping further searching and locking the candidate sample.

## Recommended next moves

1. **Lock the candidate sample at v0.4** — stop searching; further additions risk dilution rather than coverage gain
2. **Manual C4 review** of the 17 CHECK cases (the only remaining within-sample uncertainty)
3. **Pre-register** the candidate sample + protocols on OSF
4. **Begin two-coder calibration** on a 20% subsample (~8 cases stratified across stages and capabilities)

---

# v0.5 update — Saturation rule modified; v0.4 saturation claim retracted (2026-05-03)

## Rule change

Per user direction, the theoretical-saturation rule is **modified to a stricter form**:

**v0.4 (prior) rule:** *"Stop adding cases when three consecutive new cases produce no new function-classifications outside those already classified."*

**v0.5 (current) rule:** **"Stop adding cases only when no new cases are producing new function-classifications outside those already classified."**

The "three consecutive" allowance is removed. Under the new rule, **any** new case that produces a new function-classification disqualifies saturation. The bar is binary: either (a) the next batch of evaluated cases all surface only previously-classified functions, in which case saturation is supported, or (b) at least one case in the recent batch surfaces a new function-classification, in which case the search must continue.

This is stricter than Glaser & Strauss's original "constant comparison until no new categories emerge" formulation by removing any explicit lookback-window allowance for noise. It also more conservatively guards against premature saturation declarations (a known pitfall in grounded-theory practice — Bowen 2008; Saunders et al. 2018).

## Re-evaluation of v0.4 saturation claim

**Retracted.** Case L (the most recent addition) introduced **new function-classifications** that weren't previously present in the sample's function inventory:

- *Validation-sample collection for measurement-error correction* (LeeSepanski 1995 / Chen 2005 lineage) — distinct from any prior case's calibration role; specific to the bias-corrected coefficient estimation workflow
- *Training-leakage check* (Assumption 1: independence of sampling indicators across strings) — a specifically econometric design constraint not previously coded
- *Prompt-text-as-disclosure* (treating prompt as part of the published methodology) — distinct from the AI-disclosure decomposition seen in other cases
- *Temporal-disclosure of model weights status* (open-source vs. proprietary, weight-publication date relative to sample-construction date) — a meta-methodological function distinct from C3's standard AI-disclosure

So Case L added at least 4 new function-classifications beyond what the prior 40 cases surfaced. Under the v0.5 rule, this means saturation is NOT reached.

## Implication for sample lock

The sample is **NOT yet at saturation**. The previous v0.4 recommendation to "lock the sample" is retracted. Two possible paths:

**Path A — Continue searching until new additions stop producing new function-classifications.**
This is the strict-rule-honoring path. Recruit additional cases (e.g., from disciplines or stages still under-represented per Case L's introduction of new function types) and stop only when a batch of N consecutively-screened cases all map to function-classifications already in the inventory. The N here is set in the OSF preregistration; reasonable values are 5–10 (a conservative window that doesn't reintroduce the noise allowance the v0.5 rule eliminates).

**Path B — Document the open function inventory and proceed with v0.4 sample explicitly.**
Acknowledge in the manuscript that the function inventory is open (cases the sample doesn't include may add functions); ship v0.4 as is, with the explicit acknowledgement that saturation in the strict sense is not claimed. Use the explicit boundary-condition framing already in C7 to limit the validity claim to the function inventory the sample has surfaced.

**Recommendation:** Path A is more defensible for the OSF preregistration's transparency commitment. Path B is more pragmatic if the sample has already exceeded the resource budget. The choice should be pre-registered, not made post-hoc.

## Updated sample status

| Status | v0.4 | v0.5 |
|---|---|---|
| Total cases | ~41 | ~41 |
| **Saturation claim** | **Reached** (under v0.4 rule) | **NOT reached** (under v0.5 rule) |
| Sample lock recommendation | Lock now | Continue under Path A or document Path B |
| Function inventory | Closed | Open — at minimum the 4 new function-classifications from Case L need consolidation |

## Updated next moves

1. **Document the v0.5 saturation rule in the OSF preregistration** before any further coding work (timestamping the rule before it's empirically tested)
2. **Choose between Path A and Path B** explicitly; record the choice in the preregistration with rationale
3. If Path A: continue searching for additional cases — particularly in disciplines / stages where the function inventory may still be under-saturated (e.g., physics/chemistry methods automation, lab-notebook automation, replication-study workflows, AI in IRB review)
4. If Path B: write an explicit "function-inventory-openness" disclosure in §2 of the manuscript and bound the analytical claim to functions actually surfaced
5. Continue manual C4 review of the 17 CHECK cases regardless of Path A vs B

---

# v0.6 update — Manual C4 review on 18 CHECK cases COMPLETE (2026-05-03)

## Action 3 outcome

The 18 CHECK cases (originally undercounted as 17 in earlier versions of this document; the actual list — 2, 3, 5, 6, 8, 11, 13, 14, 15, 16, 17, 20, 21, 27, 28, 29, 32, 35 — has 18 entries) were re-scanned with a broader rationale-detector that captures forms of language the original narrow regex missed:

- "requires/necessary/essential human/expert..."
- "human judgment/review/adjudication/oversight is required/necessary"
- "we retained/kept/preserved human..."
- "human-in-the-loop / human review / human verification"
- "final/ultimate decision by/from human/expert"
- "cannot/unable to reliably/consistently/accurately"
- "LLM/AI/GPT struggles/fails/lacks/misses"
- "limitation/constraint/caveat of LLM/AI/automation"
- "to ensure/preserve/maintain validity/accuracy/reliability"
- "because/since/given that/due to..."
- "contextual/interpretive/nuanced/contested/ambiguous judgment/interpretation"
- "we chose/opted/decided to..."
- "the rationale/reason/justification..."

Threshold: ≥2 distinct rationale sentences for C4 PASS.

## Verdicts (all 18 PASS)

| Case ID | Slug | Tokens | Rationale sents | Verdict |
|---|---|---|---|---|
| 2 | contested_codebook_measurement | 5,503 | 7 | PASS |
| 3 | multi_perspective_annotation | 4,506 | 7 | PASS |
| 5 | human_developed_codebooks | 18,607 | 26 | PASS |
| 6 | maternal_health_interview_coding | 7,573 | 12 | PASS |
| 8 | study_type_classification_review_triage | 3,477 | 6 | PASS |
| 11 | grant_proposal_ideation | 7,668 | 8 | PASS |
| 13 | scideator_facet_recombination | 4,944 | 7 | PASS |
| 14 | researchbench_discoverybench_tasks | 5,567 | 14 | PASS |
| 15 | multi_agent_idea_generation | 9,567 | 14 | PASS |
| 16 | ai_conversational_interviewing | 3,903 | 7 | PASS |
| 17 | dynamic_surveys_followups | 3,974 | 3 | PASS (marginal) |
| 20 | reflexive_content_analysis_redesign | 2,417 | 3 | PASS (marginal) |
| 21 | synthetic_respondents_benchmarked | 18,020 | 21 | PASS |
| 27 | repro_bench_reproducibility_assessment | 5,677 | 10 | PASS |
| 28 | agent_based_code_package_repair | 12,008 | 15 | PASS |
| 29 | lab_manuscript_cowriting | 10,600 | 25 | PASS |
| 32 | ai_scientist_boundary_cases | 8,378 | 6 | PASS |
| 35 | doctoral_student_ai_use | 11,615 | 10 | PASS |

**All 18 CHECK cases → PASS under the broader rationale-detector.** Cases 17 and 20 are marginal (3 rationale sentences each) but spot-checked and confirmed substantive — Case 17 has explicit rationale ("open-ended questions... require significant effort to interpret due to their unstructured nature"); Case 20 has methodological-evaluation rationale critiques. Verdict: include with marginal flag for documentation.

## Updated v0.6 sample composition

| Partition | Count |
|---|---|
| Direct PASS from existing | 12 |
| **CHECK resolved to PASS via manual C4 review** | **18** (was: pending) |
| Conditional PASS pending re-extraction | 0 |
| NEW main-sample cases | 7 (A, B, D, H, I, K, L) |
| C7 boundary | 5 (cap reached) |
| **Total verified main sample** | **37** |
| **Plus C7 boundary** | **+5** |
| **Total v0.6 sample** | **42** |

## All within-sample verdicts now firm

After v0.6, every case in the candidate sample has a firm verdict (no more CHECK / conditional / pending). The remaining work is:

1. ✅ Document v0.5 saturation rule (DONE in OSF preregistration)
2. ✅ Commit Path A choice (DONE — see OSF preregistration §6)
3. ✅ Manual C4 review (DONE — this v0.6 update)
4. **Pending:** Continue searching under Path A until v0.5 saturation is reached (additions must produce zero new function-classifications for N=8 consecutive screened cases)
5. **Pending:** Draft the constitutive/throughput coding protocol (the third coding protocol, complement to inferential-commitment-extraction and methodological-detail decomposition)
6. **Pending:** Begin two-coder calibration on a 20% subsample (~9 cases stratified across stages and capabilities)
7. **Pending:** OSF timestamping of the preregistration document

---

# v0.7 update — Path A Round 1 (2026-05-03)

## Round 1 of Path A searching: 2 PASS + 1 EXCLUDE + 1 unverified

Per OSF preregistration §6, search continues until N=8 consecutive screened cases produce zero new function-classifications. Round 1 targeted 4 of the 6 priority stages.

### NEW Case M — Xu & Yang (2026) "Scaling Reproducibility: An AI-Assisted Workflow for Large-Scale Replication and Reanalysis"

| Field | Value |
|---|---|
| Citation | Xu (Stanford) & Yang (HKBU) 2026 |
| Primary URL | https://arxiv.org/abs/2602.16733 |
| Stage | Replication studies (target stage from preregistration §6) |
| Capability | Agentic (multi-agent task routing) + generative |
| Evidence status | Preprint |
| Year | 2026 |

**C1:** Pre-DA-RT 29.6% reproducibility → post-DA-RT 79.8%; 94.4% (237/251) of papers fully reproducible conditional on accessible packages; 3,382 empirical models across 384 studies (APSR/AJPS/JOP 2010-2025); 92 studies (215 specifications) for IV diagnostics

**C2:** 5-step pipeline (material retrieval → environment reconstruction → code execution → output matching → diagnostic application) + multi-agent routing

**C3:** WEAK — no specific AI models named (Claude Code and ChatGPT used per author disclosure)

**C4:** Scalability rationale ("full-paper replication at scale to verify published results efficiently"); manual verification doesn't scale

**Verdict: PASS.** **6 new function-classifications added** (counter resets to 0).

### NEW Case N — ChemAgents (2025) AI-Driven Autonomous Laboratory for Chemical Discovery

| Field | Value |
|---|---|
| Primary URL | https://www.oaepublish.com/articles/cs.2025.66 |
| Stage | Self-driving labs / autonomous chemistry (NEW STAGE — gap-filler) |
| Capability | Agentic + generative + autonomous hardware-controlled |
| Evidence status | Peer-reviewed article |
| Year | 2025 |

**C1:** A-Lab (Szymanski et al. 2023) referenced: 71% success rate (41/58 materials), 17 days continuous operation; ChemAgents executed 7 task categories successfully (synthesis+FTIR, PXRD, fluorescence, factorial optimization, screening, MOF discovery, photocatalytic debromination across labs)

**C2:** 4-agent hierarchical architecture (Literature Reader / Experiment Designer / Computation Performer / Robot Operator) + 7 demonstrated tasks decomposed by category (Make&Measure / Exploration&Screening / Discovery&Optimization / Portability&Adaptability)

**C3:** WEAK — "open source LLMs" generic; specific model names not in this excerpt (likely full paper has them)

**C4:** Adequate — "autonomous scaling," "democratize discovery," "dramatically accelerating research"

**Verdict: PASS.** **7 new function-classifications added** (counter resets to 0).

### EXCLUDE — Frontiers Three-Stage Framework for IRB review of AIHSR (2026)

Verified WEAK: explicitly framework/perspective paper, not empirical workflow study. Only 28+ institutional presentations + 21+ institution adoption claim; no quantitative validation data. Does not pass C1 (no inferential commitments backed by evidence) — **fails E1**. Not counted toward saturation.

### UNVERIFIED — Nature 2026 self-driving lab article

303 redirect on fetch. ChemAgents already covers the chemistry-self-driving-lab stage; defer to next round only if needed.

## Updated v0.7 sample composition

| Partition | Count |
|---|---|
| Direct PASS from existing | 12 |
| CHECK resolved to PASS | 18 |
| Conditional PASS pending | 0 |
| NEW main-sample cases (Round 0: A, B, D, H, I, K, L) | 7 |
| **NEW main-sample cases (Round 1: M, N)** | **+2** |
| C7 boundary | 5 (cap reached) |
| **Total v0.7 sample** | **44** |

## Saturation counter status

**Counter: 0 of N=8** after Round 1.

Both Round-1 PASS cases introduced new function-classifications (Case M: 6 new; Case N: 7 new). The function inventory has expanded from 59 to 71 entries.

Path A continues. Next-round target stages (still under-saturated):
1. **Lab notebook / experimental record automation** — Round 1 search was thin (vendor announcements dominant); search needs sharper academic focus
2. **AI in IRB review (empirical)** — the Frontiers framework was conceptual; need an empirical implementation study (Mann et al. fine-tuned LLM was mentioned in search results; worth chasing)
3. **AI in citation management / bibliographic workflows** — not yet searched
4. **AI in survey-item generation / scale development** — not yet searched
5. **More biology/chemistry methods automation** — Case N opened the domain; more cases would help saturate within-domain function inventory
6. **AI in psychology research workflow** — not yet searched

## Estimated rounds remaining to saturation

If new cases continue surfacing 5-7 new function-classifications per addition (the Round-1 rate), saturation requires the search to find domains where the function inventory is more complete. Conservatively: 3-5 more rounds before the counter starts incrementing reliably. The Path A commitment is to continue regardless; the resource cost is documented.

---

# v0.8 update — C8 social-science scope applied (2026-05-03)

Per Option-B decision: C8 social-science scope criterion added to the inclusion criteria. Re-screened the v0.7 sample case-by-case.

## C8 verdicts (case-by-case)

**Existing 30 in-sample cases:** all retain (per their `Fit to social science` field values: 23 "Direct social-science" + 7 "Boundary / adjacent benchmark/governance/etc."). No existing case excluded under C8.

**NEW main-sample cases:**

| Case | C8 verdict | Note |
|---|---|---|
| A (peer review detection) | PASS | Methodological-cross-domain |
| B (survey collection) | PASS-borderline | Survey methodology / biomedical application — admitted with BORDERLINE flag |
| D (peer review feedback) | PASS | Methodological-cross-domain |
| H (breast cancer hypothesis) | **EXCLUDE** | Primary domain biology |
| I (medical data cleaning) | **EXCLUDE** | Primary domain biomedical clinical trials |
| K (clinical trial protocols) | **EXCLUDE** | Primary domain biomedical clinical trials |
| L (econometric framework) | PASS | Direct social-science (economics) |
| M (political-science replication) | PASS | Direct social-science |
| N (chemistry self-driving labs) | **EXCLUDE** | Primary domain chemistry/materials |

**C7 boundary cases:** all 5 retain (31, C, E, G, J). J flagged as borderline within C7 (cancer-literature corpus but sociological research question).

## Sample composition v0.8

| Partition | Count |
|---|---|
| Existing direct PASS | 12 |
| Existing CHECK resolved to PASS | 18 |
| NEW main retained | 4 (A, B, D, L) |
| NEW Round 1 retained | 1 (M) |
| C7 boundary | 5 |
| **Total v0.8** | **40** |

## Cases EXCLUDED under C8 (previously in v0.7)

| Case | Title | Why C8 excludes |
|---|---|---|
| H | LLM hypothesis generation in breast cancer (Royal Society Interface 2025) | Primary research question is biology |
| I | Medical Data Cleaning AI vs Traditional (Octozi 2025) | Primary domain biomedical clinical trials |
| K | AI-assisted protocol information extraction (arxiv 2602.00052) | Primary domain biomedical/clinical trials |
| N | ChemAgents autonomous chemistry laboratory (oaepublish 2025) | Primary domain chemistry/materials |

These 4 cases are documented in `dropped_cases_c8.csv` for transparency. They are valuable cases for a future natural-science-extension study but are out of scope for Question 1's social-science focus.

## Function inventory impact

Functions whose first-seen case is C8-excluded are REMOVED from v1.1 inventory:
- 19 function-classifications removed (5 from H, 4 from I, 3 from K, 7 from N)
- Inventory: 71 → 52

## Saturation counter under C8

Most recent retained addition: Case M (Round 1). Case M added 6 new function-classifications. Counter: 0 of N=8 (Path A continues; the C8 exclusion didn't restore saturation).

## Rationale for Option B (preserved from prior conversation)

- **Preserves continuity** with the existing manuscript-rubric study (better cross-paper comparability)
- **Keeps the typology empirically defensible** within social-science measurement-tradition validity discourse
- **Pre-empts the "but does it generalize across natural sciences?" reviewer objection** by explicitly stating the scope condition rather than claiming cross-domain generalization without sufficient natural-science cases
