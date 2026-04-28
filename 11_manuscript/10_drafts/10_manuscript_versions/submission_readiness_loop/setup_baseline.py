"""Phase 1.1 setup: save baseline, extract text, build structure.json + state files."""
from __future__ import annotations

import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path("/Users/ryanwong/Human roles/p1_role_systems_db")
SRC = ROOT / "11_manuscript/10_drafts/10_manuscript.md"
LOOP = ROOT / "11_manuscript/10_drafts/10_manuscript_versions/submission_readiness_loop"

# 1. Save baseline
shutil.copy(SRC, LOOP / "v00_baseline.md")

# 2. Extract working text — for .md, the working copy IS the source; copy as current_text.txt
md = SRC.read_text(encoding="utf-8")
(LOOP / "current_text.txt").write_text(md, encoding="utf-8")

# 3. Build structure.json: sections by ATX heading
HEADING_RE = re.compile(r"^(#+)\s+(.*?)\s*$", re.MULTILINE)
lines = md.splitlines()
sections = []
prev = None
for i, line in enumerate(lines, start=1):
    m = re.match(r"^(#+)\s+(.*?)\s*$", line)
    if m:
        if prev is not None:
            prev["end_line"] = i - 1
            sections.append(prev)
        prev = {
            "title": m.group(2),
            "level": len(m.group(1)),
            "start_line": i,
            "end_line": None,
        }
if prev is not None:
    prev["end_line"] = len(lines)
    sections.append(prev)

# Word count per section
def words(text: str) -> int:
    return len(re.findall(r"\b[A-Za-z][A-Za-z'\-]*\b", text))

for s in sections:
    body = "\n".join(lines[s["start_line"]:s["end_line"]])
    s["word_count"] = words(body)

structure = {
    "total_word_count": words(md),
    "section_count": len(sections),
    "sections": sections,
}
(LOOP / "structure.json").write_text(
    json.dumps(structure, indent=2, ensure_ascii=False), encoding="utf-8"
)

# 4. Init loop_state.json
loop_state = {
    "loop": "submission_readiness_loop",
    "task": "ensure the manuscript is ready for submission",
    "target_venue": "Organizational Research Methods (ORM)",
    "baseline_version": "v39_title_revised + TR5 (uncommitted; 42-word §6.2 insertion)",
    "started": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    "max_iterations": 5,
    "iteration": 0,
    "agents": {
        "A": "Methodology Specialist (ORM construct-validity, BARS, formative measurement)",
        "B": "Domain Theory Expert (typology theory, role theory, AI-in-research)",
        "C": "Journal Editor / Prose (ORM register, hedging, claim ceiling)",
        "D": "Comparative Methods Expert (cross-case sampling, inference under N=36)",
        "E": "Submission-Process Auditor (compliance with ORM submission requirements)",
        "F": "Data Integrity Auditor (manuscript stats vs. 06_analysis_tables/ ground truth)",
    },
    "do_not_change": [
        "All inferential statistics (chi2, Cramer V, p, kappa, CIs) — must match section6_analysis_output.json and intercoder_agreement_stats.json byte-for-byte",
        "Title (just shipped at v39 after deliberate revision)",
        "Case IDs and exemplar assignments",
        "Pre-registered hypotheses (H1, H2, H3) and tie-breaker rules",
        "Release tag v1.0.0-ORM-submission and Zenodo references",
    ],
    "scope_includes": [
        "TR5 (already applied) — verify integration",
        "Submission-readiness gaps surfaced by reviewer agents",
        "Data-manuscript alignment (Agent F)",
        "Cross-section consistency on shared statistics",
        "Reference list integrity",
        "ORM-style register/hedging consistency",
    ],
    "scores": [],
    "agent_history": [],
    "convergence": None,
}
(LOOP / "loop_state.json").write_text(
    json.dumps(loop_state, indent=2, ensure_ascii=False), encoding="utf-8"
)

# 5. Init changelog.md
changelog = (
    f"# Submission-Readiness Edit Loop — Changelog\n\n"
    f"**Started:** {loop_state['started']}\n"
    f"**Baseline:** v39_title_revised + TR5 (live `10_manuscript.md`, uncommitted)\n"
    f"**Target:** Organizational Research Methods (ORM) submission\n"
    f"**Total baseline words:** {structure['total_word_count']}\n"
    f"**Sections:** {structure['section_count']}\n\n"
    f"---\n\n"
    f"## Pre-loop state notes\n\n"
    f"- v39 shipped at commit `c80dc6c`, pushed to `origin/main` 2026-04-27.\n"
    f"- TR5 (§6.2 “v1.0 baseline” sentence, +42 words) applied to live md only.\n"
    f"- Earlier transplant inventory (TR1, TR2a, TR2c, TR4, TR6, TR7) confirmed already applied across v31–v39.\n"
    f"- TR3 partial (positioning choice, not edit gap); TR8 closed by v39 title revision.\n\n"
    f"## Iterations\n\n"
)
(LOOP / "changelog.md").write_text(changelog, encoding="utf-8")

print(f"Baseline saved: {LOOP/'v00_baseline.md'}")
print(f"Total words: {structure['total_word_count']}")
print(f"Sections: {structure['section_count']}")
print(f"Top-level sections:")
for s in sections:
    if s["level"] <= 2:
        print(f"  L{s['level']} {s['title'][:70]:<70} ({s['word_count']:>5} w)")
