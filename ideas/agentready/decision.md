# Decision record: Agent-ready checkout for independent merchants

- **Idea:** `agentready`
- **Date:** 2026-09-21
- **Run:** `20260921T065316Z-normal`
- **Decision:** kill
- **State:** `discovered` -> `killed`
- **Actor:** worker

## What changed

Generated from a real, dated discontinuity: agentic checkout went live (OpenAI/Stripe ACP, 29 September 2025) and was standardised and bundled (Shopify/Google UCP; Stripe Agentic Commerce Suite with WooCommerce, 11 December 2025; Shopify Agentic Storefronts from March 2026). The change is strong, but it is adverse to a standalone wedge: the platforms and payment networks that opened the surface are giving readiness away inside their standard offer.

## Why now? discovery gate

- **Changed:** agent-mediated discovery and checkout became a live platform surface; see the dossier Why now? object.
- **Changed date:** 2025-09-29
- **Evidence:** `evidence/agentready/2026-09-21-agentic-commerce-landscape.md`
- **Strength:** strong.
- **Competitors responded:** yes, comprehensively — Shopify, Google, OpenAI, Stripe, PayPal, WooCommerce, BigCommerce and Salesforce. The novelty/incumbent check failed on "exact product exists", "multiple credible providers", "already a standard feature" and "feature of a category".

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | Buyer segment identifiable; budget for this job not evidenced. |
| painful_frequent_or_budgeted | unknown | Possible lost sales; no buyer-side pain/budget evidence. |
| non_paid_distribution | unknown | Agency/marketplace routes plausible only. |
| defensible_wedge | fail | Platforms bundle readiness free; protocols open-sourced; feature of commerce platforms. |
| no_network_effects_needed | unknown | Not explicitly assessed. |
| plausible_margins | unknown | No cost/price evidence. |
| acceptable_risk | unknown | Platform/protocol dependence not assessed in depth. |
| cheap_disconfirming_test | unknown | Not specified because the wedge already fails. |
| not_all_optimistic | unknown | Viability would need many simultaneous favourable assumptions. |

## Evidence considered

- `evidence/agentready/2026-09-21-agentic-commerce-landscape.md` (primary platform/payment sources; establishes both the change and the bundled competitive response).

## Scores

Weighted total **49.0** against threshold **65** (meets threshold: false). Details in `ideas/agentready/scorecard.json`. Gating dimensions: problem 2/5, buyer 2/5, evidence strength 3/5.

## Review

No review triggered or required: this is a hard-filter rejection below threshold, which `method/review-policy.md` lists as not needing review. Review status `not-required`.

## Reasons if killed

The discontinuity is real but captured by the incumbents who created it. Readiness for ACP/UCP is becoming a standard, free capability of the commerce platforms themselves; a small entrant cannot defend ground that the protocol owners are subsidising, and merchants rationally wait for their platform. What would change the decision: durable evidence that a substantial off-platform segment is unserved *and* pays a third party, with a non-paid route to those buyers (see seed `agent-checkout-offplatform`).

## False-negative audit (killed ideas only)

- Audited: no — this is kill #4; `method/review-policy.md` triggers an audit every fifth killed idea (recorded against the oldest un-audited kill at #5).
- Reviewer / date: n/a
- Verdict: n/a
- What new evidence would justify reopening: independent evidence that off-platform/custom-storefront merchants pay for agent-readiness and that platforms leave that slice unserved.
