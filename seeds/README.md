# Seeds

Adjacent opportunity seeds are lightweight observations preserved when an idea is
rejected or killed. They exist so a useful insight is not lost and does not have to be
re-derived, without resurrecting the killed idea.

## Rules

- A seed is **not a candidate**. It has no score, no confidence, no evidence level and
  no lifecycle state, and it must never inherit any of those from its parent idea.
- A seed records: the observation, its origin idea, why it is materially different from
  that parent, the evidence it rests on, and what a later run should check first.
- To become a candidate, a later run must research it from scratch under
  `method/discovery.md` and create its own dossier, evidence and scorecard. The seed's
  origin idea stays killed.
- Seeds are append-only. Update `status` (`unexplored` -> `exploring` -> `promoted` |
  `dropped`) and append to the outcome table; never rewrite the observation.

## Files

- `seeds/index.json` — machine-readable register (required by `scripts/validate_repo.py`).
- `seeds/<slug>.md` — one file per seed, from `templates/seed/entry.md`.

Recording a seed is part of run protocol step 11 (`method/run-protocol.md`): when a
rejection surfaces an adjacent opportunity, record it here rather than leaving it in a
decision record or, worse, in chat.
