# OSF Upload Handoff

## Before you begin (one-time setup)

1. Create an OSF account at https://osf.io if you don't already have one (free; ORCID login works).
2. Confirm the OSF registration template you will use: https://osf.io/registries — select "OSF Preregistration" (not "Open-Ended Registration" and not "Registered Report Protocol").

## The upload steps (≤ 15 minutes)

1. Open `/Users/ryanwong/Human roles/p1_role_systems_db/11_manuscript/30_reviews/OSF_preregistration.md` in a browser / editor.

2. On OSF, create a **new project** titled *"Inter-coder Reliability Pass for From Repository to Role System (ORM submission)"*. Set visibility to public.

3. Inside that project, click **Registrations → Create Registration → OSF Preregistration Template**.

4. Paste the full contents of `OSF_preregistration.md` into the registration form. Most fields accept markdown. Key mappings:
   - "Title" → match the project title
   - "Study information" → §§1–2 of the OSF document
   - "Design" → §3
   - "Analysis plan" → §4–5
   - "Sample size" → 68 cells (4 cases × 17 roles)
   - "Variables" → the six observable statuses plus `unclear` / `not_applicable`

5. **Before clicking Register, confirm two things:**
   - The *second coder has not yet seen the rubric or the case files*. If they have, you must label this as a **pre-analysis plan** in §1 of the OSF document before submitting (change the heading and add a note). The convergence-report memo explains why this matters.
   - The drop-dead date (2026-06-15) is still feasible. If not, update §6 of the OSF document to a realistic date before submitting.

6. Click **Register**. OSF timestamps the registration to the second.

7. Copy (a) the OSF URL (shape: `https://osf.io/<5-char-id>/`), and (b) the ISO-formatted timestamp shown on the registration page (shape: `2026-MM-DDTHH:MM:SS.nnnnnnZ`).

## Apply to the manuscript

Run the following one-liner — it finds the two OSF placeholder strings in the manuscript and replaces them with your real URL and timestamp, then regenerates the .docx:

```bash
cd "/Users/ryanwong/Human roles/p1_role_systems_db"
OSF_URL="https://osf.io/XXXXX/"           # paste from OSF
OSF_TIMESTAMP="2026-MM-DDTHH:MM:SSZ"       # paste from OSF (ISO 8601 UTC)

python3 - <<EOF
import re
from pathlib import Path

md_path = Path("11_manuscript/10_drafts/10_manuscript.md")
md = md_path.read_text()

# Replace the Transparency-and-Disclosures OSF placeholder
old_1 = "The second-coder protocol for Appendix B (four cases, 68 cells, stratified across the four largest case-family clusters) is to be preregistered on OSF before the second coder begins work; the OSF URL and ISO timestamp will be inserted here at resubmission."
new_1 = f"The second-coder protocol for Appendix B (four cases, 68 cells, stratified across the four largest case-family clusters) is preregistered on OSF at $OSF_URL, timestamped $OSF_TIMESTAMP — predating the second coder's first sight of the rubric."

# Replace the contingency sentence
old_2 = "If the OSF registration does not predate the second-coder pass, the Appendix B κ will be labeled as a pre-analysis plan rather than as preregistration."
new_2 = ""  # contingency no longer needed once OSF is posted

if old_1 not in md: raise SystemExit("Placeholder 1 not found; manuscript may have drifted from v08.")
md = md.replace(old_1, new_1)
md = md.replace(old_2 + "\n", "").replace("\n" + old_2, "")
md_path.write_text(md)
print("Manuscript updated.")

# Also update Appendix B placeholder
apx = Path("11_manuscript/10_drafts/appendix_B_kappa.md")
ax = apx.read_text()
ax = ax.replace("[link to be finalized at submission]", "$OSF_URL")
ax = ax.replace("[link to be finalized]", "$OSF_URL")
apx.write_text(ax)
print("Appendix B updated.")
EOF

# Regenerate docx with current column widths
python3 09_scripts/md_to_docx.py
python3 - <<'PY'
from docx import Document
from docx.shared import Inches
path = "/Users/ryanwong/Human roles/p1_role_systems_db/11_manuscript/10_drafts/10_manuscript.docx"
d = Document(path)
plans = {
    0: [0.80, 1.60, 2.20, 1.40],
    1: [1.70, 0.95, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42, 0.42, 0.41],
    2: [2.40, 1.80, 1.80],
    3: [1.70, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.70],
    4: [1.40, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 0.45, 1.00],
    5: [1.90, 0.82, 0.82, 0.82, 0.82, 0.82],
}
for idx, widths in plans.items():
    t = d.tables[idx]
    if len(t.columns) == len(widths):
        for row in t.rows:
            for cell, w in zip(row.cells, widths):
                cell.width = Inches(w)
d.save(path)
print("docx regenerated.")
PY
```

## Verify

After running the one-liner:

1. Open `10_manuscript.docx` and search for "OSF" — the Transparency and Disclosures section should now show the live URL and timestamp, not a placeholder.
2. Open `appendix_B_kappa.md` — the OSF link line should show the live URL.
3. Grep the manuscript for any remaining bracket placeholders to catch what's left:
   ```bash
   grep -n '\[.*to be.*\]\|\[TBD\]\|\[link.*\]' \
       "/Users/ryanwong/Human roles/p1_role_systems_db/11_manuscript/10_drafts/10_manuscript.md" \
       "/Users/ryanwong/Human roles/p1_role_systems_db/11_manuscript/10_drafts/appendix_B_kappa.md"
   ```
   Expected remaining: repository URL, Zenodo DOI, Appendix B κ values, and (until coder is finished) the disagreement log.

## What's still deferred

After OSF upload the three remaining author-owned items are:

1. **Repository URL** — push to GitHub / institutional repository under tag `v1.0.0-ORM-submission`. One-time action.
2. **Cohen's κ values** — filled automatically when the spawned second-coder task completes (drop-dead 2026-06-15).
3. **Zenodo DOI** — minted automatically on ORM acceptance; no pre-submission action needed.

All other submission-prep items are closed.
