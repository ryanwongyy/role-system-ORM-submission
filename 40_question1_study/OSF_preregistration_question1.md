# OSF Preregistration — Question-1 Study (Constitutive vs Throughput in AI-Embedded Research Workflows)

**Document status at this commit:** **pre-analysis plan**. Intended to be timestamped via OSF posting before any C1–C7 inclusion verdicts on new candidates are finalized and before any constitutive/throughput coding-pass begins. The git commit history of this file (in `40_question1_study/OSF_preregistration_question1.md`) serves as in-repository ordering proof.

**Companion documents (this same `40_question1_study/` directory):**
- `candidate_registry_v0.1.md` — current candidate sample at v0.5 (~41 cases including CHECK and C7)

**Companion documents (other repository locations):**
- `30_reviews/OSF_preregistration.md` — the v1.0-rubric study's pre-analysis plan (different study)
- `30_reviews/OSF_preregistration_computational.md` — the Strategy-5 computational triangulation pre-analysis plan (different study)

This preregistration is **separate from** the v1.0-rubric and Strategy-5 preregistrations. The Question-1 study is a fresh-start design that does not rely on the existing 6-status rubric or 17-role typology.

---

## 1. Purpose

The Question-1 study tests:

> *Which functions in scientific work are constitutive of research validity — cannot be delegated to AI without losing the validity claim — and which are throughput labor whose delegation does not affect what the research can claim?*

The study reframes Cronbach-Meehl-Messick construct validity at the function level. The central methodological move is a **counterfactual delegation test** applied per (function × case) cell: *if this function were fully delegated to AI, would the case's inferential commitments still hold?* — yes ⇒ throughput; no ⇒ constitutive; cannot determine ⇒ contested.

**Theoretical contribution:** mid-range theory (Merton 1968 sense) of how scientific functions distribute across constitutive/throughput categories conditional on research stage, AI capability type, and task evaluability.

**Target venue (primary):** *Organizational Research Methods*. Secondary venues: *Sociological Methods & Research*; *Philosophy of Science*.

## 2. Study design

**Unit of analysis:** (function × case) cell. Per case, 3–10+ functions identified inductively; per function, one performer-attribution + one delegation-test verdict.

**Sample:** Theoretically-sampled, purposive, not statistically representative. Stratified across:
- Research stage (agenda/measurement/coding/synthesis/analysis/reproducibility/authorship)
- AI capability (generative/agentic/predictive)
- Task evaluability (high public ground truth / clean post-hoc auditability / contested adjudication)
- Workflow autonomy (partial / hybrid / near-autonomous / boundary-autonomous)

**Two-coder design:** All inclusion judgments and all (function × case) coding done by two coders independently, with κ-based agreement targets and disagreement-resolution protocol.

## 3. Inclusion criteria (C1–C6 + C7)

**C1 — Empirical research with quantifiable inferential commitments.** The case file must contain at least one explicit validity claim quotable verbatim (≥1 supporting evidence sentence with section/page reference).

**C2 — Function-level methodological detail.** Workflow described at sufficient granularity to identify ≥3 distinct functions performed, each with verbatim sentence-level support.

**C3 — AI involvement documented at function level.** AI use specified per function (which steps used AI, which were human, which were hybrid), not just globally.

**C4 — Author rationale for delegation choices.** For every function classified human-only or hybrid in C3, the case file provides (or the coder can clearly infer from the methods/discussion) why that function was not fully delegated to AI.

**C5 — Temporal scope.** Published or preprinted 2023-01-01 → present (post-LLM-saturation).

**C6 — English-language source.** Operational constraint, documented as scope condition.

**C7 — Boundary-condition admittance (capped at 5).** Cases where AI is embedded in scholarly identity, authorship governance, or institutional response systems may be admitted as boundary-condition cases (max 5) with explicit narrative-only treatment in the manuscript's Discussion section. They are excluded from the main C1–C4 coding pass.

## 4. Exclusion criteria (E1–E10)

**E1** — Pure conceptual / commentary / opinion (no empirical workflow)
**E2** — AI as object of study (LLM-benchmark studies, evaluation papers; AI is the *evaluand*, not embedded research function)
**E3** — AI as incidental writing aid only (no methodological role)
**E4** — Off-research applications (clinical decision support, industrial deployment, consumer products, classroom AI without research-workflow framing)
**E5** — Methodological surveys / proposed designs without case-level evidence (synthesizes others' work but doesn't expose its own workflow at function level; OR proposed pedagogical/experimental configurations not yet executed)
**E6** — Inadequate AI-use disclosure (acknowledges AI but doesn't specify function-level use)
**E7** — Missing inferential commitments (descriptive case studies, ethnographies, design papers without explicit validity claims)
**E8** — Insufficient methodological transparency (workflow described only in summary form)
**E9** — Pre-2023 AI uses (LLM landscape pre-saturation)
**E10** — Same-source duplicates (same paper as primary source for two cases without distinct framings; ≥30% disjoint role-cell coverage required for stratified-pair admission)

## 5. Saturation rule (v0.5 — strict form)

**Rule:** *Stop adding cases only when no new cases are producing new function-classifications outside those already classified.*

The "three consecutive new cases" allowance from prior versions is removed. **Any** new case producing a new function-classification disqualifies the saturation claim.

**Operationalization:**
- Maintain a function inventory updated after each case is decomposed under the methodological-detail decomposition rubric
- After each new case is coded, compute: did this case introduce ≥1 function-classification not previously in the inventory?
- Saturation is declared only when **N consecutive screened cases all yielded zero new function-classifications**, where **N = 8** (pre-committed in this preregistration)

The N=8 value is chosen to be conservative enough to guard against premature saturation declarations while not so large as to require unbounded recruitment. The choice is recorded here before any case-screening for saturation purposes begins.

**Rationale for the strict rule:** Premature saturation declarations are a known pitfall in grounded-theory practice (Bowen 2008; Saunders et al. 2018). The "three consecutive" allowance from earlier versions tolerated a noise window that this preregistration removes. Fewer false saturation claims; more honest accounting of theoretical reach.

## 6. Path A commitment (sample-recruitment strategy)

**Choice (pre-registered):** Path A — continue searching until the v0.5 saturation rule is satisfied.

**Rationale for Path A over Path B:** Path A honors the strict saturation rule directly; Path B (acknowledge open inventory and proceed with v0.4 sample) is pragmatic but weakens the analytical generalization. For a methods-oriented ORM submission where the constitutive/throughput typology IS the contribution, the typology's defensibility depends on the function inventory being adequately saturated. Path A is the more defensible choice; the resource cost is acceptable.

**Currently NOT-YET-SATURATED status (per v0.5 re-evaluation of v0.4 sample):**
The v0.4 candidate registry (~41 cases) is **not yet at saturation** under the v0.5 rule. The most recent addition (Case L — Ludwig & Mullainathan econometric framework) introduced ≥4 new function-classifications:
1. Validation-sample collection for measurement-error correction (Lee-Sepanski 1995 / Chen 2005 lineage)
2. Training-leakage check (Assumption 1: independence of sampling indicators across strings)
3. Prompt-text-as-disclosure (prompt as part of published methodology)
4. Temporal-disclosure of model weights status (open vs. proprietary; publication date vs. sample-construction date)

Because Case L expanded the function inventory, the saturation counter resets to zero. The next ≥8 consecutively-screened cases must all yield zero new function-classifications before saturation can be declared.

**Target stages for next-round case recruitment:**
- Physics / chemistry methods automation (under-represented)
- Lab-notebook / experimental-record automation (absent)
- Replication-study workflows (Cases 27, 28 cover some; more recent work exists)
- AI in IRB / research-ethics review (likely absent)
- AI in citation-management / bibliographic workflows (under-represented)
- AI in survey-item generation / scale development (NEW B covers data collection but not item generation)

**Stopping condition:** Recruit and screen one batch at a time. Update the function inventory after each addition. Declare saturation when N=8 consecutively-screened cases produce zero new function-classifications. If this never converges within a resource ceiling (e.g., 60 total screened cases), invoke a documented escalation procedure: either widen the function-classification grain (and re-evaluate), or transparently acknowledge non-saturation in the manuscript.

**Documentation:** Each case-screening's verdict on "new function-classifications introduced" is logged in `40_question1_study/saturation_log.csv` (created on first additional screening). The log shows the full audit trail of additions and their function-inventory effects.

## 7. Coding protocols

**7a. Inferential-commitment-extraction protocol.** Already drafted in this conversation; v0.1. Operationalizes C1. Two coders independently extract commitments from each included case; κ ≥ 0.70 on the per-commitment-judgment.

**7b. Methodological-detail decomposition rubric.** Already drafted in this conversation; v0.1. Operationalizes C2 / C3 / C4. Two coders independently decompose each case; κ ≥ 0.70 on each of C2, C3, C4 individually.

**7c. Constitutive-vs-throughput coding protocol.** **STILL TO DRAFT.** Will operationalize the counterfactual delegation test per (function × case) cell. Three-category outcome (Constitutive / Throughput / Contested). Two coders independently code; κ ≥ 0.60 on the C/T/X judgment.

All three protocols are pre-committed before main-pass coding begins. Calibration-pass results (5 anchor cases per protocol) are recorded and the protocols may be amended once after calibration; amended protocols are re-timestamped.

## 8. Reliability protocol

| Stage | Coders | Subsample | Threshold |
|---|---|---|---|
| Inclusion verdicts (C1–C7 + E1–E10) | 2 | 20% of all screened cases | κ ≥ 0.70 on inclusion judgment |
| Inferential-commitment extraction | 2 | 20% of included cases | κ ≥ 0.70 on per-commitment validity |
| Methodological-detail decomposition (C2/C3/C4) | 2 | 20% of included cases | κ ≥ 0.70 on each criterion |
| Constitutive/Throughput coding | 2 | 25% of included cases | κ ≥ 0.60 on C/T/X verdict |

**Disagreement resolution:** Cases with discrepant verdicts go to consensus discussion or third-coder adjudication; resolution logged in `40_question1_study/disagreement_log.csv`.

**Falsification of the protocol-itself:** If post-calibration κ on any single criterion < 0.50, the protocol is judged inadequate and re-drafted (new calibration pass). Between 0.50 and the threshold, the protocol is amended once and re-calibrated.

## 9. Analytical falsification criteria

**Sample-level falsification:**
- If <50% of (function × case) cells code C/T (i.e., >50% are Contested), the binary distinction lacks empirical traction and the typology is judged not viable; report the failure and pivot to an alternative framework.
- If a "robustly constitutive" function (defined as constitutive in ≥75% of cases where it appears) is shown to be successfully AI-delegated in any case in the sample with the inferential commitment surviving, the constitutive label for that function is judged falsified; the function is re-coded as conditional or throughput depending on patterns.

**Theoretical falsification:**
- If the constitutive/throughput distribution shows no relationship to research stage, AI capability, or task evaluability, the typology has no explanatory traction; the manuscript reports a null finding.

**Coding-pass falsification (procedural):**
- See §8.

## 10. Replication path

The full pipeline is reproducible via:

```
1. Fetch case sources from URLs in candidate_registry_v0.X.md
2. Extract via pymupdf (for PDFs) or BeautifulSoup (for HTML)
3. Apply clean_extracted_text.py (in 09_scripts/)
4. Apply inferential-commitment-extraction protocol (humans with calibrated coding)
5. Apply methodological-detail decomposition rubric (humans with calibrated coding)
6. Apply constitutive/throughput coding protocol (humans with calibrated coding)
7. Aggregate to (function × case) matrix
8. Compute per-function constitutive-share + per-function-condition truth tables
9. Apply Holm correction across the family of confirmatory tests
```

The PDF and extracted text are gitignored per existing copyright policy (`03_raw_sources/`, `04_extracted_text_cleaned/`); replicators re-fetch from canonical URLs.

## 11. Disclosure

The first author conducts all coding (with second-coder calibration on subsamples). Generative AI is used for prose editing of the preregistration and the eventual manuscript, NOT for any coding judgment in C1–C7 or in the constitutive/throughput coding pass. The two-coder structure includes one human coder + one human second-coder; no AI coder.

Funding: none. Competing interests: none declared.

## 12. Pre-registration ordering proof

The git commit history of this file in `40_question1_study/OSF_preregistration_question1.md` precedes:
- Any further candidate-registry updates beyond v0.5
- Any C1-C7 inclusion verdict on new candidates introduced after this commit
- Any constitutive/throughput coding pass

OSF timestamping (uploading this document to OSF as a Registration) is the recommended next step for stronger external proof; the current registration is in-repository only.
