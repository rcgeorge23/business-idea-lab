# Decision record: EwsRegister: Exchange Web Services dependency discovery before the 2027 shutdown

- **Idea:** `ewsregister`
- **Date:** 2026-09-21
- **Run:** `20260921T085149Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

The candidate was generated from the source class "software shutdown / end-of-life /
forced-migration gaps" - searched this run after the previous run's accounting-EOL scan. Microsoft
has a hard, dated EWS disablement (from 1 October 2026) and shutdown (1 April 2027), and the
dependency set is genuinely invisible by default. But the core discovery need is already met by a
free, authoritative first-party tool (Microsoft's EWS usage report) plus tenant controls
(`EWSEnabled`, `EWSAllowedAppIDs`), and the residual work is a one-shot migration that MSPs and
consultancies already sell as services. The candidate therefore fails `defensible_wedge` and is
killed; no buyer, price or channel evidence was found.

## Why now? (discovery gate)

- What changed / when: Microsoft begins tenant-by-tenant EWS disablement in Exchange Online on
  1 October 2026 and permanently shuts EWS down on 1 April 2027 (ITECS 2026-08-20, citing
  Microsoft's plan and the tenant controls).
- Why it materially improves the opportunity: a dated, non-negotiable shutdown creates a forced-
  action window that did not exist before, and EWS is commonly buried in backup jobs, archive
  connectors, public-folder workflows, scheduling apps and scripts.
- Strength: `strong`
- If `weak` or `absent`: n/a - strength is strong, but strong why-now does not rescue a wedge that a
  free first-party tool and existing services already cover.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Buyer assumed (MSPs / SMB IT managers on Microsoft 365); no evidence anyone buys a standalone discovery tool rather than an MSP project. `resolve_via`: ask 5 MSPs what they charge and what tools they use today. |
| painful_frequent_or_budgeted | unknown | Breakage is real and dated but infrequent (one-time), and the pain is the tenant's, not necessarily a budget holder's. `resolve_via`: buyer interviews on budget ownership for EWS migration. |
| non_paid_distribution | unknown | MSP communities and marketplaces are plausible; no prospects or channel were identified. `resolve_via`: one MSP-community launch measured for qualified inbound. |
| defensible_wedge | fail | Microsoft's free EWS usage report and `EWSEnabled` / `EWSAllowedAppIDs` controls already cover the core discovery need, and the residual work is one-shot migration services MSPs already sell. See evidence file sections 1-2. |
| no_network_effects_needed | unknown | A per-tenant scanner may be useful alone, but benchmark or cross-tenant value is unproven. `resolve_via`: confirm single-tenant utility satisfies the buyer. |
| plausible_margins | unknown | A one-shot need priced monthly is a poor recurring subscription; support and spec-maintenance costs unmodelled. `resolve_via`: model 20 tenants and the post-migration job. |
| acceptable_risk | unknown | Reading a tenant's EWS usage needs Microsoft Graph permissions and a security review. `resolve_via`: minimal-scope design review. |
| cheap_disconfirming_test | pass | A zero-cost desk competitive scan was sufficient to disconfirm the wedge this run (evidence file). |
| not_all_optimistic | unknown | Viability rests on several untested assumptions (buyer, willingness to pay, recurrence). `resolve_via`: name and test the weakest assumption first. |

Status values are `pass` | `unknown` | `fail`; see `method/scorecard.md`. `unknown` entries name
what would resolve them in the scorecard's `resolve_via`.

## Evidence considered

- `evidence/ewsregister/2026-09-21-ews-retirement-and-usage-visibility.md` (accessed 2026-09-21) -
  the Microsoft EWS timeline and the first-party usage-report/controls that kill the wedge, plus the
  wider 2026 EOL context.
- Sources that cut against the decision: the disclosure that Microsoft's usage report covers only
  7/30/90-day windows and is aggregated weekly, so infrequent or seasonal EWS use can be missed, and
  that Graph parity gaps remain for public folders and in-place archive. These support the pain but
  describe a narrow, one-shot consulting gap rather than a defensible product position.

## Scores

Weighted total `44.6` against threshold `65`; 5 of 10 dimensions scored
(`problem_severity_frequency` 3, `buyer_budget_clarity` 2, `evidence_strength` 2,
`differentiation` 2, `economics` 2); overall confidence `low`. See
`ideas/ewsregister/scorecard.json`.

## Review

Review not required. This is a first-time candidate rejected on a failed hard filter at screening
with a documented reason (review-policy "obvious filter rejections"), so `review.status` is
`not-required` with empty history. No review outcome existed for this idea and none was overwritten.

## Reasons if killed

- Binding reason: `defensible_wedge` fail - a free authoritative alternative (Microsoft's EWS usage
  report) plus tenant controls covers the core need, and the residual work is one-shot migration
  services already served by MSPs and consultancies.
- Secondary reasons: temporary market with a hard expiry (gone by mid-2027), no recurring revenue,
  no buyer or channel evidence, services-heavy delivery.
- What evidence would have changed the decision: a named MSP segment paying today for third-party
  EWS discovery because the first-party report demonstrably misses their estates, with a durable
  post-migration job that recurs.
- Preserved for future reference: if a later run revisits forced-migration discovery, the first-party
  tooling must be shown to be inadequate for a specific, budgeted segment before it is re-screened.

## False-negative audit (killed ideas only)

- Audited: no
- Reviewer / date: -
- Verdict: -
- What new evidence would justify reopening: named MSPs paying for third-party discovery, plus
  evidence the first-party usage report misses their EWS workloads.
