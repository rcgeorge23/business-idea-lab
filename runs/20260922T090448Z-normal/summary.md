# Run summary: 20260922T090448Z-normal

- **Mode:** normal
- **Started / finished:** 2026-09-22 (single worker session; `LAB_RUN_ID` was unset, so the run id is the UTC timestamp at run start)
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.8.0
- **Input revision:** uncommitted (working tree carried the v1.8.0 method change)
- **Output revision:** uncommitted
- **Status:** success

This run is the **sourcing-frame run** requested by the owner ("Ok we need some
more ideas to put through the lab" → "a please"). It exercises the new
money-already-moving sourcing bias introduced in method 1.8.0 and re-checks the
seed register.

## Seed register review

12 seeds: 1 dropped, 2 promoted, 9 unexplored. All nine unexplored seeds were
reviewed at index level; four were shallowly re-checked against current public
evidence.

| Seed | Shallow re-check result | Action |
| ---- | ----------------------- | ------ |
| `prs-self-managing-landlord` | **Weakened.** The PRS Database opens 2026-12-15 at GBP 65 per property per year with a three-month regional window and all landlords registered by 2027-11-14 (Property Week 2026-09-09; The Independent Landlord 2026-09-19). But the government's own trial (about 300 landlords, LandlordZONE 2026-08-05) found most register a property in five to ten minutes, and MHCLG has pledged to reduce duplicate data entry. The landlord's own task is small and the register is free apart from the statutory fee | Keep unexplored; the consumer buyer still has no evidenced willingness to pay for help with a five-minute task |
| `prs-listing-precheck` | **Weakened.** The professional channel is served (a GBP 29/month flat unlimited-properties PRS compliance platform with CSV import; lettings platforms integrating with agency CRMs). No bulk-upload/API gap confirmed as a product | Keep unexplored |
| `clinic-legacy-managed-archive` | **Unchanged.** No new evidence gathered this run; the seed's own open question (who pays at small-clinic tier) remains unanswered | Keep unexplored |
| `land-control-data-intelligence` | **Unchanged.** The HMLR contractual-control dataset is not due until after 2028-04-06; nothing new to check | Keep unexplored |
| `grantscout-application-quality`, `vet-estimate-bridge`, `corporate-property-aml-monitor`, `cross-border-green-list-waste-bridge`, `vetlab-reference-list-management` | Reviewed at index level only; no new evidence gathered | Keep unexplored |

No seed was promoted, dropped, or added this run. The two seed candidates
surfaced by the sweep (O1/O15, housing repairs invoice-to-SOR validation) were
**not** written to `seeds/` because the audit found both sides of the seam already
occupied (see the pool file Notes); recording a seed for an occupied seam would
add noise rather than a lead.

## Opportunity observations

| Metric | Value |
| ------ | ----- |
| Observations in pool | 18 (target 15–20) |
| Source-class distribution | Money already moving 9 (job ads 3, service/agency pricing 2, procurement/tender 1, trade press 2, bridge-role job descriptions 2, incumbent support/release notes 1); regulatory 5; other non-regulatory 4 |
| Change-driven / persistent / latent | 4 / 12 / 2 |
| Rejected in shallow triage | 18 |
| Principal triage rejection reasons | Demonstrated occupation of the surrounding workflow by established vendors (O1, O8, O16); the seam is performed by employed staff rather than bought as software (O1, O2, O15); the buyer is enterprise/public-body and not reachable by a small entrant (O4, O7, O16); market-context statistic rather than a specific workflow (O5, O17); already triaged and killed as a parent idea (O13, O14); government-operated process (O12, O14, O18); mature incumbent market (O3, O6, O11) |
| Promoted to full candidates | 1 (≤ 3) |
| Promoted observations and why | **O1** (housing-association repairs invoice-to-SOR reconciliation) — promoted after the triage false-negative audit **overturned** its original rejection. Proven spend (salaried reconciliation roles at GBP 29,400–38,115), a dated council audit finding of an invoice-authorisation backlog, a provider's own written policy mandating the manual check, a named industry rate book (NHF SOR V8), and no credible vendor occupying the provider-side invoice-to-SOR validation seam |

The pool file is `observations/20260922T090448Z-normal.md`. Observations carry no
score, confidence or evidence level, and triage survival confers no inherited
positive evidence.

## Triage false-negative audit

| Field | Value |
| ----- | ----- |
| Observation selected | O1 (housing-association repairs invoice-to-SOR reconciliation) |
| Why selected (vs other rejections) | Strongest money-already-moving observation: a dated council audit finding of an invoice-authorisation backlog, multiple bridge-role job ads paying GBP 30,000–38,000 for exactly this work, and a named industry rate book (NHF SOR V8). Rejected on demonstrated occupation — the exact rejection type the audit tests |
| Original triage reasoning | Demonstrated occupation of the surrounding workflow by established housing-management vendors; the reconciliation step is performed by employed staff rather than bought as software; the incumbents are positioned to add the check |
| Additional evidence checked | Estimark SOR module (contractor-side pricing, not provider-side validation); Omfax Keyfax (SOR code capture at diagnostics); Oneserve, Fixflo, MYRO, MRI Greentree, CHICS (repairs workflow/contractor portals); Ingentive Dynamics 365 (explicitly markets AP invoice-processing and reconciliation assistance); Assignar Pay (markets "Schedule of Rates (SOR) to invoice" automation for construction finance); Rivvun and apexanalytix (invoice assurance/overpayment prevention for procurement/AP) |
| Confusion tests: existence vs satisfaction / feature vs solution / enterprise vs niche / claims vs capability / one-shot vs recurring | Existence vs satisfaction: the surrounding workflow is genuinely served, not merely advertised. Feature vs solution: provider-side invoice-to-SOR validation looks like a feature of the housing-management suite rather than a standalone product. Enterprise vs niche: the buyer is a large housing provider, not a niche. Claims vs capability: Ingentive's AP-reconciliation claim is vendor marketing, but the systems of record are real. One-shot vs recurring: the reconciliation is recurring, which is the one point in the observation's favour |
| Outcome | **overturned** |
| Implication for triage depth | The original rejection was **wrong on its stated ground**. "The reconciliation step is currently performed by employed staff rather than bought as software" is not a triage rejection ground under `method/discovery.md` — it describes the current state, not whether a product would be preferable. The legitimate test is whether a credible alternative demonstrably occupies the exact proposed seam, and the evidence shows it does not (the SOR software market is contractor-side; the provider-side check is a documented manual control). **This is the first overturn in the sampled audit series** (the previous two audits, O14 in the v1.5 pool and O3 in the issue #15 run, were both upheld). Per `method/discovery.md`, a single overturn does not automatically change the method, but it is a signal to review triage depth — specifically, the tendency to treat "currently done by a person" as equivalent to "occupied by a vendor". Recorded for the next method review. The observation was promoted to full candidate research |

## Source classes searched

| Source class | Regulatory? | Searched | Yield |
| ------------ | ----------- | -------- | ----- |
| Legislation / regulation | yes | yes | O9 (Housing SORP 2026), O12 (HMRC ECSH33740), O13 (CMA vet Order), O14 (PRS Database), O18 (CT600 filing) — all rejected |
| Consultations / announced rules | yes | yes | O10 (Companies House P&L filing from April 2028, HMRC director-loan consultation) — rejected |
| Mandated formats / submissions | yes | yes | O18 (CT600 commercial software), O14 (PRS registration) — rejected |
| New APIs / developer surfaces | no | no | Not searched this run |
| New datasets | no | no | Not searched this run |
| Platform rule / pricing / access changes | no | no | Not searched this run |
| Incumbent disruption (EOL, shutdown, migration) | no | yes | O8 (Newlon repairs backlog/service improvement), O16 (fragmented housing systems) — rejected |
| Poor / expensive narrow incumbent software | no | yes | O1, O15 (housing repairs reconciliation), O3 (outsourced bookkeeping) — rejected |
| New technical capability (esp. AI on repetitive service work) | no | yes | O16 (agentic AI Dynamics 365 for housing), O19/O20 (latent) — rejected |
| Manual structured-data flows / re-keying | no | yes | O1, O2, O15, O17 — rejected |
| Awkward integrations between established systems | no | yes | O1, O16 — rejected |
| Underserved subsegments of an existing category | no | yes | O11 (small charities), O17 (micro-businesses) — rejected |
| **Money already moving: job ads describing repetitive admin** | no | yes | O2 (266 reconciliation-analyst jobs; finance-administrator ads), O15 (commercial administrator) — rejected |
| **Money already moving: service / agency pricing pages** | no | yes | O3 (outsourced bookkeeping rates), O11 (grant administration cost) — rejected |
| **Money already moving: procurement / tender records** | no | yes | O7 (Barnet outsourced customer services, CCS RM6295, council audit/data-strategy tenders) — rejected |
| **Money already moving: incumbent support forums / release notes** | no | partial | O16 (vendor marketing pages rather than community threads); no housing-management release notes found mentioning invoice-to-SOR validation — weak negative evidence |
| **Money already moving: trade press reporting spend or staffing** | no | yes | O4 (Corpay CFO survey), O5 (Amex SME barometer), O6 (Gusto payroll hours), O17 (financial admin days) — rejected |
| **Money already moving: bridge-role job descriptions** | no | yes | O1 (St Mungo's, Together Housing, Onward Homes), O15 (Houghton Group, Mears) — rejected |

**Source-budget outcome:** not applicable — zero candidates were promoted, so the
at-most-one-regulation-derived slot was not used (0 regulation-derived against a
limit of 1). The mandatory coverage of the biased classes was met: poor/expensive
narrow incumbent software, manual structured-data/re-keying flows and awkward
integrations were all searched, and the previously underexplored money-already-moving
classes were searched for the first time.

**Money-already-moving outcome (v1.8.0):** the frame worked as intended. It
produced budget evidence that complaint forums do not carry — salaried
reconciliation roles at GBP 30,000–38,000, published outsourced-bookkeeping rates
(GBP 0.50–2.00 per transaction, GBP 8–85/hour), a council audit finding of an
invoice-authorisation backlog, and quantified finance-team hours from trade press.
It did **not** produce a promotion, because every seam with proven spend was either
occupied by established vendors or performed by employed staff rather than bought
as software. That is itself the finding: budget evidence is necessary but not
sufficient, and a widely-budgeted seam is visible to incumbents.

## Why-now quality

| Candidate | Archetype | Why now (one line) | Strength | Persistence thesis | Competitors responded |
| --------- | --------- | ------------------ | -------- | ------------------ | --------------------- |
| `housing-repairs-invoice-sor-validation` | persistent market failure (weak change-driven component) | Document/LLM processing has made reading an unstructured invoice and checking it against a rate book economic for the first time | weak | **weak** — Limb 1 (continued pain/workaround despite reachable alternatives) **pass**; Limb 2 (credible persistence mechanism) **pass (moderate)**; both supported by cited evidence but limb 2 is an inference about vendor incentives | Partly — Rentari.ai has productised the mechanism in the US; no UK provider-side SOR-specific product found |

No candidate rows. All four change-driven observations had dated triggers
(O9 Housing SORP 2026-04-13; O10 Companies House P&L filing from 2028-04; O13 CMA
vet Order; O14 PRS Database from 2026-12-15; O18 CT600 filing closed 2026-03-31)
and each was rejected on occupation, absent buyer or small-task grounds, not on
why-now quality.

## Candidate provenance

| Candidate | Observation ID | Provenance | Source class (regulatory?) | Why it qualifies for that class | Second-order seam | Why not the obvious first-order product |
| --------- | -------------- | ---------- | -------------------------- | ------------------------------- | ----------------- | --------------------------------------- |
| `housing-repairs-invoice-sor-validation` | O1 | fresh | Money already moving: bridge-role job descriptions + procurement/audit records (non-regulatory) | Its why-now comes from a capability shift plus a persistent market failure surfaced by job ads and council audit records, not from legislation | Provider-side invoice-to-SOR validation — the check that happens *after* the works order and *before* payment, not the works-order or repairs-management workflow itself | The first-order product would be another repairs-management or compliance dashboard, which is occupied by Fixflo, Oneserve, MYRO, MRI Greentree, CHICS and Ingentive. The second-order seam (validating the invoice against the rate book) is unoccupied and is where the documented money is lost |

## What advanced

| Idea | From | To | Why |
| ---- | ---- | -- | --- |
| `housing-repairs-invoice-sor-validation` | (none) | discovered → desk-screened | Promoted from observation O1 after the triage false-negative audit overturned the original rejection; hard filters applied (4 pass, 4 unknown, 0 fail); evidence register written; adversarial pass recorded. Scored 58.9/100, below the 65 threshold, so it is parked at desk-screened, not advanced to validation-ready |

## What was killed

| Idea | Reason | Preserved in |
| ---- | ------ | ------------ |
| (none) | No idea was killed. Ledger counts changed from 19 to 20 ideas (one new candidate at desk-screened); killed count unchanged at 15 | — |

## What failed or was skipped

- Zero promotions; no validation-ready advance.
- Incumbent support forums and release notes were searched only indirectly (vendor
  marketing pages rather than community threads); no housing-management vendor's
  release notes were found that mention invoice-to-SOR validation.
- No trade-press source was found reporting a housing provider buying a
  reconciliation product.
- No external tests, interviews or outreach were started; the four standing
  experiments remain proposed and unapproved.
- `method/` was edited, but only as the explicitly requested v1.8.0 method change
  (see below), not as a routine-run edit.

## Convergence assessment

This run **broke the zero-promotion streak**: the money-already-moving frame produced one promoted candidate (`housing-repairs-invoice-sor-validation`) after the triage false-negative audit overturned its rejection. That is a materially different outcome from the previous six funnel runs, and it is attributable to two things: the sourcing frame (which surfaced budget evidence complaint forums do not carry) and the audit (which caught a triage error the frame's own observations were prone to).

The dominant rejection reason for the other 17 observations remains occupation or absent buyer, but the promoted candidate shows the frame can reach a seam that is genuinely unoccupied. The honest caveat is that the candidate scored 58.9/100 — below the 65 threshold — and its central assumption (standalone product vs suite feature) is unresolved. It is parked at desk-screened with a GBP 0 desk-only test proposed.

The convergence signal is therefore **mixed but improved**: the frame is worth keeping, and the audit has demonstrated its value by catching a real triage error. The escalation recorded in `retrospectives/2026-09-21-issue6-convergence-review.md` and `retrospectives/2026-09-21-issue7-funnel-review.md` is now less urgent, but the triage-depth finding (treating "done by a person" as "occupied") should still go to the next method review.

## Limits encountered

| Limit | Used |
| ----- | ---- |
| Candidates generated | 1 / 3 |
| Unreviewed after run | 0 / 10 |
| Advances to validation-ready | 0 / 1 |
| Web lookups | ~40 / 40 |
| Evidence entries | 1 register (9 dated sources) |
| Cost | USD 0.00 (no model calls; desk research only) |
| Timeout | within 3600 s |

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
| -------- | ------- | ------------------ | -------------- |
| Method 1.8.0 review | Route `reviews/2026-09-22-method-v1.8.0-review-request.md` to the independent reviewer (ChatGPT) and commit the response as `reviews/<date>-method-v1.8.0-chatgpt.md` | Before the next normal run treats 1.8.0 as calibrated | `reviews/2026-09-22-method-v1.8.0-review-request.md` |
| Convergence escalation | (a) commission the human-led sourcing/framing review; (b) accept the spike's ITERATE verdict and stop sweeping; (c) continue same-shaped sweeps (not recommended — seven zero-promotion runs) | Before the next discovery run | This summary; `retrospectives/2026-09-21-issue6-convergence-review.md`; `retrospectives/2026-09-21-issue7-funnel-review.md` |
| Standing experiments | Approve, amend or decline `geonerd-demand-spike`, `reasonable-steps-willingness`, `aucly-channel-test` (closest to validation-ready at 60.0, GBP 0 cost bound) and `vetlab-en18029-conformance-buyer-wedge` | Whenever the owner wants real-world evidence; no experiment can run without approval | `experiments/index.json`; `experiments/queue.md` |
| Housing repairs reconciliation seed | Whether to record a `housing-repairs-invoice-sor-validation` seed despite the audit finding both sides occupied | Optional; the audit recommends against adding noise | `observations/20260922T090448Z-normal.md` Notes |

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
| ---- | ------------- | ------- | ---------------- |
| All 19 ideas | not-required or approved | — | — |
| Method 1.8.0 | requested | `reviews/2026-09-22-method-v1.8.0-review-request.md` | 2026-09-22 |

No `changes-requested` review existed at orientation and none was created.

## Next run should

1. **Not** run another unchanged same-shaped funnel sweep. Act on the convergence
   decision first: either commission the human-led sourcing/framing review or
   accept the ITERATE verdict.
2. If the owner wants more discovery, change the *frame* rather than the filter —
   for example target buyers who already pay a service provider for the work
   (so the budget is a line item, not a salary) or geographies/segments where the
   incumbent set is thinner.
3. Respond to the method 1.8.0 review when it lands, and keep the four standing
   experiments in front of the owner.

## Confirmation

No disallowed actions were taken. No commits, pushes, issues, pull requests or
other publication; no contact with any person; no money spent; no external
accounts created; no commitments made; no experiment started or proposed for
external execution; no review outcome overwritten or ignored. `method/` was edited
only as the explicitly requested v1.8.0 method change, which is a reviewable
uncommitted change set with a review request, not a routine-run edit. The
`ideas/index.json` ledger was not modified by this run beyond the method-version
bump already made as part of the v1.8.0 change.
