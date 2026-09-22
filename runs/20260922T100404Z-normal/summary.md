# Run summary: 20260922T100404Z-normal

- **Mode:** normal
- **Started / finished:** 2026-09-22T10:04:04Z / 2026-09-22T10:09:17Z
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.8.0
- **Input / output revision:** `uncommitted` / `uncommitted`
- **Status:** success

**Run type note.** This was an **owner-directed scoped assessment**, not a general
opportunity-funnel run. The owner asked: does it pay to expand `aucly` (flat-fee
auction platform) into Ireland, the US, Australia or New Zealand - cost, benefit,
market conditions, regulation? A locale variant has the same buyer, problem and
mechanism as `aucly`, so per the duplicate rules this **updates the existing idea**
rather than creating a candidate. No new candidate was generated, no promotion was
made, and no score or hard filter was changed. The observation-funnel machinery
(pool, triage, one false-negative audit, source-class budget) was still run so the
assessment is evidence-disciplined rather than opinion.

## Seed register review

| Seed | Shallow re-check result | Action (candidate / stays seed / status change) |
|---|---|---|
| grantscout-application-quality | Not re-checked this run (owner-directed run, not a funnel sweep) | stays seed |
| vet-estimate-bridge | Not re-checked this run | stays seed |
| prs-listing-precheck | Not re-checked this run | stays seed |
| corporate-property-aml-monitor | Not re-checked this run | stays seed |
| cross-border-green-list-waste-bridge | Not re-checked this run (thematically adjacent to "cross-border" but a different buyer/problem) | stays seed |
| prs-self-managing-landlord | Not re-checked this run | stays seed |
| clinic-legacy-managed-archive | Not re-checked this run | stays seed |
| vetlab-reference-list-management | Not re-checked this run | stays seed |
| land-control-data-intelligence | Not re-checked this run | stays seed |

The register was read at orientation. Nine seeds remain unexplored; two are already
promoted (`agent-checkout-offplatform`, `vetlab-standard-conformance`); one is
dropped (`uk-epr-small-producer-tooling`). **Skipped step, flagged:** no seed was
given the protocol's shallow re-check this run because the run was a single-idea
owner request; see "What failed or was skipped".

## Opportunity observations

| Metric | Value |
|---|---|
| Observations in pool | 20 (target 15-20) |
| Source-class distribution | 10 regulatory / 10 non-regulatory |
| Change-driven / persistent market failure / latent opportunity | 4 / 16 / 0 |
| Rejected in shallow triage | 20 |
| Principal triage rejection reasons | (a) a free or near-free incumbent already occupies the seam in every locale at both price ends; (b) no evidence of unmet demand or switching, in any locale; (c) the regulatory findings are compliance headwinds/costs, not opportunities, and are only triggered once money moves |
| Promoted to full candidates | 0 (<= 3) |
| Promoted observations and why | none - every observation was either a replication of `aucly` (already in the ledger) or a regulation/tax cost, neither of which is a materially distinct candidate |
| Latent observations found / triaged / promoted / rejected | 0 / 0 / 0 / 0 (zero promotions acceptable) |

**Pool file:** `observations/20260922T100404Z-normal.md`. Observations carry no
score, confidence or evidence level, and triage survival confers no inherited
positive evidence on a promoted candidate.

Zero promotions is the correct outcome here, not filler: the only promotable
insight surfaced is a variant of the existing idea `aucly`, which the duplicate
rules require to update `aucly` rather than create a new candidate.

## Triage false-negative audit

| Field | Value |
|---|---|
| Observation selected | O20 - "US fundraising-auction spend is large and already budgeted (money already moving)" |
| Why selected (vs other rejections) | Highest-ambiguity, most-promising rejection: it had the strongest signal of real money moving (a large budgeted category with multiple paid incumbents and a big installed base of PTAs/PTOs), i.e. exactly the class the audit prefers |
| Original triage reasoning | Rejected because the US is saturated at both price ends - free/near-free tiers (Auctria Explorer free up to US$10k event income; GalaBid free-with-tips) and cheap per-event/annual paid options (SchoolAuction.net from US$79/event; Auctria US$375-750/yr) - leaving no evidenced unmet demand |
| Additional evidence checked | Auctria free-tier limits (up to US$10,000 event income/year, 250 bidders); SchoolAuction.net 501(c)(3)/US tax-id requirement; GalaBid region-specific paid pricing (~US$1,250/campaign); Charleston Principles on when an online charity auction triggers state solicitation registration |
| Confusion tests: existence vs satisfaction / feature vs solution / enterprise vs niche / claims vs capability / one-shot vs recurring | existence vs satisfaction: incumbents exist AND are low-cost, but satisfaction is not directly evidenced - unresolved, which is why this was audited rather than dismissed; feature vs solution: auction tooling is a full product category, not a missing feature; enterprise vs niche: both ends covered (free self-service and managed full-service); claims vs capability: Auctria/SchoolAuction feature sets corroborate capability; one-shot vs recurring: auctions recur annually, so a paying niche plausibly persists |
| Outcome | **upheld** (rejection stands), with the reason restated as "the category is served at both price ends" rather than "competitors exist" |
| Implication for triage depth | Triage depth was adequate. One residual seam is worth a future look: willingness to pay **above** Auctria's US$10k free-tier ceiling (i.e. larger events that outgrow free tiers), but that is a different segment from `aucly`'s small volunteer-run auctions and was not promoted |

## Source classes searched

| Source class | Regulatory? | Searched? | What it yielded (or why nothing) |
|---|---|---|---|
| Legislation / regulation | yes | yes | GST/VAT/sales-tax thresholds; privacy-act scope; charity-fundraising rules (see regulation evidence file) |
| Consultations / announced rules | yes | yes | AU Privacy Amendment exposure draft (2026-08-31, small-business exemption retained); Ireland GRA 2024 charitable licence not opening 2026 |
| Mandated formats / submissions | yes | no | Not relevant to a locale-expansion question |
| New APIs / developer surfaces | no | no | Not relevant |
| New datasets | no | yes | Official school-count datasets (DfE, IE Dept of Education, ABS, Education Counts NZ, NCES) used for market sizing |
| Platform rule / pricing / access changes | no | yes | Incumbent pricing pages/policy: Auctria, SchoolAuction.net, GalaBid, Toko |
| Incumbent disruption (EOL, shutdown, migration) | no | no | Nothing found in the time box |
| Poor / expensive narrow incumbent software | no | yes | iDonate.ie, Fundraising Solutions (zero platform fee), FundRaisely.ie, Toko (free for NZ schools), Raised.nz |
| New technical capability (esp. AI on repetitive service work) | no | no | Not relevant to this question |
| Manual structured-data flows / re-keying | no | no | Not relevant to this question |
| Awkward integrations between established systems | no | no | Not relevant |
| Underserved subsegments of an existing category | no | partial | School/PTA-specific auction tools exist per locale; no clearly underserved locale subsegment found |
| Money already moving: job ads describing repetitive admin | no | no | Not searched (out of scope this run) |
| Money already moving: service / agency pricing pages | no | yes | Professional/managed fundraiser service pricing (e.g. GalaBid managed pricing; Fundraising Solutions zero-platform-fee model) |
| Money already moving: procurement / tender records | no | no | Not searched |
| Money already moving: incumbent support forums / release notes | no | no | Not searched; a genuinely underexplored class for a future run |
| Money already moving: trade press reporting spend or staffing | no | no | Not searched (no trade-press locale spend data found) |
| Money already moving: bridge-role job descriptions | no | no | Not searched |

**Money-already-moving outcome (v1.8.0):** two money-moving sub-classes were
searched and both yielded budget evidence rather than only complaint-forum evidence:
service/agency pricing pages (Auctria paid tiers; SchoolAuction.net paid tiers;
GalaBid managed/campaign pricing) and new datasets (official school counts used to
size the addressable market). Four of the twenty observations (O2, O3, O4, O20) were
money-already-moving. Unsuccessful searches, recorded: no Ireland/NZ/AU
practitioner-forum complaints about incumbent auction tools were found, and no
switching-intent or willingness-to-pay evidence was found in any target locale. Not
searched this run: job ads, procurement/tender records, support forums/release
notes, trade-press spend, bridge-role job descriptions.

**Source-budget outcome:** **met (trivially)** - 0 candidates were promoted, so the
"at least 2 of 3 candidate slots non-regulatory / at most 1 regulation-derived"
constraint is not binding. The only promotable insight was a variant of the existing
idea `aucly`, which must update the idea rather than become a candidate. A previously
underexplored **non-regulatory** class was nevertheless actually searched: poor /
expensive narrow incumbent software (per-locale incumbents and their pricing). No
filler candidate was manufactured.

## Why-now quality

| Candidate | Archetype | Why now (one line) | Strength | Persistence thesis | Competitors responded |
|---|---|---|---|---|---|
| `aucly` (locale-expansion variant - not promoted) | persistent market failure | No favourable change; expansion would be a positioning choice, not a discontinuity | absent | **absent** - no two-part persistence thesis was evidenced for any locale: lens (1) continued pain despite alternatives is unproven, and lens (2) no credible persistence mechanism was shown (free tiers and zero-fee incumbents already serve the seam) | n/a - incumbents already price at or below zero at the entry end |

The expansion proposition therefore remains under the missing-why-now cap; it does
not lift it and does not inherit the home idea's operating evidence.

## Candidate provenance

| Candidate | Observation ID | Provenance (seed:<slug> or fresh) | Source class (regulatory?) | Why it qualifies for that class | Second-order seam | Why not the obvious first-order product |
|---|---|---|---|---|---|---|
| none promoted | - | - | - | - | - | - |

For completeness, the **assessed entity** is `aucly` itself (expansion variant,
provenance `fresh` assessment of an existing idea), originating from observations
O1 (home acquisition failure), O2-O4 and O12-O16 (per-locale incumbents), O5-O11 and
O17-O19 (regulation/tax), O15 (market size), O20 (money already moving). No second-
order operational seam (re-keying, reconciliation, exception handling, integration
gap) was found in the locale-expansion proposition: it is a geography change to an
existing product, not a new operational seam.

## What advanced

| Idea | From | To | Why |
|---|---|---|---|
| none | - | - | No idea met the validation-ready threshold; `aucly` remains `adversarially-researched` (parked) at 60.0 |

## What was killed

| Idea | Reason | Preserved in |
|---|---|---|
| none | - | - |

No idea was killed or advanced. Rejections were of **observations**, not candidates.

## What failed or was skipped

- **Seed shallow re-check skipped.** The protocol's step-1 seed re-check was not
  performed because this was an owner-directed single-idea assessment rather than a
  funnel sweep. All nine unexplored seeds therefore remain un-re-checked in this run.
  Flagged for method review: the protocol assumes every normal run is a funnel run,
  and does not describe how to record an owner-directed assessment run.
- **Aucly source repository unreadable.** `/home/richard/projects/aucly-micronaut` is
  outside the permitted external-directory scope, so the assessment relies on the
  existing `evidence/aucly/*` registers (which cite specific repo revisions) and on
  desk research. Localisation cost is therefore an indicative estimate, not a
  measured one.
- **A small number of vendor pages were transiently unavailable** (e.g. an Auctria
  pricing fetch returned 429 before retry); figures recorded are from the pages that
  did load, with access dates.

## Convergence assessment

This run did **not** search for new opportunities; it stress-tested one existing idea
against four locales. The result is convergent with the previous run's guidance
("do not run another unchanged same-shaped funnel sweep"): the binding constraint on
`aucly` is **distribution at home**, not geography. The assessment found that every
target locale already has a free or near-free incumbent (Toko free for NZ schools;
Fundraising Solutions zero platform fee in Ireland; Auctria free tier and free-with-
tips GalaBid in the US; GalaBid's scale across AU/NZ), so expansion would reset
distribution to zero in a market with equal-or-stronger price competition. The
modelled revenue illustration shows the UK opportunity at 5% penetration exceeds
Ireland + New Zealand + Australia at 1% combined, which is the clearest evidence that
geography is not the bottleneck. **No filter was weakened, and no candidate was
manufactured to make the run look productive.**

## Limits encountered

- Candidates generated: 0 / 3 (owner-directed assessment, not a generation run)
- Unreviewed after run: 0 / 10
- Advances to validation-ready: 0 / 1
- Web lookups: ~25 / 40
- Cost: not captured (LAB_RUN_ID unset; finalize wrapper not running). Method bound
  $1.00 was not approached (desk-only run, no external spend).

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
|---|---|---|---|
| Approve or decline `aucly-channel-test` (UK unpaid-outreach test) | Approve / decline / amend | Before any expansion work; it is the gating test for the home market | `experiments/aucly-channel-test/plan.md`, `ideas/aucly/decision.md` |
| Approve or decline `aucly-ireland-demand` (conditional locale probe) | Approve / decline / park | Only after `aucly-channel-test` reports; it is meaningless as a first test | `experiments/aucly-ireland-demand/plan.md`, `ideas/aucly/expansion-assessment.md` |
| Whether locale expansion is in scope at all before home distribution is proven | In scope / out of scope until home channel answered | Owner's call | `ideas/aucly/expansion-assessment.md` |

No commit, push, contact, account creation, spend or commitment was made. All
experiments remain proposals requiring human approval.

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|
| `aucly` | not-required (parked idea) | - | - |
| method 1.8.0 sourcing frame | requested | `reviews/2026-09-22-method-v1.8.0-review-request.md` | 2026-09-22 |

No `changes-requested` review existed at orientation and none was created; nothing
was overwritten.

## Next run should

1. **Stop desk-researching Aucly expansion.** The decision hinges on a real-world
   test, not more desk evidence. Get an owner decision on `aucly-channel-test` first.
2. **Change the discovery frame** as the previous run recommended (target buyers who
   already pay a service provider, or geographies/segments where the incumbent set
   is thinner) rather than repeating a same-shaped sweep.
3. If more Aucly work is wanted before then, deepen the **internal** question - actual
   cost/hours per launched auction and second-year return - since `plausible_margins`
   and `distribution` are the two unknown filters holding the idea at 60.0.
