# Agent-ready checkout for independent merchants

- **ID / slug:** `agentready`
- **State:** `killed`
- **Evidence level:** Plausible
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** run `20260921T065316Z-normal`

## One-sentence proposition

> A service that makes independent, off-platform online merchants ready for agent-mediated discovery and checkout (product feed plus ACP/UCP checkout integration), sold to merchants and their agencies.

## Why now?

- **What changed:** OpenAI and Stripe launched Instant Checkout / the Agentic Commerce Protocol (ACP) on 29 September 2025; Shopify and Google then published the Universal Commerce Protocol (UCP), with majors including Amazon, Mastercard, Meta, Microsoft, Salesforce, Stripe, Target, Walmart and Visa backing it. Stripe shipped an Agentic Commerce Suite with WooCommerce (11 December 2025) and Shopify began giving merchants access to AI storefront channels from March 2026. Agent-mediated commerce moved from concept to live platform surface within about 12 months.
- **Changed date:** 2025-09-29
- **Evidence:** `evidence/agentready/2026-09-21-agentic-commerce-landscape.md`
- **Why it materially improves the opportunity:** before late 2025 there was no live agentic checkout surface for a merchant to be "ready" for; the question did not exist. The change creates a genuine new integration job.
- **Did competitors respond?** Yes — this is the problem. Shopify/Google (UCP), OpenAI/Stripe (ACP), PayPal, WooCommerce, BigCommerce and Salesforce Commerce Cloud are all shipping, and the platforms bundle readiness into their standard offer at "no fees beyond standard processing". The window is already being closed by the very parties that opened it.
- **Strength:** strong (a real, dated, material change) — but the change is adverse to a standalone wedge, not favourable to one.

## Novelty / incumbent sanity check

| Check | Answer | Evidence | Reason to continue / stop |
|---|---|---|---|
| Does an exact product already exist? | Yes, effectively | platform docs; Shopify "Agentic Storefronts" | Stop: exact readiness is a shipped feature |
| Multiple credible providers? | Yes | Shopify, Google, OpenAI, Stripe, PayPal, WooCommerce | Stop |
| Is the wedge already a standard feature? | Yes | bundled at no incremental fee | Stop |
| Adequate free/authoritative alternative? | Yes for platform merchants | UCP/ACP open standards; Stripe suite | Stop for platform merchants |
| Well-capitalised player showed hostile unit economics? | Not applicable | — | — |
| Merely a feature of a category? | Yes | compliance/integration feature of commerce platforms | Stop |

Outcome: the check is failed and no reason to continue was found; the idea was killed before deep research.

## Buyer

Independent/off-platform e-commerce merchants and their agencies (buyer defined but not evidenced as a budget holder for this job). The platform-merchant majority is served first-party.

## Problem

New agent-mediated buying surfaces require product-feed quality and checkout-endpoint readiness; merchants may not be ready and may lose sales. However, pain frequency, severity and search behaviour were not evidenced.

## Mechanism / wedge

Guided feed preparation plus ACP/UCP checkout integration service/tooling. The wedge is offered by the platforms themselves for free, so it is not defensible.

## Distribution

No non-paid route to early buyers was evidenced. Agency partnerships and app-marketplace listings are plausible but were not tested; distribution score is capped at 2 (plausible only).

## Economics (assumptions labelled)

- **Assumption:** a subscription or one-off integration fee would be chargeable to off-platform merchants.
- **Assumption:** support cost per merchant is low once integrated.
- Neither is evidenced; the economics dimension is scored 2 with low confidence because it is modelled and untested.

## Founder fit

Would suit a commerce-integration engineer with agency relationships. Not evidenced for our owner.

## Adversarial case (strongest case this is wrong)

The whole category is being standardised and subsidised by the largest platforms and payment networks. Even the off-platform slice is being addressed by Stripe/WooCommerce/agency tooling. A small entrant cannot out-execute the protocol owners, and merchants rationally wait for the platform they use to ship it.

## Strongest supporting case

A persistent tail of custom-storefront and legacy merchants with no first-party route means a narrow integration/assurance service could survive; see the adjacent seed. That is a services business at best, not a defensible product wedge.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| Independent merchants will pay a third party for agent-readiness | Price test with off-platform merchants | untested |
| Platforms will not cover off-platform stacks adequately | Track platform/agency coverage | untested |
| Integration support cost is low | Pilot delivery | untested |

## Cheapest decisive experiment

Not proposed: the `defensible_wedge` hard filter fails, which kills the idea under `method/scorecard.md`. Spending on a test would be unjustified.

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-21 | `discovered` -> `killed` | `defensible_wedge` hard-filter fail; platforms bundle readiness free | `ideas/agentready/decision.md` |
