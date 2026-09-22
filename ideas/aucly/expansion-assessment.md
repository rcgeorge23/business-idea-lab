# Aucly — locale expansion assessment (Ireland, US, Australia, New Zealand)

- **Idea / slug:** `aucly`
- **Question (owner-directed, 2026-09-22):** assess the business value of expanding
  Aucly into another locale — Ireland, the US, Australia or New Zealand — including
  cost, benefit, different market conditions and different regulation.
- **Run:** `20260922T100404Z-normal` · **Date:** 2026-09-22 · **Method version:** 1.8.0
- **Status of this document:** a scoped assessment of a *variant* of an existing
  idea. Per `method/discovery.md` duplicate rules it does **not** create a new
  ledger candidate (same buyer, same problem, same mechanism — only geography
  changes). It therefore leaves `ideas/index.json`, `scorecard.json` scores and
  recorded hard filters **unchanged** and adds no inherited evidence level.
- **Evidence:** `evidence/aucly/2026-09-22-locale-market-and-incumbents.md`,
  `evidence/aucly/2026-09-22-locale-regulation-and-tax.md`, plus the existing
  `evidence/aucly/2026-09-21-*` files.

---

## 1. Bottom line

**Do not expand now.** The evidence does not support expansion into any of the four
locales, and the decisive reason is not cost or regulation — it is that the binding
constraint on Aucly is **unpaid demand, which is still unsolved in the home market**.

- Aucly's measured home distribution is **inconclusive, not proven negative**: a
  recorded window of 2,333 visitors produced 0 accounts, 0 auctions and £0
  revenue, but the owner states that traffic is **largely bots** — the
  application counter is ~18x Cloudflare's bot-filtered 130 visits — so human
  reach is **unmeasured** and the channel is effectively untested (Evidence:
  `evidence/aucly/2026-09-21-seo-and-acquisition.md`,
  `evidence/aucly/2026-09-22-acquisition-bot-correction.md`).
- Every locale examined already has **free or low-cost incumbents aimed at exactly
  this segment** — free-for-NZ-schools (Toko), zero-platform-fee (Fundraising
  Solutions, IE), free-with-tips (GalaBid, AU/NZ), and a free tier plus
  US$79/event option (Auctria, SchoolAuction.net, US).
- Entering a new locale resets domain authority, case-study relevance, email
  deliverability and word-of-mouth to **zero**, and multiplies the unsolved channel
  problem rather than addressing it.
- If, and only if, a repeatable unpaid route is proven at home, the evidence
  ranks the locales **Ireland first (cheapest discriminating probe), then
  Australia, then New Zealand, then the US** — see §7.

The genuine first-order question remains the one already recorded:
`experiments/aucly-channel-test/plan.md`.

---

## 2. Scope and method note

- This is a desk assessment. No outreach, no accounts, no spend, no publication
  was performed.
- Cost figures that are not drawn from a dated source are labelled **inference** or
  **assumption** and are excluded from scoring; modelled revenue is labelled as
  modelled and is not evidence (`method/evidence-policy.md`).
- The hard-filter table in §6 assesses the **expansion proposition**, not the
  recorded `aucly` idea. It is deliberately **not** written into
  `scorecard.json`, because doing so would silently overwrite the recorded parent
  idea's filter statuses. The parent idea's recorded filters (3 `pass`, 4
  `unknown`, 0 `fail`) stand unchanged.
- No score changed. `aucly` remains `adversarially-researched`, 60.0, threshold not
  met. See the 2026-09-22 entry appended to `ideas/aucly/decision.md`.

---

## 3. Market conditions compared

| Dimension | UK (home, baseline) | Ireland | Australia | New Zealand | United States |
|---|---|---|---|---|---|
| Schools | 24,499 (DfE 2025/26) | ~3,788 (3,067 primary + 721 post-primary) | 9,673 (ABS 2025) | 2,536 (Education Counts, 1 Jul 2025) | 99,297 public (NCES SY2023–24) |
| Language / legal family | English, common law | English, common law, closest to UK | English, common law | English, common law | English, common law, state-by-state |
| Relevant incumbents | Jumblebee, PTA Events, GalaBid, Givergy, Generosity Works | Fundraising Solutions (zero platform fee), iDonate.ie, FundRaisely.ie, GalaBid ROI | GalaBid (dominant, ~1,000 events/yr AU+NZ), AirAuctioneer, Oktion | Toko (100% free for NZ schools), Raised, GalaBid | Auctria (free tier), SchoolAuction.net (from US$79/event), GalaBid, plus the wider US gala market |
| Free / very-low-cost option for this buyer? | Partly (GalaBid free plan, beeFree) | Yes — zero platform fee | Partly — free-with-tips | Yes — free for schools | Yes — free tier |
| Price pattern an entrant must beat | £60/£120 flat (Aucly) | £0 platform fee; low txn fees | 4.9% or US$1,250/campaign; free-with-tips | 5% for associations; free for schools | Free; US$79/event + 3%; US$375–2,000/yr |
| Market-size verdict | — | Too small to matter on its own | Moderate | Smallest | Largest, but most crowded |
| Demand evidence **specific to the locale** | Real auctions (Furzedown, Lingfield) | None found | None found | None found | None found |

**Reading of the table.** Market size is not the constraint: the US is ~4× the UK
in schools and yet is the hardest entry; Ireland is ~15% of the UK and is the
easiest. The constraint that repeats in every column is a **free or near-free
incumbent serving the same buyer**, and the absence of any locale-specific
evidence that organisers are dissatisfied with them.

---

## 4. Regulation and tax compared

Full citations are in `evidence/aucly/2026-09-22-locale-regulation-and-tax.md`.

| Issue | Ireland | Australia | New Zealand | United States |
|---|---|---|---|---|
| Indirect tax on the service | **Worst early burden.** A UK (non-EU) seller cannot use the Union OSS and must charge **destination (Irish) VAT from the first sale**, filing via Non-Union OSS or per-state registration; Ireland standard VAT 23% | GST at 10% once GST turnover connected with Australia is **A$75,000+** (A$150,000 non-profit); simplified registration; business-recipient supplies excluded | GST once supplies to NZ customers are **NZ$60,000+**; business-recipient supplies excluded | State sales tax; economic nexus typically **US$100,000** per state (higher in AL/MS/CA/NY/TX); SaaS taxable in many states |
| Privacy | GDPR applies to EU data subjects; UK controller with no EEA establishment must **appoint an EEA representative (Art 27)** | Privacy Act small-business exemption (≤A$3m turnover) **still in force as at Sep 2026** — lightest touch | **Privacy Act 2020: no small-business exemption**, applies to overseas agencies carrying on business in NZ through online activity; privacy officer required — heaviest touch relative to size | State privacy laws with thresholds; no federal omnibus; less burden at low volume |
| Fundraising / charity | Charities Regulator guidelines; third-party fundraising agents need written contracts; Gambling Regulation Act 2024 charitable licence not expected to open in 2026 | State fundraising rules vary | Charities Services registration; fundraising rules | **~41 states + DC require the organising charity to register before soliciting**; a silent auction counts as solicitation; fees US$25–300/state |
| Electronic marketing | Irish ePrivacy / DPC charity guidance | **Spam Act 2003**: consent, identification, unsubscribe within 5 business days; rising penalties | UEMA | CAN-SPAM |
| Net early-stage regulatory friction | **Highest** (VAT from sale 1) | Low (below GST threshold) | Medium (below GST threshold, but privacy has no de minimis) | Medium at low volume, **highest at scale** (multi-state tax + solicitation patchwork) |

**Two practical points that matter more than the table:**

1. **Indirect tax only bites once money moves.** A demand probe that uses Aucly's
   free tier incurs no VAT/GST/sales tax at all, so regulation does not block a
   cheap test — it only raises the cost of *success*.
2. **The US compliance tail is the worst because it is many-jurisdiction, not
   one-jurisdiction.** Charitable-solicitation registration sits on the organising
   charity (not the platform), but a platform that makes cross-state targeting
   easier inherits an argument that it is facilitating unregistered solicitation —
   a sales objection as much as a legal one.

---

## 5. Cost to expand (itemised)

Costs below are **inferences/assumptions** unless a source is cited; they are not
scored and are indicative only.

| Cost item | Ireland | Australia | New Zealand | United States |
|---|---|---|---|---|
| Localised landing pages / copy | Low (English; minor spelling/terminology) | Low | Low | Medium (US spelling, 501(c)(3)/PTA-PTO vocabulary) |
| Local currency pricing + Stripe multi-currency | Low (product work; Stripe supports all four) | Low | Low (note: incumbents use Windcave) | Low–medium (USD price points to design) |
| Domain / brand presence (e.g. `aucly.ie`) | ~£10/yr + content | ~£10/yr + content | ~£10/yr + content | ~£10/yr + content |
| Indirect-tax registration & filing | Medium (Non-Union OSS from first paid sale) | Low until A$75k | Low until NZ$60k | Medium–high at scale (per-state) |
| Privacy compliance | Medium (EEA representative) | Low (exemption in force) | Medium–high (no de minimis; privacy officer) | Low at low volume |
| Terms/legal review per locale | Medium | Medium | Medium | High (state patchwork) |
| Email deliverability warm-up + sender domain | Medium (starts near zero each locale) | Medium | Medium | Medium |
| Support hours (timezone) | Low (UTC/IST ≈ UK) | High (+8–11h) | High (+12–13h) | High (−5 to −8h) |
| Content/SEO ramp (new domain authority) | High effort, historically negative at home | High | High | Very high |
| **Dominant real cost** | Founder time + opportunity cost | Founder time + timezone | Founder time + timezone | Founder time + compliance complexity |

**One-off / recurring money cost (inference):** low four figures per locale up front
and low hundreds per year, *excluding* founder time. The binding cost is that
Aucly is founder-operated: every hour spent on a locale is an hour not spent on the
one measured failure (unpaid acquisition at home).

---

## 6. Benefit analysis

### 6a. What the revenue could plausibly be (modelled illustration — not evidence)

At Aucly's Unlimited price of £120 per paid auction, assuming (optimistically) **1%
of schools in the locale run one paid auction per year through Aucly, with zero paid
acquisition cost**:

| Locale | Schools | 1% penetration × £120 | 5% penetration × £120 |
|---|---|---|---|
| Ireland | ~3,788 | ~£4,546/yr | ~£22,728/yr |
| New Zealand | 2,536 | ~£3,043/yr | ~£15,216/yr |
| Australia | 9,673 | ~£11,608/yr | ~£58,038/yr |
| United States | 99,297 | ~£119,156/yr | ~£595,782/yr |
| UK (for contrast) | 24,499 | ~£29,399/yr | ~£146,994/yr |

These are **modelled**, assume 1%/5% unpaid capture (itself unfounded — the UK
home market yielded 0 accounts against a largely non-human visitor count, so it
has no demonstrated repeatable channel), and ignore the free tier (most
organisers would use it). They are included only to show the shape of the
opportunity, not as a valuation.

### 6b. The decision-relevant observation

The UK 5% column (~£147k) is larger than Ireland, New Zealand and Australia at 1%
combined. **Geography is not the bottleneck; the channel is.** Solving unpaid
acquisition in the UK is worth more than any of these expansions, and the same
solution would then be portable. Expansion before that is spending the scarce
resource (founder time) on a market where the same channel failure will repeat,
with new regulatory cost layered on top.

### 6c. Where expansion could still add value

- **Portable proof.** If a locale converted *without* a UK track record, that would
  be strong evidence the product sells itself and the UK failure is market-specific
  (e.g. UK incumbent entrenchment). That is worth knowing — but it is a test to run
  cheaply, not an expansion to fund.
- **Adjacent-segment spillover.** None evidenced; UK case studies (Furzedown) do not
  transfer to non-UK organisers.

---

## 7. Ranked recommendation (if expansion is pursued at all)

Ordered by evidence-weighted attractiveness for a founder-operated, cash-constrained
business:

1. **Ireland — best first probe, weakest standalone business.** Highest similarity
   to the UK (English, common law, comparable school/PTA culture, brand/TLD
   adjacency) makes it the cheapest way to test whether the UK failure is
   market-specific. But it is ~3,788 schools with zero-platform-fee incumbents and
   the worst early indirect-tax rule (VAT from the first paid sale).
2. **Australia — best standalone economics of the non-US options, higher cost.**
   9,673 schools, a Privacy Act exemption that keeps compliance light, and GST only
   above A$75k. But GalaBid is entrenched (~1,000 events/yr AU+NZ) and the timezone
   imposes real support cost.
3. **New Zealand — smallest market, free incumbent, heaviest privacy burden.** Toko
   is explicitly free for NZ schools; the Privacy Act 2020 has no small-business
   exemption. This is the least attractive jurisdiction examined.
4. **United States — largest prize, worst risk-adjusted entry.** ~99,297 public
   schools, but a free tier (Auctria) and US$79/event option (SchoolAuction.net)
   already serve this exact buyer, plus multi-state sales tax and a ~41-state
   charitable-solicitation patchwork. Not a bootstrapper's first locale.

**Recommendation: none of the four now.** Keep the option open; revisit only after
the home channel question is answered.

---

## 8. Cheapest decisive experiment (proposed, not run)

**`aucly-ireland-demand`** — a zero-spend discriminating probe.

- **Central assumption it could disprove:** that unmet demand exists in Ireland for
  a flat-fee, no-commission self-service auction tool despite free/low-cost
  incumbents.
- **Method:** approach **20 Irish primary-school PTAs** outside any existing
  network with a locally relevant case study and free-tier setup help; measure real
  auctions launched within 30 days at **zero paid spend**.
- **Proceed if:** ≥2 of 20 launch a real auction within 30 days.
- **Kill if:** 0 launch, or the dominant objection is that a free platform already
  satisfies them.
- **Cost bound:** £0 (free tier avoids all indirect tax), ~20 human hours, 30 days.
- **Dependency (important):** run this **only after or alongside**
  `aucly-channel-test`. If the UK test also fails, the conclusion is a channel
  problem, not a geography problem, and expansion is unsupported. If the UK test
  succeeds, the Ireland probe's marginal value is small. Its real value is the
  case where UK fails *and* Ireland succeeds.
- Plan: `experiments/aucly-ireland-demand/plan.md`.

---

## 9. What would change this conclusion

- A repeatable unpaid acquisition channel demonstrated in the UK (via
  `aucly-channel-test`), which would make portability worth funding.
- Evidence that organisers in a locale are *dissatisfied* with the free incumbent
  (e.g. support-forum complaints, migration away from Toko/Fundraising Solutions),
  which would replace "competitor exists" with "competitor unsatisfying".
- A locale-specific regulatory discontinuity that favours the flat-fee model (none
  found; all changes identified add cost rather than remove it).
- A partner/distributor route that removes the cold-start distribution cost
  (none evidenced).

## 10. Limits of this assessment

- No locale-specific demand evidence exists; this is a desk assessment of market
  structure, incumbents and regulation only.
- Cost figures are indicative inferences, not quoted prices or accountant/legal
  advice.
- The revenue illustration depends on an assumed penetration rate that is not
  evidenced and should not be used as a forecast.
- Aucly's own codebase could not be inspected in this repository (the
  `/home/richard/projects/aucly-micronaut` path is outside the permitted
  workspace), so localisation *implementation* cost is estimated, not measured.
