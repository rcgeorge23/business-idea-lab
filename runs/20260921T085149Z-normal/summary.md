# Run summary: 20260921T085149Z-normal

- **Mode:** normal
- **Started / finished:** 2026-09-21T08:51:56Z / 2026-09-21T09:03:30Z
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.4.0
- **Input / output revision:** `a403682` / `uncommitted`
- **Status:** success

## Seed register review

Register reviewed before generation: 6 `unexplored` seeds, 1 `dropped`. Two seeds were re-checked
against current evidence; the rest were register-level only. No seed inherited a parent score,
confidence or evidence level.

| Seed | Shallow re-check result | Action (candidate / stays seed / status change) |
|---|---|---|
| `agent-checkout-offplatform` (origin `agentready`, killed) | **Weakened/captured.** The off-platform gap is real but already served: hosted UCP hubs, commerce-platform middleware (commercetools AI Hub), platform-native support (Salesforce B2C Commerce 26.9; Adobe Commerce MCP), an open-source Shopify `ucp-proxy` and general middleware vendors all operate this layer. | Promoted to a candidate and researched from scratch, then killed on `defensible_wedge`. Seed status `unexplored` -> `promoted`; outcome row appended. |
| `prs-listing-precheck` (origin `prsregister`, killed) | **Weakened.** The regime is now concrete (in force 2026-12-15; regional rollout to 2027-11-14; £65/property/year; landlord must initiate), but an incumbent already sells a £29/month flat PRS compliance platform and a major lettings platform is publicly building PRS support; agency CRMs already exchange compliance data. Bulk-upload/API availability still unknown. | Stays a seed (`unexplored`); outcome row appended; new evidence path added. Not promoted - it did not merit full fresh research on this evidence. |
| `prs-self-managing-landlord` (new, origin `prsregister`) | New adjacent observation recorded from the re-check: the per-property annual duty falls on individual self-managing landlords, while all visible supply targets agents and portfolios. | New seed created (`unexplored`); no score or evidence level. |
| `grantscout-application-quality` | Not re-checked this run; no evidence from the searched classes touched it. | Stays a seed. |
| `vet-estimate-bridge` | Not re-checked this run; the CMA fee-transparency thread was not re-examined. | Stays a seed. |
| `corporate-property-aml-monitor` | Not re-checked this run; the HMLR identifier timing is unchanged. | Stays a seed. |
| `cross-border-green-list-waste-bridge` | Not re-checked this run (the parent `wastetrack` was killed last run). | Stays a seed. |
| `uk-epr-small-producer-tooling` | Already `dropped`; no change. | Dropped (unchanged). |

Register counts after this run: 8 seeds - 6 `unexplored`, 1 `promoted`, 1 `dropped`.

## Source classes searched

| Source class | Regulatory? | Searched? | What it yielded (or why nothing) |
|---|---|---|---|
| Legislation / regulation | yes | yes | PRS Database Regulations 2026 (in force 2026-12-15, regional rollout to 2027-11-14, £65/property/year). Yielded a shallow re-check that re-confirmed the incumbent crowding; no candidate promoted. |
| Consultations / announced rules | yes | no | Not searched this run. |
| Mandated formats / submissions | yes | no | Not searched this run. |
| New APIs / developer surfaces | no | **attempted, failed** | The search query returned HTTP 429 from the search provider twice; the class was not completed and no conclusions are drawn from it. |
| New datasets | no | no | Not searched (the combined new-APIs/datasets attempt failed). |
| Platform rule / pricing / access changes | no | yes | Rich: Gemini API key/auth-key migration from 2026-06-19; Microsoft Exchange Web Services disablement 2026-10-01 / shutdown 2027-04-01; Google Dynamic Search Ads -> AI Max auto-upgrade September 2026; Salesforce Headless 360 (April 2026) and reported credit/transaction metering at Workday, ServiceNow, SAP; Autodesk Data Model API pricing from 2026-08-17. Produced two candidates (`apispend`, `ewsregister`), both rejected. |
| Incumbent disruption (EOL, shutdown, migration) | no | yes | 2026 EOL wave: Sage BusinessVision EOL 2026-12-31; Dynamics GP new sales ended 2026-04-01; QuickBooks Desktop 2023 support ended 2026-05-31; Project Online service stops 2026-09-30; MySQL 8.0, Node 20, Exchange Server 2016/2019, SQL Server 2016, SharePoint 2016/2019, Office LTSC 2021. All are services/one-shot migration plays; used as context for `ewsregister` and recorded, no separate candidate. |
| Poor / expensive narrow incumbent software | no | no | Not specifically searched this run. |
| New technical capability (esp. AI on repetitive service work) | no | yes | Private/on-prem AI for UK regulated firms (multiple incumbent providers at £18-28k/yr builds); vertical AI capture under way (Checkbox "First Pass" with 100+ enterprise legal teams; EdVisorly $13.3M Series A; HyperVerge MSME underwriting; Candor DI mortgage documents; Dacxi "Ironstone" verification layer). Both show an actively capitalised, contested class; no candidate (no defensible wedge found). |
| Manual structured-data flows / re-keying | no | no | Not searched this run. |
| Awkward integrations between established systems | no | no | Not searched this run (the agentic-checkout integration thread overlapped it and was rejected). |
| Underserved subsegments of an existing category | no | partly | Surfaced only through the PRS re-check (individual self-managing landlords), captured as a new seed rather than a candidate. |

**Source-budget outcome:** met. All 3 candidate slots (the maximum) were non-regulatory
(`apispend`, `ewsregister`, `agent-checkout-offplatform`); 0 were regulation-derived, so the
at-most-1 regulatory limit was respected. At least one previously underexplored non-regulatory class
was genuinely searched: **platform rule / pricing / access changes** and **new technical capability**
had been recorded as unsearched in the previous two runs and were both searched this run. Two
searches failed (HTTP 429) and the new-APIs/datasets class could not be completed; that is reported
here rather than papered over. No filler candidates were manufactured: the third slot is a seed
re-check, and the two fresh candidates come directly from the searched classes.

## Why-now quality

| Candidate | Why now (one line) | Strength | Competitors responded |
|---|---|---|---|
| `apispend` | Enterprise SaaS moved API access to metered/agent-traffic consumption during 2026 (Autodesk Data Model API pricing 2026-08-17; Salesforce Headless 360 April 2026). | strong | Yes - gateways and FinOps/observability vendors already sell attribution and budgets |
| `ewsregister` | Microsoft disables Exchange Web Services from 2026-10-01 and shuts it down on 2027-04-01. | strong | Partly - free first-party usage report and controls; consultancy migration services |
| `agent-checkout-offplatform` | UCP launched Jan 2026, Tech Council expanded 2026-04-24, Salesforce GA in B2C Commerce 26.9; custom/headless stores are the named exception. | strong | Yes - hosted hubs, middleware, platform-native and an open-source proxy |

All three why-nows are evidenced, dated and material rather than general trends; in all three cases
the strength of the why-now did **not** rescue the wedge.

## Candidate provenance

| Candidate | Provenance | Source class (regulatory?) | Why it qualifies for that class | Second-order seam | Why not the obvious first-order product |
|---|---|---|---|---|---|
| `apispend` | fresh | Platform rule / pricing / access changes (no) | Its why-now comes from vendors repricing API access and metering agent traffic, not from a mandate | Per-integration/per-agent traffic attribution, quota reconciliation and chargeback when agent traffic exhausts limits for human-facing integrations | The first-order product (an API gateway/observability dashboard) is exactly what incumbents already ship; the seam was the only plausible differentiation and it is also served |
| `ewsregister` | fresh | Incumbent disruption / EOL / forced migration (no) | Its why-now comes from a platform shutdown date, not a regulation | The inverse seam: first-party reporting misses infrequent EWS use (7/30/90-day window, weekly aggregation), so discovery is incomplete | The first-order product (a migration project) is one-shot services; the seam (a maintained register) is still covered by free first-party tooling |
| `agent-checkout-offplatform` | `seed:agent-checkout-offplatform` (origin `agentready`, killed) | Platform rule / pricing / access changes (no) | Its why-now comes from the ACP/UCP platform changes, not from a regulation | Integration + conformance assurance for the custom/headless exception, i.e. the operational seam the platform bundles do not reach | The first-order platform-native capability is free for hosted merchants; the off-platform seam is already served by hubs, middleware and an open-source proxy |

The re-checked seed was researched from scratch (own fingerprint, evidence, hard filters and
scorecard) and inherited nothing from the parent.

## What advanced

| Idea | From | To | Why |
|---|---|---|---|
| - | - | - | No idea advanced this run. |

## What was killed

| Idea | Reason | Preserved in |
|---|---|---|
| `apispend` (40.0) | `defensible_wedge` fail - attribution, budgets and chargeback are standard gateway/FinOps functionality already marketed by WSO2 AI Gateway, Moesif, Workato Enterprise MCP, Arcade and n8n | `ideas/apispend/decision.md`, `evidence/apispend/2026-09-21-metered-api-pricing-shift.md` |
| `ewsregister` (44.6) | `defensible_wedge` fail - Microsoft's free EWS usage report plus `EWSEnabled`/`EWSAllowedAppIDs` covers the core need; residual work is one-shot MSP migration services | `ideas/ewsregister/decision.md`, `evidence/ewsregister/2026-09-21-ews-retirement-and-usage-visibility.md` |
| `agent-checkout-offplatform` (49.2) | `defensible_wedge` fail - hosted UCP hubs, commerce-platform middleware, platform-native support and an open-source Shopify proxy already serve the off-platform gap | `ideas/agent-checkout-offplatform/decision.md`, `evidence/agent-checkout-offplatform/2026-09-21-offplatform-agentic-checkout-incumbents.md` |

All three are preserved in the ledger as `killed` with their why-now analysis intact; nothing was
deleted.

## What failed or was skipped

- Two web searches failed with HTTP 429 from the search provider, so the **new APIs / developer
  surfaces** and **new datasets** classes were not completed. No candidate was generated from them.
- **Poor / expensive narrow incumbent software** was not specifically searched this run.
- **Manual structured-data flows / re-keying** and **awkward integrations between established
  systems** were not searched as standalone classes (the second was partly covered and rejected via
  the agentic-checkout thread).
- No experiment was proposed: all three candidates were killed on a hard filter, so none is parked
  with a live disconfirming test. The existing queue in `experiments/queue.md` is unchanged.
- Two false-negative audits (shiftswap, bikpayroll) were already discharged by recorded review
  responses; with 13 kills the validator's periodic "audit due" warning (which fires at every 5th
  kill) is no longer raised.

## Convergence assessment

Discovery is **not** converging on better-defended opportunities, and this is the signal the
retrospectives asked to watch. The last three runs have each produced candidates whose binding
rejection is the same hard filter, `defensible_wedge`:

1. the run that killed `agentready`, `packproof`, `vetcma`, `prsregister` and `propident`;
2. the run that killed `wastetrack` (and later `bikpayroll` on the same filter);
3. this run, which killed `apispend`, `ewsregister` and `agent-checkout-offplatform`.

The notable difference this run is that the refused hypothesis space changed: for the first time the
candidates came from the previously underexplored non-regulatory classes (platform pricing/access
changes and new technical capability) rather than from a new mandate. That did not help. The
evidence now points to a structural finding rather than a sourcing oversight: whichever class is
searched, the opportunities reached are either (a) already served by well-capitalised platform,
infrastructure or incumbent vendors, or (b) one-shot services with thin margins and no recurring
wedge. This is the escalation condition recorded in
`retrospectives/2026-09-21-issue4-convergence-review.md`; it should go to a human-led review of
discovery sourcing and framing. The filter must **not** be relaxed - a crowding finding is a valid
outcome, and the alternative (weakening `defensible_wedge`) would defeat the loop.

## Limits encountered

- Candidates generated: 3 / 3 (maximum; one was a seed re-check, two fresh).
- Unreviewed after run: 0 / 10 limit (0 ideas are in `discovered`).
- Advances to validation-ready: 0 / 1.
- Web lookups: 11 / 25 (two returned HTTP 429 and are counted as unsuccessful, not omitted).
- Cost: not measured by the worker; the wrapper writes `runs/20260921T085149Z-normal/usage.json`
  after this run. No budget breach was observed by the worker, and no experiment was proposed, so no
  external spend is implied.
- No run limit was exceeded; no memory/step pressure required stopping the run early.

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
|---|---|---|---|
| Escalate the third consecutive `defensible_wedge` cluster | (a) commission a human-led review of discovery sourcing/framing as the issue-4 retrospective specifies; (b) accept the crowding finding and continue rotating source classes; (c) change the founder/market hypothesis (target segment, geography or business-model shape) rather than the filter. The hard filter must not be weakened. | Now - the trigger has fired | this summary; `retrospectives/2026-09-21-issue4-convergence-review.md` |
| Experiment queue | `reasonable-steps-willingness` first, `aucly-channel-test` second, `geonerd-demand-spike` deferred; each needs explicit human approval before any external action | When a human is available to approve | `experiments/queue.md`; `experiments/index.json` |
| Pending method review | `reviews/2026-09-21-method-v1.4.0-review-request.md` is still `requested` with no response; the run proceeded under 1.4.0 as written | Before the next routine run | `reviews/2026-09-21-method-v1.4.0-review-request.md` |
| Latent ledger inconsistency (flagged, not changed) | `ideas/bikpayroll/scorecard.json` records `experiment.status = "proposed"` with `results: null`, while `experiments/index.json` and `ideas/index.json` record `bikpayroll-incumbent-capability` as `completed` with results at `experiments/bikpayroll-incumbent-capability/results.md`. The validator does not cross-check this. | Next run or during a review | this summary |
| No `changes-requested` reviews exist | Nothing to answer; recorded for completeness | n/a | `reviews/2026-09-21-review-queue-reconciliation.md` |

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|
| `geonerd` | approved | `reviews/2026-09-20-geonerd-review-request.md` (v2) | reviewed 2026-09-21 |
| `shiftswap` | approved | `reviews/2026-09-21-false-negative-audit-request.md` | reviewed 2026-09-21 |
| `bikpayroll` | approved | `reviews/2026-09-21-false-negative-audit-request-bikpayroll.md` | reviewed 2026-09-21 |
| `apispend` | not-required | - | - |
| `ewsregister` | not-required | - | - |
| `agent-checkout-offplatform` | not-required | - | - |
| method 1.4.0 | requested | `reviews/2026-09-21-method-v1.4.0-review-request.md` | 2026-09-21 |

No `changes-requested` review exists anywhere in the repository, so there was nothing to answer
first this run, and no review outcome was overwritten or ignored.

## Next run should

1. Complete the two classes this run could not finish - **new APIs / developer surfaces** and
   **new datasets** - and search **poor / expensive narrow incumbent software** and **manual
   structured-data flows / re-keying**, since none of these has been properly covered.
2. Treat the third `defensible_wedge` cluster as a live escalation: either wait for the human-led
   sourcing review before generating more candidates from the same hypothesis space, or deliberately
   shift the hypothesis space (different buyer profile, service/agency model, or geography) rather
   than re-rolling the same product shapes. Do not weaken the filter.
3. Route the pending method 1.4.0 review and the experiment-queue approvals, and decide whether to
   reconcile the `bikpayroll` scorecard/experiment status inconsistency.

---

**Disallowed actions confirmation.** No commits, pushes, branches, issues or pull requests were
made. No one was contacted, no money was spent, no external accounts were created, nothing was
published and no commitments were made. No experiment was approved or run (only proposals exist, and
none was added this run). No files under `method/` were edited. All ledger changes are left
uncommitted for human review. `runs/index.jsonl`, `runs/<run-id>/run.json` and `usage.json` are
written by the wrapper, not by this worker.
