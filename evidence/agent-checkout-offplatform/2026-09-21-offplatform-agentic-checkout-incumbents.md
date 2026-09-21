# Evidence: off-platform agentic checkout already has hosted and middleware providers

- **Idea / scope:** `agent-checkout-offplatform`
- **Register:** evidence
- **Source:** sources listed per claim below (URLs recorded)
- **Accessed / dated:** 2026-09-21
- **Credibility:** primary for vendor docs and the open-source proxy; credible secondary for agency
  and industry write-ups; vendor claim for the hosted-hub and commerce-platform vendors

## Claim(s) supported

- ACP and UCP are the agentic-checkout protocols; major platforms implement them natively, and the
  acknowledged exception is a custom or headless store.
- The custom/headless gap is already served by hosted "UCP hub" vendors and by commerce-platform
  middleware vendors, and Shopify has open-sourced a UCP proxy for existing stores.
- Agentic-checkout integration is priced work, but vendor-quoted ranges are unverified.

## Exact detail

### 1. Protocol landscape and the off-platform exception

DecodeIQ, "Agentic commerce protocols" (`https://decodeiq.ai/blog/agentic-commerce-protocol/`),
dated 2026-07-02. Reported: ACP launched September 2025 by OpenAI with Stripe; OpenAI stepped back
from in-chat checkout in March 2026; UCP launched January 2026 by Google with Shopify, Etsy, Target
and Wayfair; Amazon, Meta, Microsoft, Salesforce and Stripe joined the UCP Tech Council on
24 April 2026. Quoted: "On Shopify, Amazon, and Etsy, the platform handles the protocol
integration... The one exception is a custom or headless store, which may implement the protocols
directly or buy an integration."

### 2. Platform-native implementation

Salesforce Developers, SFRA UCP guide (`https://developer.salesforce.com/docs/commerce/sfra/guide/ucp-index.html`),
accessed 2026-09-11: UCP is generally available in B2C Commerce 26.9 (en-US only, Google as the first
live platform, platform-agnostic, with post-purchase order webhooks). This is a vendor primary
source showing a large commerce platform shipping the capability natively.

Shopify, `ucp-proxy` (`https://github.com/Shopify/ucp-proxy`): an open-source, stateless per-tenant
proxy that exposes the UCP checkout API (REST and MCP) over an existing store. Open source is a
free/authoritative alternative for precisely the merchant segment the candidate targets.

Contra Collective (`https://contracollective.com/blog/universal-commerce-protocol-shopify-google-agentic-checkout-standard-2026`),
dated 2026-08-23: UCP is co-developed by Shopify and Google, launched with Walmart, Target, Etsy,
Amex, Mastercard, Stripe and Visa; headless Shopify Plus builds must make catalog data structured and
inventory/pricing authoritative. Shero Commerce
(`https://sherocommerce.com/blogs/insights/ucp-mcp-server-ecommerce`), dated 2026-06-26: Shopify
merchants get Storefront MCP/UCP free at platform level; WooCommerce, Magento, BigCommerce,
Salesforce Commerce Cloud and commercetools merchants must do the setup themselves (plugin or
gateway-server pattern); "Several middleware vendors now operate this layer as a managed service";
WooCommerce MCP is in developer preview with Woo 10.3; Adobe Commerce MCP server launched at Adobe
Summit April 2026.

### 3. Hosted hubs already sell the exact position (vendor claims)

- ucphub.ai, "Hosted hub vs manual DIY integration in 2026"
  (`https://ucphub.ai/ucp-setup-tutorial-hosted-hub-vs-manual-diy-integration-in-2026/`), dated
  2026-09-15: markets a hosted UCP hub against DIY, claiming hosted gets merchants live in hours or
  days versus 2-8 weeks DIY "plus an endless spec-maintenance tail", explicitly for standard Shopify
  and lean-team WooCommerce merchants - "For the overwhelming majority of merchants... the hosted
  hub". This is the candidate's proposed wedge, already productised by a vendor.
- commercetools, "Google UCP merchant guide to agentic commerce"
  (`https://commercetools.com/blog/google-ucp-merchant-guide-to-agentic-commerce`), dated
  2026-06-03: AI Hub supports UCP product feeds and checkout in Google Gemini and orchestrates
  Gemini/ChatGPT/Copilot; UCP is available to select US merchants, rolling to Canada/Australia/UK by
  end 2026.
- The Universal Commerce Protocol, merchant economics pages
  (`https://theuniversalcommerceprotocol.com/ucp-merchant-economics-roi-calculator/`,
  `.../understanding-the-ucp-pricing-model-fees-costs-and-value-for-merchants/`), dated 2026-03-11
  and 2026-05-03: quotes mid-market UCP integration at USD 15k-50k, enterprise at USD 80k-200k+,
  and states Shopify agentic commerce began charging 1-2% of checkout GMV from Q2 2026. Vendor-ish
  and unverified; used only to show that a paid integration market is believed to exist.

## Why it is credible

The Salesforce developer documentation and the Shopify open-source repository are primary and
checkable. DecodeIQ and Shero Commerce are industry/agency write-ups consistent with those primaries.
The hosted-hub, commercetools and pricing pages are vendor marketing and are labelled as such; they
are cited to show that providers *claim* to serve the position, which is enough to establish
competitor presence, not enough to establish market size.

## What it does NOT show

- No evidence of what off-platform merchants or small agencies actually pay for this, or that they
  pay a recurring amount rather than a one-off build fee.
- No buyer interviews, prospects, win/loss data or market size.
- Vendor claims about speed, "spec-maintenance tail" and ROI are unverified.
- Nothing here shows an unserved seam: the same sources show hosted hubs, platform-native support,
  open-source proxies and agency/middleware providers covering the gap.

## Links

- Used by: `ideas/agent-checkout-offplatform/scorecard.json#problem_severity_frequency`,
  `#buyer_budget_clarity`, `#evidence_strength`, `#differentiation`, `#economics`,
  `#defensible_wedge`, `#cheap_disconfirming_test`
