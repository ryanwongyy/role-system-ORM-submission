"""Compute the Appendix D 17-role sensitivity table.
Excluded cases: 25, 26, 32, 33, 34 (autonomy-heavy boundary cases).
For each role, report (robust / conditional / transformed / shrinking / split_pressure)
counts on (all 36) and (excl 31) and Δ.
"""
import csv
from collections import defaultdict

EXCLUDE = {'25', '26', '32', '33', '34'}

with open('/Users/ryanwong/Human roles/p1_role_systems_db/06_analysis_tables/role_coding_master.csv') as f:
    rows = list(csv.DictReader(f))

# Role group ordering per the existing Appendix D placeholder
role_order = [
    ('Relevance adjudicator', 'starting_role'),
    ('Mechanism disciplinarian', 'starting_role'),
    ('Construct and perspective boundary setter', 'starting_role'),
    ('Corpus pluralist', 'starting_role'),
    ('Protocol and provenance architect', 'starting_role'),
    ('Counterfactual and transportability judge', 'starting_role'),
    ('Situated interlocutor / context witness', 'starting_role'),
    ('Accountability and labor allocator', 'starting_role'),
    ('Construct boundary setter', 'split_candidate'),
    ('Perspective sampler', 'split_candidate'),
    ('Counterfactual / transportability judge', 'split_candidate'),
    ('Calibration architect', 'split_candidate'),
    ('Situated interlocutor', 'split_candidate'),
    ('Context witness', 'split_candidate'),
    ('Routine first-pass screener', 'shrinking_task_cluster'),
    ('Routine coder on high-consensus, ground-truth-rich tasks', 'shrinking_task_cluster'),
    ('Structural prose polisher / drafter', 'shrinking_task_cluster'),
]

statuses = ['robust', 'conditional', 'transformed', 'shrinking', 'split_pressure']

def count_status(rows, role, status):
    return sum(1 for r in rows if r['role_label'] == role and r['status_in_case'] == status)

rows_excl = [r for r in rows if r['case_id'] not in EXCLUDE]

print("| Role | Group | R (all/excl/Δ) | C | T | S | SP |")
print("|---|---|---|---|---|---|---|")
for role, group in role_order:
    cells = []
    for status in statuses:
        a = count_status(rows, role, status)
        e = count_status(rows_excl, role, status)
        d = e - a
        cells.append(f"{a}/{e}/{d:+d}")
    print(f"| {role} | {group} | " + " | ".join(cells) + " |")

# Also report column totals
print()
print("**Column totals:**")
for status in statuses:
    a = sum(1 for r in rows if r['status_in_case'] == status)
    e = sum(1 for r in rows_excl if r['status_in_case'] == status)
    print(f"  {status}: {a}/{e}/{e-a:+d}")
