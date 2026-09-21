# Decision record: ApiSpend: metered API and agent-traffic cost governance for software teams

- **Idea:** `apispend`
- **Date:** 2026-09-21
- **Run:** `20260921T085149Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

The candidate was generated from a previously underexplored source class (platform rule / pricing /
access change) after two consecutive runs missed it, then desk-screened and killed in the same run.
The 2026 metered-API discontinuity is evidenced for at least one major vendor (Autodesk, primary),
but the proposed position - per-integration and per-agent traffic attribution, forecasting and
budget guardrails - is already marketed by API gateways and FinOps/observability vendors (WSO2 AI
Gateway, Moesif, Workato Enterprise MCP, Arcade, n8n). No buyer or willingness-to-pay evidence was
found, so the candidate fails `defensible_wedge` and remains unscored on distribution, feasibility
and risk.

## Why now? (discovery gate)

- What changed / when: Autodesk introduced pricing for AEC/Manufacturing Data Model APIs from
  17 August 2026 (vendor primary, 2026-06-08); Salesforce raised its AppExchange connector fee and
  launched Headless 360 in April 2026, monetising API/MCP access (industry commentary 2026-07-23);
  reported credit/transaction metering at Workday, ServiceNow and SAP (weak secondary 2026-05-29).
- Why it materially improves the opportunity: metered consumption converts an invisible fixed cost
  into a variable one that must be attributed, forecast and governed, and agent traffic multiplies
  call volume per human action.
- Strength: `strong`
- If `weak` or `absent`: n/a - strength is strong, but strong why-now does not rescue a wedge that
  incumbents already occupy.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Buyer assumed (eng/finance leads at 20-200 staff software firms); no evidence anyone buys a standalone tool. `resolve_via`: interviews with 5 target teams about current API-cost tooling and spend. |
| painful_frequent_or_budgeted | unknown | Repricing pain documented mainly in vendor/opinion sources and one unverifiable diary; no buyer-specific frequency or budget evidence. `resolve_via`: buyer interviews plus review of gateway/observability renewal spend. |
| non_paid_distribution | unknown | Developer content/OSS/community channels plausible; no prospects or channel evidence. `resolve_via`: one content or OSS launch measured for qualified inbound. |
| defensible_wedge | fail | Metering, attribution, quota and chargeback are standard gateway/FinOps functionality and multiple vendors already market the position (Moesif per-agent attribution; WSO2 AI Gateway token budgets; Workato Enterprise MCP; Arcade; n8n). See evidence file section 5. |
| no_network_effects_needed | unknown | A single-tenant tool may be useful alone, but value may depend on aggregated benchmark data. `resolve_via`: confirm utility without cross-customer data. |
| plausible_margins | unknown | Self-serve price and support load unmodelled. `resolve_via`: model 20 design partners. |
| acceptable_risk | unknown | Reading customer API traffic raises telemetry/privacy/security exposure. `resolve_via`: security review of a minimal-scope design. |
| cheap_disconfirming_test | pass | A zero-cost desk competitive scan was sufficient to disconfirm the wedge this run (evidence file). |
| not_all_optimistic | unknown | Viability rests on several untested assumptions (buyer, price, channel). `resolve_via`: name and test the weakest assumption first. |

Status values are `pass` | `unknown` | `fail`; see `method/scorecard.md`. `unknown` entries name
what would resolve them in the scorecard's `resolve_via`.

## Evidence considered

- `evidence/apispend/2026-09-21-metered-api-pricing-shift.md` (accessed 2026-09-21) - includes the
  Autodesk vendor primary supporting why-now and the incumbent vendor sources that kill the wedge.
- Sources that cut against the decision: the Autodesk primary shows a real, dated pricing change;
  the OperatorBook diary shows a real operator harmed by repricing. Both support the pain but
  neither shows a defensible product position.

## Scores

Weighted total `40.0` against threshold `65`; 5 of 10 dimensions scored
(`problem_severity_frequency` 2, `buyer_budget_clarity` 2, `evidence_strength` 2,
`differentiation` 2, `economics` 2); overall confidence `low`. See
`ideas/apispend/scorecard.json`.

## Review

Review not required. This is a first-time candidate rejected on a failed hard filter at screening
with a documented reason (review-policy "obvious filter rejections"), so `review.status` is
`not-required` with empty history. No review outcome existed for this idea and none was overwritten.

## Reasons if killed

- Binding reason: `defensible_wedge` fail - the proposed position is standard API-gateway/FinOps
  functionality and at least five vendors market it.
- Secondary reasons: no buyer evidence, no willingness-to-pay evidence, no non-paid channel, no
  margin model, category feature risk.
- What evidence would have changed the decision: a buyer segment with a dated, budgeted pain that
  gateways demonstrably do not serve (for example, agent-specific quota failures blocking
  human-facing integration traffic, with named prospects willing to pay), or evidence that a
  self-serve developer-first wedge could win where enterprise FinOps tools do not.
- Preserved for future reference: if a later run revisits metered agent-traffic governance, it must
  first explain why the incumbent set below does not already cover it: WSO2 AI Gateway, Moesif,
  Workato Enterprise MCP, Arcade, n8n, Kong/Apigee.

## False-negative audit (killed ideas only)

- Audited: no
- Reviewer / date: -
- Verdict: -
- What new evidence would justify reopening: a named buyer segment paying today, with evidence that
  gateway/FinOps features fail their specific agent-traffic scenario.
