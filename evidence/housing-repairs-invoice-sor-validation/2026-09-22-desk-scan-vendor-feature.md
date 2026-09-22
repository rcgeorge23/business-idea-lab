# Desk scan: invoice-to-SOR validation feature in housing-management vendors

- **Idea:** housing-repairs-invoice-sor-validation
- **Date:** 2026-09-22
- **Run:** 20260922T090448Z-normal
- **Test:** the pre-fixed cheapest decisive experiment from `ideas/housing-repairs-invoice-sor-validation/dossier.md`
- **Cost:** GBP 0, ~2 human hours, same day (within the 4-hour / 7-day bound)
- **Method:** desk-only web search of housing-management vendor product pages and release notes. No outreach, no contact, no spend.

## Pre-fixed decision rule

> **Proceed** to interview design only if the desk scan finds no shipped or announced invoice-to-SOR validation feature from any housing-management vendor; **stop** if any vendor has shipped or announced one.

## Vendors checked

| Vendor | What it does with invoices | Invoice-to-SOR validation? |
| ------ | -------------------------- | -------------------------- |
| **MYRO** (Visionbase) | Tracks the full lifecycle "Report → Triage → Approve → Assign → Complete → **Invoice** → Close"; attaches invoices to the job; tracks payment status; "Repair Cost by Contractor" reporting; budget monitoring; "Bills Paid and Outstanding" | **No.** It records and reports the invoice; it does not validate invoice lines against the SOR rate book |
| **Fixflo** | "Manage works orders more efficiently and ensure the right costs are applied to the contractor and job type using your schedule of rates" | **No.** Applies SOR to works-order costing, not inbound invoice validation |
| **Oneserve** | Scheduling, dispatch, mobile working, resident communications, contractor supply chain; Capterra lists Billing & Invoicing as a feature | **No.** No invoice-validation feature found |
| **Aareon** (QL; 250+ providers) | Cloud-native, AI-powered housing management; "AI-first ecosystem"; housing management, tenant self-service, mobile working, private housing solution | **No.** No invoice-validation feature announced; AI positioning is general |
| **SDM Housing** | Purchase ledger, sales ledger, nominal ledger, fixed asset register; MTD-compliant VAT; "insert invoices, purchase orders, credit notes" | **No.** Accounting modules, not invoice-to-SOR validation |
| **Dwellant** | Invoice Processing Application (IPA) with S20 spending warnings: "If they are set property managers will be warned when raising a work order or approving an invoice if the limit is breached" | **No.** A threshold alarm on the invoice total, not line-level SOR validation |
| **Landlord Vision** (social housing) | "Statement lines automatically matched with invoices and payments"; "Manual reconciliation for unmatched transactions"; "Reconcile lump sum payments across multiple invoices" | **No.** Generic bank-statement reconciliation, not SOR-specific |
| **CHICS** | Repairs & maintenance, contractor portal, "raise invoices" | **No.** No invoice-validation feature found |
| **MRI Greentree** | Repairs lifecycle "right through to invoicing and customer satisfaction" | **No.** No invoice-validation feature found |
| **Ingentive** (Dynamics 365) | "Assists accounts payable teams with invoice processing, supplier payment queries and reconciliation workflows" | **No.** An integration service, not a SOR-specific product |
| **Plentific** (via FlowRunner) | Compares the invoiced amount to the approved quote and the closing state of the work order; separates mismatches | **No.** Compares to the approved quote, not the versioned NHF rate book |

## Outcome

**No housing-management vendor has shipped or announced invoice-to-SOR validation.** The pre-fixed rule therefore says **proceed**.

## Honest caveats

1. **The scan is a point-in-time desk check, not proof of absence.** Vendor release notes are not all public, and a feature could exist behind a demo or in a roadmap not published on the website. The negative finding is weak evidence.
2. **The incumbents are one release away.** MYRO's lifecycle already reaches invoice closure and contractor cost reporting; Aareon is explicitly "AI-first"; Ingentive already markets AP reconciliation assistance. The seam is unoccupied *today*, not structurally protected.
3. **The closest adjacent capability is Dwellant's S20 threshold warning** — a total-level alarm, not line-level validation. That is the shape a suite vendor would most cheaply add.
4. **The buyer's revealed preference remains headcount.** Brighton & Hove added quantity-surveying resource; Winchester added process notes and training. Neither bought software. The desk scan does not change that.

## Implication for the candidate

The `defensible_wedge` hard filter moves from `unknown` toward `pass` on the narrow ground that no vendor demonstrably occupies the exact seam — but the filter should stay `unknown` rather than `pass`, because the evidence is a negative desk finding rather than affirmative evidence of a durable wedge, and the feature-absorption risk is documented. The candidate remains parked at desk-screened below threshold (58.9/100).

The next step, if the owner wants to continue, is a small number of interviews with repairs finance managers (requiring owner approval under `method/experiment-rules.md`). The interview would test the central assumption directly: would the provider buy a standalone check, or wait for its suite vendor?

## Boundaries

No commits, pushes, issues, pull requests or publication. No contact with any person. No money spent. No external accounts. No commitments. Desk research only.
