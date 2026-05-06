# Function Inventory v1.0 — Question-1 Study Baseline

**Status:** Baseline derived from the 42 v0.6 cases (37 main + 5 C7 boundary).
**Purpose:** Reference list for the v0.5 saturation rule: any new case that introduces a function-classification not in this inventory resets the saturation counter to zero.
**Maintenance:** Updated after each new case is decomposed under the methodological-detail decomposition rubric. Every addition logged in `saturation_log.csv`.

---

## Tier 1 — Existing 17 role labels (from `06_analysis_tables/role_coding_master.csv`)

These come from the prior corpus's role-coding scheme; they form the function-classification baseline at v0.5.

| # | Function | Coverage in sample |
|---|---|---|
| 1 | Relevance adjudicator | All 36 existing cases |
| 2 | Mechanism disciplinarian | All 36 existing cases |
| 3 | Construct and perspective boundary setter | All 36 existing cases |
| 4 | Construct boundary setter | All 36 existing cases (split-candidate) |
| 5 | Perspective sampler | All 36 existing cases (split-candidate) |
| 6 | Corpus pluralist | All 36 existing cases |
| 7 | Protocol and provenance architect | All 36 existing cases |
| 8 | Counterfactual and transportability judge | All 36 existing cases |
| 9 | Counterfactual / transportability judge | All 36 existing cases (split-candidate) |
| 10 | Calibration architect | All 36 existing cases (split-candidate) |
| 11 | Situated interlocutor / context witness | All 36 existing cases |
| 12 | Situated interlocutor | All 36 existing cases (split-candidate) |
| 13 | Context witness | All 36 existing cases (split-candidate) |
| 14 | Accountability and labor allocator | All 36 existing cases |
| 15 | Routine first-pass screener | All 36 existing cases |
| 16 | Routine coder on high-consensus, ground-truth-rich tasks | All 36 existing cases |
| 17 | Structural prose polisher / drafter | All 36 existing cases |

## Tier 2 — Function-classifications added by the 7 NEW main-sample cases (A, B, D, H, I, K, L)

These are functions surfaced by NEW cases that were not represented in the existing 17 roles. They expand the inventory beyond the prior corpus's coding scheme.

### From Case A (PLOS One peer-review detection)

| # | Function | First seen in |
|---|---|---|
| 18 | Watermark candidate selection | Case A |
| 19 | Statistical detection algorithm design | Case A |
| 20 | PDF font-embedding (manuscript artifact tampering for adversarial testing) | Case A |
| 21 | Cryptic prompt injection optimization | Case A |
| 22 | Adversarial review-generation simulation | Case A |
| 23 | Paraphrasing-defense evaluation | Case A |

### From Case B (Survey collection with conversational agents)

| # | Function | First seen in |
|---|---|---|
| 24 | Conversational survey administration | Case B |
| 25 | Real-time call-flow management | Case B |
| 26 | Audio-to-text transcription | Case B |
| 27 | Self-consistency multi-pass voting for response extraction | Case B |
| 28 | REDCap / structured-data upload via API | Case B |

### From Case D (LLM peer-review feedback usefulness)

| # | Function | First seen in |
|---|---|---|
| 29 | Automated reviewer-style commentary generation on full-PDF papers | Case D |
| 30 | Prospective user-evaluation study on AI-generated feedback usefulness | Case D |

### From Case H (LLM hypothesis generation, lab-validated)

| # | Function | First seen in |
|---|---|---|
| 31 | Drug-pair hypothesis generation with mechanistic rationale | Case H |
| 32 | Iterative refinement based on experimental feedback (round 2/3) | Case H |
| 33 | Cell-line selection (MCF7 vs MCF10A specificity test) | Case H |
| 34 | SynergyFinder 3.0 / IC50 / ANOVA wet-lab validation | Case H |
| 35 | Biological-error documentation (epistemological-uncertainty audit) | Case H |

### From Case I (Medical data cleaning)

| # | Function | First seen in |
|---|---|---|
| 36 | Tabular medical data error processing | Case I |
| 37 | Domain-heuristic-augmented LLM cleaning | Case I |
| 38 | Database-lock acceleration | Case I |
| 39 | False-positive query reduction | Case I |

### From Case K (RAG protocol extraction)

| # | Function | First seen in |
|---|---|---|
| 40 | Retrieval-augmented protocol section extraction | Case K |
| 41 | Clinical Research Coordinator (CRC) human baseline | Case K |
| 42 | Vision-based tabular data extraction | Case K |

### From Case L (Ludwig & Mullainathan econometric framework)

| # | Function | First seen in |
|---|---|---|
| 43 | Validation-sample collection for measurement-error correction | Case L |
| 44 | Training-leakage check (Assumption 1: independence of sampling indicators) | Case L |
| 45 | Prompt-text-as-disclosure (prompt as part of published methodology) | Case L |
| 46 | Temporal-disclosure of model weights status | Case L |
| 47 | Bias-corrected coefficient estimation (Lee-Sepanski 1995 / Chen 2005 lineage) | Case L |
| 48 | Embedding-feature extraction for prediction problems | Case L |

## Tier 3 — Function-classifications added by C7 boundary cases (Cases 31, C, E, G, J)

These functions are at the institutional / population-research / scholarly-meta-research layer, not within-paper-workflow.

### From Case 31 (Project Rachel)

| # | Function | First seen in |
|---|---|---|
| 49 | Anagram-based AI-author identity construction | Case 31 |
| 50 | Web-server publication infrastructure (bypass of preprint platform restrictions) | Case 31 |
| 51 | Action-research observation of scholarly-system response | Case 31 |
| 52 | Authored-content human-approval-and-decline | Case 31 |

### From Case C / G (Liang et al. Pair-C, prevalence tracking)

| # | Function | First seen in |
|---|---|---|
| 53 | Population-level word-frequency mixture-model framework | Case C |
| 54 | Cross-domain corpus stratification (discipline / venue / year) | Case C |
| 55 | Cross-society corpus stratification (academic / consumer / corporate / governance) | Case G |

### From Case E (He & Bu PNAS journal policies)

| # | Function | First seen in |
|---|---|---|
| 56 | Pre/post journal-policy comparative analysis | Case E |
| 57 | Disclosure-rate auditing on full-text corpus | Case E |

### From Case J (Scancar paper-mill detection)

| # | Function | First seen in |
|---|---|---|
| 58 | BERT-based binary text classification on retraction-trained dataset | Case J |
| 59 | Image-integrity-expert independent validation | Case J |

## Inventory total (v1.0)

**Total function-classifications:** 59 (17 from existing roles + 30 from main-sample new cases + 12 from C7 boundary cases)

## Saturation accounting

Per the v0.5 rule: any new case that introduces a function-classification NOT in this inventory resets the saturation counter to zero. The counter advances only when a new case is decomposed and **all its function-classifications are already in this inventory**.

The N=8 stopping condition (per OSF preregistration §5) requires 8 consecutive new cases that contribute zero new function-classifications.

**Current saturation counter:** 0 (the most recent addition, Case L, contributed 6 new function-classifications — entries 43-48).

## How to use this inventory

When a new candidate case is decomposed under the methodological-detail decomposition rubric:
1. List all functions in the case's workflow
2. Check each function against this inventory
3. If ALL functions match existing entries: counter += 1, log as "no new functions"
4. If ANY function is NEW: counter = 0, add the new functions to this inventory, log as "introduced N new functions"

Stop search when counter = 8.

---

# v1.1 update — Round 1 of Path A search (2026-05-03)

## Functions added by NEW Case M (Xu & Yang 2026 scaling reproducibility)

| # | Function | First seen in |
|---|---|---|
| 60 | Replication-package access and validation | Case M |
| 61 | Computational environment reconstruction | Case M |
| 62 | Automated code execution at scale | Case M |
| 63 | Output-matching against published regression tables | Case M |
| 64 | Standardized diagnostic application across studies | Case M |
| 65 | Multi-agent task routing | Case M |

## Functions added by NEW Case N (ChemAgents 2025 autonomous chemistry laboratory)

| # | Function | First seen in |
|---|---|---|
| 66 | Hierarchical multi-agent architecture (Literature Reader / Experiment Designer / Computation Performer / Robot Operator) | Case N |
| 67 | Wet-lab experimental protocol generation by LLM | Case N |
| 68 | Autonomous computational chemistry calculations | Case N |
| 69 | Hardware-execution-via-robot-operator | Case N |
| 70 | Bayesian optimization with LLM coordination | Case N |
| 71 | PXRD / FTIR / fluorescence multi-modal characterization | Case N |
| 72 | Cross-facility autonomous-system redeployment | Case N |

## v1.1 inventory total

71 function-classifications (was 59 at v1.0; +12 in Round 1).

## Saturation counter status after Round 1

**Counter: 0 of N=8.** Both PASS cases in Round 1 introduced new function-classifications, resetting the counter.

| Case | Outcome | New functions | Counter after |
|---|---|---|---|
| M (Xu & Yang reproducibility) | PASS | 6 | 0 (reset) |
| N (ChemAgents autonomous chemistry) | PASS | 7 | 0 (reset) |
| Frontiers IRB three-stage framework | FAIL E1 | n/a (not decomposed) | 0 (unchanged) |
| Nature self-driving lab article | UNVERIFIED | n/a | 0 (unchanged) |

## Implications

The function inventory expanded substantially in Round 1. This is the **expected and correct outcome** under Path A: the goal is to surface new function-classifications until additions stop producing them. Both new cases were in stages (replication / chemistry-lab-automation) that genuinely differ from the prior corpus, so new functions surfacing is methodologically valid.

**Path A continues.** Next-round target stages (still needing recruitment):
- Lab notebook / experimental record automation (this round was thin — mostly vendor announcements)
- AI in IRB review workflows (this round's framework paper was conceptual; need empirical implementation)
- AI in citation-management / bibliographic workflows
- AI in survey-item generation / scale development
- Additional chemistry/materials/biology lab automation cases (function inventory still expanding in this domain)

---

# v1.2 update — C8 social-science scope applied; 19 functions removed (2026-05-03)

Per the Option-B decision, the following 19 function-classifications are REMOVED from the inventory because their first-seen case (H, I, K, or N) is excluded under C8:

## Removed (first-seen in Case H — biology, breast cancer)

- #31 Drug-pair hypothesis generation with mechanistic rationale
- #32 Iterative refinement based on experimental feedback
- #33 Cell-line selection (MCF7 vs MCF10A)
- #34 SynergyFinder 3.0 / IC50 / ANOVA wet-lab validation
- #35 Biological-error documentation

## Removed (first-seen in Case I — biomedical clinical trials)

- #36 Tabular medical data error processing
- #37 Domain-heuristic-augmented LLM cleaning
- #38 Database-lock acceleration
- #39 False-positive query reduction

## Removed (first-seen in Case K — biomedical / clinical trials)

- #40 Retrieval-augmented protocol section extraction
- #41 Clinical Research Coordinator (CRC) human baseline
- #42 Vision-based tabular data extraction

## Removed (first-seen in Case N — chemistry/materials)

- #66 Hierarchical multi-agent architecture (Lit. Reader / Exp. Designer / Comp. Performer / Robot Operator)
- #67 Wet-lab experimental protocol generation by LLM
- #68 Autonomous computational chemistry calculations
- #69 Hardware-execution-via-robot-operator
- #70 Bayesian optimization with LLM coordination
- #71 PXRD / FTIR / fluorescence multi-modal characterization
- #72 Cross-facility autonomous-system redeployment

## v1.2 inventory total

71 (v1.1) − 19 = **52 function-classifications**.

The removed functions remain documented here for the audit trail. They could be re-introduced if (a) future cases retained under C8 surface them, or (b) a separate natural-science-extension study is conducted.

## Saturation counter status

Counter: **0 of N=8** (unchanged from v1.1 status; Case M still the most recent retained addition with 6 new functions).
