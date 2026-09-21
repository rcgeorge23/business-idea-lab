# Run summary — 20260921T122128Z-normal (ad hoc session)

`LAB_RUN_ID` was not set for this session (it was not launched through
`scripts/run.sh`), so the run id `20260921T122128Z-normal` was chosen to match
the `runs/` naming convention. Consequently there is no `run.json`,
`usage.json`, `validation.json` or `runs/index.jsonl` entry from the wrapper;
this summary and `issue-review.md` are the run record. The repository
validator was run manually and passes.

## What this run was

A repository-maintenance session responding to the open GitHub issues
#9–#14, not an opportunity-observation funnel run. No observation sweep, no
candidate promotion, no Method lifecycle changes. The user's request was to
review and work on open GitHub issues; a follow-up request to commit and push
was declined per the worker boundaries, and the session then verified that the
painmine package can be run locally on this laptop.

## What changed (all uncommitted, for human review)

Implemented **issue #10** (cross-run persistence of pain signals and cluster
identity):

- New `painmine/fingerprint.py`: exact SHA-1 fingerprint plus 24-permutation
  MinHash/LSH candidate lookup.
- `painmine/state.py` rewritten as state v0.2.0: bounded signal records, stable
  cluster lineage (`created`/`matched`/`merged`/`split` with score and matched
  dimensions), current vs cumulative recurrence, per-dimension independence
  (source/author/organisation), TTLs (180/365 days) and caps (2,000/200/60/60),
  corruption quarantine with degraded health, legacy v0.1 migration, atomic
  saves.
- `painmine/cli.py`: cross-run linking before clustering, lineage assignment,
  `cross-run-links.json`, `cross_run` and `state_health` in `run-meta.json`,
  current-vs-cumulative reporting.
- `painmine/limits.json`: documented `state` section; `painmine/README.md`:
  "Cross-run state (v0.2.0)" section and local-run notes.
- Tests: `test_fingerprint.py`, `test_state_v2.py` (15 tests),
  `test_cross_run_pipeline.py` and fixture `raw_items_run2.jsonl`.

Implemented **issue #12** (discovery ranking separate from Method 1.6
triage/promotion):

- `painmine/to_observation.py` exports ranked observation inputs only: no
  promote/watch/reject labels, no candidate selection, no consumption of the
  three-candidate limit; `--max-promote` replaced by `--max-observations`.
- Tests: `test_to_observation.py` rewritten; `test_cli.py` proves the pipeline
  never writes `ideas/index.json`; zero/fewer-than-15-cluster pools render
  without filler.
- Committed PoC observation pool regenerated under the new contract.

Full acceptance mapping and evidence: `runs/20260921T122128Z-normal/issue-review.md`.

## Local runnability (verified on this laptop)

- `python3 -m painmine.cli pipeline --family all --max-requests 24 --state
  painmine/state/state.json --out painmine/state/local-run-1 --run-id
  pm-local-1` → 24/24 requests, 50 raw items, 37 signals, 2 clusters (band A:
  2), 24.8 s, no errors; legacy v0.1 state migrated in place to v0.2.0.
- `validate` → 37 signals, 0 problems; `observations` → 2 inputs rendered;
  `report` → regenerated.
- Requests are spent in source order (HN, Stack Exchange, GitHub, Reddit), so
  later sources are skipped when the 24-request cap is reached; GitHub and
  Reddit received no requests in this run. This is the reporting/counter
  discrepancy tracked by issue #13.
- Offline fixture runs and the test suite need no network. Model synthesis
  (`--enable-llm`) remains disabled by default and was not exercised (spend
  requires owner approval); the `opencode` binary is present on this laptop.

## Verification

- `python3 -m unittest discover -s painmine/tests -t .` → 121 tests, OK
  (95 before issue #10, 119 after #10, 121 after #12).
- `python3 scripts/validate_repo.py --json` → status pass; only pre-existing
  warnings (killed-idea false-negative audit due; historical run method
  versions).
- Scratch multi-run proof (gitignored): stable cluster id across runs, one
  exact restatement linked, cumulative independent sources 3 → 6, repeat run
  leaves recurrence unchanged with `runs_seen` 3.

## Discovery-funnel statistics

Not applicable: this session did not run the opportunity-observation funnel.
Total observations: 0; source classes searched: none (no web lookups were made
for the lab ledger); candidates promoted: 0; seeds added: 0. No filler
candidates were manufactured (zero promotions is a valid run outcome).

## Issue status after this run

- **#10** implemented and tested; ready for review.
- **#12** implemented and tested; ready for review.
- **#9** spike remains open pending #10/#11 validation.
- **#11** not started: workflows still do not install the `opencode` binary, no
  GHA run has validated either workflow, and the daily/weekly schedules remain
  active despite the ITERATE recommendation. Needs a human decision (recommend
  holding schedules until a controlled manual run passes).
- **#13** not started: the request/source/budget accounting discrepancy is
  confirmed and documented (24 actual HTTP requests vs 60 query-attempt rows).
- **#14** not started (issue explicitly lower priority).

## Decisions awaiting human input

1. Review and, if acceptable, commit the uncommitted changes listed below
   (committing/pushing is outside the worker's boundaries).
2. Decide whether to disable or hold the painmine GHA schedules (#11).
3. Approve any model-synthesis spend before `--enable-llm` is used locally or
   in Actions (default caps: 6 calls, 40k tokens, USD 0.25 per run).
4. Prioritise #11, #13 and #14 follow-ups.

## Uncommitted files

Modified: `painmine/README.md`, `painmine/SPIKE-REPORT.md`, `painmine/cli.py`,
`painmine/limits.json`, `painmine/state.py`, `painmine/to_observation.py`,
`painmine/tests/test_cli.py`, `painmine/tests/test_to_observation.py`,
`painmine/poc/20260921-live-all/observations.md`,
`painmine/poc/20260921-live-all/observations.json`.
New: `painmine/fingerprint.py`, `painmine/tests/test_fingerprint.py`,
`painmine/tests/test_state_v2.py`, `painmine/tests/test_cross_run_pipeline.py`,
`painmine/tests/fixtures/raw_items_run2.jsonl`,
`runs/20260921T122128Z-normal/issue-review.md`,
`runs/20260921T122128Z-normal/summary.md`.
Gitignored scratch/local outputs: `painmine/state/scratch-*`,
`painmine/state/local-run-1/`, `painmine/state/state.json` (migrated in place).

## Boundaries confirmed

No commits, pushes, issues, pull requests, publication, outreach, accounts or
spend. `method/` and `ideas/index.json` were not modified. Experiments were not
run; none were proposed this session.
