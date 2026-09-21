# Seed: Agentic-checkout readiness for off-platform merchants

- **Seed ID / slug:** `agent-checkout-offplatform`
- **Origin idea:** `agentready` (state: `killed`)
- **Recorded:** 2026-09-21
- **Status:** `unexplored`

> Seeds carry **no score, confidence or evidence level**. They are observations
> preserved from a rejection, not candidates. A seed does not inherit anything from its
> parent idea, and a later run must research it from scratch and create its own dossier,
> evidence and scorecard before it can be anything more than a seed.

## Observation

The AgentReady kill found that the major commerce platforms bundle agentic checkout and
AI-channel distribution into their standard offering: Shopify's Agentic Storefronts was
described as needing "no apps, no custom integrations, no fees beyond standard
processing", and Shopify/Stripe/Google/WooCommerce/BigCommerce/Salesforce are all
shipping ACP/UCP support. During that review the following narrower observation was
recorded:

> Merchants on **off-platform / custom storefronts** (bespoke builds, headless, small
> agencies) do not get a first-party agentic channel. A narrow integration-and-assurance
> service for custom stacks might persist where the platform bundles do not reach.

## Why this is materially different from the parent

- **Different buyer:** custom/headless merchants and the small agencies that build for
  them, not the general "independent merchant" population that the platforms already
  cover for free.
- **Different mechanism:** integration/assurance work on top of ACP/UCP endpoints and
  product feeds, rather than a productised readiness tool.
- **Different competitive position:** the threat is the platform bundle; the wedge only
  exists off-platform, which the parent's commodity kill did not test.
- **Non-inheriting:** the parent's score (49.0), its kill reason and its `Plausible`
  evidence level are irrelevant to this seed; it starts at `unexplored` with no score.

## Evidence

- `ideas/agentready/decision.md` — adversarial pass and kill rationale.
- `evidence/agentready/2026-09-21-agentic-commerce-landscape.md` — protocol and platform
  bundling evidence (Shopify Agentic Storefronts, Stripe/WooCommerce, ACP/UCP).

## What a later run should check first

1. Do custom/headless merchants actually lack ACP/UCP support today, or do the cart or
   agency platforms (Shopify Hydrogen, Commerce Layer, BigCommerce headless) already
   expose it?
2. Is there evidence these merchants pay for integration work at a price that clears the
   service burden, or is it a one-off low-value build?
3. Is there a dated discontinuity that makes off-platform readiness urgent (a new channel
   launch, a mandate, or a fee change), or is this just a feature of the agency market?

## Outcome (append-only)

| Date | Status | Note |
|---|---|---|
| 2026-09-21 | unexplored | Recorded from the AgentReady kill; no research performed yet. |
