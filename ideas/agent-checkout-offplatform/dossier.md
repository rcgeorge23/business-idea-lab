# AgentCheckout Off-Platform: agentic-checkout integration and assurance for custom storefronts

- **ID / slug:** `agent-checkout-offplatform`
- **State:** `killed`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** worker run `20260921T085149Z-normal`, from seed `agent-checkout-offplatform`
  (origin idea `agentready`, killed). Seed promoted to a candidate and researched from scratch this
  run - it inherited nothing from the parent.

## One-sentence proposition

> Merchants on custom or headless storefronts and the small agencies that build for them do not get
> first-party agentic checkout, so they must implement ACP/UCP themselves; we provide
> integration-plus-assurance on top of their existing stack at a project or retainer price.

## Why now?

> This was not an attractive business three years ago, but it might be now because agentic-checkout
> protocols (ACP, UCP) launched, consolidated and shipped into major platforms during 2025-2026,
> creating a compliance surface that only platform-hosted merchants get for free.

- What changed: UCP launched in January 2026 with Google, Shopify, Etsy, Target and Wayfair; Amazon,
  Meta, Microsoft, Salesforce and Stripe joined the UCP Tech Council on 24 April 2026; Salesforce
  shipped UCP in B2C Commerce 26.9 and commerce platforms and hosted hubs began selling UCP
  enablement; the acknowledged exception is a custom or headless store.
- When it changed: January 2026 (UCP launch), 24 April 2026 (Tech Council), September 2026
  (hosted hubs and enterprise-platform GA).
- Evidence (dated source):
  `evidence/agent-checkout-offplatform/2026-09-21-offplatform-agentic-checkout-incumbents.md`
  (DecodeIQ 2026-07-02; Salesforce developer docs accessed 2026-09-11; Shero Commerce 2026-06-26;
  ucphub.ai 2026-09-15; commercetools 2026-06-03; Shopify `ucp-proxy` OSS).
- Why this materially improves the opportunity now: agent-mediated buying is new, so no merchant had
  to be agent-checkout-ready three years ago; the protocol churn creates ongoing maintenance work.
- Have competitors already responded? Yes - hosted UCP hubs, commerce-platform middleware, platform-
  native support and an open-source Shopify proxy already serve this exact gap.
- Strength: `strong`

## Buyer

- Who exactly pays (role, company size, segment): assumed to be merchants on custom/headless
  storefronts and the small agencies that build and maintain them.
- Who uses it: agency developers and merchant e-commerce leads.
- Evidence: the sources establish the *gap*, not the buyer's budget or willingness to pay
  (scorecard `resolve_via`).

## Problem

- What is painful/frequent/expensive: off-platform merchants must implement and maintain ACP/UCP
  endpoints, product feeds and post-purchase flows themselves, and the specifications keep moving.
- Current alternatives and their weaknesses: buy a hosted UCP hub; use platform/middleware support;
  adopt the open-source Shopify proxy; or build in-house.
- Evidence: `evidence/agent-checkout-offplatform/2026-09-21-offplatform-agentic-checkout-incumbents.md`.

## Mechanism / wedge

- What we would actually do: implement UCP/ACP endpoints and feeds for a merchant and keep them
  conformant as specifications update, sold to agencies as a white-label delivery partner.
- Why it is defensible against the cheapest credible incumbent: it is not - hosted hubs and commerce
  platforms already sell managed UCP enablement, and Shopify open-sourced a proxy for existing
  stores, so the wedge is a feature of the platform/agency category.
- Evidence: `evidence/agent-checkout-offplatform/2026-09-21-offplatform-agentic-checkout-incumbents.md`.

## Novelty / incumbent sanity check

| Check | Answer | Evidence |
|---|---|---|
| Does this exact product already exist? | Yes - hosted UCP hubs sell managed setup | ucphub.ai 2026-09-15 |
| Are there multiple credible providers? | Yes - UCPhub, commercetools AI Hub, Adobe Commerce MCP, Salesforce native, Shopify OSS proxy, middleware vendors | evidence file |
| Is the wedge already a standard feature? | Yes - platform-native for hosted merchants; managed service for the rest | Shero 2026-06-26; Salesforce docs |
| Is a free/authoritative alternative already adequate? | Shopify `ucp-proxy` is free and open source; WooCommerce/Adobe ship native MCP | GitHub; Shero |
| Has a well-capitalised company shown hostile unit economics? | No evidence | - |
| Is this merely a feature of an established category? | Yes - commerce integration agencies | evidence file |

If any check fails, state the reason to continue anyway: it was not continued. The seed was promoted
specifically to test whether the off-platform gap survived the parent's commodity kill; the evidence
shows it does not.

## Distribution

- Route to the first 10 buyers without paid acquisition: none evidenced. Agency partnerships are
  plausible but no prospects or channel were identified.
- Evidence: none.

## Economics (assumptions labelled)

- Price hypothesis (assumption): project fees or a small retainer; vendor-quoted UCP integration
  ranges (USD 15k-50k mid-market) are unverified marketing.
- Cost drivers (assumption): delivery labour (services-heavy), continuous spec maintenance.
- Contribution margin at realistic scale: not modelled; the cited vendor material itself says
  merchants below roughly USD 1.5m GMV should defer to the platform, which removes the small end of
  the market.

## Founder fit

- Reach, skills, motivation (evidence only; `null` if unknown): `null`.

## Adversarial case (strongest case this is wrong)

The one exception named in the protocol literature - a custom or headless store - is exactly where
managed providers already compete hardest. UCPhub sells a hosted hub for standard Shopify and
lean-team WooCommerce merchants; commercetools AI Hub, Adobe Commerce MCP and Salesforce B2C
Commerce ship the capability natively for their own customers; Shopify has open-sourced `ucp-proxy`
so an existing store can expose UCP endpoints without a vendor. What remains is bespoke
implementation work: a services business with thin margins, no recurring revenue, and a market the
protocol vendors themselves say should wait. The seed's question 2 - do these merchants pay a price
that clears the service burden - has no positive evidence, and question 3 is answered negatively:
this is a feature of the agency/platform market, not an urgent, dated discontinuity for a product.

## Strongest supporting case

The gap is real and documented (Salesforce's own guidance names headless as the exception;
WooCommerce, Magento, BigCommerce and commercetools merchants must self-serve), the protocol surface
changes often enough to create maintenance work, and a small, focused agency could win white-label
delivery from other agencies.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| Off-platform merchants lack first-party support | Check whether Hydrogen/Commerce Layer/BigCommerce headless already expose ACP/UCP | partly answered - gap confirmed, but served by third parties |
| They pay a price clearing the service burden | Ask 3 agencies what they charge and whether merchants buy | unresolved |
| Maintenance is recurring revenue, not churn | Track a delivered integration over two spec cycles | unresolved |

## Cheapest decisive experiment

- Assumption under test: the off-platform gap is unserved.
- Proposed test: none. The desk scan already found hosted, native and open-source providers in the
  gap; no experiment proposed.
- Pre-fixed decision rule: n/a.
- Cost bound: n/a (desk research, 1 human-hour, £0).
- Status: not proposed (idea killed)
- Link: none

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-21 | `discovered` -> `killed` | `defensible_wedge` fail: hosted UCP hubs, commerce-platform middleware, platform-native support and an open-source Shopify proxy already serve off-platform agentic checkout. | `ideas/agent-checkout-offplatform/decision.md` |
| 2026-09-21 | (seed) `unexplored` -> `promoted` | Seed re-checked against current evidence and promoted to a candidate; candidate killed the same run, so the seed carries no parent score and is closed. | `seeds/agent-checkout-offplatform.md` |
