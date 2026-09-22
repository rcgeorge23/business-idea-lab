# housing-repairs-invoice-sor-validation

- **ID / slug:** housing-repairs-invoice-sor-validation
- **Industry:** `property-lettings`
- **State:** desk-screened
- **Evidence level:** Promising
- **Owner:** human owner
- **Created:** 2026-09-22
- **Updated:** 2026-09-22
- **Source:** observation O1 of run 20260922T090448Z-normal (money-already-moving sourcing frame, method 1.8.0); promoted after the triage false-negative audit overturned the original rejection

> **One-sentence proposition:** A provider-side check that reads a contractor's repairs invoice, extracts the Schedule of Rates codes and quantities, and validates them against the works order and the versioned NHF rate book before payment — catching the overcharges that housing providers currently employ people to find.

## Why now?

> This was not an attractive business three years ago, but it might be now because document and LLM processing has become cheap enough to read an unstructured contractor invoice and check it line-by-line against a rate book, at a cost below the salaried reconciliation work it replaces.

- **What changed:** The cost of extracting structured line items from an unstructured invoice (photo, PDF, docket) and matching them against a reference rate set has fallen sharply with current document/LLM tooling. Rentari.ai has already productised the mechanism for the US market (live "AI Invoice Check for Repairs").
- **When it changed:** 2025–2026 (Rentari.ai invoice check live as of 2026; the capability is current, not speculative).
- **Evidence (dated source):** `evidence/housing-repairs-invoice-sor-validation/2026-09-22-repairs-invoice-sor-evidence.md` — Rentari.ai product page (accessed 2026-09-22); Winchester CAB3557(H) (2026-07-06); NLM policy (2026-03).
- **Why this materially improves the opportunity now:** The check is only economic if reading an invoice costs less than the human time it saves. That threshold has now been crossed.
- **Have competitors already responded?** **Partly.** Rentari.ai has productised the mechanism in the US (per-unit pricing, 50-state/HUD focus). No UK provider-side SOR-specific product was found. Joblogic, Automio and Estimark sell SOR software but contractor-side. Fixflo applies SOR to works-order costing. Plentific compares invoices to the approved quote, not the rate book.
- **Strength:** `weak` — the capability change is real and dated, but it is a general capability shift rather than a specific market discontinuity, and a competitor has already moved on the mechanism in another geography.
- **Archetype:** `persistent market failure` (with a weak change-driven component from the capability shift).

### Persistence thesis (archetype B)

- **Limb 1 — continued pain or workaround despite alternatives that exist and are reachable for this buyer:** **pass.** Housing providers still employ dedicated reconciliation staff (St Mungo's GBP 34,116–38,115; Together Housing; Onward Homes GBP 29,400; Houghton Group GBP 30,000–32,000) and their own written policies mandate a manual invoice-to-works-order check (NLM, 2026-03). Council audits keep finding the control failing: Winchester found a backlog and delay authorising invoices, no cost breakdown on large work orders, and 25 properties with indications of duplication (2026-07-06); Brighton & Hove found ~GBP 300,000 of overcharging from five SOR codes charged for materials not fitted. The workaround persists despite the housing-management systems of record being available and reachable.
- **Limb 2 — a credible present-tense mechanism explaining why the market has not adequately resolved the problem for this segment:** **pass (moderate).** The systems of record (Orchard, QL, EBIS, Documotive) are owned by housing-management vendors whose product is workflow and compliance evidence, not invoice validation; the SOR software market is contractor-side because the contractor is the party who prices the invoice; and the provider-side check has historically been cheaper to staff than to automate. The recent fall in document-processing cost is what changes that calculus.
- **Net thesis quality:** `weak` — both limbs are supported by cited evidence, but limb 2 is an inference about vendor incentives rather than a documented statement, and the "recent fall in build cost" is a general capability shift. The thesis is strong enough to lift the missing-why-now cap, but only just.

## Buyer

- **Who pays:** the housing provider's repairs and maintenance finance function — specifically the Head of Landlord Services / Repairs and Maintenance Manager who owns the audit action plan, or the Finance/Assets director who signs off the invoice-authorisation control. In a contractor-side variant, the contractor's commercial manager.
- **Who uses it:** the reconciliation administrator / finance officer who currently performs the check, and the Head of Assets who gives final authorisation.
- **Evidence:** Winchester CAB3557(H) names the Head of Landlord Services and Repairs and Maintenance Manager as owning the action plan; NLM's policy names the Finance Officer and Head of Assets; the job ads name the reconciliation administrator role.

## Problem

- **What is painful, frequent or expensive:** every contractor repairs invoice must be checked against the works order and the Schedule of Rates before payment. The check is manual, recurring (every invoice, every month), and demonstrably fails: Winchester's audit found a backlog and delay in authorising invoices, no cost breakdown on large work orders, and 25 properties with indications of duplication; Brighton & Hove found ~GBP 300,000 of overcharging from five SOR codes; Circle Housing Merton Priory admitted overcharging and hired Savills to investigate.
- **Current alternatives and their weaknesses:** the housing-management systems of record (Orchard, QL, EBIS, Documotive) hold the works orders but do not validate the invoice against the rate book; the SOR software market (Joblogic, Automio, Estimark) is contractor-side; Fixflo applies SOR to works-order costing, not inbound invoice validation; Plentific compares invoices to the approved quote, not the SOR code and rate; Ingentive's AP assistance is a Dynamics 365 integration service. The practical alternative is to employ a person.
- **Evidence:** the evidence register above.

## Mechanism / wedge

- **What we would actually do:** read the contractor's invoice (photo, PDF or docket), extract the SOR codes, quantities and rates, and validate each line against (a) the works order raised in the provider's system, (b) the versioned NHF Schedule of Rates rate set with the client's agreed uplift, and (c) the contractor's own history on that code. Flag mismatches, missing codes, duplicate charges, variations not recorded on the works order, and materials charged but not fitted. Human approves or queries; nothing is auto-rejected.
- **Why it is defensible against the cheapest credible incumbent:** the incumbent systems of record are workflow tools whose vendors have no incentive to build a provider-side check that disputes their own contractor customers' invoices; the SOR software vendors sell to the contractor, not the provider; and the check requires the provider's works-order data plus the versioned rate book, which is a data-integration position rather than a feature. **However**, Rentari.ai has already built the mechanism (US), and a housing-management vendor could add it as a feature. The wedge is narrow.
- **Evidence:** the evidence register above.

## Novelty / incumbent sanity check

| Check | Finding | Evidence |
| ----- | ------- | -------- |
| 1. Does this exact product already exist? | **Partly.** Rentari.ai "AI Invoice Check for Repairs" performs the mechanism (invoice → line extraction → compare to accepted quote and contractor history → flag). It is US-focused and compares against the quote, not the NHF rate book | Rentari.ai product page, accessed 2026-09-22 |
| 2. Are there multiple credible providers? | **No** for the UK provider-side SOR-specific check. The SOR software market is contractor-side (Joblogic, Automio, Estimark); Plentific compares to the quote | Joblogic, Automio, Estimark, FlowRunner/Plentific |
| 3. Is the proposed wedge already a standard feature of an incumbent? | **Not yet found.** Fixflo applies SOR to works-order costing; Ingentive markets AP reconciliation assistance as an integration service. No standard invoice-to-SOR validation feature found | Fixflo, Ingentive |
| 4. Is an authoritative or free alternative already adequate? | **No.** The alternative is a salaried employee; there is no free tool | NLM policy, job ads |
| 5. Has a well-capitalised company already shown the unit economics are hostile? | **No evidence either way.** Rentari.ai is a small US entrant, not a category leader demonstrating hostile economics | — |
| 6. Is this merely a feature of an established category rather than a standalone product? | **This is the central risk.** It could be a feature of the housing-management suite rather than a standalone product | Fixflo, Ingentive, Plentific |

**If any check fails, state the reason to continue anyway:** checks 1 and 6 are the material risks. The reason to continue is that the UK provider-side SOR-specific check is unoccupied, the pain is documented by council audits, and the buyer already spends GBP 29,000–38,000/year on staff to do it — so a product that costs less than the staff has a clear value proposition. The candidate proceeds to desk screening with these risks recorded, not resolved.

## Distribution

- **Route to the first 10 buyers without paid acquisition:** UK social housing is a defined, reachable segment (hundreds of registered providers, plus local-authority housing and ALMOs). Routes: the sector's own audit and finance networks (the Southern Internal Audit Partnership and other internal-audit partnerships publish findings); the Chartered Institute of Housing and the National Housing Federation; the repairs-and-maintenance manager community; and the contractors themselves (Mears, Wates, Houghton Group) who are already paying for quantity-surveying resource to resolve disputes. A council audit finding of an invoice-authorisation backlog is a warm, dated trigger.
- **Evidence:** Winchester CAB3557(H) (audit findings and named owners); Brighton & Hove (Mears paying for additional QS resource); Houghton Group job ad (contractor-side commercial administrator).
- **Confidence:** low — the channels are plausible but no prospect has been produced.

## Economics (assumptions labelled)

- **Price hypothesis (assumption):** GBP 500–2,000/month per provider depending on invoice volume, or a per-invoice price of GBP 0.50–2.00. Anchored on the cost of the salaried role it replaces (GBP 29,000–38,000/year fully loaded) and on the outsourced-bookkeeping per-transaction benchmark (GBP 0.50–2.00).
- **Cost drivers (assumption):** document/LLM processing per invoice; integration with the provider's works-order system (Orchard, QL, EBIS, Documotive) or a CSV/export bridge; the NHF rate book is a paid subscription held by the provider (M3 Housing sells it to social landlords, not to contractors), so the product would consume the provider's own licensed rate set rather than redistribute it.
- **Contribution margin at realistic scale (assumption):** unknown. Modelled only.
- **Evidence:** job-ad salary bands; outsourced-bookkeeping pricing; M3 Housing SOR subscription terms.

## Founder fit

- **Reach:** unknown — no evidence about the founder's access to UK social-housing finance teams.
- **Skills:** the mechanism is buildable with current document/LLM tooling; the harder part is the works-order integration and the sector's procurement.
- **Motivation:** unknown.
- **Evidence:** none. Recorded as null.

## Adversarial case (strongest case this is wrong)

**This is a feature, not a product, and the buyer will not buy it separately.**

1. **The systems of record will absorb it.** Fixflo already applies SOR to works-order costing; Ingentive already markets AP invoice-processing assistance; Plentific already reconciles invoices against approved quotes. Any of them can add invoice-to-SOR validation as a feature of a suite the provider already owns. A standalone product would be competing against an incumbent's roadmap.
2. **The buyer's revealed preference is headcount, not software.** Brighton & Hove's response to a GBP 300,000 overcharge was to have Mears pay for an additional quantity-surveying resource. Winchester's response was process notes, training and contract terms. Neither bought software. That is direct evidence of the buyer's actual behaviour.
3. **The mechanism is already productised elsewhere.** Rentari.ai has built exactly this for the US market. If the mechanism were the hard part, that would be a moat; since it is not, the moat has to be UK-specific data (the NHF rate book, the works-order integrations) — which is a services/integration position, not a product.
4. **The sector's procurement is slow and framework-bound.** Housing providers buy through frameworks and long contracts; a small entrant has no route in without framework status.
5. **The rate book is licensed to the provider, not the vendor.** M3 Housing sells the NHF Schedule of Rates to social landlords and explicitly states contractors and consultants cannot buy it directly. A vendor cannot redistribute the rate set; it must consume the provider's own licence, which makes the integration bespoke per customer.

**Why it survives (for now):** the UK provider-side SOR-specific check is genuinely unoccupied, the pain is documented by primary council audits, and the buyer already spends GBP 29,000–38,000/year on staff. The adversarial case is strong enough that this candidate should **not** advance past desk screening without a cheap test of whether a provider would buy a standalone check rather than wait for its suite vendor to add one. The central assumption is exactly that.

## Strongest supporting case

A dated council audit found the invoice-authorisation control failing (backlog, no cost breakdown, 25 properties with duplication indications); a second council found GBP 300,000 of overcharging from five SOR codes; a housing association's own policy mandates a manual check; and providers pay GBP 29,000–38,000/year for staff to do it. The UK provider-side SOR-specific validation seam is unoccupied, and the capability to build it has just become cheap.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
| ---------- | ------------------------- | ------ |
| A provider would buy a standalone invoice-to-SOR check rather than wait for its suite vendor | Ask providers whether they have ever evaluated or bought such a tool; check housing-management vendor roadmaps/release notes | unresolved |
| The check can be built without redistributing the licensed NHF rate book | Confirm M3 Housing's terms allow a vendor to consume a provider's licensed rate set | unresolved |
| The works-order integration is feasible without bespoke work per provider | Test against one provider's system (Orchard, QL, EBIS) | unresolved |
| The economics work at GBP 500–2,000/month per provider | Model against invoice volume and processing cost | unresolved |
| The buyer is reachable without paid acquisition | Identify a non-paid channel that produces a conversation | unresolved |

## Cheapest decisive experiment

- **Assumption under test:** a UK housing provider would buy a standalone provider-side invoice-to-SOR validation check rather than wait for its housing-management suite vendor to add one.
- **Proposed test:** 30-minute semi-structured interviews with 5 repairs finance managers / Heads of Landlord Services at UK housing providers. No demo, no pricing sheet, no commitment request. Questions cover how invoices are validated today, who does it and how long it takes, whether the control has failed, whether they have evaluated a tool, what they would do if a standalone check existed, and who approves the purchase.
- **Pre-fixed decision rule:** **proceed** iff ≥2 of 5 describe an active budgeted intent to buy a standalone check or a current paid workaround they would replace; **iterate** if exactly 1 of 5 or the dominant answer is "we would wait for our suite vendor"; **stop** if 0 of 5 or the dominant answer is "this is a feature, not a product".
- **Cost bound:** GBP 0, 12 human hours, 21 calendar days.
- **Status:** proposed — `experiments/housing-repairs-invoice-sor-buyer-wedge/plan.md`. **Requires owner approval before any contact.** No contact, spend or publication until `approval.granted` is recorded.

### Desk scan (completed 2026-09-22)

The first, cheaper step of this experiment has already been run: a desk-only scan of 11 housing-management vendors found **no vendor that has shipped or announced invoice-to-SOR validation**. The pre-fixed rule said proceed. See `evidence/housing-repairs-invoice-sor-validation/2026-09-22-desk-scan-vendor-feature.md`.

## Decision log (append-only)

| Date | State change | Why | Link |
| ---- | ------------ | --- | ---- |
| 2026-09-22 | (none) → discovered | Promoted from observation O1 of run 20260922T090448Z-normal after the triage false-negative audit overturned the original rejection | `ideas/housing-repairs-invoice-sor-validation/decision.md` |
| 2026-09-22 | discovered → desk-screened | Hard filters applied; no fail; evidence register written; adversarial pass recorded | `ideas/housing-repairs-invoice-sor-validation/decision.md` |
