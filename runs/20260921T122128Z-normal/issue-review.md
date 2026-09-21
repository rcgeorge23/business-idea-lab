# Issue review — 2026-09-21 (ad hoc session, no LAB_RUN_ID)

Scope: the user asked to "review and work on open github issues". This was a
repository-maintenance session, not a discovery funnel run: no observation
sweep, no candidates and no Method lifecycle changes were made. No commits,
pushes, issues, pull requests, outreach or spend occurred; everything below is
left uncommitted for human review.

| Issue | Status after this session |
| --- | --- |
| #9 painmine spike | Delivered earlier (`03f2489`, `SPIKE-REPORT.md`); recommendation ITERATE; remains open pending #10/#11 validation |
| #10 persist signals/cluster identity across runs | **Implemented and tested** (uncommitted) — ready for review |
| #11 validate OpenCode Go synthesis and stage GHA rollout | **Not started**; #10 prerequisite now satisfied; schedules still active — human decision needed |
| #12 keep discovery ranking separate from Method 1.6 triage/promotion | **Implemented and tested** (uncommitted) — ready for review |
| #13 auditable request/source/budget accounting | **Not started**; discrepancy documented below |
| #14 harden painmine module and workflow boundaries | **Not started** (issue says lower priority) |

Issues #1–#8 were delivered in earlier commits and remain open only
administratively.

## #10 — persist pain signals and cluster identity across runs

New `painmine/fingerprint.py` (exact SHA-1 fingerprint plus 24-permutation
MinHash/LSH), rewritten `painmine/state.py` (state v0.2.0), and pipeline
integration in `painmine/cli.py`. `limits.json` gained a documented `state`
section and `painmine/README.md` a "Cross-run state (v0.2.0)" section.

Acceptance mapping:

1. **Different-URL duplicate linked to the earlier signal, not counted again** —
   `State.link_signals` sets `duplicate_of` to the prior signal; registration
   skips it. `test_state_v2.test_exact_repost_links_and_does_not_inflate`,
   `test_mirror_is_linked_as_near_duplicate`.
2. **Repeat collection does not increase recurrence** — same `signal_id`
   re-collected is a refresh, never a self-link (explicit guard in
   `link_signals`). `test_repeat_collection_refreshes_without_self_link_or_inflation`;
   pipeline run 3 in `test_cross_run_pipeline`.
3. **Independent new evidence increases an existing cluster's recurrence** —
   `test_independent_new_evidence_increases_cumulative_recurrence`;
   `test_cross_run_pipeline` (cumulative 6 > current 3, `runs_seen` 2).
4. **Cluster identity stable and explainable as membership changes** —
   `assign_cluster_lineage` scores role family, role, key terms, named systems
   and label, and records `action` (`created`/`matched`/`merged`/`split`),
   `match_score`, `matched_via`, `first_seen_run`.
   `test_stable_cluster_identity_across_membership_change`,
   `test_competing_clusters_split_with_explanation`.
5. **Source, author and organisation independence separated** — independence
   keys per dimension; primary recurrence uses `(source_type, author)` when an
   author exists. `test_independence_dimensions_are_tracked_separately`.
6. **Retention/expiry/max-state documented and enforced** — signal TTL 180 days,
   cluster TTL 365 days, caps 2,000/200/60/60; `prune()` runs on load and save;
   documented in `limits.json` and the README. `test_expiry_prunes_old_records`,
   `test_independent_and_member_caps_never_overcount`.
7. **State survives cache/artifact lifecycle** — versioned state file, relative
   paths, atomic save (`path.tmp` + `os.replace`).
   `test_save_is_atomic_and_versioned`. *Caveat: the actual GHA cache
   round-trip has not been executed; that belongs to #11.*
8. **Corrupt/unavailable state fails safely** — unreadable, non-object or
   unknown-version state is quarantined to `<path>.corrupt-<stamp>` and history
   is reported unavailable; recurrence is never inferred.
   `test_corrupt_state_quarantines_and_degrades`,
   `test_unknown_state_version_is_not_guessed`.
9. **Reports distinguish current-run from cumulative** — `report.json` history
   block, `cross_run` volumes and a "Cross-run evidence state" section in
   `report.md`; `cross-run-links.json` per run; `test_cross_run_pipeline`.
10. **Deterministic tests** — exact duplicates, paraphrased reposts, mirrors,
    independent recurrence, expiry and input-order independence are covered in
    `test_fingerprint.py`, `test_state_v2.py` and `test_cross_run_pipeline.py`.
11. **Multi-run fixture accumulates one coherent cluster** — two offline
    fixtures plus a repeat run prove a stable cluster id (`c-f09ee670`),
    cumulative recurrence growth and no repeat inflation. *Caveat: the fixtures
    simulate rotated query families via different sources/dates; an actual
    query-family rotation run was not executed.*
12. **No Method 1.6 semantics change** — `method/` untouched; the pipeline never
    writes `ideas/index.json` (`test_cli.test_pipeline_does_not_touch_idea_ledger`).

Known limitations: MinHash near matching is deliberately conservative (5-gram
shingles, threshold 0.62), so only substantial verbatim overlap links as a
near duplicate; paraphrases that share meaning but not wording rely on
clustering, not linking. Clustering quality (the open problem in
`SPIKE-REPORT.md`) is unchanged.

## #12 — discovery ranking separate from Method 1.6 triage/promotion

`painmine/to_observation.py` now exports ranked observation **inputs** only:
no promote/watch/reject labels, no candidate selection, no consumption of the
three-candidate limit. `--max-promote` was replaced by `--max-observations`
(default 20) in both the pipeline and `observations` subcommands.

Acceptance mapping:

- **Inputs only, no triage labels** — `test_to_observation.test_observation_carries_no_method_triage_labels`,
  `test_render_pool_input_contract`; observations carry cluster/evidence
  identity, buyer/job/pain/workaround, source class, recurrence, discovery
  priority, persistence hypotheses, incumbent check and extraction caveats.
- **No candidate selection / no three-candidate limit** —
  `to_observations(clusters, max_observations=20)` slices by priority and never
  demotes; `test_observation_cap_and_no_filler`.
- **Later Method run does its own sweep, triage and false-negative audit** —
  the rendered pool states this explicitly and no longer fills a "promoted"
  section.
- **Band changes cannot change Method lifecycle or candidate state** —
  `test_priority_band_is_an_input_not_a_state`; the pipeline byte-compares
  `ideas/index.json` before/after (`test_pipeline_does_not_touch_idea_ledger`).
- **Zero-cluster and fewer-than-15-cluster cases handled without filler** —
  `test_empty_pool_renders_without_filler`, `test_small_pool_is_not_padded`.
- **Method 1.6 weights, threshold 65, hard filters, evidence levels and
  lifecycle unchanged** — `method/` untouched.
- The committed PoC observation pool (`painmine/poc/20260921-live-all/`) was
  regenerated under the new contract (6 inputs, no Triage column).

## #11 — OpenCode Go synthesis and GHA rollout (recommended next, needs human decisions)

Not started. The outstanding gaps remain as written in the issue: the workflows
do not install the `opencode` executable expected by `llm.py`; no GHA run has
validated either workflow; both schedules are still active (daily collect,
weekly cluster) even though the spike recommendation was ITERATE. The state
prerequisite (#10) is now implemented, but the corrected state model has not
yet been exercised in Actions.

Suggested sequence for a human-approved follow-up: disable or keep schedules
off until a controlled manual run passes; add a pinned, documented OpenCode
install (or the smallest bounded worker architecture using DeepSeek via OpenCode
Go); prove a deterministic no-credential run on a clean runner; then a bounded
synthesis dispatch using repo secrets with provider/model/tokens/cost/failure
visible in the summary; two independent synthesis passes on the same top
cluster with agreement/disagreement recorded; cache restore/save and artifact
retention verified across at least two manual runs; no fallback provider;
missing binary/credentials/outage/timeout fail safely and visibly; hard
call/token/USD/runtime limits verified in Actions including stop-before-overrun;
documented human approval before each schedule. Scheduled runs must emit
experimental discovery artefacts only and never promote Method candidates.

## #13 — request/source/budget accounting (recommended after #11)

Not started. The discrepancy described in the issue is confirmed by inspection:
`budget.requests` counts actual HTTP calls (24 in the live PoC), while
`summarise_statuses` labels each query attempt as a "request", so the source
table shows 15 attempts per source (60 rows) including budget-prevented and
item-cap rows, and reports them as failed requests. No retries are implemented,
so retry counters are not yet meaningful. The fix requires distinct run-level
counters (source attempted, query attempted, HTTP request initiated, HTTP
response received, retry, item returned, item accepted, per-source item cap
reached, request prevented by budget exhaustion, source access failure), one
reconciling ledger, consistent definitions across `report.json`, `run-meta.json`,
Markdown and Actions summaries, and the test matrix listed in the issue
(success, pagination, retry, timeout, HTTP failure, item cap, mid-run budget
exhaustion, cap never exceeded, runtime/model-cost reconciliation).

## #14 — module and workflow boundaries

Not started (issue explicitly lower priority). The four items stand:
duplicated workflow logic between `painmine-collect.yml` and
`painmine-cluster.yml`; `cli.py` mixing parsing, orchestration, persistence,
report construction and Markdown rendering; untyped dict records between
cluster/persistence/ranking/observation-export/report boundaries; and the
desire for explicit typed records or schema validation with actionable errors
and preserved behavioural tests. The #10/#12 work touched `cli.py` and
`state.py` but did not restructure module boundaries.

## Evidence and verification for this session

- `python3 -m unittest discover -s painmine/tests -t .` → **121 tests, OK**
  (95 before issue #10; 119 after #10; 121 after #12).
- `python3 scripts/validate_repo.py --json` → **status pass**, only pre-existing
  warnings (killed-idea audit due; historical run method versions).
- Scratch multi-run verification (gitignored `painmine/state/scratch-*`):
  run 1 produced accounting cluster `c-f09ee670`; run 2 linked one exact
  restatement, matched the same stable id (action `matched`, score 0.64,
  matched via role family/role/key terms/systems/label) and raised cumulative
  independent sources from 3 to 6; run 3 re-collected run 1 and left cumulative
  recurrence unchanged with `runs_seen` 3.
- No web lookups were made; no external sources were contacted.
