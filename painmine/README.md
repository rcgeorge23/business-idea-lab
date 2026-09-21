# painmine

A bounded, cheap **pain-signal mining** spike for this lab (GitHub issue #9).
It collects public practitioner statements of recurring business pain,
extracts them into an auditable schema, collapses duplicates, clusters them
into candidate opportunity patterns, ranks them by *discovery priority* (not
business score) and renders the strongest into the Method 1.6 observation-pool
format.

> **Status: spike / ITERATE.** See [`SPIKE-REPORT.md`](SPIKE-REPORT.md) for
> the Part 10 evaluation, measured results and the recommendation. This
> package does not score ideas, does not run triage for the lab and does not
> change `method/` in any way.

## Design (issue #9 parts)

```
query families ──► bounded fetchers ──► schema extraction ──► dedupe
                                                             │
      observations ◄── ranking ◄── persistence thesis ◄── clusters
      (Method 1.6 format)          (both limbs)        (TF-IDF + roles)
```

- **Part 1 schema** — `pain-signal.schema.json` + `schema.py`. One record per
  independently sourced pain signal, with source URL/type/date, role,
  organisation hint, task, pain statement, workaround, named systems,
  frequency/time/money clues, dissatisfaction and integration clues,
  confidence and full extraction provenance. Only a bounded `raw_excerpt`
  (<= 600 chars) is retained for audit; the authoritative copy stays at the
  source URL.
- **Part 2 source portfolio** — `sources.json`. Every class from the issue is
  listed with access mechanism, terms/robots constraints, expected quality,
  expected volume, rate limits, collection cost and whether unattended
  collection is practical. Classes that need an account, a ToS review or a
  bypass are disabled with a written reason. Nothing is enabled that requires
  circumventing access controls.
- **Part 3 retrieval/extraction/dedupe/clustering** — `fetch.py`, `extract.py`,
  `dedupe.py`, `cluster.py`. Retrieval is query-family driven and bounded;
  extraction is deterministic cue matching (no model needed); dedupe collapses
  exact reposts and near-duplicates and counts only genuinely independent
  authors; clustering is TF-IDF + cosine agglomeration with a role-compatibility
  guard so different buyer roles do not merge on shared vocabulary alone.
- **Part 4 discovery-priority ranking** — `rank.py`. A 0-100 score built from
  independent recurrence, identifiable economic buyer, explicit cost evidence,
  manual workaround/re-keying, dissatisfaction/switching, incumbent integration
  seam, recency and segment reachability, minus penalties for duplicates,
  consumer-only noise, stale evidence and transient incidents. Explicitly
  separate from Method 1.6 business scoring and never a substitute for
  validation.
- **Part 5 contradiction/persistence mining** — `persistence.py`. For each
  cluster it computes the two-limb persistence thesis (continued pain/workaround
  despite existing alternatives; supported persistence mechanism such as
  price/minimum-contract, partial-or-manual integration, implementation
  complexity, excluded segment, legacy architecture, low vendor priority) and
  records archetype (change-driven vs persistent). The output is hypotheses for
  the lab, never an asserted wedge.
- **Part 6 independent synthesis** — `synthesis.py`. Optional: two DeepSeek
  interpretations of the same cluster, produced from differently ordered
  evidence so they cannot anchor on each other; agreement and disagreement are
  preserved verbatim. Spend-gated and off by default.
- **Part 7 scheduled collector** — `.github/workflows/painmine-collect.yml`
  (daily, non-round-minute, plus `workflow_dispatch`) and
  `painmine-cluster.yml` (weekly plus dispatch).
- **Part 8 cost controls** — `limits.json` + `budget.py`. Hard caps for HTTP
  requests, items per source and total, minimum gap between requests, request
  timeout, model calls, input/output/total tokens, USD, wall-clock runtime and
  retained data. The pipeline stops with partial results when a cap is hit.
- **Parts 9/10 PoC and evaluation** — `poc/` artefacts and
  [`SPIKE-REPORT.md`](SPIKE-REPORT.md).

## Limits (defaults)

See `limits.json`; the CLI can only clamp `--max-requests` downwards.

| Limit | Default |
| --- | --- |
| HTTP requests / run | 24 |
| Items / source / run | 50 |
| Items total / run | 240 |
| Min gap between requests | 1.0 s |
| Request timeout | 20 s |
| Model calls / run | 6 (spend disabled unless `--enable-llm`) |
| Model tokens / run | 40,000 |
| Model USD / run | 0.25 |
| Wall clock / run | 420 s |
| Retained raw item rows / run | 240 (600-char excerpts) |
| GHA artifact retention | 14 days |

## Inference policy

Scheduled or manual model use must go to **DeepSeek via OpenCode Go**, the same
provider family as the lab worker (`opencode-go/deepseek-v4.1-flash`, agent
`painmine-extractor`). There is deliberately **no fallback provider**: if
OpenCode Go is unavailable, the deterministic pipeline still runs and the run
summary records that model assistance was skipped. Provider, model, calls,
tokens and USD are recorded in `run-meta.json`/`report.json`.

## GitHub Actions setup

Both workflows use the repository's default branch, a shared concurrency group
(so daily and weekly runs serialise), `contents: read` and **no commit/push
step**. Outputs are uploaded as short-retention artefacts; cross-run state is
round-tripped through `actions/cache`.

Authentication (choose one; provider credentials are never stored in Git):

1. `OPENCODE_API_KEY` repository secret — the gateway key the OpenCode Go
   provider accepts via the standard environment variable.
2. `OPENCODE_AUTH_JSON` repository secret — the owner copies the OpenCode Go
   entry from their local `~/.local/share/opencode/auth.json` (or the whole
   file). The workflow writes it to `~/.local/share/opencode/auth.json` with
   mode 0600 before running.

If neither secret is present, the workflow logs that model assistance is
disabled and runs deterministic-only. It never substitutes another inference
provider.

Trigger manually: **Actions -> painmine-collect -> Run workflow**, choosing a
query family (`a_manual_rekey`, `b_tooling_gap`, `c_cost_pain`, `all`) and a
request cap, and optionally synthesis. The scheduled collector rotates the
family by day-of-year; the weekly job uses `all`.

## Local usage

```bash
# bounded live run against public sources
python3 -m painmine.cli pipeline --family all --max-requests 24 \
  --state painmine/state/state.json --out painmine/poc/<run-dir> --run-id <run-id>

# offline run against the test fixture (no network)
python3 -m painmine.cli pipeline --offline-fixture painmine/tests/fixtures/raw_items.jsonl \
  --out /tmp/painmine-offline

# optional: allow model use (owner approval required for spend)
python3 -m painmine.cli pipeline --family all --enable-llm --synthesis \
  --synthesis-top 2 --out painmine/poc/<run-dir>

# validate a completed run, re-render observations, rebuild the report
python3 -m painmine.cli validate --run-dir painmine/poc/<run-dir>
python3 -m painmine.cli observations --run-dir painmine/poc/<run-dir> --max-promote 3
python3 -m painmine.cli report --run-dir painmine/poc/<run-dir>

# tests (no network)
python3 -m unittest discover -s painmine/tests -t .
```

## Data retention

- Raw collected items (`poc/**/raw-items.jsonl`) and cross-run state
  (`state/`) are **not** committed (see `.gitignore`).
- Structured artefacts are kept in `poc/<run>/`: `signals.jsonl`,
  `dedupe-stats.json`, `clusters.json`, `observations.md/json`, `report.json/md`,
  `run-meta.json` — all small and auditable.
- Excerpts are capped and linked back to their public source; no bulk
  copyrighted text is retained.

## Hard boundaries

- No authentication bypass, anti-bot circumvention, paywall access or private
  community scraping; access failures are recorded (e.g. Reddit 403) and not
  worked around.
- No outreach, no external spend without owner approval, no publication.
- Method 1.6 scoring, thresholds, evidence levels, lifecycle gates, funnel
  sizes and audit rules are untouched by this package.
