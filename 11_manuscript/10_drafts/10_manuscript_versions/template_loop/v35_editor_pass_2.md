# A Behaviorally-Anchored Rubric for Coding Role-System Change Under AI Embedding: Comparative Typology Audit of 36 Cases

## Abstract

Debate about AI in research is still often framed as a contest between humans and models. That framing is too coarse for the current evidence. We make three contributions. *First*, we recast a source-backed repository of 36 AI-in-research cases as a role-system dataset, with 93 source rows, 144 evidence extracts, and 612 role × case codings traced to local full-text PDFs. *Second*, we develop a behaviorally-anchored rubric distinguishing six role statuses — robust, conditional, transformed, shrinking, split pressure, merge pressure — mutually exclusive within each (role × case) cell. *Third*, we apply the rubric to the 36 cases and report the resulting pattern: three procedural-validity roles (protocol-and-provenance architect, calibration architect, accountability-and-labor allocator) co-occur as a *durable* configuration in 12 of 36 cases, 1.52× the count expected under marginal independence — the candidate *epistemic-guardian* signature; three throughput clusters shrink in 40 observations (routine first-pass screening, high-consensus coding on ground-truth-rich tasks, structural prose polishing). H3 is supported as a cell-level association (*p* = 0.0002) but does not reach significance under the clustering-aware case-level null at *N* = 36 (*p* = 0.58). Inter-coder agreement was below the pre-committed κ ≥ 0.60 threshold; v1.1 instruments (configural-invariance test, marker-variable CMV bound, human second-coder pass) are pre-committed. We offer this as a candidate framework with a v1.0 rubric and hope it serves as a catalyst for instrument-grade audits of role-system change under AI embedding.

## 1. Introduction

Claims that AI is reshaping research labor are ubiquitous, and the recent review literature catalogues both what large language models can do across social-science workflows and what they cannot. Surveys of generative AI in social-science research (Bail, 2024; Grossmann et al., 2023) and benchmark evaluations across computational social-science tasks (Ziems et al., 2024) document substantial capability ranges; practical guides describe how to use LLMs for text analysis (Törnberg, 2023). What remains thin is the vocabulary used to adjudicate role-level claims. Methods-journal reviewers increasingly face manuscripts whose automation claims straddle the line between shrinkable task clusters — routine screening, high-consensus coding, structural prose polishing — and constitutive research roles where meaning, provenance, calibration, and accountability are at stake. A shared coding vocabulary for that adjudication does not yet exist, and the resulting debate oscillates between blanket displacement narratives and blanket continuity narratives without a role-level evidence base.

*Organizational Research Methods* has a sustained tradition of behaviorally-anchored audit rubrics (Aguinis et al., 2023; Hickman et al., 2022; Bergh et al., 2017 on credibility) but has not yet produced one for adjudicating role-level automation claims at the (role × case) cell level under AI embedding.

This paper offers methods-journal readers a behaviorally anchored rubric for coding role-status change in research workflows under AI involvement, and a worked application of that rubric to 36 cases. We treat the role, not the human or the model, as the unit of analysis — though we note that the rubric's *transformed* anchor was developed on AI-embedding cases and is not symmetric to non-AI comparison. The rubric distinguishes six statuses on two axes: an *allocation* axis (robust → conditional → transformed → shrinking) tracking how human performance yields first scope, then content, then volume as AI is embedded; and a *specification* axis (split and merge pressure) revising the unit of analysis itself. We propose the rubric, report inter-coder agreement on a pre-specified subsample, and release the case files so the rubric can be applied, contested, and extended.

Before describing the audit, we clarify the rubric's paradigm location. The audit operates within the modernist measurement tradition of organizational research, in the construct-validity lineage. It engages the configurational-theorizing, content-analysis, typology-as-theory, organizational-routines (ostensive aspect), and high-reliability-organizing traditions. Adjacent traditions — paradox-theoretic, institutional, practice-theoretic, evolutionary — name rival readings the v1.0 rubric does not adjudicate; the §6 reliability and limits section identifies them.

A recurring framing problem in this literature is to ask whether "humans" or "AI" perform better — a framing that is sometimes appropriate but is too coarse for the role-level evidence base assembled here. Research is not one task: it is a role system composed of boundary setting, procedure design, coding, calibration, interpretation, accountability, repair, disclosure, and many other forms of labor. We use *role system* to mean a set of activity-level roles individuated by their contribution to epistemic validity, distributable across human and non-human performers, and observable through behavioral anchors rather than occupational title. The construct draws on three lines of prior work and rescales each. From the sociology of professions, it borrows Abbott's (1988, 2005) jurisdictional mechanisms — diagnosis, legitimation, segmentation, and consolidation — but rescales them from the occupational profession to the activity-level role; recent work in this tradition (Eyal, 2013) similarly treats *expertise* rather than *the profession* as the unit at which jurisdictional change is observed. From classical role theory, it borrows the relational specification of role bundles (Merton, 1957) but operationalizes them as behaviorally observable activities; the recent role-theory synthesis treats roles as structured, partially overlapping bundles within an intrapersonal network (Ramarajan, 2014), an idea the rubric extends from the human person to the activity-level role under AI embedding.

The rubric's central constructs are distinguishable from their closest predecessors: *status* operates at the activity-level role-cell rather than the occupational profession; *transformed* requires a verb-swap or new-sub-task anchor at the role-cell level (cf. Barley's 1986 occupational change); *split pressure* registers rubric-revision pressure on the audit instrument rather than identity-work performed by occupational members. Once the empirical unit shifts from "the human" to "the role," a different picture appears. The strongest current evidence does not point to blanket human replacement. It points to uneven redistribution: durable human roles where meaning, admissible procedure, provenance, calibration, and accountability are at stake, and cleaner shrinkage where tasks have public ground truth or a strong audit trail (Keith, 2026; Baccolini, 2026; Larson, 2024; Kang, 2025).

This paper develops that claim from a completed 36-case database spanning contested political measurement, review screening, synthetic respondents, reflexive memoing, autonomous empirical analysis, reproducibility assessment, manuscript co-writing, and autonomy-heavy research systems.

The paper asks a straightforward research question: across the full repository, which human research roles are robust, conditional, transformed, shrinking, or mis-specified under generative, agentic, and predictive AI? It carries three hypotheses into the comparative analysis. First, boundary-setting and procedure-setting roles should survive more often than routine production tasks. Second, shrinkage should cluster where tasks have public ground truth and clean post hoc auditability. Third, role status should vary more by research stage and institutional setting than by AI capability label alone.

The argument is narrower than many automation narratives: the repository becomes most useful once read as a role-system archive, where the durable question is not "can the model do research?" but "which human roles remain constitutive of epistemic validity when models become embedded in the workflow?"

The contribution is *methodological* — a behaviorally-anchored rubric for coding role-status change at the (role × case) cell level — with a secondary *integrative-theoretical* component that rescales Abbott's jurisdictional mechanisms from occupation to activity-level role: *robust* corresponds to settled human jurisdiction over an activity's diagnostic or legitimation function; *conditional* to contested moderator-dependent jurisdiction; *transformed* to jurisdictional content revision (humans retain the territory but redefine what is done within it); *shrinking* to deskilling and task-cluster delegation; *split pressure* to jurisdictional segmentation; *merge pressure* to consolidation. The rubric's behavioral anchors are operationalizations of these mechanisms, not atheoretical labels. The rubric extends ORM's measurement-tradition lineage at a level that lineage has not yet covered; the paper does not claim a stand-alone theoretical contribution in the Whetten (1989) sense.

## 2. Data and Design

### 2.1 Sampling and case selection

The analysis is built from a local database rather than from a narrative reading of a few high-profile examples. Cases were seeded by the following rule: (i) published or preprinted 2023–2026; (ii) primary empirical object is AI use in a research step — measurement, screening, interpretation, synthesis, reproducibility, authorship, or autonomous pipelines; (iii) full text retrievable for coding. The sampling logic follows the systematic-review tradition of explicit inclusion rules and reporting (Page et al., 2021; Tranfield et al., 2003; Siddaway et al., 2019). The 36-case audit is best characterized in Snyder's (2019) three-type framework as a *semi-systematic* review: it maps theoretical approaches (the eight starting roles plus six split-candidate roles) and identifies knowledge gaps (the rubric-revision pressure documented as split and merge pressure) rather than aiming for an exhaustive enumeration. The seed pool was assembled from targeted searches of methodological venues plus forward and backward citation from four anchor papers (Törnberg, 2025; Keith, 2026; Larson, 2024; Kang, 2025), and supplemented with preprint-server queries for autonomy-heavy systems not yet peer-reviewed. A dropped-case list with exclusion reasons is released alongside the database.

The seed strategy concentrates on AI-in-research projects that are visibly identified as such — methodological-venue search and forward/backward citation preferentially surface high-visibility cases — and we acknowledge a *visibility-bias* limitation that operates at the case-selection layer separately from publication bias on individual cases (Bail, 2024). The 36 cases sample from a larger population of attempted AI-in-research workflows whose population boundary the rubric does not name; an evolutionary reading (Aldrich & Ruef, 2006; Hannan & Freeman, 1977) treats publication as a non-random selection mechanism and the durable-roles signature as partly the selection-survivorship residue.

### 2.2 Database, recording units, and coding logic

The recording unit for coding is the (role × case) cell, the context unit is the full case file plus its registered secondary sources, and the encounter sequence directs the coder to read the case's abstract and methods before encountering the evidence extracts (Krippendorff, 2011; Hruschka et al., 2004). The database contains 36 seeded cases, 93 source rows (57 external), 144 evidence extracts, and 612 role-coding rows. All 36 cases are analysis-ready; every primary source cited is stored locally as full-text PDF or lawful green-OA deposit. After a full-text review pass, 437 of the 612 role-coding rows are high-confidence, 165 medium-confidence, and 10 low-confidence, so the comparative claims below rest on direct source evidence rather than on workbook defaults. The cases cover eight family clusters, with particularly strong representation in predictive simulation and design, measurement and coding, evidence synthesis, qualitative interpretation, and reproducibility. This structure creates a comparative frame in which cases can be aligned on role status, evidence strength, research stage, institutional setting, autonomy pressure, task ground truth, and post hoc auditability.

Role-status assignment is a form of content analysis (Stemler, 2001; Duriau et al., 2007; Hruschka et al., 2004). The coding logic begins from a starting typology that includes relevance adjudication, mechanism discipline, construct and perspective boundary setting, corpus pluralism, protocol and provenance architecture, counterfactual and transportability judgment, situated interlocution or context witnessing, and accountability or labor allocation. It then permits three kinds of revision pressure: roles may *split* (calibration becoming a distinct role rather than a subpart of transportability judgment), *merge* (roles inseparable in practice), or be re-read as *shrinking task-clusters* where routine throughput dominates the work. The audit's load-bearing tradition is *content analysis in the Krippendorff sense*, augmented by case-based theorizing (Eisenhardt, 1989) and typology-as-theory-building (Doty & Glick, 1994).

This is a typological audit with association statistics, not a Qualitative Comparative Analysis (QCA): at *N* = 36 cases × 17 roles, truth-table minimization is non-identified, so the consistency and coverage measures in §4 are used descriptively rather than as the inferential engine. The comparative design is disciplined in two ways. First, every analytic field traces back to source identifiers plus local files or URLs. Second, the paper treats live-project and autonomy-heavy systems conservatively: Project APE, AgentSociety, and The AI Scientist are included because they stress the typology, not because they settle it. H1 and H2 are pattern-level claims aggregating across roles; H3 is a role-level claim tested via a paired sign test across 16 roles with defined *V*. Tables 2 and 3 report aggregate distributions; §6 reports the confirmatory test.

### 2.3 Rubric development (v0.1 → v0.4)

The rubric in Table 1 was developed iteratively. Behavioral anchors are operationalizations of the role-construct in the validity sense developed in measurement theory: anchors are observable features that license inferences about the underlying status, and the rubric's claim is to construct validity in the Cronbach-Meehl-Messick lineage (Cronbach & Meehl, 1955; Messick, 1995; Borsboom et al., 2004), where validity is a property of inferences rather than of the instrument alone. The mutability of the typology — its capacity to admit split and merge pressure — follows the typology-as-theory-building tradition: typologies are productive when they are revisable under empirical pressure (Doty & Glick, 1994; Fiss, 2011; Delbridge & Fiss, 2013; Cornelissen, 2017; Cornelissen et al., 2021). The rubric performs configurational theorizing in the sense of Furnari et al. (2021): the typology's mutability operationalizes their *scoping*, *linking*, and *naming* heuristics.

The four v0.1 base statuses were not a priori categories: *robust* and *shrinking* surfaced in the first read-through of Cases 1–2 as the polar anchors the case-text language itself supplied; *conditional* and *transformed* were filled in by constant comparison across the next six cases. The rubric grew across four versions: v0.2 added *split pressure* after Case 3 (Gligorić) showed *construct and perspective boundary setter* conflated diagnostic and sampling sub-activities; v0.3 added *merge pressure* after Case 10 (Hajishirzi) showed provenance and accountability inseparable; v0.4 tightened the conditional-vs-transformed tie-breaker. Split pressure is recorded when (a) at least two cases within the same primary AI capability show status divergence across conflated sub-activities and (b) the divergence reflects distinct sub-activities rather than magnitude variation; *corpus pluralist* fails (b) and is excluded. Merge pressure is recorded when evidence for two roles is inseparable within a single case. A date-stamped codebook version history is released with the database. The four-case pilot also served as coder-development: the first coder re-coded Cases 1 and 2 under v0.4 to verify earlier codings remained stable; full-corpus stability is a v1.2 commitment.

### 2.4 Construct form, scope conditions, and edge cases

The six statuses constitute a categorical typology (Doty & Glick, 1994); cells are mutually exclusive within applicable (role × case) cells but the typology is not exhaustive (37 cells coded *unclear*, 316 *not_applicable*), so *V* values in §6 are read against the 259-cell observable-and-coded denominator. The anchor-status relationship is *formative* (Edwards & Bagozzi, 2000): anchors constitute the status by definition. The rubric codes the *ostensive* aspect of role behavior in the Feldman & Pentland (2003) sense — the abstract pattern as case authors describe it — not the *performative* aspect; the κ failure on *conditional* and *transformed* (§6) is partly diagnostic of that scope. The codings are single-snapshot slices presupposing local equilibrium; for cases where the role is co-constituted with an iteratively-updated learning algorithm (Faraj & Pachidi, 2021), the snapshot may be a moment in ongoing co-evolution, and the v1.1 two-snapshot transition-direction test is the appropriate instrument. The audit codes at the activity-level role, jointly across the individual and team performer level; the v1.1 within-case extension flagged in §6 separates the two. The *transformed* anchor's before/after language is scope-conditioned to author-stated retrospective verb-swap or new-sub-task language quotable from the case file, not to observed longitudinal transition.

The framework's role-status codings are licensed for (i) published or preprinted research-workflow cases where AI involvement is visibly identified as such; (ii) the 2024–2026 capability window; (iii) English-language venues. The framework is *not* licensed for industry-internal or quietly-deployed AI-in-research workflows; pre-2024 cases where the *transformed* anchor would be coded against an unobserved baseline; substantive subfields outside the eight case-family clusters represented (e.g., bench biology, formal economics); or cross-occupation aggregation, which presupposes occupational invariance the audit has not established (the v1.1 occupational-coding extension is the appropriate instrument). Generalization beyond these scope conditions is empirically open, not assumed.

Three edge cases required explicit adjudication rules: (i) *multi-version cases* — for preprints that later appeared in a peer-reviewed venue (Cases 25, 32, 34), we coded the version on which the empirical evidence is strongest, recording the version selection in the case registry; (ii) *joint-performance cases* where human and AI co-execute the role without a clean lead performer are coded *conditional* by default, flagged so a second coder can reopen the decision; (iii) *cases that redefine the role mid-analysis* (Xiao, n.d., 150-agent multiverse is the clearest instance) are coded on the final role definition used for the paper's inferences. Approximately 28 of the 612 cells are tagged with one of these three edge-case notes in the released database.

### 2.5 Decision flow and rubric

Figure 1 is a coder-workflow schematic showing the order in which a coder consults the rubric's decision points when applying Table 1 to a new (role × case) cell. It is not a decision tree over rubric *outputs* — the six statuses are not strictly hierarchical — but it records the sequence in which observability, reconfiguration, and the conditional-vs-transformed tie-breaker are checked. The feedback edge to *rubric revision* annotates the downstream pressure that *split* and *merge* codings place on the rubric itself. Table 1 specifies the rubric's diagnostic criteria by status.

![Figure 1. Role-coding decision flow (coder-workflow schematic). Each (role × case) cell passes through the observability gate, then the reconfiguration gate, then the allocation sub-gate (tie-breaker), in that order. The split / merge pressure terminal annotates the rubric-revision feedback that these codings trigger for the next rubric version.](figure_1_decision_flow.png)

Before reporting the role-status distribution, Table 1 specifies the rubric used to code it.

**Table 1. Role-status rubric with behavioral anchors.** Each status is defined by observable features of the case so that a second coder can apply the rubric without consulting the authors. Rows are mutually exclusive within a (role × case) cell but not across cells of the same role: a single role may be *robust* in one case and *shrinking* in another.

| Status | Operational definition | Diagnostic criterion — signature pattern and its behavioral indicators | Counter-indicator (evidence *against*) |
|---|---|---|---|
| Robust | The role is performed by humans and is treated by the case authors as load-bearing for the study's inferences. (The rubric operationalizes *author-stated* load-bearingness as an observable proxy for contribution to epistemic validity; it does not independently adjudicate whether the role genuinely warrants the inferences.) | (a) A section heading, methods paragraph, or limitations paragraph names this role (or a near-synonym) as load-bearing for the study's inferences; (b) authors specify human labor at this step and describe why AI substitution would not preserve validity; (c) the role recurs in the reported limitations as a constraint on what the study can claim. | Case reports AI performing the role without human checking and reports no validity loss. |
| Conditional | The role is performed by humans contingent on specified moderators (task features, data quality, institutional setting); AI can partially substitute outside those moderators. | (a) Case specifies the conditions under which human performance is needed; (b) reports empirical variation in AI adequacy across those conditions; (c) retains a human-in-the-loop step for edge cases. | Case reports blanket human or blanket AI performance with no moderator analysis. |
| Transformed | The role persists but its content has been redefined around AI involvement (e.g., from drafting to reviewing, from coding to auditing, from authoring to disclosing). | (a) Authors explicitly flag a change in what humans do at this step, using before/after language or a verb swap (e.g., "write" → "review"); (b) new sub-tasks (disclosure, credit allocation, calibration audit) are introduced and named as new; (c) the case reports at least one human activity at this step that would not be recognizable in a pre-AI description of the role. | Case reports the role as unchanged, or reports it as absent. |
| Shrinking | The task-cluster is increasingly performed by AI with human labor reduced to audit or exception handling; the role label is retained but its scope has contracted. | (a) Public ground truth or high-consensus targets exist; (b) case reports AI matching or exceeding human performance on a defined subset; (c) residual human labor is characterized as rescue, triage, or verification. | No public ground truth; disagreement across coders is the inferential object. |
| Split pressure | The case reveals that the starting role conflates two distinct activities that should be coded separately (e.g., *construct boundary setting* and *perspective sampling*). | (a) AI performance differs systematically across the conflated sub-activities; (b) the case's own analysis distinguishes them; (c) collapsing them back into one role loses substantive information. | Case treats the role as indivisible and the evidence supports that treatment. |
| Merge pressure | The case reveals that two starting roles are entangled in practice and cannot be cleanly separated without losing information (e.g., *authorship* and *labor allocation* in LLM-assisted drafting). | (a) The case's evidence for one role is inseparable from evidence for the other; (b) attempting to code them independently produces arbitrary splits; (c) the case authors themselves treat the two as a joint object. | The two roles are coded independently with no loss of information. |

When a case satisfies indicators for both *conditional* and *transformed*, apply the three-part tie-breaker. (i) *Conditional* requires the case to name at least one *explicit moderator variable* — a specific feature of the task, data, or institutional setting — under which human performance is needed. Inference from adjacent discussion is not sufficient. (ii) *Transformed* requires at least one *explicit role-content change* — a named new sub-task, a before/after verb swap, or an activity that would not be recognizable in a pre-AI description of the role. Mere presence of AI in the workflow is not sufficient. (iii) If neither (i) nor (ii) can be documented with a quotable sentence from the case file, the cell defaults to *unclear*, not to either candidate status. The `observable`-vs-`not_applicable` threshold is correspondingly strict: a role is observable only if the case file contains at least one sentence that could be quoted as evidence of that activity being performed or deliberately not performed. This tighter tie-breaker was introduced in response to the Appendix B reliability pass (Cohen's κ = 0.289), which identified the conditional-vs-transformed distinction and the observable-vs-`not_applicable` threshold as the two most-common disagreement axes.

With the rubric in hand, Table 2 reports the role × status counts that §§3–5 unpack.

**Table 2. Role × status counts across all 36 cases.** Counts are case-level: the unit is one role × one case. Columns `unclear` and `not_applicable` are the complements that sum rows to 36.

| Role | Role group | Robust | Conditional | Transformed | Shrinking | Split pressure | Merge pressure | Unclear | Not applicable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Relevance adjudicator | starting_role | 1 | 8 | 3 | 0 | 1 | 0 | 6 | 17 |
| Mechanism disciplinarian | starting_role | 2 | 6 | 2 | 0 | 4 | 0 | 4 | 18 |
| Construct and perspective boundary setter | starting_role | 3 | 4 | 2 | 0 | 4 | 0 | 1 | 22 |
| Corpus pluralist | starting_role | 2 | 7 | 2 | 0 | 0 | 0 | 2 | 23 |
| Protocol and provenance architect | starting_role | 15 | 5 | 7 | 0 | 4 | 1 | 1 | 3 |
| Counterfactual and transportability judge | starting_role | 2 | 11 | 2 | 0 | 3 | 0 | 0 | 18 |
| Situated interlocutor / context witness | starting_role | 4 | 2 | 1 | 0 | 2 | 0 | 0 | 27 |
| Accountability and labor allocator | starting_role | 5 | 8 | 7 | 0 | 6 | 1 | 7 | 2 |
| Construct boundary setter | split_candidate | 5 | 5 | 1 | 0 | 2 | 0 | 2 | 21 |
| Perspective sampler | split_candidate | 2 | 2 | 0 | 0 | 4 | 0 | 0 | 28 |
| Counterfactual / transportability judge | split_candidate | 0 | 12 | 0 | 0 | 3 | 0 | 4 | 17 |
| Calibration architect | split_candidate | 8 | 10 | 1 | 0 | 2 | 0 | 5 | 10 |
| Situated interlocutor | split_candidate | 3 | 3 | 0 | 0 | 2 | 0 | 0 | 28 |
| Context witness | split_candidate | 4 | 6 | 1 | 0 | 1 | 0 | 2 | 22 |
| Routine first-pass screener | shrinking_task_cluster | 0 | 0 | 0 | 13 | 0 | 0 | 1 | 22 |
| Routine coder on high-consensus, ground-truth-rich tasks | shrinking_task_cluster | 0 | 1 | 0 | 15 | 1 | 0 | 1 | 18 |
| Structural prose polisher / drafter | shrinking_task_cluster | 0 | 2 | 1 | 12 | 0 | 0 | 1 | 20 |

## 3. Durable Roles: Procedure, Boundary Setting, and Calibration

### 3.1 Exemplars

Before turning to the durable-role pattern, we name one exemplar case per status to index the argument. We label these exemplars *prototypes* in the Lord et al. (1984) sense rather than only as illustrative cases: each was the cognitive referent against which subsequent codings of that status were prototype-matched. A second coder lacking access to these prototypes will have to reconstruct them from the anchors alone, and the per-status κ failure on *conditional* and *transformed* (§6) is partly diagnostic of that prototype-reconstruction failure. For *robust* roles, Keith (2026; Case 2) exemplifies *construct and perspective boundary setter*: the codebook turns broad political ideas into operational constructs, defines edge cases, and makes error analysis methodologically legible before any model is treated as a measurement instrument. For *conditional* roles, Baccolini (2026; Case 7) exemplifies *protocol and provenance architect in its conditional register*: compact LLMs reduce screening workload, but admissible-evidence rules, gray-literature rescue, and provenance logging remain human-performed and contingent on task features. For *transformed* roles, Yin (n.d.; Case 29) exemplifies *accountability and labor allocator*: once LLM-assisted drafting is embedded, the role persists but its content shifts toward disclosure, credit allocation, and version-history discipline rather than toward writing itself.

For *shrinking* task clusters, Törnberg (2025; Case 1) exemplifies the *routine coder on high-consensus, ground-truth-rich tasks*: GPT-4 outperforms supervised classifiers and human coders on objective party-affiliation annotation, yet the surrounding interpretive role is not removed. For *split pressure*, Gligorić (n.d.; Case 3) exemplifies the need to split *construct and perspective boundary setting*: disagreement across subgroups is itself the quantity of interest, so a single correction target collapses the inferential object. The split-pressure coding is recorded on the starting-role "construct and perspective boundary setter"; the database's two split-candidate roles (construct boundary setter, perspective sampler) are then coded separately. For *merge pressure*, Hajishirzi (2026; Case 10) is the exemplar: in retrieval-augmented literature synthesis, *protocol and provenance architecture* and *accountability and labor allocation* cannot be coded independently because the provenance trail — which citations are real, which are hallucinated — is inseparable from sign-off authority. Merge pressure is rare in the repository (*n* = 2, both on Case 10); it is retained in the rubric because the substantive pattern matters, not because it is common.

Cases are named as exemplars of one status each for expositional economy; the full status profile for every case is in the released database. Exemplar selection in case-based management methodology has well-known risks of cherry-picking and of theoretical replication-vs-direct-replication confusion (Eisenhardt, 1989, 2021; Flyvbjerg, 2006; Langley, 1999; Welch et al., 2011, who distinguish four methods of theorizing from cases — inductive, interpretive, natural-experiment, contextualised explanation — and argue for pluralism rather than a single exemplar logic); we address those risks by (a) selecting one exemplar per status from cases the rubric's anchors fire on cleanly, (b) disclosing pilot-origin for the three exemplars that were in the rubric-development pilot (Keith, 2026 / Case 2; Baccolini, 2026 / Case 7; Törnberg, 2025 / Case 1), and (c) holding their exemplar-status labels fixed through the main coding pass. The disagreement log released with the database records any pilot-vs-main-pass status revisions. Exemplars are referenced by case ID throughout §§3–5.

### 3.2 The procedural cluster: protocol-and-provenance, calibration, and accountability

The clearest durable pattern is procedural. Protocol and provenance architect is robust in 15 cases, conditional in 5, and transformed in 7 — 27 cases in robust, conditional, or transformed status and zero shrinking, with 5 further cases registering split or merge pressure. The same mixed profile recurs for accountability and labor allocator (5 robust, 8 conditional, 7 transformed): *transformed* is a common landing point for roles that redefine rather than abandon procedural work. The codebook has to turn broad political ideas into operational constructs, define edge cases, and make error analysis methodologically legible (Keith, 2026; see §3.1). Procedure is not residual to the task; it constitutes the task.

We adopt a *constitutive* reading of the durable-roles pattern: procedural roles are individuated by the rubric's anchors as the role-cells whose performance case authors treat as load-bearing for inferential validity. That this signature concentrates on three roles (procedure, calibration, accountability) — rather than dispersing — is the substantive finding the audit licenses. The three durable roles together discharge what the HRO literature (Weick & Sutcliffe, 2007) describes as *mindful organizing*: preoccupation with failure (calibration), reluctance to simplify (provenance), sensitivity to operations (procedure), commitment to resilience and deference to expertise (accountability). Codebook-equivalents — Keith's construct definitions, Baccolini's inclusion rules, Larson's calibration benchmark — recur as the artifact through which procedural roles remain human-anchored even when LLMs perform the underlying classification.

The same logic reappears in review automation. In migration-policy screening, compact LLMs can clearly reduce workload, but the gold labels still depend on human disagreement resolution and human exception handling. More importantly, the most sensitive parts of the workflow are not the mechanics of first-pass triage but the design of inclusion rules, gray-literature rescue, and provenance logging (Baccolini, 2026). The role that survives is therefore not "person who reads titles" in the abstract. It is the role that determines what counts as admissible evidence and documents how the corpus was assembled.

At the case-configuration level, the durable-roles claim takes a sharper form. Treating each case as a 17-tuple of role-statuses and collapsing status to `durable` (robust / conditional / transformed), `shrink`, `pressure` (split / merge), or `na`, the modal configuration on the three H1 roles is `durable | durable | durable`, occurring in 12 of 36 cases. A further 12 cases carry durable on two of the three (typically protocol + accountability, with calibration `not_applicable`); only two cases carry pressure-status on all three. Marginal P(durable) on the three H1 roles is 0.750, 0.528, and 0.556 across the 36 cases; under marginal independence the expected count of all-three-durable cases is 7.92, and the observed 12 is 1.52× expected. The triple co-occurrence is a real configurational signal, not a sum of marginal coincidences. The lift is descriptive within-sample: it is conditioned on the visibility filter (publishable workflows over-represent durable procedure) and on procedural-prose density (cases that write more about procedure register more procedural-robust codings; Williams et al., 2010). The durable-status collapse (robust + conditional + transformed) absorbs the per-status disagreement on *conditional* and *transformed* that §6 documents, so the 12-of-36 lift survives even when the individual transition-coded anchors do not.

We label this cluster the *candidate epistemic-guardian signature* (v1.0) and define it operationally as a (case × three-H1-roles) profile in which all three roles carry a durable status; the qualifier reflects that the signature awaits the v1.1 within-case extension. The 36-case repository codes at the case level and cannot adjudicate whether the lift reflects intrapersonal role-attachment (Ramarajan, 2014), team-composition capacity (Woolley et al., 2010), or coordination-architecture clustering (Puranam et al., 2014); the v1.1 within-case extension that codes who-performs-the-role-cell is the appropriate test.

Calibration shows a related pattern. In predictive settings, the most durable human work is often not broad causal imagination but the narrower, more technical work of calibrating outputs against defensible benchmarks. The synthetic-respondent case is especially clarifying here. Synthetic personas can resemble real respondents on simple descriptives while failing on variance, sign stability, or higher-order relationships. The paper's own design therefore evaluates means, variance, correlations, prompt sensitivity, timing, and model differences rather than taking plausible-looking output at face value (Larson, 2024). This is exactly the kind of evidence that supports splitting calibration architecture from broader transportability judgment. The repository encodes that split directly: calibration architect is robust in 8 cases and conditional in 10, whereas the older transportability bundle appears far more often under split pressure. In jurisdictional terms, calibration architect is emerging as a segmented-then-consolidated sub-jurisdiction within what had been a single transportability role.

## 4. Shrinkage and Transformation: Throughput Tasks Are Not Whole Roles

If §3 traces where human roles consolidate, §4 traces where they contract. Shrinkage in this repository has three distinct jurisdictional shapes that are consistent with mechanisms catalogued in the labor-economics literature on automation; the audit codes the realized shape and does not adjudicate among the underlying mechanisms. *Deskilling* — the role's content is simplified and the skill demand on the human contracts — is consistent with Autor's (2015) routinization-pressure mechanism, and fits the Bleier (n.d.) reproducibility-repair pattern. *Delegation* — the task is reassigned to a non-human performer with humans retained for exception handling — is consistent with the substitution mechanism Frey and Osborne (2017) catalogue across occupational tasks, and fits the Törnberg (2025) objective-coding pattern. *Boundary redefinition* — the task cluster is excised from the human role altogether and the role narrows — is consistent with task-level automation reshaping occupational composition (Brynjolfsson & Mitchell, 2017), and the structural-prose-polishing pattern (Yin, n.d.; Cox, n.d.) is its role-level analog. The shapes are not deterministic outcomes of AI capability: they are *occasions* for structuring whose realized form is shaped by the occupational community into which the workflow lands (Barley, 1986). Each shape also implies a different configuration of the AI as an organizational member — primary performer, embedded tool, partial member — and the typology's value to an organization designing an AI-embedded research workflow is that it diagnoses which configuration is in play (Puranam, 2021). The "routine" descriptor here refers to *high-consensus repeatable throughput* (Autor, 2015), not to *organizational routines* in the Feldman & Pentland (2003) sense.

The shrinkage story is real but narrower than public discourse suggests. The database records routine first-pass screener as shrinking in 13 cases, routine coder on high-consensus ground-truth-rich tasks in 15, and structural prose polisher in 12 — 40 shrinking observations concentrated in 11 of 36 cases; 25 cases carry zero shrinking codings, the asymmetry §3 turns on. What unites these clusters is the joint presence of routinized output, clean evaluation, and low discretion about admissible procedure. Operating on a case-family proxy for public ground truth (Measurement & coding, Evidence synthesis & corpus, Reproducibility & autonomous research), the consistency score for (ground-truth-rich → has-shrinking) is 0.857 — clearing Ragin's (2008) 0.75 minimum but below the 0.90 strong-sufficiency threshold — and coverage is 0.500. The 0.500 coverage implies a second equifinal path: 9 of the 12 shrinking cases outside ground-truth-rich families concentrate in structural prose polishing where the task has *clean post-hoc auditability* (draft vs. published prose) rather than public ground truth. The two-path reading *ground-truth-rich* ∨ *clean-post-hoc-auditability* → *has-shrinking* recovers ~0.875 joint coverage; we report this as descriptive, not Boolean-minimized.

The objective party-affiliation case is the cleanest coding example. Here the task has public ground truth, and the paper finds that GPT-4 can outperform both supervised classifiers and human coders on identifying party affiliation from a single message across 11 countries (Törnberg, 2025). This is a harder case for the "role persists" reading than the surrounding cases, because Törnberg reports GPT-4 drawing on interpretive skills — contextual inference, implicit reference, cross-linguistic judgment — that had previously been treated as distinctly human. The rival explanation is built into the database itself: objective annotation may be unusually favorable terrain for automation and may not travel to contested constructs. The implication is not that "coding" disappears. It is that some high-consensus coding tasks shrink toward audit and exception handling, while the interpretive activities that Törnberg surfaces as newly machine-tractable migrate into the *calibration architect* role rather than disappearing.

Review screening shows a similar structure. Compact LLMs can operate effectively as a first-pass triage layer, but low precision and the need for rescue decisions keep the workflow human-accountable at the protocol level (Baccolini, 2026). Post-publication repair makes the pattern even sharper. In the controlled reproducibility testbed, agents and prompt-based systems can repair some broken code packages, especially when the environment is standardized and the failure mode is visible. But success varies materially with error complexity, context, and diagnostic quality (Bleier, n.d.). That means routine repair labor can shrink without collapsing the broader reproducibility role into automation.

Manuscript drafting belongs in the same family, but with a twist. Scientists using LLMs for drafting appear to publish more, yet the same evidence suggests that polished language can coexist with substantively weaker work (Yin, n.d.). Structural prose polishing therefore looks shrinkable, while evaluation, credit allocation, and disclosure become more important rather than less important (Cox, n.d.). Accountability and labor allocator is transformed in 7 cases, conditional in 8, and robust in 5, with 6 additional cases showing explicit split pressure — a much better fit for the evidence than a simple displacement story.

## 5. Split Pressure and Boundary Cases

Some of the most important lessons in the repository are not about robustness or shrinkage. They are about mis-specified roles. The case on multi-perspective annotation shows why. Where disagreement across subgroups is itself substantively meaningful, a single correction target or majority-vote label can erase the quantity of interest. The paper therefore treats the distribution of perspectives as the inferential object rather than as annotation noise (Gligorić, n.d.). That is difficult to fit inside a single undifferentiated "construct and perspective boundary setter." The repository is right to register split pressure here — in jurisdictional terms, the diagnostic sub-activity (which categories exist) is segmenting from the sampling sub-activity (whose perspectives count), which were formerly welded together.

Reflexive memoing and anthropological fieldnotes add a related pressure from a different direction. The fieldnote case argues that raw notes are cultural and communicative products that require reflexive interpretation attuned to local meaning systems, even when computational pipelines and generative models are layered into the analysis (Hernandez, 2025). The problem is not only construct definition. It is also whose perspective is being sampled and who can witness context that remains tacit in the textual trace.

Multiverse-style autonomous analysis and simulation cases strengthen the same conclusion. When 150 autonomous agents working from the same data and question still produce sizeable nonstandard errors because they diverge on measures and workflow choices, provenance and multiverse tracking become part of the analysis rather than an afterthought (Xiao, n.d.). And when large-scale simulation systems are used as testbeds for survey, interview, and intervention questions, calibration and transportability can no longer be the same human role (Li, n.d.). Split pressure is therefore not a weakness in the typology but a configurational finding: in Furnari et al.'s (2021) vocabulary, split pressure operates as the *scoping* heuristic and merge pressure as *linking*.

Five cases (25 and 26 Project APE, 32 The AI Scientist, 33 Deep Research, 34 AgentSociety) describe research systems built around AI capability from the outset. The rubric's *transformed* and *shrinking* anchors are coded against a hypothetical pre-AI decomposition; the affected cells are tagged and a sensitivity analysis excluding these cases is reported in §6 (Table 4). For research configurations that were never assembled in a pre-AI form, the rubric codes a counterfactual decomposition rather than an observed transition (Orlikowski, 2007; Suchman, 2007); the rubric is appropriate as a *separability-presupposing* audit instrument across the 36 cases and we do not claim it adjudicates fully co-constituted research systems.

Project APE and The AI Scientist concentrate the strongest current automation ambitions into visible systems. Project APE relies on tournament-style evaluation, model ensembles, and internal quality proxies that do not map cleanly onto journal, policy, or public-accountability standards (Project APE, n.d.). The AI Scientist draws most of its evidence from AI or machine-learning research rather than from social science (Ha, n.d.). These cases stress-test the typology without settling it.

## 6. Rival Explanations and Limits

### 6.1 Rival explanations

The repository is strong enough to support a comparative argument, but it is not immune to rival explanations. *Publication bias* matters: some cases become visible precisely because they are dramatic, novel, or unusually favorable to AI — the standard credibility-crisis concern in management research (Bergh et al., 2017; Ioannidis, 2005).

*Repository coding bias* also matters: even a well-documented database reflects earlier curation and coding decisions, and the coder's hypotheses-in-mind risk what Gelman and Loken (2014) describe as the garden of forking paths. The coding reported here is first-author-led (see §2 for confidence stratification and coding procedure).

*Benchmark artificiality* remains a live issue in the screening, reproducibility, and autonomy-heavy cases, where clean tasks or internal evaluation frameworks may flatter automation relative to messier live settings; the holistic-evaluation literature (Liang et al., 2022) and broader LLM evaluation surveys (Chang et al., 2024) document this gap between benchmark performance and deployed-context behavior, and the foundation-models literature catalogs the same artifact as a property of the models themselves (Bommasani et al., 2022; Weidinger et al., 2021).

### 6.2 Inter-coder reliability

To assess coding reliability, an independent second coder — a sandboxed LLM agent with context restricted to the rubric and case files — re-coded a stratified 10% subsample (four cases, 68 role × case cells) blind to the first coder's evidence summaries. The pass yields raw agreement 52.9% and pooled Cohen's κ = 0.289, 95% bootstrap CI [0.147, 0.439] (*B* = 2,000; seed 20260423); Krippendorff's α on the same data is 0.278 (7-cat) / 0.298 (8-cat). The result fails the pre-committed acceptance threshold κ ≥ 0.60 (McHugh, 2012). Per-status κ reveals the failure structure: *robust* (0.402) and *shrinking* (0.549) achieve moderate agreement; *conditional* (0.009) and *transformed* (0.000) show essentially no agreement above chance. We read the κ failure as construct-validity-relevant — the two failing anchors are configurationally non-invariant across case families (Vandenberg & Lance, 2000), and *conditional* and *transformed* describe role *transitions* whose observable features differ across families (Ramarajan, 2014). The LLM agent's lack of access to the §3.1 case prototypes amplifies the gap on transition-coded statuses; a human second-coder pass with calibration sessions on the §3.1 prototypes is the appropriate v1.1 instrument. Counts within the four allocation-related statuses are read as conditioned on textual legibility: tacit-knowledge-load-bearing roles may be systematically under-counted in *robust* (Barley & Kunda, 2001).

Two rubric refinements follow: the tie-breaker now requires an explicit moderator variable for *conditional* or explicit role-content change for *transformed*, with indeterminate cells defaulting to *unclear*; and the observable-vs-`not_applicable` threshold requires at least one quotable evidence sentence. The rubric, second-coder CSV, and disagreement log are released with the database (Nosek et al., 2015). A two-extreme bracket on the operationally undifferentiated *conditional* status (92 of 612 rows) — reassigning all 92 to *robust* (extreme A) or to *transformed* (extreme B) — yields sign-test *p* = 0.004 (A) or 0.021 (B): the verdict is robust to either prior. The v1.1 pre-analysis plan filed at OSF commits a CFA marker-variable test, a configural-invariance test with two human coders and ≥50 cases per family, and strengthened 1st-order quotation discipline.

### 6.3 Robustness checks

A HARKing-risk hold-out addresses the pilot-case circularity directly. Excluding the four pilot cases (1 Törnberg, 2 Keith, 7 Baccolini, 21 Larson) and re-running the role-level paired sign test on the remaining 32 cases yields 13 positive differences out of 15 defined roles (one role drops because its *V* is undefined on the 32-case subset; two-sided binomial *p* = 0.007), *V*_family = 0.253, *V*_capability = 0.208, and *V* gap = +0.045 — all consistent in direction with the full-sample values and still statistically significant. The pilot cases contribute to specific role counts (e.g., removing Törnberg drops the routine-coder shrinking count from 15 to 13) but do not drive the H3 verdict. First-coder non-blindness is a real and disclosed limitation (H1, H2, H3 were specified before coding but the coder held the hypotheses in mind during coding); the pre-specified blind second-coder pass and Appendix C stranger-coder protocol are the paper's response.

### 6.4 H3 confirmatory test (two complementary lenses)

We test H3 through two complementary lenses on the same 612 role-coding observations: *Lens 1* (Table 3a) asks whether *research kind* predicts role status pooling across AI capability; *Lens 2* (Table 3b) asks whether *AI-capability modality* predicts role status pooling across research kind. The lens comparison is a descriptive convergence check; H3 is supported only if Lens 1 is consistently larger than Lens 2.

**Table 3a. Status distribution by Case family.** Each cell is the count of role-rows with that status across all cases in the family (17 role rows per case × `n_cases`).

| Case family | n_cases | Robust | Conditional | Transformed | Shrinking | Split pressure | Merge pressure | Unclear | Not applicable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Predictive simulation & design | 7 | 7 | 7 | 9 | 6 | 17 | 0 | 4 | 69 |
| Measurement & coding | 6 | 18 | 21 | 2 | 5 | 4 | 0 | 5 | 47 |
| Agenda, theory & discovery | 5 | 2 | 18 | 2 | 6 | 5 | 0 | 4 | 48 |
| Evidence synthesis & corpus | 5 | 6 | 9 | 5 | 10 | 0 | 2 | 12 | 41 |
| Interviews, fieldwork & qualitative interpretation | 5 | 10 | 18 | 6 | 2 | 12 | 0 | 2 | 35 |
| Governance, authorship & labor | 3 | 2 | 6 | 2 | 1 | 0 | 0 | 4 | 36 |
| Reproducibility & autonomous research | 3 | 5 | 7 | 1 | 6 | 0 | 0 | 5 | 27 |
| Pedagogy & training | 2 | 6 | 6 | 3 | 4 | 1 | 0 | 1 | 13 |
| **TOTAL** | **36** | **56** | **92** | **30** | **40** | **39** | **2** | **37** | **316** |

**Table 3b. Status distribution by Primary AI capability.** Same aggregation as Table 3a, grouped by AI-capability label instead of case family.

| Primary AI capability | n_cases | Robust | Conditional | Transformed | Shrinking | Split pressure | Merge pressure | Unclear | Not applicable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Generative | 18 | 26 | 58 | 13 | 12 | 11 | 2 | 18 | 166 |
| Agentic | 12 | 16 | 25 | 13 | 22 | 16 | 0 | 13 | 99 |
| Predictive | 6 | 14 | 9 | 4 | 6 | 12 | 0 | 6 | 51 |
| **TOTAL** | **36** | **56** | **92** | **30** | **40** | **39** | **2** | **37** | **316** |

*Lens 1 verdict.* Case family clearly matters. Measurement & coding is robust-heavy (18 robust / 21 conditional / 5 shrinking); Evidence synthesis & corpus is shrinking-heavy (10 shrinking / 6 robust); Agenda, theory & discovery is conditional-heavy (18 conditional / 2 robust); Interviews, fieldwork & qualitative interpretation is split-pressure-heavy (12 split pressure). These are differences of kind, not only of degree. *Lens 2 verdict.* AI capability also matters. Generative cases lean conditional; agentic cases carry most of the shrinkage (22 of 40 observations) and the highest split-pressure density per case; predictive cases are relatively robust but concentrate transportability-related split pressure. *Combined verdict.* The pre-specified primary confirmatory test is the per-role paired sign test (*p* = 0.004 on 14 of 16 positive differences); the paired Wilcoxon on the same 16 differences yields *W* = 7, *p* = 0.0006. χ² on status × case-family is 87.67 (df=35, *p* < 10⁻⁵, V = 0.260); on status × AI capability, χ² = 29.80 (df=10, *p* < 10⁻³, V = 0.240). The 0.020 V gap is directional-only and uninterpretable absent the configural-invariance test pre-committed to v1.1.

The script released with the database reports two Monte-Carlo permutation tests on the cross-lens contrast under explicitly different unit-of-randomization assumptions, and we report them with equal prominence rather than as a primary-versus-supplementary pair. The *cell-level* Monte-Carlo test (10,000 permutations, seeds 20260423 and 20260424) treats the 612 role-coding cells as the units of randomization and yields *p* = 0.0002 for case family and *p* = 0.0012 for AI capability — but this null ignores within-case clustering (17 role-rows per case are not independent observations of role status). The *case-level* Monte-Carlo test re-randomizes the 36 case-family labels under the clustering-aware null and yields *p* = 0.58 for case family and *p* = 0.33 for AI capability — i.e., once randomization respects the case as the unit, the H3 family-vs-capability cross-lens contrast is *not significant*. The cell-level test is descriptive of cell-level association; the case-level test is the inferentially-disciplined test for a 36-case sample. We additionally report a *case-cluster bootstrap* (B = 2,000, seed 20260425, resampling cases with replacement), which yields V_family 95% CI [0.261, 0.430], V_capability 95% CI [0.193, 0.451], and V_gap 95% CI [−0.096, 0.156] with P(gap > 0) = 0.69; the cluster-bootstrap CI on V_gap straddles zero and is consistent with the case-level Monte-Carlo result.

A Holm step-down correction across the six pre-specified confirmatory tests (computed in `scripts/section6_analysis.py` with running-max monotonicity enforcement) leaves the four cell-level tests significant: (1) cell-level Monte-Carlo on case family (raw *p* = 0.0002, adj. 0.0012); (2) per-role Wilcoxon (raw 0.0006, adj. 0.003); (3) cell-level Monte-Carlo on AI capability (raw 0.0012, adj. 0.005); (4) per-role paired sign test (raw 0.004, adj. 0.013). Both case-level Monte-Carlos do not survive: (5) on AI capability (raw 0.33, adj. 0.66); (6) on case family (raw 0.58, adj. 0.66).

H3 is therefore *supported as a cell-level repository pattern but not significant under the clustering-aware case-level null at N* = 36 *cases*. The two lenses return the same direction at the cell level — case family is the stronger associate of role status (V = 0.260 vs. 0.240; V_family > V_capability in 14 of 16 per-role tests) — but the case-level test does not have the power to detect a corresponding case-family effect at this sample size, and the manuscript should not over-claim. The pattern is consistent with Abbott's (1988) prediction that jurisdictional stability follows task structure rather than tool novelty, but the 36-case repository cannot license that theoretical claim at the population level; we do not generalize beyond the sample, and a 2027 extension that increases the case-level *N* is the appropriate test of the case-level null.

Removing the five autonomy-heavy system cases (25 and 26 Project APE, 32 AI Scientist, 33 Deep Research, 34 AgentSociety) barely moves the headline pattern.

**Table 4. Sensitivity to exclusion of autonomy-heavy system cases.** Rows shown are the six roles named in H1 (three durable — protocol and provenance architect, calibration architect, accountability and labor allocator) and H2 (three shrinking task-clusters); the full 17-role Δ table is released with the database as Appendix D. Columns in each block: *all* = full 36 cases; *excl* = 31 cases; *Δ* = `excl` − `all`.

| Role | Robust (all / excl / Δ) | Conditional | Transformed | Shrinking | Split pressure |
|---|---|---|---|---|---|
| Protocol and provenance architect | 15 / 12 / −3 | 5 / 5 / 0 | 7 / 6 / −1 | 0 / 0 / 0 | 4 / 4 / 0 |
| Calibration architect | 8 / 6 / −2 | 10 / 9 / −1 | 1 / 1 / 0 | 0 / 0 / 0 | 2 / 2 / 0 |
| Accountability and labor allocator | 5 / 4 / −1 | 8 / 7 / −1 | 7 / 6 / −1 | 0 / 0 / 0 | 6 / 5 / −1 |
| Routine first-pass screener | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | 13 / 9 / −4 | 0 / 0 / 0 |
| Routine coder on high-consensus, ground-truth-rich tasks | 0 / 0 / 0 | 1 / 1 / 0 | 0 / 0 / 0 | 15 / 12 / −3 | 1 / 1 / 0 |
| Structural prose polisher / drafter | 0 / 0 / 0 | 2 / 2 / 0 | 1 / 1 / 0 | 12 / 8 / −4 | 0 / 0 / 0 |

The five excluded cases contribute 11 of the 40 shrinking-task-cluster observations and 6 of the procedural-or-calibration `robust`/`transformed` counts; dropping them compresses the magnitudes but not the direction. Protocol and provenance architect is still the most durable role by a wide margin (12 robust + 5 conditional + 6 transformed versus any other row). Calibration architect remains predominantly robust-or-conditional (6 robust + 9 conditional). The three shrinking-task clusters are still overwhelmingly shrinking (9, 12, and 8 observations respectively, with no case flipping to robust or transformed). H1 and H2 therefore survive the exclusion; the abstract's aggregate of 40 shrinking observations should be read as the full-repository figure, with 29 shrinking observations remaining under this exclusion.

### 6.5 Bounded claims

These limitations do not collapse the argument, but they do constrain it. The paper can say that H1 is broadly supported because boundary-setting and procedure-setting roles survive more often than routine production clusters. It can say that H2 is conditionally supported because the clearest shrinkage clusters where auditability and public ground truth are strongest. It can also say that H3 is supported as a *cell-level* repository pattern but is *not* significant under the clustering-aware case-level null at N = 36: case family is the stronger associate of role status at the cell level (aggregate V = 0.260 versus 0.240 for capability; V_family > V_capability in 14 of 16 per-role tests; cell-level Monte-Carlo *p* = 0.0002 survives Holm correction) while the case-level Monte-Carlo *p* = 0.58 does not, so the H3 conclusion is bounded to the cell-level association and the case-level test awaits a larger-*N* extension. What it should not say is that the repository proves a universal law of role disappearance.

Framed this way, the audit's claims are within-sample associations at N = 36, not population-level effect estimates or causal claims; the §7 prescriptive recommendations are normative inferences from the descriptive pattern, and the 2027 hold-out, the v1.1 within-case extension, the configural-invariance test, and a stranger-coder replication are the appropriate next instruments (King et al., 1994).

The framework does not claim to replace the broader literatures on professions, human-AI collaboration, or computational social science. Instead, it provides a comparative empirical bridge among them: a way to describe changing research work in terms of role durability, transformation, shrinkage, and split pressure rather than in terms of undifferentiated human-versus-AI competition.

## 7. Conclusion

### 7.1 Findings synthesis

Once the cases are aligned as a role-system dataset, the most interesting question is no longer whether AI can "do research" but which roles remain constitutive of *epistemic validity* — the warrantability of a study's inferential claims — under generative, predictive, and agentic support. Roles tied to meaning, admissible procedure, calibration, provenance, and accountability are more durable than routine throughput clusters; some tasks shrink where evaluation is clean; some roles transform around authorship, disclosure, and labor allocation; and some inherited categories are no longer precise enough.

The six statuses cluster onto two aggregate dimensions that emerged from the audit rather than being imposed from prior theory (Gioia et al., 2013): an *allocation* axis (robust → conditional → transformed → shrinking) tracking how human performance yields scope, content, then volume; and a *specification* axis (split and merge pressure) revising the unit of analysis. The two-axis structure was not visible at v0.1; it surfaced after Case 10's merge-pressure coding made it impossible to read split and merge as further points on the allocation axis. The typology is six rather than four because reconfiguration and reallocation are independent forms of jurisdictional revision (Abbott, 1988; Freidson, 2001).

### 7.2 Three propositions for the 2027 hold-out

The two-axis framing yields three forward-looking propositions for the pre-specified 2027 hold-out (target *N* = 60; analysis script `scripts/section7_2027_holdout.py` filed at the release tag): **P1** procedural roles co-occur as a single epistemic-guardian configuration; **P2** shrinkage clusters where *public-ground-truth* ∨ *post-hoc-auditability* holds, not where AI capability is highest; **P3** as agentic autonomy rises, protocol-and-provenance and accountability-and-labor undergo merge pressure rather than independent transformation.

### 7.3 Stakeholder recommendations

The rubric serves three audiences. *Methods researchers* receive a role-first vocabulary and six behaviorally-anchored statuses applicable to a new case without consulting the underlying database. *Reviewers and editors* receive an audit scaffold: the role × status table and the §3.1 exemplar index let them locate whether a manuscript's automation claims operate at the task-cluster layer (where shrinkage is defensible) or the role layer (where evidence in this repository does not support disappearance). *Institutional actors* — PhD methods curricula, replication archives, methods-policy committees — receive a diagnostic for which roles warrant curricular and editorial investment as throughput tasks migrate. Table 5 maps these audiences onto research stages; Table 6 specifies status-by-status authorial imperatives with implied coordination mechanisms.

**Table 5. Stakeholder × research-stage recommendations.** The grid maps three audiences onto three research stages (planning, implementation, reporting), with one imperative recommendation per cell.

| Stage | Methods researchers | Reviewers and editors | Institutional actors |
|---|---|---|---|
| Planning | Identify which of the six statuses each role in the design is expected to occupy; pre-register moderator variables that would distinguish *conditional* from *transformed* (cf. Case 3 Gligorić split-pressure evidence). | Require a pre-coding rubric with behaviorally anchored status definitions; reject blanket automation claims not tied to a named role. | Fund role-level training modules in PhD methods curricula: procedure and provenance architecture, calibration, accountability (cf. Cases 2, 27 as robust-procedure exemplars). |
| Implementation | Code at the role × case level; record the quoted sentences that anchor the status assignment; keep a disagreement log when two coders diverge (cf. Case 10 Hajishirzi merge-pressure requiring joint-object coding). | On a submitted manuscript, locate whether each automation claim operates at the task-cluster layer (cf. Case 1 Törnberg objective-annotation shrinkage) or at the role layer (where disappearance requires stronger evidence). | Maintain replication archives that capture role-level codings, not only outcome statistics; require a rubric version tag on deposits. |
| Reporting | Release the role-coding CSV alongside the paper; report Cohen's κ on a subsample as a limitation alongside other limitations. | Check that claims sit inside the ceiling the reliability evidence supports; flag auditable-instrument claims made on single-coder evidence (cf. the reliability disclosure in this paper's §6). | Publish aggregate role-status distributions from deposited datasets as a public benchmark against which new cases can be compared. |

**Table 6. Status-conditional authorial recommendations.** One conditional recommendation per status, with the exemplar case from §3.1, the implied human-AI coordination mechanism, and the count of role × case cells coded at that status in the current repository (denominator = 612 cells throughout). The recommendations are scope-conditioned to the §2 framework licensing; deviations may be appropriate where the case's research configuration warrants them.

| Status | Authors should consider… | Implied coordination mechanism | Exemplar case | Repository count |
|---|---|---|---|---|
| Robust | …where the role is treated as load-bearing for inferences, tying it to a methods or limitations claim and specifying the validity loss AI substitution would incur. | Human-as-sole-performer; AI excluded from this role-cell. | Keith, 2026 / Case 2 | 56 / 612 cells robust (15 of 36 cases carry ≥ 1) |
| Conditional | …naming at least one moderator variable under which human performance is required and reporting empirical variation in AI adequacy across that moderator. | Moderator-gated sign-off: AI performs the role and a human signs off contingent on the named moderator. | Baccolini, 2026 / Case 7 | 92 / 612 cells conditional |
| Transformed | …using before/after language or a verb swap; naming new sub-tasks (disclosure, credit allocation, calibration audit) as new rather than as extensions. | Content-redefined human role: AI absorbs the prior content, the human's task list changes around it (Puranam, 2021). | Yin, n.d. / Case 29 | 30 / 612 cells transformed |
| Shrinking | …reporting the public ground truth or high-consensus target; characterizing residual human labor as rescue, triage, or verification; not extending the shrinkage claim to role-layer disappearance. | Exception-handling oversight: AI as default performer, human routed in for triage and rescue only. | Törnberg, 2025 / Case 1 | 40 / 612 cells shrinking (concentrated in 11 cases) |
| Split pressure | …showing that AI performance differs across the conflated sub-activities; distinguishing the sub-activities in the analysis and revising the typology accordingly. | Role bifurcation: two separately-coordinated sub-roles, each with its own performer assignment. | Gligorić, n.d. / Case 3 | 39 / 612 cells split pressure (7 of 8 starting roles triggered) |
| Merge pressure | …reporting evidence that the two roles are inseparable in practice within the case; treating them as a joint object rather than as independent activities. | Joint-object coordination: the two role-cells must be performed by a single accountable unit. | Hajishirzi, 2026 / Case 10 | 2 / 612 cells (both on Case 10) |

Three artifacts together constitute the contribution: (1) the v1.0 rubric — a behaviorally-anchored instrument for coding role-status change at the (role × case) cell level; (2) the released applied-use pipeline — case CSV, codebook, decision tree (Appendix E), reviewer-audit checklist (Appendix F) — at the v1.0.0-ORM-submission release tag; (3) the disconfirmation apparatus — pre-committed 2027 hold-out, human second-coder pass, and parallel-rubric application by independent groups on a 2027–2030 sample. The rubric sits within computational social science (Lazer et al., 2009, 2020) at a level the existing CSS literature has under-theorized: not the pipeline (Hickman et al., 2022) and not the model, but the activity-level role within which both pipeline and model are embedded. We acknowledge a governmentality dimension: once the six statuses circulate as a measurement convention, researchers will plausibly organize their work around the rubric, which will partly *produce* the role-system it claims to describe; this is the inescapable side of any methodological-rubric contribution. We hope the rubric serves as a catalyst for instrument-grade audits of role-system change under AI embedding. The empirical terrain has changed: not from human research to machine research, but from one research role system to another.

## Data and Code Availability

All artifacts supporting this paper are archived at https://github.com/ryanwongyy/role-system-ORM-submission under release tag [`v1.0.0-ORM-submission`](https://github.com/ryanwongyy/role-system-ORM-submission/releases/tag/v1.0.0-ORM-submission), mirrored at a Zenodo DOI to be minted on acceptance. The release contains: (1) `role_coding_master.csv` (612 rows, CC-BY-4.0); (2) `cases_master.csv` (36 cases, CC-BY-4.0); (3) `role_coding_secondcoder_subsample.csv` (68 rows, released concurrently with Appendix B κ); (4) the codebook with a date-stamped version history; (5a) `scripts/section6_analysis.py` (MIT) reproduces every inferential value in §6 — χ² = 87.67 (family) and 29.80 (capability), Cramér's *V* = 0.260 (family) and 0.240 (capability), cell-level Monte-Carlo *p* = 0.0002 / 0.0012 (seeds 20260423 and 20260424), case-level Monte-Carlo *p* = 0.58 / 0.33 under the clustering-aware null, case-cluster bootstrap *V* CIs (*B* = 2,000, seed 20260425), per-role paired Wilcoxon *W* = 7 / *p* = 0.0006 and the sign-test companion *p* = 0.004, *V*_family = 0.267 on the 204 high-confidence rows, and Holm-adjusted *p*-values across the six-test confirmatory family. (5b) `scripts/appendix_b_reliability.py` (MIT) reproduces every reliability value in §6 and Appendix B — Cohen's κ = 0.289 with bootstrap 95% CI [0.147, 0.439] (*B* = 2,000, seed 20260423), per-status κ (robust 0.402, shrinking 0.549, conditional 0.009, transformed 0.000), and Krippendorff's α = 0.278 (7-cat) / 0.298 (8-cat). Runtime is under 60 s on a 2023 laptop; dependencies are pinned in `requirements.txt`. (6) Appendix E (coder checklist, instrument-grade) and Appendix F (reviewer-audit checklist), both under CC-BY-4.0, function as the applied-use artifacts for the rubric. All counts reported in this manuscript are computed against the release-tagged snapshot; subsequent coding revisions are tracked in `CHANGELOG.md` and will not overwrite the reviewed snapshot.

## Transparency and Disclosures

The first author conducted all role-status coding. The second-coder protocol for Appendix B (four cases, 68 cells, stratified across the four largest case-family clusters) is specified as a pre-analysis plan in `30_reviews/OSF_preregistration.md`, released with the database at tag `v1.0.0-ORM-submission`. The pre-analysis plan documents the subsample, the coder-blindness protocol, the κ ≥ 0.60 acceptance threshold, and the tie-breaker-revision remedy. The evidentiary standard for temporal precedence is the git commit history, not an OSF timestamp: an independent OSF registration was not posted before the second-coder pass, and we flag OSF registration as a recommended follow-up rather than claiming it retrospectively. Competing interests: none declared. Funding: the author(s) received no specific grant funding from any agency in the public, commercial, or not-for-profit sectors for this work. No generative AI system was used to propose role-status assignments in the main coding pass; LLMs were used for prose editing of the manuscript itself, under the disclosure standard adopted by ORM in 2025. H1, H2, and H3 were specified before the main coding pass; the sign test was identified as the primary confirmatory test before analysis; all other inferential objects in §6 are reported as robustness checks. The codebook version history is released with the database.

## References

Abbott, A. (1988). *The system of professions: An essay on the division of expert labor*. University of Chicago Press.

Abbott, A. (2005). Linked ecologies: States and universities as environments for professions. *Sociological Theory*, *23*(3), 245–274.

Aguinis, H., Ramani, R. S., & Alabduljader, N. (2023). Best-practice recommendations for producers, evaluators, and users of methodological literature reviews. *Organizational Research Methods*, *26*(1), 46–76. https://doi.org/10.1177/1094428120943281

Aldrich, H. E., & Ruef, M. (2006). *Organizations evolving* (2nd ed.). Sage.

Autor, D. H. (2015). Why are there still so many jobs? The history and future of workplace automation. *Journal of Economic Perspectives*, *29*(3), 3–30.

Baccolini, R. (2026). Compact large language models for title and abstract screening in systematic reviews: An assessment of feasibility, accuracy, and workload reduction.

Bail, C. A. (2024). Can generative AI improve social science? *Proceedings of the National Academy of Sciences*, *121*(21), e2314021121.

Barley, S. R. (1986). Technology as an occasion for structuring: Evidence from observations of CT scanners and the social order of radiology departments. *Administrative Science Quarterly*, *31*(1), 78–108.

Barley, S. R., & Kunda, G. (2001). Bringing work back in. *Organization Science*, *12*(1), 76–95.

Bergh, D. D., Sharp, B. M., Aguinis, H., & Li, M. (2017). Is there a credibility crisis in strategic management research? Evidence on the reproducibility of study findings. *Strategic Organization*, *15*(3), 423–436.

Bleier, A. (n.d.). Automating computational reproducibility in social science: Comparing prompt-based and agent-based approaches.

Bommasani, R., et al. (2022). On the opportunities and risks of foundation models. *arXiv:2108.07258*.

Borsboom, D., Mellenbergh, G. J., & van Heerden, J. (2004). The concept of validity. *Psychological Review*, *111*(4), 1061–1071.

Brynjolfsson, E., & Mitchell, T. (2017). What can machine learning do? Workforce implications. *Science*, *358*(6370), 1530–1534.

Chang, Y., et al. (2024). A survey on evaluation of large language models. *ACM Transactions on Intelligent Systems and Technology*, *15*(3), 1–45.

Cornelissen, J. P. (2017). Editor's comments: Developing propositions, a process model, or a typology? Addressing the challenges of writing theory without a boilerplate. *Academy of Management Review*, *42*(1), 1–9.

Cornelissen, J. P., Höllerer, M. A., & Seidl, D. (2021). What theory is and can be: Forms of theorizing in organizational scholarship. *Organization Theory*, *2*(3), 1–19.

Cox, J. (n.d.). AI disclosure with DAISY.

Cronbach, L. J., & Meehl, P. E. (1955). Construct validity in psychological tests. *Psychological Bulletin*, *52*(4), 281–302.

Delbridge, R., & Fiss, P. C. (2013). Editors' comments: Styles of theorizing and the social organization of knowledge. *Academy of Management Review*, *38*(3), 325–331.

Doty, D. H., & Glick, W. H. (1994). Typologies as a unique form of theory building: Toward improved understanding and modeling. *Academy of Management Review*, *19*(2), 230–251.

Duriau, V. J., Reger, R. K., & Pfarrer, M. D. (2007). A content analysis of the content analysis literature in organization studies. *Organizational Research Methods*, *10*(1), 5–34.

Edwards, J. R., & Bagozzi, R. P. (2000). On the nature and direction of relationships between constructs and measures. *Psychological Methods*, *5*(2), 155–174.

Eisenhardt, K. M. (1989). Building theories from case study research. *Academy of Management Review*, *14*(4), 532–550.

Eisenhardt, K. M. (2021). What is the Eisenhardt method, really? *Strategic Organization*, *19*(1), 147–160.

Eyal, G. (2013). For a sociology of expertise: The social origins of the autism epidemic. *American Journal of Sociology*, *118*(4), 863–907.

Faraj, S., & Pachidi, S. (2021). Beyond Uberization: The co-constitution of technology and organizing. *Organization Theory*, *2*(1), 1–14.

Feldman, M. S., & Pentland, B. T. (2003). Reconceptualizing organizational routines as a source of flexibility and change. *Administrative Science Quarterly*, *48*(1), 94–118.

Fiss, P. C. (2011). Building better causal theories: A fuzzy set approach to typologies in organization research. *Academy of Management Journal*, *54*(2), 393–420.

Flyvbjerg, B. (2006). Five misunderstandings about case-study research. *Qualitative Inquiry*, *12*(2), 219–245.

Freidson, E. (2001). *Professionalism, the third logic: On the practice of knowledge*. University of Chicago Press.

Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change*, *114*, 254–280.

Furnari, S., Crilly, D., Misangyi, V. F., Greckhamer, T., Fiss, P. C., & Aguilera, R. V. (2021). Capturing causal complexity: Heuristics for configurational theorizing. *Academy of Management Review*, *46*(4), 778–799.

Gelman, A., & Loken, E. (2014). The statistical crisis in science. *American Scientist*, *102*(6), 460–465.

Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research: Notes on the Gioia methodology. *Organizational Research Methods*, *16*(1), 15–31.

Gligorić, K. (n.d.). Multi-perspective LLM annotations for valid analyses in subjective tasks.

Grossmann, I., Feinberg, M., Parker, D. C., Christakis, N. A., Tetlock, P. E., & Cunningham, W. A. (2023). AI and the transformation of social science research. *Science*, *380*(6650), 1108–1109.

Ha, D. (n.d.). The AI Scientist: Towards fully automated open-ended scientific discovery.

Hajishirzi, H. (2026). Synthesizing scientific literature with retrieval-augmented language models.

Hannan, M. T., & Freeman, J. (1977). The population ecology of organizations. *American Journal of Sociology*, *82*(5), 929–964.

Hernandez, A. (2025). Reading children's moral dramas in anthropological fieldnotes: A human-AI hybrid approach.

Hickman, L., Thapa, S., Tay, L., Cao, M., & Srinivasan, P. (2022). Text preprocessing for text mining in organizational research: Review and recommendations. *Organizational Research Methods*, *25*(1), 114–146.

Hruschka, D. J., Schwartz, D., St. John, D. C., Picone-Decaro, E., Jenkins, R. A., & Carey, J. W. (2004). Reliability in coding open-ended data: Lessons learned from HIV behavioral research. *Field Methods*, *16*(3), 307–331.

Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine*, *2*(8), e124.

Kang, J. (2025). REPRO-Bench: Can agentic AI systems assess the reproducibility of social science research?

Keith, K. A. (2026). Codebook LLMs: Evaluating LLMs as measurement tools for political science concepts.

King, G., Keohane, R. O., & Verba, S. (1994). *Designing social inquiry: Scientific inference in qualitative research*. Princeton University Press.

Krippendorff, K. (2011). Computing Krippendorff's alpha-reliability. *Annenberg School for Communication Departmental Papers*, University of Pennsylvania.

Langley, A. (1999). Strategies for theorizing from process data. *Academy of Management Review*, *24*(4), 691–710.

Larson, J. (2024). Synthetic replacements for human survey data? The perils of large language models.

Lazer, D., et al. (2009). Computational social science. *Science*, *323*(5915), 721–723.

Lazer, D., et al. (2020). Computational social science: Obstacles and opportunities. *Science*, *369*(6507), 1060–1062.

Li, J. (n.d.). AgentSociety: Large-scale simulation of LLM-driven generative agents advances understanding of human behaviors and society.

Liang, P., et al. (2022). Holistic evaluation of language models. *arXiv:2211.09110*.

Lord, R. G., Foti, R. J., & DeVader, C. L. (1984). A test of leadership categorization theory: Internal structure, information processing, and leadership perceptions. *Organizational Behavior and Human Performance*, *34*(3), 343–378.

McHugh, M. L. (2012). Interrater reliability: The kappa statistic. *Biochemia Medica*, *22*(3), 276–282.

Merton, R. K. (1957). The role-set: Problems in sociological theory. *British Journal of Sociology*, *8*(2), 106–120.

Messick, S. (1995). Validity of psychological assessment: Validation of inferences from persons' responses and performances as scientific inquiry into score meaning. *American Psychologist*, *50*(9), 741–749.

Nosek, B. A., et al. (2015). Promoting an open research culture. *Science*, *348*(6242), 1422–1425.

Orlikowski, W. J. (2007). Sociomaterial practices: Exploring technology at work. *Organization Studies*, *28*(9), 1435–1448.

Page, M. J., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, *372*, n71.

Project APE. (n.d.). Project APE: Can policy evaluation be automated?

Puranam, P. (2021). Human-AI collaborative decision-making as an organization design problem. *Journal of Organization Design*, *10*(2), 75–80.

Puranam, P., Alexy, O., & Reitzig, M. (2014). What's "new" about new forms of organizing? *Academy of Management Review*, *39*(2), 162–180.

Ramarajan, L. (2014). Past, present and future research on multiple identities: Toward an intrapersonal network approach. *Academy of Management Annals*, *8*(1), 589–659.

Siddaway, A. P., Wood, A. M., & Hedges, L. V. (2019). How to do a systematic review: A best practice guide. *Annual Review of Psychology*, *70*, 747–770.

Snyder, H. (2019). Literature review as a research methodology: An overview and guidelines. *Journal of Business Research*, *104*, 333–339.

Stemler, S. (2001). An overview of content analysis. *Practical Assessment, Research & Evaluation*, *7*(1), 17.

Suchman, L. A. (2007). *Human-machine reconfigurations: Plans and situated actions* (2nd ed.). Cambridge University Press.

Tranfield, D., Denyer, D., & Smart, P. (2003). Towards a methodology for developing evidence-informed management knowledge by means of systematic review. *British Journal of Management*, *14*(3), 207–222.

Törnberg, P. (2023). How to use LLMs for text analysis. *arXiv:2307.13106*.

Törnberg, P. (2025). Large language models outperform expert coders and supervised classifiers at annotating political social media messages.

Vandenberg, R. J., & Lance, C. E. (2000). A review and synthesis of the measurement invariance literature: Suggestions, practices, and recommendations for organizational research. *Organizational Research Methods*, *3*(1), 4–70.

Weick, K. E., & Sutcliffe, K. M. (2007). *Managing the unexpected: Resilient performance in an age of uncertainty* (2nd ed.). Jossey-Bass.

Weidinger, L., et al. (2021). Ethical and social risks of harm from language models. *arXiv:2112.04359*.

Welch, C., Piekkari, R., Plakoyiannaki, E., & Paavilainen-Mäntymäki, E. (2011). Theorising from case studies: Towards a pluralist future for international business research. *Journal of International Business Studies*, *42*(5), 740–762.

Whetten, D. A. (1989). What constitutes a theoretical contribution? *Academy of Management Review*, *14*(4), 490–495.

Williams, L. J., Hartman, N., & Cavazotte, F. (2010). Method variance and marker variables: A review and comprehensive CFA marker technique. *Organizational Research Methods*, *13*(3), 477–514.

Woolley, A. W., Chabris, C. F., Pentland, A., Hashmi, N., & Malone, T. W. (2010). Evidence for a collective intelligence factor in the performance of human groups. *Science*, *330*(6004), 686–688.

Xiao, X. (n.d.). Nonstandard errors in AI agents.

Yin, S. (n.d.). Scientific production in the era of large language models.

Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2024). Can large language models transform computational social science? *Computational Linguistics*, *50*(1), 237–291.
