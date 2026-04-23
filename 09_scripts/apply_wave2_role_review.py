#!/usr/bin/env python3
"""Wave-2 role-coding confidence upgrades for cases 3, 10, 11, 12, 13.

Each case had all 17 role rows at low confidence because they were initialized
from repository curation without full-text review. This script replaces those
rows with evidence-grounded codings derived from the stored full-text sources,
then rebuilds role_coding_master.csv, role_confidence_report.csv, and the
role-coding sections of data_inventory.md and known_gaps.md.
"""
from __future__ import annotations

import csv
import io
from collections import Counter, defaultdict
from pathlib import Path
from textwrap import dedent

PROJECT_ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")

ROLE_FIELDS = [
    "case_id",
    "role_label",
    "role_group",
    "role_observable_in_case",
    "status_in_case",
    "confidence",
    "evidence_basis_summary",
    "main_supporting_source_ids",
    "main_contrary_source_ids",
    "notes",
]

CASE_SLUGS: dict[int, str] = {}
for path in sorted((PROJECT_ROOT / "02_cases").iterdir()):
    if path.is_dir():
        cid = int(path.name.split("_", 1)[0])
        CASE_SLUGS[cid] = path.name


CASE_UPDATES_CSV: dict[int, str] = {
    3: dedent('''\
        case_id,role_label,role_group,role_observable_in_case,status_in_case,confidence,evidence_basis_summary,main_supporting_source_ids,main_contrary_source_ids,notes
        3,Relevance adjudicator,starting_role,no,not_applicable,high,Paper takes POPQUORN politeness and offensiveness subsets as given corpora (§3.4) with no human work selecting which materials belong in the analysis universe.,C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms corpus is pre-selected benchmark data.
        3,Mechanism disciplinarian,starting_role,no,not_applicable,high,Paper is a statistical-inference method (IPW/PPI-style correction) and makes no causal-mechanism claims requiring human discipline (§3.2).,C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms no causal-mechanism work.
        3,Construct and perspective boundary setter,starting_role,yes,split_pressure,high,"Paper's central move is reframing the estimand from a scalar ground truth to a vector over demographic perspectives (§1, §3.1), which is precisely the boundary/perspective decision and pressures splitting into boundary vs. perspective components.",C003_P1; C003_REGISTRY,,Upgraded from low: abstract and §3.1 make the split-pressure reading explicit.
        3,Corpus pluralist,starting_role,no,not_applicable,medium,"Pluralism in the paper operates over annotator perspectives, not over multiple corpora; only POPQUORN politeness and offensiveness subsets plus synthetic data are used (§3.4).",C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms single-source corpus with no pluralist-of-sources argument.
        3,Protocol and provenance architect,starting_role,partial,split_pressure,high,"PDI is itself a protocol for allocating a human annotation budget across burn-in and adaptive batches with IPW correction and bootstrap CIs (§3.2), but the paper does not address logging, versioning, or disclosure, hence partial and split pressure between workflow-design and provenance components.",C003_P1; C003_REGISTRY,,Upgraded from low: Methods §3.2 supports workflow-design component; provenance/disclosure not discussed.
        3,Counterfactual and transportability judge,starting_role,no,not_applicable,medium,"Discussion §5 gestures at generalizing PDI to RLHF, LLM-as-judge, and survey simulation but frames this as future work, not as human transportability adjudication within the case.",C003_P1; C003_REGISTRY,,"Upgraded from low: full text shows transportability is mentioned only as extension, not performed."
        3,Situated interlocutor / context witness,starting_role,no,not_applicable,high,"Annotations come from Prolific crowd workers rated on scales (§3.4); no fieldwork, interview, or interpretive-setting work is present.",C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms crowdsourced rating design.
        3,Accountability and labor allocator,starting_role,no,not_applicable,medium,"Paper allocates human annotation budget across demographic groups (§3.2, Tables 2 and 4) but this is statistical sample allocation, not authorship/disclosure/accountability assignment.",C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms no authorship/accountability framing; labor allocation is purely sampling.
        3,Construct boundary setter,split_candidate,yes,robust,high,"Humans define the rating constructs (politeness 1-5, offensiveness 1-5) and the demographic stratification axes (gender/age/education) used for the estimand (§3.1, §3.4); these boundary decisions are necessary for validity.",C003_P1; C003_REGISTRY,,Upgraded from low: §3.1 and §3.4 are explicit about human-set categories and scales.
        3,Perspective sampler,split_candidate,yes,robust,high,"PDI's core contribution is adaptive human sampling concentrated on demographic groups where LLM proxies are least reliable, explicitly to preserve subgroup disagreement rather than collapse to majority vote (Abstract, §1, §3.2).",C003_P1; C003_REGISTRY,,Upgraded from low: paper is directly about preserving this role.
        3,Counterfactual / transportability judge,split_candidate,no,not_applicable,high,"No counterfactual or cross-population transportability claims are adjudicated; the paper stays within POPQUORN and synthetic simulations (§3.4, §4.3).",C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms absence.
        3,Calibration architect,split_candidate,no,not_applicable,medium,"IPW/PPI rectified estimator (§3.2) calibrates LLM proxy against human labels, but this is statistical correction to a held-out human estimand, not benchmark/simulator calibration against an external reference distribution.",C003_P1; C003_REGISTRY,,Upgraded from low: role label interpreted narrowly per codebook; notes that PPI-style rectification is adjacent but not a match.
        3,Situated interlocutor,split_candidate,no,not_applicable,high,Annotation is remote Prolific rating with no fieldwork or interactive interview; humans do not shape what respondents disclose (§3.4).,C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms crowdsourced design.
        3,Context witness,split_candidate,no,not_applicable,high,"No archival, tacit, or contextual interpretive work is invoked; demographics enter only as features for the error-predictor (§3.2).",C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms absence.
        3,Routine first-pass screener,shrinking_task_cluster,no,not_applicable,high,"No title/abstract triage, study screening, or early ranking task is present; the pipeline starts from already-selected text instances (§3.1).",C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms not applicable.
        3,"Routine coder on high-consensus, ground-truth-rich tasks",shrinking_task_cluster,partial,unclear,high,"Paper explicitly argues ground truth does NOT exist for subjective tasks (§1) and that collapsing disagreement is invalid; AI substitution for routine coding is precisely what is contested, so the cluster applies only in inverted form.",C003_P1; C003_REGISTRY,,Upgraded from low: full text clarifies paper's stance - this role-cluster's premise (ground truth available) is rejected for the case's tasks.
        3,Structural prose polisher / drafter,shrinking_task_cluster,no,not_applicable,high,"Paper concerns annotation of existing text, not AI-assisted prose drafting or polishing; no role for AI as a writer appears anywhere in the pipeline.",C003_P1; C003_REGISTRY,,Upgraded from low: full text confirms not applicable.
    '''),
    10: dedent('''\
        case_id,role_label,role_group,role_observable_in_case,status_in_case,confidence,evidence_basis_summary,main_supporting_source_ids,main_contrary_source_ids,notes
        10,Relevance adjudicator,starting_role,partial,unclear,medium,"C010_S1 Methods show expert PhD writers curate queries and answer rubrics that define which retrieved passages count as relevant or seminal, and annotators note citations are sometimes outdated or less representative, indicating residual human relevance judgement over retrieval output.",C010_P1; C010_S1,,Upgraded from low; rubric design and expert critique of retrieved papers supports the partial/unclear coding.
        10,Mechanism disciplinarian,starting_role,no,not_applicable,medium,"Neither C010_P1 (citation-verification empirical audit) nor C010_S1 (retrieval-augmented synthesis) concerns constraining causal or mechanism claims; the cases are about bibliographic fidelity and coverage, not mechanism adjudication.",C010_P1; C010_S1,,Upgraded from low; sources are detailed enough to confidently mark not applicable.
        10,Construct and perspective boundary setter,starting_role,no,not_applicable,medium,"C010_P1 defines mysterious citation severity bands and C010_S1 defines rubric criteria, but neither involves constructing socially meaningful category boundaries or preserving perspective disagreement - the constructs are bibliographic correctness and answer coverage.",C010_P1; C010_S1,,Upgraded from low; sources support not-applicable.
        10,Corpus pluralist,starting_role,partial,unclear,medium,"C010_S1 explicitly combines OSDS dense retrieval, Semantic Scholar API and You.com web search to avoid collapsing onto one corpus (Ablations of retrieval section), and its limitation section flags exclusion of social sciences and license-protected papers.",C010_S1; C010_P1,,Upgraded from low; multi-source retrieval and stated coverage gaps support partial/unclear.
        10,Protocol and provenance architect,starting_role,yes,merge_pressure,high,"C010_P1 proposes submission-time DOI/PDF requirements, desk-reject policies and disclosure enforcement; C010_S1 builds the OpenScholar self-feedback + citation-verification pipeline and Semantic Scholar API checking - both sources centrally concern workflow, logging and admissible-citation procedure.",C010_P1; C010_S1,,Upgraded from low to high; this role is directly and centrally evidenced in both sources.
        10,Counterfactual and transportability judge,starting_role,no,not_applicable,medium,"C010_S1 acknowledges findings may not generalize to social sciences or restricted-access domains, but neither source turns on judging whether model-generated results travel across populations or designs.",C010_S1; C010_P1,,Upgraded from low; limitation notes make not-applicable defensible.
        10,Situated interlocutor / context witness,starting_role,no,not_applicable,medium,"Both sources involve documentary / bibliographic analysis and benchmark construction, with no fieldwork, interviewing, or interpretive co-presence.",C010_P1; C010_S1,,Upgraded from low; sources clearly rule this role out.
        10,Accountability and labor allocator,starting_role,yes,merge_pressure,high,"C010_P1 Discussion directly assigns responsibility - authors must verify bibliographies, co-authors share reputational risk, conferences must enforce disclosure, and fabricated citations are framed as scientific misconduct on par with falsification; C010_S1 emphasizes human authorship of expert answers and open-sourcing for accountability.",C010_P1; C010_S1,,Upgraded from low to high; C010_P1 is explicitly about authorship and disclosure responsibility.
        10,Construct boundary setter,split_candidate,no,not_applicable,medium,"C010_P1's severity taxonomy (minor error / rephrased title / mysterious citation) and C010_S1's rubric items are narrow labeling schemes, not the kind of category-boundary definition this split role targets.",C010_P1; C010_S1,,Upgraded from low; sources support not-applicable.
        10,Perspective sampler,split_candidate,no,not_applicable,medium,"Neither source involves preserving subgroup disagreement; C010_S1 aggregates expert ratings with inter-annotator agreement but does not treat disagreement as a substantive construct.",C010_S1; C010_P1,,Upgraded from low; sources support not-applicable.
        10,Counterfactual / transportability judge,split_candidate,no,not_applicable,medium,"Neither source pressures transportability of a causal result across settings; C010_S1's generalization caveats are about benchmark scope, not counterfactual travel.",C010_S1; C010_P1,,Upgraded from low; sources support not-applicable.
        10,Calibration architect,split_candidate,partial,unclear,medium,"C010_S1 benchmarks citation F1, rubric accuracy and hallucination rates (Table 1, Table 2) against expert-written answers as a reference distribution - a calibration-style activity - though the case's core framing is verification rather than simulator calibration.",C010_S1,,"Upgraded from low, and changed role_observable_in_case from no to partial: ScholarQABench is explicitly a benchmark-against-human-experts exercise, so treating this as weakly observable is better supported than no. Status kept unclear."
        10,Situated interlocutor,split_candidate,no,not_applicable,medium,"No interviewer or fieldworker role appears in either source; both concern desk-based bibliographic verification and literature synthesis.",C010_P1; C010_S1,,Upgraded from low; sources support not-applicable.
        10,Context witness,split_candidate,no,not_applicable,medium,"Neither source invokes tacit or archival contextual knowledge to interpret traces; manual verification in C010_P1 is straightforward existence-checking of references.",C010_P1; C010_S1,,Upgraded from low; sources support not-applicable.
        10,Routine first-pass screener,shrinking_task_cluster,partial,unclear,medium,"C010_P1's automated pipeline (PyPDF parsing, external aggregator search, then manual validation) explicitly reduces first-pass reference triage to AI and reserves humans for exception handling, fitting the shrinking-screener profile.",C010_P1,,Upgraded from low; pipeline Figure 1 in C010_P1 directly illustrates this shrinkage.
        10,"Routine coder on high-consensus, ground-truth-rich tasks",shrinking_task_cluster,partial,shrinking,medium,"C010_P1 step 6 shows humans now audit machine results for an externally-anchored task (does the cited publication exist in Crossref/dblp/OpenAlex?); this matches the shift-to-auditor pattern, so no/not_applicable understates what the source shows.",C010_P1,,"Upgraded from low and revised: changed role_observable_in_case from no to partial and status from not_applicable to shrinking. Citation existence is a ground-truth-rich task where humans now verify, not produce, labels."
        10,Structural prose polisher / drafter,shrinking_task_cluster,yes,conditional,high,"C010_P1 explicitly lists drafting/grammar/stylistic polishing as accepted LLM uses (USE AND MISUSE section) and notes one paper disclosed AI use only for grammatical edits; C010_S1 shows LLM-drafted long-form answers preferred by experts 51-70% of the time - directly demonstrating AI-taking-over drafting with humans retaining accountability.",C010_P1; C010_S1,,Upgraded from low to high; both sources centrally concern AI prose drafting with human oversight conditions.
    '''),
    11: dedent('''\
        case_id,role_label,role_group,role_observable_in_case,status_in_case,confidence,evidence_basis_summary,main_supporting_source_ids,main_contrary_source_ids,notes
        11,Relevance adjudicator,starting_role,yes,conditional,high,"P1 shows LLM-assisted proposals drift toward recently funded work (lower distinctiveness), and S1 shows LLM ideation lacks diversity and requires human rerank to surface novel ideas, making human judgment about what belongs in a proposal the binding constraint.",C011_P1; C011_S1,,upgraded from low: both sources directly speak to human decisions about which ideas should enter the funding portfolio
        11,Mechanism disciplinarian,starting_role,partial,unclear,medium,"S1 notes LLM ideas are rated slightly weaker on feasibility and that reliable evaluation of mechanism/effectiveness still depends on expert reviewers; P1 does not directly code mechanism discipline but documents concentration of NIH gains in non-hit papers, consistent with weaker mechanism pressure when LLMs dominate.",C011_P1; C011_S1,,upgraded from low: S1 feasibility/effectiveness review structure is the main anchor
        11,Construct and perspective boundary setter,starting_role,no,not_applicable,medium,"Neither source treats construct-definition or socially meaningful disagreement about the construct as the object of study; P1 measures distinctiveness as a portfolio property and S1 standardizes a single ideation template across conditions.",C011_P1; C011_S1,,upgraded from low: sources confirm construct-setting is not the operative role here
        11,Corpus pluralist,starting_role,no,not_applicable,medium,"Neither source frames the case as humans defending plural corpora; P1 treats NSF/NIH abstracts as the corpus by design and S1 constrains ideation to seven predefined NLP topics drawn from one CFP page.",C011_P1; C011_S1,,upgraded from low: corpus-construction role not invoked in either source
        11,Protocol and provenance architect,starting_role,yes,conditional,high,"P1 explicitly cites NIH NOT-OD-25-132 on AI-substantially-developed applications and NSF's disclosure notice, and S1 designs detailed protocol controls (style normalizer, topic matching, blind review, template) - both anchor human design of disclosure and admissible procedure.",C011_P1; C011_S1,,"upgraded from low and from no to yes: direct protocol/disclosure evidence in both sources; status_in_case changed to conditional because the role is visibly active (agency guidance, study protocol) rather than absent"
        11,Counterfactual and transportability judge,starting_role,no,not_applicable,medium,"P1's agency-dependent findings (NIH vs NSF) and S1's discussion of topic/style confounders touch on transportability, but neither source positions a human role as the arbiter of whether LLM-aided results travel across settings.",C011_P1; C011_S1,,upgraded from low: sources let us confirm the role is not central
        11,Situated interlocutor / context witness,starting_role,no,not_applicable,high,"Both sources are textual/archival analyses of proposal and idea abstracts with no fieldwork or interview component; no situated interlocutor is present in the evidence.",C011_P1; C011_S1,,upgraded from low: full text clearly rules this role out
        11,Accountability and labor allocator,starting_role,yes,conditional,high,"P1 directly discusses NIH's declaration that AI-substantially-developed applications will not be considered applicants' original work and NSF's investigator-responsibility language, which is exactly the authorship/accountability allocation function.",C011_P1,,upgraded from low: P1's policy paragraph on NIH/NSF guidance is direct evidence
        11,Construct boundary setter,split_candidate,no,not_applicable,medium,"Neither source adjudicates category boundaries or codebook rules; S1's review rubric uses predefined criteria (novelty, excitement, feasibility, effectiveness) rather than contesting construct boundaries.",C011_P1; C011_S1,,upgraded from low: split candidate not activated
        11,Perspective sampler,split_candidate,no,not_applicable,medium,"Neither source frames preservation of subgroup disagreement as the core role; S1 reports inter-reviewer disagreement and even uses it as a caveat, but does not position humans as pluralism guardians.",C011_P1; C011_S1,,upgraded from low
        11,Counterfactual / transportability judge,split_candidate,no,not_applicable,medium,"P1's NSF-vs-NIH contrast is suggestive of transportability pressure, but the human role doing that adjudication is not the object of either source.",C011_P1; C011_S1,,upgraded from low
        11,Calibration architect,split_candidate,no,not_applicable,medium,"Neither source centers benchmarking or simulator calibration; P1 uses Liang et al.'s detection method and S1 uses a Swiss-tournament LLM ranker validated against ICLR review scores, but calibration is not the human role at stake.",C011_P1; C011_S1,,upgraded from low
        11,Situated interlocutor,split_candidate,no,not_applicable,high,"Both sources are document-level analyses with no interview, fieldwork, or respondent interaction.",C011_P1; C011_S1,,upgraded from low: clearly ruled out by study designs
        11,Context witness,split_candidate,no,not_applicable,high,"Neither source uses tacit or archival context knowledge to interpret traces; P1 relies on abstract-level embeddings and S1 on standardized idea templates.",C011_P1; C011_S1,,upgraded from low: clearly ruled out by study designs
        11,Routine first-pass screener,shrinking_task_cluster,no,not_applicable,medium,"Neither source studies abstract/title triage or study-type classification; P1 analyzes submissions and awards without an AI-screening pipeline, and S1's screener for AI ideas is a human expert reranker, not a shrinking routine.",C011_P1; C011_S1,,upgraded from low
        11,"Routine coder on high-consensus, ground-truth-rich tasks",shrinking_task_cluster,no,not_applicable,medium,"Neither source depicts routine coding against ground truth; P1 measures aggregate textual signals, and S1's reviewers apply subjective multi-metric judgments rather than high-consensus labels.",C011_P1; C011_S1,,upgraded from low
        11,Structural prose polisher / drafter,shrinking_task_cluster,yes,shrinking,high,"P1's core finding is that LLMs are substantively rewriting proposal prose (bimodal alpha, higher reading complexity, lower distinctiveness), i.e., the drafter/polisher task is measurably being absorbed by AI; S1 additionally uses an LLM style normalizer for all ideas.",C011_P1; C011_S1,,"upgraded from low and from no to yes: P1 directly evidences AI take-over of proposal drafting; status_in_case set to shrinking per codebook definition for drafter/polisher task clusters"
    '''),
    12: dedent('''\
        case_id,role_label,role_group,role_observable_in_case,status_in_case,confidence,evidence_basis_summary,main_supporting_source_ids,main_contrary_source_ids,notes
        12,Relevance adjudicator,starting_role,yes,conditional,medium,"Authors explicitly scope the analysis universe to NSF/NIH proposals from two R1 universities (D1-D2) and the full population of public NSF/NIH awards (D3-D4) with 2021-2025 start dates, a human inclusion decision.",C012_P1; C012_REGISTRY,,Upgraded from low: source makes data-scoping choices explicit but they are design decisions not central findings.
        12,Mechanism disciplinarian,starting_role,yes,conditional,high,"Causal interpretation is explicitly disciplined by investigator and field fixed effects, requested-funding controls, and bottlenecks-perspective caveats distinguishing writing gains from execution-driven outputs.",C012_P1; C012_REGISTRY,,"Upgraded from low to high and observable changed from partial to yes: fixed-effects design, acknowledgment that ambitious labs may both use AI and write better proposals, and bottlenecks caveat are load-bearing human mechanism-disciplining moves."
        12,Construct and perspective boundary setter,starting_role,no,not_applicable,medium,"Construct boundaries (LLM involvement alpha, semantic distinctiveness percentile) are operational measurement definitions rather than socially contested construct work.",C012_P1; C012_REGISTRY,,Upgraded from low: source makes clear the constructs are operational metrics not pluralistic social constructs.
        12,Corpus pluralist,starting_role,partial,conditional,medium,"Authors pair confidential multi-university submission corpus (funded, unfunded, pending) with full-population public NSF/NIH awards, deliberately resisting reliance on only the publicly legible corpus.",C012_P1; C012_REGISTRY,,"Upgraded from low to medium and observable/status changed from no/not_applicable to partial/conditional: combining private submissions with public awards is the core corpus-pluralism move, though framed as complementarity rather than anti-homogenization."
        12,Protocol and provenance architect,starting_role,yes,conditional,high,"Paper documents a full detection/measurement protocol (Liang et al. method, 2021 pre-ChatGPT human baseline, GPT-3.5-turbo rewrites, three-month rolling windows, SPECTER2 embeddings) and explicitly discusses NIH and NSF disclosure/AI-use guidance.",C012_P1; C012_REGISTRY,,"Upgraded from low to high and observable/status changed from no/not_applicable to yes/conditional: the paper is built around a reproducible detection pipeline and explicitly references NIH NOT-OD-25-132 and NSF disclosure notices."
        12,Counterfactual and transportability judge,starting_role,yes,conditional,high,"Robustness checks (promotional words, L2 vs cosine, logit/NB, alternate comparison windows, field-level and subagency replications) plus explicit agency-heterogeneity discussion (NIH vs NSF) are sustained transportability adjudications.",C012_P1; C012_REGISTRY,,"Upgraded from low to high and observable/status changed from no/not_applicable to yes/conditional: Robustness and sensitivity section plus bottlenecks/agency-dependence discussion make this role central."
        12,Situated interlocutor / context witness,starting_role,no,not_applicable,high,"Study is a large-scale quantitative analysis of proposal and award abstracts with no fieldwork, interviews, or interpretive interaction; role is clearly not applicable.",C012_P1; C012_REGISTRY,,Upgraded from low to high: full text confirms no situated/interpretive data generation.
        12,Accountability and labor allocator,starting_role,yes,conditional,high,"Paper explicitly cites NIH NOT-OD-25-132 (applications substantially developed by AI not considered original work) and NSF's investigator-responsibility/disclosure notice as accountability mechanisms around LLM use.",C012_P1; C012_REGISTRY,,"Upgraded from low to high: the policy paragraph on NIH and NSF AI guidance directly addresses authorship, responsibility, and disclosure."
        12,Construct boundary setter,split_candidate,no,not_applicable,medium,"Alpha and distinctiveness are operational measurement definitions; no codebook-style category-boundary work is undertaken.",C012_P1; C012_REGISTRY,,Upgraded from low: source makes the absence of category-boundary work clear.
        12,Perspective sampler,split_candidate,no,not_applicable,medium,Analysis aggregates across investigators and agencies without preserving subgroup disagreement as a representational goal.,C012_P1; C012_REGISTRY,,Upgraded from low: no perspective-pluralism design evident in full text.
        12,Counterfactual / transportability judge,split_candidate,yes,conditional,high,"Agency-dependence findings (NIH effects do not transport to NSF) and bottlenecks argument against extrapolating writing gains to downstream impact are explicit transportability judgments.",C012_P1; C012_REGISTRY,,"Upgraded from low to high and observable/status changed from no/not_applicable to yes/conditional: the paper's central empirical contribution is about when LLM effects do and do not transport across agencies and across writing-vs-impact outcomes."
        12,Calibration architect,split_candidate,yes,conditional,high,"Detection method is explicitly calibrated against a 2021 pre-ChatGPT human word distribution and a GPT-3.5-turbo-0125 reference distribution, with distinctiveness percentiles benchmarked to prior-year agency funding frontiers.",C012_P1; C012_REGISTRY,,"Upgraded from low to high and observable/status changed from no/not_applicable to yes/conditional: the LLM-detection and distinctiveness measures are built on explicit calibration to external reference distributions."
        12,Situated interlocutor,split_candidate,no,not_applicable,high,No fieldwork or interviewer presence anywhere in the study design.,C012_P1; C012_REGISTRY,,Upgraded from low to high: full text confirms not applicable.
        12,Context witness,split_candidate,no,not_applicable,high,"Study analyzes abstracts computationally and does not rely on tacit or archival context interpretation; role not applicable.",C012_P1; C012_REGISTRY,,Upgraded from low to high: full text confirms not applicable.
        12,Routine first-pass screener,shrinking_task_cluster,no,not_applicable,medium,"Paper studies LLM use by applicants, not triage/screening by reviewers; no title/abstract screening task is being delegated.",C012_P1; C012_REGISTRY,,"Upgraded from low: the pipeline stages examined are submission and award, not reviewer-side screening."
        12,"Routine coder on high-consensus, ground-truth-rich tasks",shrinking_task_cluster,no,not_applicable,medium,"No human coding task with ground-truth labels is present; LLM-use detection is statistical distribution-matching, not coder replacement.",C012_P1; C012_REGISTRY,,Upgraded from low: absence of a routine-coder task is clear from the methods.
        12,Structural prose polisher / drafter,shrinking_task_cluster,yes,transformed,high,"Authors show LLM use in proposal drafting is detectable, bimodal, and consequential: it is associated with lower semantic distinctiveness and, at NIH, higher funding probability and non-hit publication counts, indicating prose drafting is being actively reshaped.",C012_P1; C012_REGISTRY,,"Upgraded from low to high and observable/status changed from no/not_applicable to yes/transformed: the paper's entire empirical object is LLM-assisted proposal drafting and its portfolio-level consequences for agenda compression."
    '''),
    13: dedent('''\
        case_id,role_label,role_group,role_observable_in_case,status_in_case,confidence,evidence_basis_summary,main_supporting_source_ids,main_contrary_source_ids,notes
        13,Relevance adjudicator,starting_role,yes,conditional,high,"C013_S1 Sections 2-4 show humans defining the 7 topic set from NLP CFPs, screening participants by Google Scholar, and the first author manually reranking LLM outputs for the AI+Rerank condition; C013_P1 abstract shows users select which facets/papers count.",C013_P1; C013_S1,,upgraded from low; direct full-text evidence of humans deciding what belongs.
        13,Mechanism disciplinarian,starting_role,yes,conditional,medium,"C013_S1 Section 2 imposes a grant-style idea template (problem/method/experiment plan/fallback) and defines four review dimensions to constrain what counts as a legitimate mechanism claim; C013_P1 facet-based novelty checker constrains mechanism novelty to facet matches.",C013_P1; C013_S1,,upgraded from low; role is present but indirect in case-specific terms.
        13,Construct and perspective boundary setter,starting_role,no,not_applicable,medium,"Neither source frames the case around social-science construct boundaries; C013_S1's construct work is about idea-quality rubrics, not socially meaningful disagreement about a study construct.",C013_P1; C013_S1,,upgraded from low; full text confirms not_applicable for this case framing.
        13,Corpus pluralist,starting_role,partial,conditional,high,"C013_P1 abstract explicitly describes the Analogous Paper Facet Finder as distance-controlled retrieval that surfaces papers from the same topic through entirely different subareas to prevent collapse onto the most-legible corpus.",C013_P1; C013_S1,,changed from no/not_applicable to partial/conditional because C013_P1 directly instantiates corpus-pluralism design.
        13,Protocol and provenance architect,starting_role,yes,robust,high,"C013_S1 Sections 2-4 detail IRB approval (Stanford 74246), standardized idea templates, blind review assignment avoiding institutional contamination, Swiss-tournament pairwise ranking protocol, deduplication threshold, LLM style normalization with manual content verification by the first author, and a release of agent code and review scores.",C013_P1; C013_S1,,changed from no/not_applicable to yes/robust; protocol design is central to the Si et al. methodology and directly adjacent to how the case would transfer.
        13,Counterfactual and transportability judge,starting_role,no,not_applicable,medium,"C013_S1 Section 1 and end of Section 1 acknowledge novelty/feasibility judgments may not transport to research outcomes and proposes an end-to-end execution study, but the case framing itself is about transferring Scideator to social-science prospectus ideation, not adjudicating transportability per se.",C013_P1; C013_S1,,upgraded from low; role is adjacent but not the operative question in this case.
        13,Situated interlocutor / context witness,starting_role,no,not_applicable,high,"Neither source involves fieldwork, interviewing, or interpretive presence; C013_S1 uses remote blind review of written proposals and C013_P1 is a HCI lab study of a tool.",C013_P1; C013_S1,,upgraded from low; clearly not applicable.
        13,Accountability and labor allocator,starting_role,partial,unclear,medium,"C013_S1 Section 4.1 documents IRB approval, consent forms, $300 writer / $25 reviewer compensation, $1000 bonus for top ideas, reviewer-author institution conflict rules, and open release of scores; but the case-level allocation of authorship / responsibility for Scideator-assisted social-science prospectuses is not directly adjudicated.",C013_P1; C013_S1,,upgraded from low; evidence supports partial/unclear judgment.
        13,Construct boundary setter,split_candidate,no,not_applicable,medium,"C013_S1's review form defines novelty/excitement/feasibility/effectiveness with 1-10 anchors, which is boundary work on idea-quality labels rather than on a social-science construct; neither source treats construct-label boundaries as the operative question.",C013_P1; C013_S1,,upgraded from low.
        13,Perspective sampler,split_candidate,no,not_applicable,medium,"C013_S1 assigns 2-4 reviewers per idea and balances topics but collapses to aggregate scores; neither source preserves subgroup disagreement as an explicit design goal.",C013_P1; C013_S1,,upgraded from low.
        13,Counterfactual / transportability judge,split_candidate,no,not_applicable,medium,"C013_S1 flags transportability of novelty judgments to research outcomes as an open problem and proposes a follow-up execution study, but the case does not turn on a transportability test of Scideator across populations.",C013_P1; C013_S1,,upgraded from low.
        13,Calibration architect,split_candidate,yes,conditional,high,"C013_S1 Section 3.3 calibrates the LLM ranker against 1200 ICLR submissions (pairwise accuracy 71.4% for Claude-3.5-Sonnet) and Section 2 calibrates reviewer scales with anchored 1-10 definitions; C013_P1 reports the facet-based novelty checker raising classification accuracy from 13.79% to 89.66%.",C013_P1; C013_S1,,changed from no/not_applicable to yes/conditional; both sources explicitly calibrate ranking/novelty pipelines against external reference distributions.
        13,Situated interlocutor,split_candidate,no,not_applicable,high,"Neither source involves an interviewer or fieldworker whose presence changes disclosure; tasks are written-idea generation and asynchronous blind review.",C013_P1; C013_S1,,upgraded from low.
        13,Context witness,split_candidate,no,not_applicable,high,"Neither source relies on contextual or tacit archival knowledge to interpret notes or transcripts; evaluation is on standardized written proposals.",C013_P1; C013_S1,,upgraded from low.
        13,Routine first-pass screener,shrinking_task_cluster,yes,shrinking,high,"C013_S1 Section 3.1 has the LLM generate Semantic Scholar API calls and score/rerank up to 120 retrieved papers on 1-10 relevance, and Section 3.3 uses an LLM pairwise ranker (Swiss tournament) to triage 4000 seed ideas down to a small set for human review; C013_P1 similarly automates facet retrieval.",C013_P1; C013_S1,,changed from no/not_applicable to yes/shrinking; first-pass paper/idea triage is materially delegated to the LLM.
        13,"Routine coder on high-consensus, ground-truth-rich tasks",shrinking_task_cluster,no,not_applicable,high,"C013_S1 Section 1 explicitly states research ideation has no consensus ground truth and that even experts struggle to judge idea quality, so the high-consensus-coder pattern does not apply here.",C013_P1; C013_S1,,upgraded from low; source directly rules out this pattern.
        13,Structural prose polisher / drafter,shrinking_task_cluster,yes,shrinking,high,"C013_S1 Section 2 describes a dedicated LLM style-normalization module that converts all human and AI ideas into the same writing/formatting style, with the first author manually verifying content preservation - exactly a structural polishing task taken over by AI without displacing accountability.",C013_P1; C013_S1,,changed from no/not_applicable to yes/shrinking; style normalization is explicitly an AI-delegated polishing step.
    '''),
}


def parse_csv_text(text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(text))
    return list(reader)


def read_csv_file(path: Path) -> list[dict[str, str]]:
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv_file(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def apply_case_updates() -> None:
    for case_id, csv_text in CASE_UPDATES_CSV.items():
        slug = CASE_SLUGS[case_id]
        rows = parse_csv_text(csv_text)
        assert len(rows) == 17, f"Case {case_id} has {len(rows)} rows, expected 17"
        path = PROJECT_ROOT / "02_cases" / slug / "role_coding.csv"
        write_csv_file(path, ROLE_FIELDS, rows)
        print(f"Wrote {path} ({len(rows)} rows)")


def rebuild_master() -> list[dict[str, str]]:
    all_rows: list[dict[str, str]] = []
    for case_id in sorted(CASE_SLUGS):
        slug = CASE_SLUGS[case_id]
        path = PROJECT_ROOT / "02_cases" / slug / "role_coding.csv"
        if not path.exists():
            continue
        all_rows.extend(read_csv_file(path))
    out = PROJECT_ROOT / "06_analysis_tables" / "role_coding_master.csv"
    write_csv_file(out, ROLE_FIELDS, all_rows)
    print(f"Rebuilt {out} ({len(all_rows)} rows)")
    return all_rows


def rebuild_confidence_report(role_master: list[dict[str, str]]) -> None:
    cases_master = read_csv_file(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    sources_master = read_csv_file(PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv")

    source_by_case: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sources_master:
        if row.get("source_role") == "registry":
            continue
        source_by_case[row["case_id"]].append(row)

    confidence_by_case: dict[str, Counter] = defaultdict(Counter)
    for row in role_master:
        confidence_by_case[row["case_id"]][row.get("confidence", "")] += 1

    out_fields = [
        "case_id",
        "case_slug",
        "case_title",
        "analysis_ready",
        "low_confidence_rows",
        "medium_confidence_rows",
        "high_confidence_rows",
        "open_external_sources",
        "non_open_external_sources",
        "uses_open_fallback_or_companion_source",
        "next_review_priority",
    ]
    rows = []
    for case in cases_master:
        case_id = case["Case ID"]
        sources = source_by_case.get(case_id, [])
        counts = confidence_by_case.get(case_id, Counter())
        open_count = sum(1 for r in sources if r.get("access_status") == "open")
        non_open_count = sum(1 for r in sources if r.get("access_status") != "open")
        uses_fallback = "yes" if open_count and non_open_count else "no"
        low = counts.get("low", 0)
        priority = "high" if low >= 15 or non_open_count else "medium" if low else "low"
        rows.append(
            {
                "case_id": case_id,
                "case_slug": case["case_slug"],
                "case_title": case["Case title"],
                "analysis_ready": case["analysis_ready"],
                "low_confidence_rows": str(low),
                "medium_confidence_rows": str(counts.get("medium", 0)),
                "high_confidence_rows": str(counts.get("high", 0)),
                "open_external_sources": str(open_count),
                "non_open_external_sources": str(non_open_count),
                "uses_open_fallback_or_companion_source": uses_fallback,
                "next_review_priority": priority,
            }
        )
    out = PROJECT_ROOT / "08_logs" / "role_confidence_report.csv"
    write_csv_file(out, out_fields, rows)
    print(f"Rebuilt {out} ({len(rows)} rows)")


def rebuild_data_inventory(role_master: list[dict[str, str]]) -> None:
    cases_master = read_csv_file(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    sources_master = read_csv_file(PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv")

    ar_counts = Counter(row["analysis_ready"] for row in cases_master)
    src_counts = Counter(
        row["access_status"] for row in sources_master if row.get("source_role") != "registry"
    )
    conf_counts = Counter(row.get("confidence", "") for row in role_master)

    by_case: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in sources_master:
        if row.get("source_role") == "registry":
            continue
        by_case[row["case_id"]].append(row)
    fallback_supported = sum(
        1
        for rows in by_case.values()
        if any(r.get("access_status") == "open" for r in rows)
        and any(r.get("access_status") != "open" for r in rows)
    )

    lines = [
        "# Data Inventory",
        "",
        f"- Cases in registry: {len(cases_master)}",
        f"- Analysis-ready `yes`: {ar_counts.get('yes', 0)}",
        f"- Analysis-ready `partial`: {ar_counts.get('partial', 0)}",
        f"- Analysis-ready `no`: {ar_counts.get('no', 0)}",
        f"- Open external sources: {src_counts.get('open', 0)}",
        f"- Paywalled external sources: {src_counts.get('paywalled', 0)}",
        f"- Inaccessible external sources: {src_counts.get('inaccessible', 0)}",
        f"- Cases with open fallback or companion-source coverage: {fallback_supported}",
        f"- Role-coding rows at `high` confidence: {conf_counts.get('high', 0)}",
        f"- Role-coding rows at `medium` confidence: {conf_counts.get('medium', 0)}",
        f"- Role-coding rows at `low` confidence: {conf_counts.get('low', 0)}",
    ]
    out = PROJECT_ROOT / "data_inventory.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Rebuilt {out}")


def rebuild_known_gaps(role_master: list[dict[str, str]]) -> None:
    cases_master = read_csv_file(PROJECT_ROOT / "01_registry" / "cases_master.csv")
    sources_master = read_csv_file(PROJECT_ROOT / "06_analysis_tables" / "sources_master.csv")

    weak_cases = [row for row in cases_master if row["analysis_ready"] != "yes"]
    title_lookup = {row["Case ID"]: row["Case title"] for row in cases_master}

    lines = ["# Known Gaps", ""]
    if weak_cases:
        lines.append("## Case-level gaps")
        lines.append("")
        for row in weak_cases:
            lines.append(
                f"- Case {row['Case ID']} ({row['Case title']}): {row['analysis_ready']} / {row['collection_status']} - {row['main_limitations']}"
            )
    else:
        lines.append("- No case-level analysis gaps remain.")

    non_open = [
        row
        for row in sources_master
        if row.get("source_role") != "registry" and row.get("access_status") != "open"
    ]
    if non_open:
        lines.extend(["", "## Residual source-access limits", ""])
        for row in non_open:
            lines.append(
                f"- Case {row['case_id']} source {row['source_id']} ({row['access_status']}): {row['URL']}"
            )
        lines.append(
            "- These remaining journal-original URL failures do not block analysis where a lawful local fallback or companion full text is already stored; the unresolved part is journal-page retrieval, often due to anti-bot or landing-page access friction."
        )

    conf_counts = Counter(row.get("confidence", "") for row in role_master)
    if role_master and conf_counts.get("low", 0):
        low_by_case: Counter = Counter(
            row["case_id"] for row in role_master if row.get("confidence") == "low"
        )
        top_cases = ", ".join(
            f"Case {case_id} ({title_lookup.get(case_id, case_id)}: {count})"
            for case_id, count in low_by_case.most_common(5)
        )
        lines.extend(
            [
                "",
                "## Residual role-coding confidence limits",
                "",
                f"- Low-confidence role rows: {conf_counts.get('low', 0)} of {len(role_master)} total.",
                f"- Medium-confidence role rows: {conf_counts.get('medium', 0)}; high-confidence role rows: {conf_counts.get('high', 0)}.",
                f"- Cases with the densest low-confidence coding: {top_cases}.",
                "- These rows remain traceable, but many still rely on workbook-driven initialization or limited direct role evidence.",
            ]
        )
    elif role_master:
        lines.extend(
            [
                "",
                "## Residual role-coding confidence limits",
                "",
                f"- Low-confidence role rows: 0 of {len(role_master)} total.",
                f"- Medium-confidence role rows: {conf_counts.get('medium', 0)}; high-confidence role rows: {conf_counts.get('high', 0)}.",
            ]
        )

    out = PROJECT_ROOT / "known_gaps.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Rebuilt {out}")


def main() -> int:
    apply_case_updates()
    role_master = rebuild_master()
    rebuild_confidence_report(role_master)
    rebuild_data_inventory(role_master)
    rebuild_known_gaps(role_master)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
