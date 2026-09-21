# Run summary — 20260921T075410Z-normal

- Run id: `20260921T075410Z-normal`
- Mode: normal
- Agent: `idea-worker`
- Model: `opencode-go/deepseek-v4.1-flash`
- Method version: 1.2.0 (weights 1.2.0)
- Started: 2026-09-21T07:54:10Z
- Input revision: `291213b`
- Outcome: 3 candidates generated, 3 killed, 0 advanced. No experiments run.

## Orientation

- Ledger on entry: 8 ideas (`adversarially-researched` 3, `killed` 5), 0 unreviewed,
  well under the 10-unreviewed generation stop.
- Review queue on entry: `geonerd` (`requested`, request v2), `shiftswap`
  (`requested`, false-negative audit), method v1.2.0 (`requested`). No response
  files exist for any of them.
- **Changes-requested reviews outstanding: none.** Protocol step 9 is therefore
  vacuous this run — there was no `changes-requested` outcome to answer. No review
  outcome was overwritten or ignored.
- Latest retrospective (`retrospectives/2026-09-21-issue2-delta-review.md`) directed
  this run at the untested source classes: incumbent disruption, poor narrow
  incumbents, manual structured-data flows, new datasets.

## Source classes searched

| Source class | Searched | Notes |
| --- | --- | --- |
| Legislation / regulation | yes | CMA vet remedies; Renters' Rights Act 2025; PRS Database regs; Leasehold & Freehold Reform Act 2024; Awaab's Law (England + Scotland) |
| Consultations / announced rules | yes | CMA draft Order 2026; PRS Database Regs 2026; HMRC/DBT e-invoicing mandate (2029); FCA CP26/22 |
| New datasets | yes | HM Land Registry UPRN/INSPIRE identifiers (28 Aug 2026); data.gov.uk registers |
| Incumbent disruption | yes | Microsoft SharePoint/Office 2016–2021 EOL; QuickBooks Desktop sunset; Acronis/Meraki EOL |
| Manual structured-data flows | yes | mortgage-broker rekeying (Finova); insurance submissions (Insly); e-invoicing |
| Poor narrow incumbents | yes | legacy vet PMS/website vendors; letting-agent software stack |
| New APIs / developer surfaces | partial | FCA Handbook API (Aug 2026); RCVS Find a Vet data submission |
| Platform rule / pricing changes | no | not reached within this run's budget |
| New technical capability | no | not used as a standalone why-now; treated as weak per method |
| Mandated formats / submissions | yes | CMA 36-service price list; RCVS Find a Vet filing; PRS Database entries |

## Candidates and why-now quality

| Slug | Proposition | Why-now quality | Outcome |
| --- | --- | --- | --- |
| `vetcma` | CMA vet price-transparency / transparency compliance for independent practices | **strong** — final decision report 2026-03-24; draft Order 2026-07-21; statutory Order deadline 2026-09-23; compliance window to 2027 | killed |
| `prsregister` | PRS Database readiness for landlords / letting agents | **strong** — Renters' Rights Act 2025; draft PRS Database Regulations 2026; phased rollout from 2026-12-15 | killed |
| `propident` | Corporate-property ownership intelligence on HM Land Registry identifiers | **strong** (dated), but commercially weak — UPRN/INSPIRE lookup tables with Price Paid Data from 2026-08-28; Companies/Overseas data later in FY2026-27 | killed |

## Advances, kills, experiments

- **Advanced to `validation-ready`: 0.** No candidate met the threshold, and the
  best two were rejected on the novelty/incumbent check before deep research.
- **Kills: 3** (`vetcma`, `prsregister`, `propident`), all on the `defensible_wedge`
  hard filter = `fail`. All three suffered the same structural problem: a dated,
  compulsory 2026 mandate that is already contested by several credible providers,
  in two cases including free-forever tools (`vetguard.uk`, `pricebook.vet`,
  `vetcompliance.co.uk`; the free GOV.UK PRS Database register; `landregistry.company`
  at £1/title over open-licence data).
- **Failed / abandoned experiments: none.** No experiment was started, approved or
  run in this run. The three existing experiments (`geonerd-demand-spike`,
  `reasonable-steps-willingness`, `aucly-channel-test`) remain `proposed` with
  approval not granted.
- Best survivor if the wedge were carved more narrowly: `vetcma` scored 61.0
  (below the 65 threshold, and a filter `fail` would block advancement regardless).

## Adjacent-opportunity seeds recorded

Three non-inheriting seeds were recorded from the rejections (each must be
re-researched from scratch before becoming a candidate):

- `vet-estimate-bridge` (origin `vetcma`) — written-estimate → itemised-bill bridge
  tied to fee capture during treatment.
- `prs-listing-precheck` (origin `prsregister`) — pre-marketing validation / API
  wedge for portals and CRM vendors, contingent on the operator API.
- `corporate-property-aml-monitor` (origin `propident`) — ongoing AML monitoring of
  corporate property ownership for small conveyancers, dependent on the FY2026-27
  Companies/Overseas identifier release.

## Limits and budget

- New candidates: 3 of 3 (limit reached).
- Advances to `validation-ready`: 0 of 1.
- Web lookups: **14 of 25** (search + fetch combined).
- Evidence entries added: 3 registers (one per idea; limit 8 per idea).
- Agent steps: well under the 80-step cap; wall-clock well under 3600s.
- Cost: reviewable behaviour stayed well within the run's scope; exact spend is
  provider-reported by the wrapper and is not observable to the worker, so
  `cost_usd`/`tokens` are recorded as `null` (not zero) in
  `runs/20260921T075410Z-normal/run.json`.
- `scripts/validate_repo.py`: **pass** (0 errors; 4 warnings, all pre-existing
  warnings about historical runs recorded under method 1.0.0 / 1.1.0).

## Review queue after the run

Unchanged, no new reviews triggered:

- `geonerd` — `requested`
  (`reviews/2026-09-21-geonerd-review-request-v2.md`)
- `shiftswap` — `requested`
  (`reviews/2026-09-21-false-negative-audit-request.md`)
- method v1.2.0 — `requested`
  (`reviews/2026-09-21-method-v1.2.0-review-request.md`; response expected at
  `reviews/<date>-method-v1.2.0-chatgpt.md`)

The three new kills are `review: not-required`; killing an idea does not itself
trigger review. Killed count is now 8, so the next false-negative audit falls due at
10 killed (the validator warns when killed is a multiple of 5).

## Decisions awaiting human input

1. **Method v1.2.0 review response** — the why-now cap has been in force for two
   runs; a response is still outstanding. Provisionally the cap behaved correctly
   this run (all three candidates had strong dated why-nows, so the cap was not the
   binding constraint — the novelty check was).
2. **`geonerd` review v2** and the **`shiftswap` false-negative audit** — both
   `requested`, awaiting a human reviewer.
3. **Calibration sign-off** — `method/calibration.md` remains unsigned; see the
   method review request.
4. **Experiment approvals** — `geonerd-demand-spike`, `reasonable-steps-willingness`
   and `aucly-channel-test` are all still `proposed`; a human owner must approve
   before any external test. Nothing was started.
5. **Method observation (no edit made)** — the "new mandate → compliance tool"
   source class now looks saturated in the UK: both 2026 flagships are served by
   multiple providers including free tools. A future run may get a better return
   from buyer-specific integration wedges inside a mandate (the seeds above) or from
   genuinely under-served incumbent-disruption gaps, rather than another broad
   compliance product. This is reported, per the rules; `method/` was not edited.

## Compliance confirmation

No disallowed actions were taken. Specifically: nothing was committed, pushed,
opened as an issue or PR, or otherwise published; no one was contacted; no money was
spent; no external accounts were created; no commitments were made; no experiment
was started (only proposed/left proposed); `method/` was not edited during this
routine run; and no recorded review outcome was overwritten or ignored. All
artefacts are unstaged working-tree changes ready for human review.

## Operator note (added after the wrapper finalised the run)

The wrapper writes `run.json` and `runs/index.jsonl` after this summary is
produced. Exact spend was **USD 0.011093** with 138,360 tokens (input 58,421 /
output 5,441 / reasoning 13,083); the authoritative values are in
`runs/20260921T075410Z-normal/run.json`. A partial index line for this run was
superseded by the wrapper's full record, and `scripts/finalize_run.py` now
updates an existing run line in place instead of skipping it.
