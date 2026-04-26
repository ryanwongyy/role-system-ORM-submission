#!/usr/bin/env python3
from __future__ import annotations

import shutil
import sys
import time
from pathlib import Path

from pypdf import PdfReader


DOWNLOADS = Path.home() / "Downloads"
LIB_ROOT = Path(
    "/Users/ryanwong/Human roles/p1_role_systems_db/11_manuscript/20_citations/expanded_reference_library"
)
PDF_DIR = LIB_ROOT / "pdfs"
INCOMING_DIR = LIB_ROOT / "browser_incoming"


RULES = [
    (
        "O2_nosek_ebersole_dehaven_mellor_2018_preregistration_revolution.pdf",
        [
            "the preregistration revolution",
            "preregistration revolution",
            "postdiction as prediction",
            "1708274114",
        ],
    ),
    (
        "A5_dillion_tandon_gu_gray_2023_ai_language_models_human_participants.pdf",
        [
            "can ai language models replace human participants",
            "s1364661323000980",
            "fh3ua",
            "human participants",
        ],
    ),
    (
        "B6_short_broberg_cogliser_brigham_2010_cata.pdf",
        [
            "construct validation using computer-aided text analysis",
            "cata",
            "entrepreneurial orientation",
        ],
    ),
    (
        "B7_bluhm_harman_lee_mitchell_2011_qualitative_management.pdf",
        [
            "qualitative research in management",
            "a decade in review",
            "a decade of progress",
            "joms_972",
        ],
    ),
    (
        "C1_doty_glick_1994_typologies_theory_building.pdf",
        [
            "typologies as a unique form of theory building",
            "toward improved understanding and modeling",
            "258704",
        ],
    ),
    (
        "C3_delbridge_fiss_2013_styles_of_theorizing.pdf",
        [
            "styles of theorizing",
            "social organization of knowledge",
            "delbridge",
            "fiss",
        ],
    ),
    (
        "C4_bailey_1994_typologies_and_taxonomies.pdf",
        [
            "typologies and taxonomies",
            "kenneth d. bailey",
        ],
    ),
    (
        "D3_brint_1994_age_of_experts.pdf",
        [
            "in an age of experts",
            "steven brint",
        ],
    ),
    (
        "D4_fournier_2000_boundary_work_unmaking_professions.pdf",
        [
            "boundary work and the",
            "un-making of the professions",
            "unmaking of the professions",
            "fournier",
        ],
    ),
    (
        "D5_susskind_susskind_2015_future_professions.pdf",
        [
            "the future of the professions",
            "richard susskind",
            "daniel susskind",
        ],
    ),
    (
        "D6_anteby_chan_dibenigno_2016_occupations_professions_organizations.pdf",
        [
            "three lenses on occupations and professions in organizations",
            "anteby",
            "dibenigno",
        ],
    ),
    (
        "E1_biddle_1986_recent_developments_role_theory.pdf",
        [
            "recent developments in role theory",
            "biddle",
        ],
    ),
    (
        "E4_merton_1957_role_set.pdf",
        [
            "the role-set",
            "problems in sociological theory",
            "merton",
        ],
    ),
    (
        "F1_messick_1995_validity_psychological_assessment.pdf",
        [
            "validity of psychological assessment",
            "messick",
            "scientific inquiry into score meaning",
        ],
    ),
    (
        "F3_borsboom_mellenbergh_van_heerden_2004_concept_validity.pdf",
        [
            "the concept of validity",
            "borsboom",
            "mellenbergh",
        ],
    ),
    (
        "F4_edwards_2011_formative_measurement_fallacy.pdf",
        [
            "the fallacy of formative measurement",
            "edwards",
        ],
    ),
    (
        "F5_bagozzi_yi_phillips_1991_construct_validity_organizational_research.pdf",
        [
            "assessing construct validity in organizational research",
            "bagozzi",
            "phillips",
        ],
    ),
    (
        "F6_diamantopoulos_riefler_roth_2008_formative_measurement_models.pdf",
        [
            "advancing formative measurement models",
            "diamantopoulos",
            "riefler",
        ],
    ),
    (
        "G3_hruschka_etal_2004_reliability_coding_open_ended_data.pdf",
        [
            "reliability in coding open-ended data",
            "hruschka",
            "hiv behavioral research",
        ],
    ),
    (
        "G5_duriau_reger_pfarrer_2007_content_analysis_organization_studies.pdf",
        [
            "a content analysis of the content analysis literature in organization studies",
            "duriau",
            "pfarrer",
        ],
    ),
    (
        "H1_cohen_1960_agreement_nominal_scales.pdf",
        [
            "a coefficient of agreement for nominal scales",
            "cohen",
        ],
    ),
    (
        "H3_hayes_krippendorff_2007_standard_reliability_measure.pdf",
        [
            "answering the call for a standard reliability measure for coding data",
            "hayes",
            "krippendorff",
        ],
    ),
    (
        "H5_lombard_snyder_duch_bracken_2002_intercoder_reliability.pdf",
        [
            "content analysis in mass communication",
            "assessment and reporting of intercoder reliability",
            "lombard",
        ],
    ),
    (
        "H6_landis_koch_1977_observer_agreement_categorical_data.pdf",
        [
            "the measurement of observer agreement for categorical data",
            "landis",
            "koch",
        ],
    ),
    (
        "I3_fiss_sharapov_cronqvist_2013_large_n_qca_econometric.pdf",
        [
            "opposites attract",
            "large-n qca",
            "cronqvist",
        ],
    ),
    (
        "I4_kraus_ribeiro_soriano_schussler_2018_fsQCA_entrepreneurship_innovation.pdf",
        [
            "fuzzy-set qualitative comparative analysis",
            "fsqca",
            "entrepreneurship and innovation research",
        ],
    ),
    (
        "I5_greckhamer_furnari_fiss_aguilera_2018_qca_best_practices.pdf",
        [
            "studying configurations with qualitative comparative analysis",
            "best practices in strategy and organization research",
            "greckhamer",
        ],
    ),
    (
        "J2_eisenhardt_1989_building_theories_case_study_research.pdf",
        [
            "building theories from case study research",
            "eisenhardt",
        ],
    ),
    (
        "J3_eisenhardt_2021_eisenhardt_method_really.pdf",
        [
            "what is the eisenhardt method, really",
            "strategic organization",
        ],
    ),
    (
        "J5_langley_1999_theorizing_process_data.pdf",
        [
            "strategies for theorizing from process data",
            "langley",
        ],
    ),
    (
        "K2_tranfield_denyer_smart_2003_systematic_review_management.pdf",
        [
            "towards a methodology for developing evidence-informed management knowledge by means of systematic review",
            "tranfield",
            "denyer",
        ],
    ),
    (
        "K3_rousseau_manning_denyer_2008_evidence_management_organizational_science.pdf",
        [
            "evidence in management and organizational science",
            "rousseau",
            "denyer",
        ],
    ),
    (
        "K4_short_2009_art_writing_review_article.pdf",
        [
            "the art of writing a review article",
            "journal of management",
            "short",
        ],
    ),
    (
        "K5_siddaway_wood_hedges_2019_how_to_do_systematic_review.pdf",
        [
            "how to do a systematic review",
            "siddaway",
            "hedges",
        ],
    ),
    (
        "L3_wallach_2018_css_not_cs_plus_social_data.pdf",
        [
            "computational social science",
            "computer science + social data",
            "wallach",
        ],
    ),
    (
        "L4_edelmann_wolff_montagne_bail_2020_css_sociology.pdf",
        [
            "computational social science and sociology",
            "edelmann",
            "bail",
        ],
    ),
    (
        "L5_lazer_etal_2020_css_obstacles_opportunities.pdf",
        [
            "computational social science: obstacles and opportunities",
            "aaz8170",
            "lazer",
        ],
    ),
    (
        "N2_frey_osborne_2017_future_employment_computerisation.pdf",
        [
            "the future of employment",
            "susceptible are jobs to computerisation",
            "frey",
            "osborne",
        ],
    ),
    (
        "N3_brynjolfsson_mitchell_2017_machine_learning_workforce.pdf",
        [
            "what can machine learning do",
            "workforce implications",
            "brynjolfsson",
            "mitchell",
        ],
    ),
    (
        "N4_acemoglu_restrepo_2020_robots_jobs_us_labor_markets.pdf",
        [
            "robots and jobs",
            "evidence from us labor markets",
            "acemoglu",
            "restrepo",
        ],
    ),
    (
        "N5_raisch_krakowski_2021_automation_augmentation_paradox.pdf",
        [
            "the automation-augmentation paradox",
            "artificial intelligence and management",
            "raisch",
            "krakowski",
        ],
    ),
    (
        "O6_bergh_etal_2016_mase_strategic_management.pdf",
        [
            "using meta-analytic structural equation modeling to advance strategic management research",
            "bergh",
            "heavey",
        ],
    ),
]


def wait_until_stable(path: Path, tries: int = 6, sleep_s: float = 2.0) -> bool:
    last_size = -1
    for _ in range(tries):
        try:
            size = path.stat().st_size
        except FileNotFoundError:
            return False
        if size > 0 and size == last_size:
            return True
        last_size = size
        time.sleep(sleep_s)
    return False


def extract_pdf_text(path: Path) -> str:
    try:
        reader = PdfReader(str(path))
        chunks = []
        for page in reader.pages[:2]:
            text = page.extract_text() or ""
            chunks.append(text)
        return "\n".join(chunks).lower()
    except Exception:
        return ""


def infer_target_name(path: Path, text: str) -> str | None:
    haystack = f"{path.name.lower()}\n{text}"
    for target, needles in RULES:
        if any(needle in haystack for needle in needles):
            return target
    return None


def copy_unique(src: Path, dst: Path) -> Path:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.copy2(src, dst)
        return dst
    stem = dst.stem
    suffix = dst.suffix
    counter = 2
    while True:
        candidate = dst.with_name(f"{stem}__{counter}{suffix}")
        if not candidate.exists():
            shutil.copy2(src, candidate)
            return candidate
        counter += 1


def main() -> int:
    INCOMING_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    started = time.time()
    seen: set[tuple[str, int, int]] = set()

    print(f"Watching {DOWNLOADS} for new PDFs...")
    sys.stdout.flush()

    while True:
        for path in DOWNLOADS.glob("*.pdf"):
            try:
                stat = path.stat()
            except FileNotFoundError:
                continue
            if stat.st_mtime < started:
                continue
            key = (path.name, int(stat.st_mtime), stat.st_size)
            if key in seen:
                continue
            if not wait_until_stable(path):
                continue
            try:
                if path.read_bytes()[:5] != b"%PDF-":
                    seen.add(key)
                    print(f"SKIP non-pdf payload: {path.name}")
                    sys.stdout.flush()
                    continue
            except Exception:
                continue

            text = extract_pdf_text(path)
            target_name = infer_target_name(path, text)
            if target_name:
                final_path = copy_unique(path, PDF_DIR / target_name)
                print(f"CAPTURED {path.name} -> pdfs/{final_path.name}")
            else:
                final_path = copy_unique(path, INCOMING_DIR / path.name)
                print(f"CAPTURED {path.name} -> browser_incoming/{final_path.name}")
            seen.add(key)
            sys.stdout.flush()
        time.sleep(2.0)


if __name__ == "__main__":
    raise SystemExit(main())
