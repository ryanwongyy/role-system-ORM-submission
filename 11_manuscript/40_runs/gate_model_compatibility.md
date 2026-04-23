# Gate Model Compatibility Note

## Current Runner State

- Active gate model version: `autonomy_split_v1`
- Effective date for this runner patch: `2026-04-09`
- Historical run rows created before this patch may still use the legacy composite-gate model.

## Legacy-To-Current Mapping

- `journal_choice_gate` -> `provisional_journal_target` + `framing_lock`
- `claim_ceiling_gate` -> `safe_claim_floor` + `claim_escalation`
- `theory_novelty_gate` -> `novelty_risk_downgrade` + `novelty_endorsement`
- `citation_inclusion_gate` -> `reference_hygiene` + `final_reference_scope`
- `disclosure_gate` -> `disclosure_packet_completeness` + `disclosure_signoff`
- `submission_gate` -> `submission_packet_ready` + `final_submit_authority`
- `role_ontology_freeze_gate` and `boundary_autonomy_gate` remain adapter-local gates used by the role-system runner.

## Interpretation Rule

Read older run logs, gate registries, delivery-artifact rows, and pre-redesign assessment memos through the mapping above. They remain historically accurate snapshots and should not be interpreted as the current live control-panel gate inventory.
