# Human-Gate Proposed Decisions

Draft recommendations for the six `human_resolved_only` gates in the
`autonomy_split_v1` model. Each section gives current state, the
AI-recommended decision, its rationale, and alternatives a human reviewer
might pick. Nothing here has been applied — the form at
[human_gate_input_form.csv](human_gate_input_form.csv) is for your signatures.

---

## 1. `framing_lock` — Journal / framing lock

- **Current state:** `waived`. Drafting target `orm` is provisional.
- **AI recommendation:** Lock **Organizational Research Methods (ORM)** as the
  submission-facing target.
- **Why:** ORM is a methods journal. The manuscript is explicitly positioned
  in [theory_novelty_memo.md](theory_novelty_memo.md) as a bounded methods/framework
  contribution — a comparative empirical typology audit — which fits ORM's
  scope better than a general theory outlet.
- **Alternatives:** (a) lock a different journal if you prefer a sociology-of-
  science or HCI outlet; (b) keep `waived` if you want to keep journal choice
  open longer.

## 2. `claim_escalation` — Ceiling above `framework`

- **Current state:** `waived`. Safe floor `framework` is in effect.
- **AI recommendation:** **Confirm waive.** Do not escalate.
- **Why:** The evidence is a source-backed comparative typology across 36
  cases with clear rival explanations and explicit limits. Escalating beyond
  `framework` (e.g., to a general-theory claim) would overreach what the
  evidence licenses, per the "what the evidence still does not license"
  section of the theory memo.
- **Alternatives:** Escalate only if you want to claim e.g. "a general theory
  of AI-enabled research reorganization" — not recommended without additional
  corpora beyond this repository.

## 3. `novelty_endorsement` — Strong novelty framing

- **Current state:** `waived`. Novelty is downgraded to bounded methods
  language.
- **AI recommendation:** **Confirm waive.** Do not endorse strong novelty.
- **Why:** Bounded novelty framing — "changes the unit of analysis from
  AI-vs-human to a role-system dataset" — is defensible and already explicit
  in the theory memo. Strong novelty endorsement creates reviewer pushback
  risk without added benefit given the framework-level claim.
- **Alternatives:** Endorse novelty if you plan to position the paper against
  a specific prior claim (e.g., Shneiderman's HCAI or Abbott's jurisdictional
  theory) as superseding rather than extending.

## 4. `final_reference_scope` — Bibliography lock

- **Current state:** `waived`. Working set is hygiene-reviewed but not
  finalized.
- **AI recommendation:** **Defer.** Retain `waived` until submission prep.
- **Why:** Locking the bibliography now forecloses late additions (e.g., if
  new Case 23/35 sources become accessible, or if reviewer norms shift). The
  reference hygiene packet in [reference_inclusion_decisions.md](../20_citations/reference_inclusion_decisions.md)
  is conservative and ready.
- **Alternatives:** Lock now only if you want an immutable submission packet
  before sharing the manuscript externally.

## 5. `disclosure_signoff` — AI-use disclosure wording

- **Current state:** `waived`. Proposed disclosure text exists and is
  auto-constrained to the most conservative ORM-compliant wording.
- **AI recommendation:** **Sign off** on the current wording in
  [disclosure_statement.md](disclosure_statement.md) as-is.
- **Why:** The current wording is:
  > "Generative AI tools were used in a local workflow to support lawful source
  > organization, structured extraction, database upkeep, and draft-language
  > generation. All evidence verification, coding judgments, interpretive claims,
  > and final manuscript text remain subject to human review and approval. No AI
  > system is listed as an author."
  This matches ORM's emerging expectations and is defensible at review.
- **Alternatives:** Narrow or broaden the scope if your institution has a
  stricter template, or if ORM publishes a specific form.

## 6. `final_submit_authority` — Actual submission

- **Current state:** `waived`. Packet is prepared but no authority recorded.
- **AI recommendation:** **Defer.** Do not authorize submission yet.
- **Why:** Submission should only follow after `framing_lock`,
  `disclosure_signoff`, and `final_reference_scope` are resolved. The three
  `auto_constrain_then_escalate` submission-readiness gates
  (`submission_packet_ready`, `disclosure_packet_completeness`,
  `reference_hygiene`) are already green, but the human chain is not closed.
- **Alternatives:** None — this should always be the last gate.

---

## Order of resolution (if you do intend to submit)

1. `framing_lock` (confirms journal) → triggers any journal-specific
   formatting requirements.
2. `claim_escalation` and `novelty_endorsement` (pair; both currently
   waived-is-fine) → ensures rhetorical scope is settled before citations lock.
3. `final_reference_scope` (locks bibliography) → triggers final formatting.
4. `disclosure_signoff` (signs off AI-use statement).
5. `final_submit_authority` (authorizes external submission).

## Applying your decisions

The existing `09_scripts/ingest_human_gate_inputs.py` only recognises the
older 8-gate model and will not work with this 14-gate form unchanged.
Either:

- Fill in the form and manually update [gate_state_registry.csv](gate_state_registry.csv) +
  [gate_decisions.md](gate_decisions.md) to reflect your choices, or
- Extend `ingest_human_gate_inputs.py`'s `GATE_ROLE_MAP` to include the six
  gate IDs above and re-run it.

Flagging the script gap as a separate follow-up.
