# Single-source leads from the painmine corpus (2026-09-21)

**Status: leads, not candidates.** Nothing here has recurrence evidence. Every
lead below rests on **one source** (mostly one Discourse community, often one
author). Under Method 1.6 these are *observation inputs*, not scored ideas: no
evidence level, no score, no triage outcome, and they do not consume the
three-candidate limit. They are written up so a human can decide whether any is
worth a cheap disconfirming test.

## How this list was built

Aggregated every `signals.jsonl` and `raw-items.jsonl` across the 28 local
painmine runs (`painmine/state/local-run-*/`), deduped by `signal_id` /
`source_id`: **564 unique signals, 748 unique raw items**.

Source mix of that corpus:

| Source | Signals | Assessment |
|---|---|---|
| `github_issues` | 231 | **Noise.** Auto-generated agent digests ("Hot Issues (Top 10 by Community Signal)", "Developer Pain Points \| Pain point \| Frequency / impact \| Typical workaround"), LaTeX package lists, AWS botocore changelogs. Role inference mislabels these as Accountant / Construction / E-commerce because the digest text mentions those words. **Excluded.** |
| `hn_algolia` | 215 | **Mostly developer/infra commentary** (C++, MySQL, Notion, SharePoint, Slack) plus the known-inflated "double entry bookkeeping" philosophy cluster. A handful of genuine business-workflow comments survive. |
| `stack_exchange` | 103 | Mostly programming Q&A (JRE, MySQL, Python, Excel VBA). A few genuine business-workflow questions. |
| `discourse_public_json` | 14 | **The richest buyer-side material** — real merchants describing real operational seams. |
| `reddit_public_json` | 1 | Reddit is IP-blocked (HTTP 403); effectively absent. |

**Concentration warning.** Of the 13 most substantive Shopify threads, **8 were
authored by one merchant (`SealSubs-Roan`)**. Those are one voice, not eight
independent buyers. `LitExtension` is a vendor fishing for content;
`michael010101go` looks like a researcher/vendor probing a workflow. The
genuinely independent merchant voices are `juhyun_han` (engagement 80),
`Romainhtw` (38), `closecheck_retail` (11) and `vikasmaur13`.

---

## Lead A — Shopify inventory / purchase-order reconciliation

**The seam.** Low-stock → purchase order → transfer → receive is a manual,
duplicate-edited loop. Merchants read an inventory report, calculate quantities
by hand, cross-reference a supplier catalogue, enter the PO, then re-enter the
same data when stock transfers between supplier and store.

**Evidence (single source, community.shopify.com):**
- `:682289` (2026-09-15, SealSubs-Roan): *"If your process for creating a new
  Purchase Order looks like opening an inventory report, checking low-stock
  items, manually calculating quantities, cross-referencing your supplier
  catalog, and entering everything into a…"*
- `:682404` (2026-09-16, SealSubs-Roan): *"Please make linked inventory
  transfers update automatically when new products are added to their purchase
  order. The current workflow requires duplicate manual edits. Transfer T0217 is
  an example."*
- `:630533` (2026-06-02, closecheck_retail, engagement 11): *"What a cluster
  f\*\*\*. Just seems to have been launched on us. Lots of extra steps. Stupid
  need to indicate transfer from supplier to store. We have ordered the product,
  we load the purchase order, we receive it. Why ove…"*
- `:682873` (2026-09-16, SealSubs-Roan): bulk inventory editor regression —
  *"the previous workflow was much faster: click a cell, enter the quantity,
  then press Tab… Now, you need to double-click each cell."*
- `:681928` (2026-09-14, SealSubs-Roan): no on-hand inventory valuation report.

**Scrutiny.**
- *Economic buyer:* yes — the merchant/operator themselves; inventory accuracy
  is directly money.
- *Existing alternatives:* Shopify native POs (which merchants in these threads
  say are a "minimal ledger interface"), Stocky (being sunset), and a long tail
  of inventory apps. **This is a crowded seam** — the wedge would have to be
  the *reconciliation between* systems, not another inventory app.
- *Why now:* weak-to-moderate. The `:630533`/`:682404` complaints are about a
  **Shopify-native PO redesign** (a vendor regression), not a market
  discontinuity. Regressions get fixed.
- *Defensibility:* low as stated. "Better PO entry" is a feature, not a company.
- *Cheap disconfirming test:* search the Shopify App Store for PO/transfer
  automation and count how many already claim to sync POs and transfers; if
  several do, the seam is occupied.
- **Verdict: weak.** Real pain, but it is a vendor-regression complaint inside a
  platform that owns the workflow. Not a standalone business.

---

## Lead B — Stocky sunset (August 2026) forcing an inventory migration

**The seam.** Shopify is retiring the Stocky inventory app in **August 2026**.
Merchants who use Stocky for purchase orders, receiving and cost adjustment are
being forced to migrate mid-year, and the native replacement is widely reported
as inadequate.

**Evidence (single source, community.shopify.com):**
- `:587292` (2026-02-04, juhyun_han, **engagement 80**): *"I am concerned about
  hearing that the Stocky App is going away this year. What are any of you doing
  to manage your inventory? We currently use Stocky to create and receive
  purchase orders, adjust our costs when receiving…"*
- `:587141` (2026-02-03, Romainhtw, **engagement 38**): *"I received a notice
  today that stocky is being sunset in August 2026. Does anyone have a good
  replacement? I briefly looked at shopify's and it doesn't look great — you
  have to use suppliers not vendors, there's no 'fill…'"*
- `:587146` (2026-02-04, rainline): *"Stocky should remain in use over Shopify
  native Purchase Orders because it supports real-world inventory operations,
  whereas Shopify POs are a minimal ledger interface designed for state capture,
  not o…"*

**Scrutiny.**
- *Economic buyer:* yes — merchants with real inventory operations, and the
  engagement numbers (80, 38) show this is a live concern, not one person.
- *Existing alternatives:* Shopify native POs (rejected by these merchants), and
  the inventory-app market. **The migration itself is a one-shot event** — a
  services opportunity, not recurring software revenue.
- *Why now:* **strong and dated** — a vendor-forced discontinuity with a
  published deadline (August 2026). This is the only lead here with a genuine
  "why now".
- *Defensibility:* low for "a replacement inventory app" (crowded, and Shopify
  controls the platform). Higher for a *migration + reconciliation* tool that
  bridges Stocky data into whatever the merchant moves to.
- *Cheap disconfirming test:* check whether the Shopify App Store already has
  several "Stocky replacement / Stocky migration" apps with reviews; if yes, the
  window is already being served.
- **Verdict: the most interesting lead, but likely a one-shot services play.**
  Worth one cheap check on incumbent migration apps before any further effort.

---

## Lead C — Marketplace/channel fee tracking

**The seam.** When a merchant sells on multiple channels via Shopify Marketplace
Connect, the marketplace deducts its fee from the payout **before the money
reaches Shopify**, so the fee never appears as a line item. Merchants cannot see
their true per-channel margin.

**Evidence (single source, community.shopify.com):**
- `:682829` (2026-09-16, SealSubs-Roan): *"A channel fee is incurred when you
  sell on multiple channels using Shopify Marketplace Connect. And It's not
  tracked in Shopify because the marketplaces deduct it directly from the
  payouts before the money ever hits you…"*
- Related threads in the same community: *"Reporting granularity gaps (card type
  splits, fee itemization, and how merchants handle it)"* (2026-04-14) and
  *"Overcharged on fees?"* (2026-09-16).

**Scrutiny.**
- *Economic buyer:* yes — margin visibility is money, and multi-channel sellers
  are exactly the ones with budget.
- *Existing alternatives:* accounting tools (QuickBooks/Xero) and payout
  reconciliation apps; the 2024 thread *"Best way to match the Shopify payouts
  with the Sales Receipts of each order in QBO?"* shows this is a known,
  partially-served problem.
- *Why now:* weak. Multi-channel selling is not new; the pain is structural, not
  a discontinuity.
- *Defensibility:* moderate — fee normalisation across marketplaces is fiddly
  and data-shaped, which is a real moat if done well.
- *Cheap disconfirming test:* search for existing "marketplace fee
  reconciliation" tools and check whether any already normalise Marketplace
  Connect fees.
- **Verdict: plausible but unproven.** Needs a check that it is not already
  solved by payout-reconciliation apps.

---

## Lead D — E-commerce order re-keying into 3PL / fulfilment / stock trackers

**The seam.** Orders are exported from the store and re-keyed by hand into a
third-party logistics system, a fulfilment system, or a spreadsheet stock
tracker, because the integration is missing or one-way.

**Evidence (multiple sources — the only lead here with more than one):**
- `902c3a7b96a11547` (stack_exchange, stackoverflow.com/q/68500700, E-commerce
  operator, Excel+WooCommerce): *"Everyday I need to MANUALLY export Order from
  WC in csv and run the C# program to import the csv data into MSSQL and then
  generate the report and send to branches."*
- `00c7dd9e1ecf19c3` (stack_exchange, E-commerce operator, Shopify): *"Our 3PL
  requires a CSV upload of every order because there is no integration with our
  Shopify store. We export the orders and re-key the addresses by hand every
  morning."*
- `8cd3aed86d857d90` (stack_exchange, E-commerce operator, Google
  Sheets+Shopify): *"We sell on Amazon and Shopify and then manually copy the
  order list into a Google Sheets stock tracker every day. It is error prone and
  nobody enjoys it."*
- `67ee111e71d59a7c` (hn_algolia, E-commerce operator, WooCommerce): *"every
  order has to be typed into the fulfilment system by hand because the
  integration only sends tracking numbers one way."*

**Scrutiny.**
- *Economic buyer:* yes — the operator, and the cost is daily labour.
- *Existing alternatives:* this is the **most crowded** seam of all. iPaaS
  (Zapier, Make, n8n), 3PL middleware, and dozens of Shopify↔3PL connectors
  exist. The evidence itself is from people who *could not* use Zapier.
- *Why now:* none. This is a persistent integration gap, not a change.
- *Defensibility:* low — the incumbents are large and the work is
  connector-shaped.
- *Cheap disconfirming test:* count Shopify App Store 3PL/fulfilment connectors;
  if >10, the seam is served.
- **Verdict: reject as a standalone business.** Useful as *evidence that the
  problem class is real*, not as an idea.

---

## Lead E — Recurring report assembly from emailed / exported spreadsheets

**The seam.** A recurring report is assembled by hand each period: a spreadsheet
arrives by email or export, is copied into a template, and the same manual
copy-paste happens every month.

**Evidence (multiple sources):**
- `ebaad27c4fa5471c` (stack_exchange, stackoverflow.com/q/10936404): *"I want
  this report to export to excel automatically, to the same workbook, on the
  same worksheet, every time it is run per month… I'd like to avoid exporting
  it to a new workbook, then copying and pasting into the workbook with all my
  templates manually."*
- `4c073c1ccc4e125a` (stack_exchange, stackoverflow.com/q/59136525, Excel+Gmail):
  *"I get an excel by email which I need to convert to google sheet where I
  already have a script which runs to pull data and then upload stock values."*
- `56558b7064ee835e` (stack_exchange, stackoverflow.com/q/55885085,
  Excel+Zapier): *"I am able to easily copy and paste our daily activities into
  a Google Sheet, but I need to be able to summarize by weeks, months, quarters,
  half-years and years… I cannot use Zapier or any other automation."*
- `bfe6a98d2a00b1be` (stack_exchange, superuser.com/q/1595693): *"Open the CSV
  and immediately copy and paste the data into the template file."*

**Scrutiny.**
- *Economic buyer:* **unclear.** These are individual spreadsheet users, often
  personal or small-team, not obviously a budget holder.
- *Existing alternatives:* Excel/Power Query, Google Apps Script, Zapier,
  Power Automate — all cheap and widely known.
- *Why now:* none.
- *Defensibility:* very low — this is a scripting task, not a product.
- **Verdict: reject.** No identifiable economic buyer and no wedge.

---

## Leads considered and rejected outright

| Lead | Why rejected |
|---|---|
| Shopify admin workflow regressions (bulk editor, collections admin, order buttons) | Vendor-regression complaints; Shopify owns the fix; no standalone business. |
| Slack thread context loss (`dfeca6d7b2fd9658`) | Single developer comment; Slack owns the surface; no buyer. |
| Shared Exchange calendar CSV export limits (`4e37e1c0ed77e0e5`) | Microsoft owns the surface; niche; no budget evidence. |
| Shopify bot/fraud traffic threads | Real but served by a large fraud-tooling market; not our wedge. |
| "Double entry bookkeeping" philosophy cluster | Known-inflated commentary; not buyer pain. |
| GitHub agent digests | Auto-generated noise; excluded at source. |

---

## Honest summary

Of 564 signals, **only the Shopify merchant community produced genuine
buyer-side operational pain**, and it is concentrated in one community and
largely one author. The two leads with any real substance are:

1. **Lead B (Stocky sunset, Aug 2026)** — the only lead with a dated "why now",
   but probably a one-shot migration/services play.
2. **Lead C (channel fee tracking)** — plausible, structural, needs a check
   against existing payout-reconciliation tools.

Leads A, D and E are real pain but crowded or buyer-less. **None of these is a
validated idea, and none should be promoted to a Method candidate on this
evidence.** The honest next step is a cheap incumbent check on Leads B and C
before any further work.

*No source was accessed through authentication. No commits, pushes, issues or
PRs were made. This file is a lead list, not a Method decision.*

---

# Deep-dive addendum (2026-09-21)

Both leads flagged for a cheap incumbent check were checked. **Both failed the
check.** The findings are recorded here so they are not re-litigated.

## Lead B deep-dive — Stocky sunset (Aug 2026)

**Why-now confirmed, and it is the strongest in the corpus.** From Shopify's own
help centre (`help.shopify.com/en/manual/products/inventory/transitioning-from-stocky`):

- Stocky was **delisted from the Shopify App Store on 2 February 2026** and
  **stopped working on 31 August 2026**; its APIs are dark.
- Historical Stocky data (old purchase orders, stocktakes) does **not**
  automatically move into Shopify. **Suppliers cannot be exported from Stocky.**
  Historical purchase orders **cannot be imported** into Shopify — the native CSV
  upload only adds product line items to a *new draft* PO, so past PO statuses,
  received quantities and supplier links are lost.
- Read-only export was available for at least 90 days after sunset.

**But the market has already responded — at least 5–6 active competitors:**

| Competitor | Position | Pricing |
|---|---|---|
| Plenisher (apps.shopify.com/stockpile) | "Move off Stocky"; imports suppliers, costs, min/max and PO history "in a day" | Free ≤10k products, $19/mo |
| StockKit (launched 24 Jun 2026) | "StockKit replaces Stocky"; Stocky CSV migration tool | $14 / $39 / $79 per month |
| Katana | Free full Stocky migration + 30 days support (4–6 weeks) | Free migration |
| Finaloop / InventoryIQ | "Trusted by 2,500+ consumer brands" | Free consultation |
| Stok.ly | Inventory ERP; says Shopify native tools are "a genuinely sufficient, free replacement" for simple merchants | — |
| InvoRescue | The historical cost/lead-time data rescue (one-time fee, in-browser) | One-time |

Plenisher's reviews (July–August 2026) say *"the best one we've tried since
Stocky announced it was shutting down"* and *"I was desperately looking for an
alternative to Stocky, as this is retiring and it did all we needed for free"*.

**Two structural problems.** (1) The migration is **one-shot** — after 31 Aug
2026 the discontinuity is spent, so this is a services play, not recurring
software. (2) The remaining defensible slivers are narrow and partly taken: the
`supplier_cost_price` / `received_at` export gap was identified by a merchant
(`irish.chen`, 5 Aug 2026) and he **already built InvoRescue for it**.

**Verdict: not viable as a standalone new entrant.** Real, dated discontinuity;
window closed; market responded.

## Lead C deep-dive — marketplace / channel fee tracking

**The pain is real and recurring.** Two live community threads:

- `community.shopify.com/t/shopify-payments-fee-reporting/584201` (Jan–Aug 2026):
  fees are recognised by **payout date, not transaction date**, so month-end
  (especially Black Friday/Cyber Monday) shows high sales with low fees one month
  and high fees against low sales the next. *"Shopify Payments still reports on
  payout logic, not accounting logic."*
- `community.shopify.com/t/.../673400` (28 Aug 2026): month-end reconciliation
  between channel-reported sales and net revenue after fees/refunds/chargebacks
  *"eats the most time"*.

**Shopify's native tools genuinely do not close it.** The Payout reconciliation
report only works with Shopify Payments, excludes third-party processors and
Shopify billing fees, and is explicitly *"not a statement of revenue for
accounting purposes"*.

**But the market is saturated — at least a dozen established players:** A2X
(category leader), Webgility (18 yrs, 5,000+ operators, 30+ channels,
order-level reconciliation), Bookkeep (embedded in Shopify Admin, accrual daily
journals, multi-channel), Reconcile.ly (4.9 stars, Xero partner, real-time
payouts to Xero/QBO), Amaka (daily sync, fees mapped, payout matching),
TrueProfit (5.0 stars / 717 reviews, 70k installs, profit + COGS tracking), plus
2026 entrants Payout Close, Settly and Order Invoicer. Several have free tiers,
embedded admin apps, multi-channel coverage and 4.9–5.0 ratings. The specific
"channel fee not tracked because marketplaces deduct from payouts" complaint is
already addressed by Webgility / Bookkeep / TrueProfit.

**Verdict: not viable as a standalone new entrant.** Real, recurring,
buyer-backed pain; saturated market.

## Lead F — Shopify native Purchase Orders are "too limited" for real purchasing

**The one structurally different residual thread.** Unlike Lead B this is *not* a
one-shot migration, and unlike Lead C it is *not* the payout-accounting seam that
A2X/Webgility/Bookkeep own. It is the ongoing complaint that Shopify's native
Purchase Orders are a minimal ledger interface, not a purchasing workflow.

Evidence (all community.shopify.com):

- `:587146` "Why Stocky should remain — An executive position" (`rainline`,
  4 Feb 2026): *"Stocky should remain in use over Shopify native Purchase Orders
  because it supports real-world inventory operations, whereas Shopify POs are a
  minimal ledger interface designed for state capture, not o[perations]…"*
- `:630533` "New Purchase order Process" (`closecheck_retail`, 2 Jun 2026,
  engagement 11): *"What a cluster f\*\*\*. Just seems to have been launched on
  us. Lots of extra steps. Stupid need to indicate transfer from supplier to
  store. We have ordered the product, we load the purchase order, we receive it.
  Why ove[r]…"*
- `:682404` "Purchase Orders and Transfers" (`SealSubs-Roan`, 16 Sep 2026):
  *"Please make linked inventory transfers update automatically when new products
  are added to their purchase order. The current workflow requires duplicate
  manual edits."*
- `:682289` "How to turn low-stock data into a Purchase Order?" (`SealSubs-Roan`,
  15 Sep 2026): the low-stock → PO loop is *"opening an inventory report,
  checking low-stock items, manually calculating quantities, cross-referencing
  your supplier catalog, and entering everything into a…"*
- Community thread "Critical Improvements Required for Shopify Purchase Orders
  before the Stocky replacement on August 31 2026" (9 Jul 2026).

**Scrutiny.**
- *Economic buyer:* yes — the merchant or their ops lead, already paying for
  inventory apps.
- *Existing alternatives:* Shopify native POs (the thing being complained about),
  the Stocky-replacement apps above (Plenisher, StockKit, Katana, Stok.ly), and
  inventory ERPs. **Not yet checked in detail** whether any of them solves the
  *transfer/receive reconciliation* specifically rather than PO creation.
- *Why now:* **moderate and structural, not dated.** The Stocky sunset removed
  the free tool that used to absorb this, pushing merchants onto native POs they
  find inadequate — so the sunset is a *cause* of this pain even though the pain
  itself is ongoing.
- *Defensibility:* unknown; the seam is adjacent to the crowded inventory-app
  market, so the wedge would have to be the specific reconciliation/transfer
  workflow, not "another inventory app".
- *Cheap disconfirming test:* read the reviews of Plenisher / StockKit / Katana /
  Stok.ly for complaints about PO transfer/receive reconciliation; if those apps
  already handle it, this lead dies the same way as B and C.

**Verdict: the only lead that survives the first pass of scrutiny, and the only
one worth a further cheap check.** It is still single-source, still
unvalidated, and still not a Method candidate.

### Lead F incumbent check (the cheap disconfirming test) — FAILED

The test was: read the Stocky-replacement apps' own feature pages and reviews
for evidence that they already handle PO transfer/receive reconciliation. They
do.

**Plenisher** (`plenisher.ai/features`, `apps.shopify.com/stockpile`, page dated
12 Aug 2026) is a near-exact match for the Lead F seam:

- *"Plan, order, receive. One loop, closed."*
- *"Receive and reconcile — Receive POs in full or in parts. Every change is
  audited, and every cost is kept per supplier."*
- *"Partial receipts with full history. Every change audited, nothing silent."*
- *"Live two-way sync with Shopify across all your locations, including POS. One
  source of truth, no exports, no reconciling at midnight."*
- *"Stop rebuilding the same spreadsheet every week."*
- *"Everything Stocky does, free. Forever."* — free tier, Pro for new features.
- It even migrates *"Even the data the Stocky API doesn't expose"* (suppliers,
  codes, costs, min/max, full PO history, adjustment history).

Plenisher's own roadmap lists what is *not* yet built (demand forecasting,
accounting integrations, stocktakes with barcode scanning, "create & receive POs
from delivery notes, invoices and email") — i.e. the remaining gaps are already
publicly claimed and being worked.

**Katana** (`apps.shopify.com/katana-mrp-manufacturing-and-inventory-management`,
4.2 stars / 131 reviews) covers the multi-channel and manufacturing end:
purchase order management with reorder points, production scheduling, barcode
scanning for receiving, multi-location inventory, Shopify order sync. Its
reviews show the *opposite* problem to Lead F — merchants complain it is
**too expensive and repriced aggressively** (one 6-year customer left over
GMV-based tiers; another says the core plan "at around $299 a month" escalates
past $1,000 with add-ons). That is a pricing complaint, not a missing-feature
complaint.

**Conclusion.** The Lead F seam — low-stock → PO → transfer → receive
reconciliation — is **already served**, including the specific partial-receipt
and transfer-reconciliation workflow, by a free-tier incumbent that explicitly
targets Stocky refugees. Lead F dies the same way as B and C.

## Final outcome of the deep-dive pass

All three leads that survived the first pass (B, C, F) **failed the incumbent
check**. The corpus produced no viable standalone idea. This is a negative
result and is recorded as such: it is the honest output of the spike, and it
matches the SPIKE-REPORT's ITERATE verdict.

The one durable, transferable finding is the **pattern**: public-source
trawling at this scale surfaces *known, already-monetised* markets. Every seam
with real buyer pain had at least one mature incumbent, usually several, often
with a free tier. That is a property of the method, not of these particular
queries, and it is the thing to fix before spending more effort on collection.

## Pattern across the whole corpus

The trawl reliably finds **real buyer pain**, and real buyer pain is **already
monetised**. Every lead that survived the first pass died on the incumbent check
(B: 5–6 competitors incl. free tiers; C: a dozen mature players). The honest
conclusion is that public-source trawling at this scale surfaces *known* markets,
not *unserved* ones — which is consistent with the spike's ITERATE verdict.

*No source was accessed through authentication. No commits, pushes, issues or
PRs were made. This addendum is a lead list, not a Method decision.*
