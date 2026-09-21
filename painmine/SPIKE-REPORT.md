# Painmine spike report (issue #9)

- Date: 2026-09-21
- Spike version: painmine 0.1.0
- Author: idea-worker (OpenCode + DeepSeek), bounded by the lab worker constraints
- Consumes: GitHub issue #9, `painmine/` (this repo)
- Method version deliberately untouched: 1.6.0

This report answers Part 10 of issue #9 and records the final recommendation.
It reports one bounded live PoC run plus an offline fixture run, and it states
clearly what was not done. No Method 1.6 semantics (weights, threshold 65,
`defensible_wedge`, evidence levels, lifecycle gates, the 15-20 observation
funnel, the 3-candidate limit or the sampled triage audit) were changed.

## 1. Recommendation

**ITERATE.**

The mechanics work end to end inside hard, configurable budgets: 150 raw
public items were collected from three unauthenticated source classes in
43.84 seconds with zero model spend, extracted into a documented schema,
deduplicated, clustered, ranked and rendered into a Method 1.6-shaped
observation pool, with a full audit trail and honest failure reporting.

What the spike did **not** demonstrate is that the pipeline finds *buyer + job +
pain* recurrence rather than *shared vocabulary* recurrence. The single band-A
cluster (`c-5d98df96`) was inflated by a keyword collision: 4 of its 6 members
are commentary that happens to contain "double entry", not practitioner pain.
The highest-recurrence cluster (`c-4ff80e18`, 10 independent authors) is a bag
of unrelated Stack Overflow questions that share the words "manually export …
csv/import". Until the recurrence gate is tightened, cluster scores are not
trustworthy enough to promote many observations into the Method 1.6 funnel.

The next iteration should be small and targeted:

1. Add a job-level, not vocabulary-level, recurrence gate. Cluster membership
   must agree on buyer role (or an explicit unknown-with-reason), task and
   workaround seam, not only TF-IDF similarity. Cap the recurrence credit per
   thread/source situation so one Stack Overflow question can never contribute
   more than one unit.
2. Run a bounded DeepSeek-via-OpenCode-Go extraction/qualification pass over
   the *top* clusters only (owner approval for spend; provider pinned; no
   fallback), and compare its precision against the deterministic extractor.
3. Add seam-specific query families (e.g. "export X import Y", "re-key between
   X and Y", named-system pairs) instead of broad phrases, and measure whether
   genuine buyer+job recurrence rises.
4. Assess more Part 2 source classes (reviews, job ads, procurement, forums)
   behind the documented access/terms review before enabling any of them.

STOP is not warranted: the plumbing, budgets and auditability all worked, and
the failure mode found is a calibration defect with an obvious fix. PROCEED to
a scheduled production collector is not warranted either, because precision is
not yet good enough to make unattended promotion safe.

## 2. What was built

New package `painmine/` (stdlib-only Python 3.10+, no third-party runtime
dependencies, therefore no `pip install` needed in CI):

| Component | File | Purpose |
| --- | --- | --- |
| Schema | `pain-signal.schema.json`, `schema.py` | Part 1 pain-signal record + runtime validation |
| Source portfolio | `sources.json` | Part 2 class-by-class access assessment and query families |
| Budgets | `limits.json`, `budget.py` | Part 8 hard request/item/model/runtime/cost/retention caps |
| Fetchers | `fetch.py` | Bounded public collectors (HN Algolia, Stack Exchange, GitHub, Reddit) |
| Extraction | `extract.py` | Deterministic cue-based extraction into the schema |
| Dedup | `dedupe.py` | Repost/duplicate collapse, independence counting |
| Clustering | `cluster.py` | TF-IDF + cosine agglomeration with role compatibility |
| Ranking | `rank.py` | Part 4 discovery priority, explicitly separate from business score |
| Persistence | `persistence.py` | Part 5 persistence thesis (both limbs) + mechanism hypotheses |
| Synthesis | `synthesis.py` | Part 6 two-interpreter synthesis (DeepSeek/OpenCode Go, spend-gated) |
| Observation export | `to_observation.py` | Strongest clusters -> Method 1.6 pool rows |
| CLI | `cli.py` | `pipeline` / `validate` / `observations` / `report` |
| Tests | `tests/` | 95 stdlib unittest tests (no network) |
| Agent | `.opencode/agent/painmine-extractor.md` | Strict-JSON DeepSeek extraction agent (deny-all tools) |
| CI | `.github/workflows/painmine-collect.yml`, `painmine-cluster.yml` | Part 7 scheduled + manual collector/stager |

## 3. Source classes attempted (Part 2)

13 classes were assessed; 4 were enabled for the PoC. Access rules, rate
limits and expected quality are documented per class in `painmine/sources.json`.

| # | Class | Status in spike | Access mechanism / constraint observed |
| --- | --- | --- | --- |
| 1 | Hacker News (practitioner discussion) | **enabled, worked** | Public Algolia API, no auth, no rate limit hit |
| 2 | Stack Exchange network (practitioner Q&A) | **enabled, worked** | Public API v2.3, no auth, quota 300/day; `quota_remaining` recorded. Updated 2026-09-21: sites are configurable in `sources.json` and rotate by query position (Stack Overflow, Web Applications, Money, Workplace, ...) so one family reaches business users without extra requests |
| 3 | GitHub issues/discussions (business tooling) | **enabled, worked** | Public search API, 10 req/min unauthenticated; `GITHUB_TOKEN` used when present (documented API auth, not an access-control bypass) |
| 4 | Reddit public JSON | **enabled, blocked from this network** | HTTP 403 Blocked. Recorded as an access failure; no proxy, header spoofing or other circumvention attempted |
| 5 | Software/app review platforms (G2/Capterra) | disabled | Commercial ToS/robots restrictions; no public API |
| 6 | Vendor support/community forums | disabled | Per-site ToS review required; heterogeneous |
| 7 | Job ads describing repetitive admin | disabled | Feeds require an account/API key or ToS review |
| 8 | Public procurement/tender docs | disabled (deferred) | High volume, low precision without entity extraction |
| 9 | Government manual-workflow instructions | disabled (deferred) | Useful for compliance context, weak pain evidence |
| 10 | Professional/trade-body discussion | disabled | Site-by-site robots review not yet done |
| 11 | Integration/app marketplace reviews | disabled | Requires per-marketplace terms review |
| 12 | Public spreadsheets/templates/checklists | disabled | Provenance/licensing risk |
| 13 | Niche trade publications | disabled | Paywalls/republishing risk |
| 14 | Discourse communities (public `/search.json`) | **implemented, disabled pending owner site approval** | Public read endpoint; each instance has its own terms/robots rules, so no site is enabled until the owner approves it. Added 2026-09-21 as a non-regulatory, buyer-side source class |

The four live classes were exercised in one run. `reddit_public_json` produced
0 items across 15 scheduled query attempts (1 real HTTP call -> 403, then 14
attempts blocked by the exhausted request budget); this is recorded, not
hidden.

**Updated 2026-09-21 (opportunity-quality work).** Two Method 1.6 sweeps showed
that the trawl finds real, cited pain but that widely-discussed pain is already
monetised, so nearly every triage rejection was "a credible incumbent already
occupies this seam". Three changes follow from that: query families now target
spend, paid workarounds and named-system seams (`d_paid_workaround`,
`e_unserved_seam` added; the generic "double entry excel process" query
dropped); extraction has a `paid_workaround` cue group, because a problem
someone already pays to work around is the strongest evidence it has a budget;
and cross-run restatements may now hold a cluster together while remaining
excluded from independent-source counts (`restated_count`), so an accumulated
state no longer collapses to zero clusters. Vendor copy can no longer be
exempted from the marketing filter by a `money_cost` or `paid_workaround` hit
alone, since those patterns also fire on phrases like "we pay attention to
detail".

**Updated 2026-09-21 (clustering precision).** A follow-up run showed the
remaining band-A clusters were false positives: auto-generated GitHub
digest/roundup posts (13 of 21 GitHub items, from `agents-radar`/`gittok` repos)
formed a construction/trade cluster, and three unrelated HN comments sharing the
literal query phrase "there has to be a better way" formed an
education-administrator cluster. Three gates now apply: digest posts are
rejected at extraction (`digest_post`); a signal must name a system and either
describe a workaround or have a buyer role (`_has_buyer_substance`); and a
signal with no workaround, time cost or money cost is commentary and cannot hold
a cluster together (`_is_commentary`). A per-thread contribution cap
(`cluster.max_members_per_thread`, default 3) stops one thread carrying a
cluster. The `"double entry" bookkeeping software` query was replaced with
`"reconcile" bank transactions spreadsheet`. After these gates a fresh
40-request run produced **zero** clusters: the noise is gone, but a single run
does not yet surface three independent buyer-side signals on one seam. That is
the honest current state - precision improved, recall is now the binding
constraint.

## 4. Bounded PoC run

Command (repo root):

```
python3 -m painmine.cli pipeline --family all --max-requests 24 \
  --state painmine/state/state.json \
  --out painmine/poc/20260921-live-all --run-id live-20260921-all
```

Artefacts: `painmine/poc/20260921-live-all/` (`report.json`, `report.md`,
`clusters.json`, `observations.md`, `observations.json`, `signals.jsonl`,
`dedupe-stats.json`, `extraction-rejects.jsonl`, `run-meta.json`;
`raw-items.jsonl` is retained locally but git-ignored by policy).

### Volumes

| Metric | Value |
| --- | --- |
| Raw items collected | 150 |
| Extracted signals | 139 |
| Extraction rejects | 11 (8 `statement_too_short`, 3 `no_pain_cue`) |
| Duplicates removed | 18 (duplicate ratio 0.129) |
| Clusters | 6 |
| Clusters with an identifiable buyer role | 3 (50%) |
| Bands | A 1, B 3, C 2 |
| Clusters with >= 3 independent sources | 6 |
| Vendor-led risk | low 6 (no vendor marketing in any cluster) |
| Signal schema validation | 139/139 clean (`validate --run-dir`) |

### Cost, runtime and budget behaviour

| Budget | Used | Limit |
| --- | --- | --- |
| HTTP requests | 24 | 24 (stop reason: request limit reached) |
| Wall clock | 43.84 s | 420 s |
| Items | 150 | 240 |
| Model calls / tokens / USD | 0 / 0 / USD 0.00 | 6 calls / 40k tokens / USD 0.25 (spend disabled) |

The run stopped cleanly **at** the request cap with complete partial results —
the "stop with partial results rather than exceed budget" behaviour required by
Part 8. Source access table from `report.json` (`requests` counts scheduled
query attempts, not just HTTP calls):

| Source | Attempts | OK | Cap-blocked | Items | Notes |
| --- | --- | --- | --- | --- | --- |
| hn_algolia | 15 | 10 | 5 | 50 | 10 HTTP calls |
| stack_exchange | 15 | 10 | 5 | 50 | 10 HTTP calls |
| github_issues | 15 | 3 | 12 | 50 | 3 HTTP calls, then item cap; no 403s |
| reddit_public_json | 15 | 0 | 0 | 0 | 1 HTTP 403, 14 budget-stopped attempts |

## 5. Cluster results and quality audit

| Cluster | Buyer | Indep. | Score/band | Persistence | Verdict |
| --- | --- | --- | --- | --- | --- |
| `c-5d98df96` | Bookkeeper | 6 | 70.8 / A | weak | **Inflated**: ~2 genuine pain signals, 4 commentary |
| `c-4ff80e18` | E-commerce operator | 10 | 67.0 / B | strong | **Inflated by shared phrasing**; 1 genuine everyday WooCommerce->MSSQL re-key seam |
| `c-054ee3da` | none | 4 | 67.5 / B | weak | False positive: Python exception/version-control chatter |
| `c-0610fb64` | none | 3 | 51.0 / B | weak | Generic spreadsheet copy/paste assistance |
| `c-4b0d977b` | none | 3 | 47.5 / C | absent | Consumer integration wishes (Linux/Fastmail/IRC) |
| `c-f574f024` | Administrator | 5 | 41.0 / C | absent | False positive: "44 million uninsured Americans", unrelated "better way" phrases |

Concrete low-quality examples (quoted from the run's own artefacts):

- `c-f574f024` merged an insurance-policy lament with an employee-permissions
  remark and a database-schema question because they share "there has to be a
  better way".
- `c-054ee3da` merged Python exception handling ("manually throw/raise an
  exception"), code-review approvals and "as with most things in Python, it
  gives you a way to do it manually".
- `c-5d98df96` counted "double entry" commentary (`hn:33600156`,
  `hn:35465108`, `hn:31621750`, `se:5110983:answer:5127062`) as independent
  recurrence alongside the two real workaround statements
  (`hn:7363903`, `se:51160263`).

What the observation renderer got right: each row carries the source URL,
date, publisher, evidence type, named systems, the incumbent/workaround
statement, an explicit "hypotheses only, Method 1.6 check still required"
caveat, and a triage reason that states the discovery score is not a business
score. The pool table matches the Method 1.6 column contract and the audit
placeholder instructs the consuming method run to perform its own sampled
false-negative audit. (Updated 2026-09-21 under issue #12: the renderer no
longer emits triage labels, promotion decisions or the three-candidate cap —
it exports ranked, evidence-backed observation *inputs* only, and the
consuming Method 1.6 run performs its own sweep, triage and audit.)

## 6. Recurrence and independence assessment

`recurrence_measurable = true` in the report, but this run shows the metric as
implemented is not yet trustworthy:

- Duplicates/reposts were correctly collapsed (18 removed; the fixture's exact
  repost pair collapses; repeated copies never add recurrence).
- However, "independent" currently means *distinct author/source id with
  similar vocabulary*. For `c-4ff80e18` that produced 10 "independent" authors
  drawn from 9 unrelated Stack Overflow threads and 1 HN comment; for
  `c-5d98df96` it counted commentary. A recurring buyer+job+pain pattern did
  not exist at those counts.
- Where a genuine seam does appear (the WooCommerce -> MSSQL nightly
  export/import in `q/68500700`), it is indistinguishable in the current output
  from adjacent generic CSV chatter.

Conclusion: dedup works; *independence* and *recurrence* need a job/seam-level
agreement gate plus per-thread contribution caps before discovery-priority
recurrence points (up to 30/100) can be earned honestly.

## 7. Contradiction and persistence mining (Part 5)

The persistence layer produced:

- Both limbs computed per cluster: continued pain/workaround despite
  alternatives, and a supported persistence mechanism (2+ independent pieces of
  evidence per mechanism, so one complaint cannot carry a mechanism).
- One `strong` thesis (`c-4ff80e18`, mechanism `partial_or_manual_integration`)
  and one `weak` (`c-5d98df96`); the remaining four were absent/weak.
- No assumption that competitor existence invalidates a cluster; no wedge is
  asserted. `observations.md` explicitly says hypotheses only and leaves the
  Method 1.6 novelty/incumbent check downstream.

This is the layer most likely to improve with the LLM pass, because mechanism
hypotheses from text benefit from semantic reading; the deterministic version
is intentionally conservative (it found only one supported mechanism across
six clusters).

## 8. Independent synthesis (Part 6)

Implemented but **not exercised with paid model calls** in this run: LLM spend
is disabled by default (`limits.json` `llm.enabled=false`, USD 0.25/run cap,
pinned `opencode-go/deepseek-v4.1-flash`, agent `painmine-extractor`, no
fallback provider). `--enable-llm --synthesis` is the explicit opt-in. The
deterministic baseline and the two-ordering prompt construction were exercised
in tests only. Enabling this for the top 2 clusters is the first cheap
follow-up (estimated well under the USD 0.25 cap; actual cost must be recorded
in the run meta).

## 9. GitHub Actions collector assessment (Part 7)

Two workflows are committed-ready but **have not been executed on GitHub**,
because the worker that produced them is forbidden from committing or pushing.
They were validated locally: YAML parses and every `run:` block passes
`bash -n`.

- `painmine-collect.yml`: daily non-round-minute cron (`17 6 * * *`) plus
  `workflow_dispatch`; default-branch-only; rotates query family by UTC
  day-of-year; defaults to 20 requests; deterministic-only unless the dispatch
  input requests synthesis; one shared concurrency group so daily/weekly runs
  serialise.
- `painmine-cluster.yml`: weekly (`43 7 * * 1`) plus dispatch; family `all`;
  optional synthesis for the top 2 clusters.

Controls: hard per-run request/item/model/token/USD/wall caps in `limits.json`
(the CLI clamps `--max-requests` downwards only), `GITHUB_TOKEN` for higher
GitHub rate limits, state round-tripped through `actions/cache`, artefacts
(no raw JSONL) uploaded with 14-day retention, `contents: read` permissions,
and no commit/push step at all. Auth (see `painmine/README.md`): provider
credentials come only from repository secrets — either `OPENCODE_API_KEY` or
`OPENCODE_AUTH_JSON` (owner-copied `auth.json` entry, written with 0600) —
never from the repository. If credentials are absent or the provider fails,
the collector still runs deterministically and the summary records provider
availability rather than silently substituting another inference provider.

Caveat for the owner: GitHub-hosted runners are datacenter IPs, so the Reddit
403 observed locally may recur, and unauthenticated GitHub search limits are
low — which is why `GITHUB_TOKEN` is wired in. This remains an unverified
assumption until the workflows actually run.

## 10. Cost controls and retention (Part 8)

- Limits are file-driven (`painmine/limits.json`) and enforced in `Budget`:
  requests 40, items/source 50, items total 240, min 1.0 s between requests,
  20 s request timeout, retries 1 per request (429/5xx and transport errors
  only), LLM calls 6, input 12k/output 1.2k per call, total tokens 40k, USD
  0.25, wall 420 s.
- The PoC used 24/24 requests, 150/240 items, 43.84/420 s, USD 0.00.
- **Updated 2026-09-21 (issue #13):** `fetch.py` now emits a run ledger with
  separate counters for queries attempted/skipped, HTTP requests initiated,
  HTTP responses received, retries, items returned, items accepted, per-source
  and total item caps, budget-prevented requests and source-access failures,
  plus a reconciliation against the `Budget` counters. The earlier PoC report
  labelled query attempts as "requests" (24 actual HTTP requests vs 60 attempt
  rows) and counted item-cap and budget-prevented rows as failures; new reports
  distinguish them, and old artefacts still render with their original numbers.
- Retention: raw item JSONL is **not** committed (`painmine/poc/**/raw-items.jsonl`
  is git-ignored), excerpts are capped at 600 chars, state keeps at most 5000
  seen ids and 200 cluster records, and GHA artefacts expire after 14 days.

## 11. Acceptance-criteria mapping

| Issue #9 criterion | Status |
| --- | --- |
| Pain-signal schema defined | Done (`pain-signal.schema.json`, runtime validation) |
| Multiple practitioner/problem source classes assessed | Done (13 assessed, 4 enabled) |
| Access/terms/rate-limit constraints documented | Done (`sources.json`) |
| Cheap extraction/dedup/clustering implemented or prototyped | Done (deterministic, stdlib-only, tested) |
| Independent recurrence distinguishable from copies/reposts | Partly — dedup yes; independence gate needs tightening (finding) |
| Discovery-priority ranking separate from business scoring | Done (`rank.py`, disclaimer on every record) |
| Contradiction/persistence pattern represented | Done (both limbs + mechanism hypotheses) |
| >= 1 bounded multi-source PoC run | Done (150 items, 4 classes attempted, 3 successful) |
| PoC cost/runtime recorded | Done (USD 0.00; 43.84 s; 24 requests) |
| Strong clusters convertible to Method 1.6 observation records | Done (`observations.md` in method pool format) |
| Scheduled GHA architecture assessed | Done; workflows written and locally validated, not yet run |
| Hard request/model/runtime/cost limits exist | Done (`limits.json` + `Budget`) |
| Repository-growth/data-retention strategy documented | Done (git-ignore + artifact retention + state caps) |
| No access controls bypassed | Confirmed (Reddit 403 recorded, not worked around) |
| No outreach or unapproved external spend | Confirmed (USD 0.00 model spend; no external contact) |
| Method 1.6 evaluation semantics unchanged | Confirmed (no `method/`, `ideas/`, scorecards or evidence touched) |
| Final PROCEED/ITERATE/STOP recorded | **ITERATE** (section 1) |

## 12. Limitations

- One live run, one day, three working source classes: this is a feasibility
  spike, not evidence about any market.
- Fixture-based test results (18 synthetic items) are test data and were never
  treated as evidence.
- Prior-run vendor dominance was not measured here; the "less vendor-led"
  observation is qualitative (no vendor marketing in any cluster) and is
  limited to the four classes attempted.
- DeepSeek/OpenCode Go extraction and Part 6 synthesis were implemented and
  unit-tested but not invoked with real spend; provider calls from CI remain
  unverified until the owner commits and runs the workflows.
- Clustering quality is the open problem: current TF-IDF grouping rewards
  shared vocabulary; role compatibility reduces but does not remove false
  merges.
