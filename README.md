# business-idea-lab

A durable, evidence-driven loop for discovering and validating business ideas,
run ad hoc with [OpenCode](https://opencode.ai) + DeepSeek. It exists to find
ideas worth testing and to kill weak ones cheaply — not to generate volume. A
run that advances nothing is a valid run.

- Method (authoritative): `method/` — lifecycle, evidence policy, scorecard,
  experiment rules, review policy, run protocol, calibration.
- Worker instructions: `AGENTS.md`.
- Ledger: `ideas/index.json` and `ideas/<slug>/`.
- Everything else: `evidence/`, `experiments/`, `reviews/`, `retrospectives/`,
  `runs/`, `templates/`, `scripts/`.

## Setup

1. Install OpenCode (`>= 1.18.30` recommended) and start it once in this
   repository. Run `/connect`, choose the opencode-go provider, and complete
   authentication. The pinned model is
   `opencode-go/deepseek-v4.1-flash` (`opencode.jsonc`).
2. If you prefer the native DeepSeek provider instead of the gateway, export
   `DEEPSEEK_API_KEY` in your shell (see `.env.example`). Never commit it —
   `.env*` is gitignored.
3. Verify plumbing without touching the ledger:

   ```bash
   scripts/run.sh --smoke
   ```

4. Run offline validation at any time:

   ```bash
   python3 scripts/validate_repo.py          # human-readable
   python3 scripts/validate_repo.py --json   # machine-readable
   python3 scripts/validate_repo.py --queue  # review queue + counters
   ```

## Running the loop

One deterministic, non-interactive command runs the complete protocol:

```bash
scripts/run.sh                 # normal run against the live ledger
scripts/run.sh --dry-run       # worker runs in a throwaway copy; live ledger untouched
```

Useful flags: `--timeout SECONDS` (default 3600), `--max-cost USD` (default
1.00), `--max-attempts N` (default 3), `--model provider/model`, `--agent NAME`,
`--allow-dirty` (only when you deliberately accept an unclean tree).

What a run does (see `method/run-protocol.md` for the full protocol and
limits):

1. Handles any outstanding `changes-requested` review first.
2. Stops generating if 10 or more ideas are unreviewed.
3. Generates at most 3 materially distinct candidates and applies the 9 hard
   rejection filters before deep research.
4. Researches survivors, runs an explicit adversarial review aimed at killing
   them, and updates the ledger, evidence registers, scorecards and decision
   records.
5. Advances at most 1 idea to `validation-ready` per run, only if the scorecard
   threshold and review policy are satisfied.
6. Proposes the cheapest experiment that could disprove the central assumption.
7. Writes the run summary to `runs/$LAB_RUN_ID/summary.md`.

Cost and retry bounds are documented in `method/run-protocol.md` and enforced
where practical by `scripts/run.sh` (wall-clock timeout, post-run cost check,
retry only when the tree is unchanged). Every run records timestamp, mode,
agent, model, method version, input/output revision, attempts and cost in
`runs/<id>/run.json` plus one line in `runs/index.jsonl`.

The worker never commits, pushes, opens issues or PRs, contacts anyone, spends
money, publishes, creates accounts, or makes commitments. It may only propose
experiments. Review the diff when the run finishes and commit it yourself.

## Reviewing a candidate

Independent review is repository-mediated: the reviewer works only from the
files in this repository.

1. Build a request package:

   ```bash
   python3 scripts/build_review_request.py --slug <slug> \
       --trigger "proposed for validation-ready" \
       --transition "adversarially-researched -> validation-ready"
   ```

   This writes `reviews/<date>-<slug>-review-request.md` containing the state,
   scores, hard filters, strongest supporting and disconfirming cases,
   unresolved assumptions, the decisive experiment and a machine-readable review
   block.

2. Give that file (and the artefact list inside it) to the reviewer. The
   reviewer writes `reviews/<date>-<slug>-<reviewer>-<model>.md` following
   `templates/review/response.md`, with a verdict of `changes-requested`,
   `approved` or `killed`.

3. Record the outcome in `ideas/<slug>/scorecard.json` under `review` and
   `review.history`. History is append-only and transitions are validated
   (`not-required -> requested -> changes-requested | approved | killed`).

4. The next worker run must answer a `changes-requested` review explicitly and
   visibly; it may not silently overwrite any outcome.

Review triggers and the false-negative audit rule (every fifth killed idea) are
in `method/review-policy.md`. A second model is not market validation.

## Recording external experiment results

The human owner runs experiments; results go into the repository:

1. Approve the experiment in `experiments/index.json`
   (`approval.granted: true`, `granted_by`, `granted_date`) — anything above 20
   human-hours or £100 needs a review request first.
2. Run it. Record raw outcomes in
   `experiments/<experiment-id>/results.md` following
   `templates/experiment/results.md` (what happened, verbatim quotes, numbers,
   deviations from the plan).
3. Apply the decision rule that was fixed in the plan **mechanically**. If the
   outcome is ambiguous, record it as ambiguous — do not move the threshold.
4. Update the ledger: if real-world demand or commercial evidence exists, the
   idea may move to `externally-tested`, `validated`, `iterate` or `killed`
   (human owner decision), and the scorecard, dossier and decision record are
   updated with the new evidence.

## Layout

| Path | Purpose |
|---|---|
| `AGENTS.md` | Worker role, boundaries, protocol in one screen |
| `method/` | Authoritative method documents + `VERSION` |
| `ideas/index.json` | Ledger: every idea, state, score, review and experiment link |
| `ideas/<slug>/` | Dossier, scorecard, decision record |
| `evidence/<slug>/` | Dated evidence registers (claims, sources, caveats) |
| `experiments/` | Experiment index, plans, results |
| `reviews/` | Review requests and responses |
| `retrospectives/` | What the loop itself should learn |
| `runs/` | Per-run metadata, usage, validation, summaries, dry-run diffs |
| `templates/` | Templates for every artefact type |
| `scripts/` | Validator, runner, usage extraction, review-request builder |
| `.opencode/agent/` | `idea-worker` (primary) and `idea-critic` (read-only subagent) |

## Calibration

Calibration compares the loop against known fixtures before its output is
trusted: GeoNerd (seeded), two weak/rejected ideas and one attractive-looking
control produced by the first worker run, plus an independent critique of at
least one DeepSeek result. Status and exit criteria: `method/calibration.md`.
The fixture-generation steps are **done**: the first normal run
(`runs/20260920T210550Z-normal`) produced two weak ideas killed through the
documented hard-filter path (`shiftswap`, `wonkybox`) and one attractive
control killed by adversarial veto (`grantscout`). The independent ChatGPT
critique is **still pending**, so the loop's output must not yet be treated as
trusted. Status and exit criteria: `method/calibration.md`.

## Status

- GeoNerd is seeded at `validation-ready` with an independent review requested
  and a proposed demand-validation experiment awaiting human approval. It has
  **no demand evidence**; the weighted total (65.3) barely clears the threshold
  (65) and must not be read as a strong signal.
- `scripts/run.sh` has completed a smoke run, a dry run and one normal run
  end-to-end (cost well under the USD 1.00 bound; validator passing).
- Scheduling of recurring runs is deliberately out of scope. Every run is
  manual.
