# Decision record: AgentCheckout Off-Platform: agentic-checkout integration and assurance for custom storefronts

- **Idea:** `agent-checkout-offplatform`
- **Date:** 2026-09-21
- **Run:** `20260921T085149Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

This idea began as the seed `agent-checkout-offplatform`, recorded when the parent idea `agentready`
was killed for commodity positioning. The seed asked whether the one exception named in the protocol
literature - a custom or headless store - leaves a durable gap. The seed was re-checked against
current evidence this run and promoted to a candidate, then researched from scratch with its own
fingerprint, evidence, hard filters and scorecard; it inherited nothing from `agentready`. The
re-check answers the seed's questions negatively: hosted UCP hubs (UCPhub 2026-09-15),
commerce-platform middleware (commercetools AI Hub 2026-06-03), platform-native support (Salesforce
B2C Commerce 26.9; Adobe Commerce MCP, April 2026), an open-source Shopify proxy (`ucp-proxy`) and
general middleware vendors already serve off-platform agentic checkout. The candidate therefore
fails `defensible_wedge` and is killed.

## Why now? (discovery gate)

- What changed / when: UCP launched January 2026 with Google, Shopify, Etsy, Target and Wayfair;
  Amazon, Meta, Microsoft, Salesforce and Stripe joined the UCP Tech Council on 24 April 2026;
  Salesforce shipped UCP in B2C Commerce 26.9 (accessed 2026-09-11) and hosted hubs began selling UCP
  enablement through September 2026.
- Why it materially improves the opportunity: agent-mediated buying is new, so no merchant had to be
  agent-checkout-ready three years ago, and protocol churn creates continuing conformance work.
- Strength: `strong`
- If `weak` or `absent`: n/a - strength is strong, but strong why-now does not rescue a wedge that
  hosted, native and open-source providers already occupy.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Buyer assumed (custom/headless merchants and their small agencies); the sources establish the gap, not a budget. `resolve_via`: ask 3 agencies what they charge and whether merchants buy. |
| painful_frequent_or_budgeted | unknown | No buyer-specific frequency or budget evidence; vendor-quoted integration ranges are unverified marketing. `resolve_via`: buyer interviews plus review of agency delivery spend. |
| non_paid_distribution | unknown | Agency partnerships and developer content are plausible; no prospects or channel were identified. `resolve_via`: one agency-partnership or content launch measured for qualified inbound. |
| defensible_wedge | fail | Hosted UCP hubs, commerce-platform middleware, platform-native support, an open-source Shopify proxy and general middleware vendors already sell this exact position; the wedge is a feature of the commerce-integration/platform category. See evidence file sections 2-4. |
| no_network_effects_needed | unknown | A single-merchant integration may be useful alone, but assurance value may scale with conformance data across merchants. `resolve_via`: confirm utility for a single merchant. |
| plausible_margins | unknown | Services-heavy delivery with continuous spec maintenance; cited vendor material says merchants below roughly USD 1.5m GMV should defer to the platform, removing the small end. `resolve_via`: model 10 integrations over two spec cycles. |
| acceptable_risk | unknown | Payment/checkout integration carries security and platform-compliance exposure. `resolve_via`: security and platform-policy review. |
| cheap_disconfirming_test | pass | A zero-cost desk competitive scan was sufficient to disconfirm the wedge this run (evidence file). |
| not_all_optimistic | unknown | Viability rests on several untested assumptions (buyer, price, recurrence). `resolve_via`: name and test the weakest assumption first. |

Status values are `pass` | `unknown` | `fail`; see `method/scorecard.md`. `unknown` entries name
what would resolve them in the scorecard's `resolve_via`.

## Evidence considered

- `evidence/agent-checkout-offplatform/2026-09-21-offplatform-agentic-checkout-incumbents.md`
  (accessed 2026-09-21) - the protocol timeline and why-now, plus the incumbent set that kills the
  wedge.
- Sources that cut against the decision: Salesforce's own guidance names the custom/headless store as
  the exception, and WooCommerce, Magento, BigCommerce, Salesforce Commerce Cloud and commercetools
  merchants must self-serve. The gap is real; it is simply already served, and the remaining work is
  bespoke services with thin margins.
- Seed provenance: `seeds/agent-checkout-offplatform.md`; parent decision `ideas/agentready/decision.md`.

## Scores

Weighted total `49.2` against threshold `65`; 5 of 10 dimensions scored
(`problem_severity_frequency` 3, `buyer_budget_clarity` 2, `evidence_strength` 3,
`differentiation` 2, `economics` 2); overall confidence `low`. See
`ideas/agent-checkout-offplatform/scorecard.json`.

## Review

Review not required. This is a first-time candidate rejected on a failed hard filter at screening
with a documented reason (review-policy "obvious filter rejections"), so `review.status` is
`not-required` with empty history. No review outcome existed for this idea and none was overwritten.

## Reasons if killed

- Binding reason: `defensible_wedge` fail - the off-platform gap is already served by hosted UCP
  hubs, platform/middleware vendors, an open-source Shopify proxy and commerce-integration agencies.
- Secondary reasons: services-heavy with continuous spec maintenance, small end of the market
  explicitly discouraged by the protocol vendors themselves, no buyer or channel evidence.
- What evidence would have changed the decision: named off-platform merchants paying today for
  managed UCP/ACP enablement at a price clearing the delivery cost, where no hosted hub or platform
  bundle can serve them.
- Preserved for future reference: if a later run revisits agentic commerce, it must first explain why
  UCPhub, commercetools AI Hub, Adobe Commerce MCP, Salesforce native UCP and Shopify `ucp-proxy` do
  not already cover the proposed position.

## False-negative audit (killed ideas only)

- Audited: no
- Reviewer / date: -
- Verdict: -
- What new evidence would justify reopening: named off-platform merchants paying for managed
  agentic-checkout enablement, where hosted hubs and platform-native support demonstrably cannot
  serve their stack.
