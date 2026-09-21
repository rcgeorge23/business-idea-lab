# VetLab EN 18029 Conformance: exchange conformance and reference-list tooling for veterinary lab and PIMS/LIMS vendors

- **ID / slug:** `vetlab-en18029-conformance`
- **State:** `desk-screened`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** worker run `20260921T100247Z-normal`, observation `O5`; provenance `seed:vetlab-standard-conformance` (origin idea `vetlab-bridge`, killed). Researched from scratch; inherits no score, evidence level or hard-filter status from the parent.

## One-sentence proposition

> Veterinary PIMS/LIMS vendors and laboratories must exchange laboratory order, result and
> acknowledgement data, and a new European standard (DIN EN 18029:2026-04) specifies the
> message format but deliberately omits the code lists needed to interpret it; we sell a
> conformance and mapping-validation toolkit with a maintained veterinary reference-list
> service to the software vendors and laboratories that must implement and attest exchange.
> **Desk-screened only: no hard filter fails, but no buyer, budget or adoption evidence
> exists yet.**

## Why now?

> This was not an attractive business three years ago, but it might be now because a
> European standard for veterinary laboratory data exchange was published in April 2026.

- What changed: DIN EN 18029:2026-04 (E) "Animal health diagnostic analyses – Electronic
  data exchange in laboratory analysis" was published, specifying request, result and
  acknowledgement files plus a data dictionary — while explicitly excluding the code lists
  required for unambiguous exchange.
- When it changed (or is due to change): standard published 2026-04 (ÖNORM EN
  18029:2026-04-15).
- Evidence (dated source), and why the change is real rather than a trend:
  `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md` (national
  standards-catalogue records). The records show publication and scope only; they do not
  show that any vendor has implemented the standard.
- Why this materially improves the opportunity now: a published message format plus a
  deliberately omitted code list creates a conformance/mapping job for every adopting pair,
  and a standard published ahead of vendor implementation is a window in which no
  implementation tooling has yet shipped (inference).
- Have competitors already responded? No conformance or reference-list product was found.
  Adjacent layers are occupied: VetXML publishes schemas and VetEnvoy operates a hub;
  Bitwerx, IDEXX DataPoint and Covetrus Connect solve connection/structural mapping;
  ManuCare and DataHub Vet occupy results delivery
  (`evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md`).
- Strength: `weak` (a standard, not a mandate; no adoption evidenced; no buyer budget
  evidenced). The missing-why-now cap therefore applies.

## Buyer

- Who exactly pays (role, company size, segment): hypothesised to be PIMS/LIMS vendors and
  smaller veterinary laboratory-software vendors that must implement exchange, and
  laboratories that must attest conformance to partners or procurement. No named buyer,
  budget or funded requirement is evidenced; this is an inferred buyer.
- Who uses it: integration engineers and laboratory IT staff implementing and testing the
  exchange; product managers attesting conformance in bids.
- Evidence: `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md`,
  `evidence/vetlab-en18029-conformance/2026-09-21-vetlab-market-and-buyer-economics.md`

## Problem

- What is painful/frequent/expensive: veterinary PIMS APIs are "closed, undocumented or
  fee-gated" across roughly 2,100 theoretical PIMS×lab integration pairs; PIMS and lab
  vendors negotiate bilateral integrations, and independent/smaller labs sit at the margins
  of integration investment. A new standard adds a conformance and mapping burden against
  two overlapping specifications (EN 18029 and VetXML) whose required code lists are not
  supplied by either. Frequency and cost are not quantified by any cited source, so this is
  documented structural friction, not a measured cost.
- Current alternatives and their weaknesses: VetXML gives free schemas and VetEnvoy a hub,
  but neither supplies EN 18029 conformance testing or a maintained cross-walk between the
  code lists; structural intermediaries stop at the connection/structural layer; generic
  LIMS vendors support HL7/XML/CSV but not veterinary-specific conformance; no free
  conformance suite surfaced.
- Evidence: `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md`,
  `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md`

## Mechanism / wedge

- What we would actually do: a conformance toolkit (schema validation, test fixtures and a
  certification report against EN 18029 request/result/acknowledgement files) plus a
  maintained veterinary reference-list service (hosted code lists and cross-walks between
  laboratory analytes, units and reference ranges), with an exception/mapping-validation
  queue for unmatched terms. Sold to vendors and laboratories as tooling/subscription, not
  operated as a delivery channel.
- Why it is defensible against the cheapest credible incumbent: the wedge is structural —
  the standard exists before any implementation, the standard itself omits the code lists,
  and the reference lists are a maintained-data asset that must be curated per jurisdiction
  and vendor. This is a different job from results delivery (ManuCare/DataHub Vet) and from
  connection middleware (Bitwerx/DataPoint/Covetrus Connect). It is, however, unproven:
  whether vendors will pay for conformance before a mandate is unknown, and a standards body
  or consortium could publish a free conformance suite (see adversarial case).
- Evidence: `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md`,
  `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md`

## Novelty / incumbent sanity check

| Check | Answer | Evidence |
|---|---|---|
| Does this exact product already exist? | Not found — no shipping EN 18029 or VetXML conformance/test-fixture product, and no maintained veterinary reference-list service, was surfaced | `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md` |
| Are there multiple credible providers? | In adjacent layers only — VetXML schemas, VetEnvoy hub, Bitwerx, IDEXX DataPoint, Covetrus Connect, ManuCare, DataHub Vet; none in the proposed conformance/reference-list seam | `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md` |
| Is the wedge already a standard feature? | No — the conformance job is created by the new standard; existing products solve connection, structural mapping or delivery | `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md` |
| Is a free/authoritative alternative already adequate? | Partly — VetXML schemas are free and VetEnvoy is a hub, but neither supplies EN 18029 conformance or the missing code lists; whether a standards body will publish a free suite is unknown | `evidence/vetlab-en18029-conformance/2026-09-21-en18029-standard-scope.md` |
| Has a well-capitalised company shown hostile unit economics? | Not directly evidenced; the segment is small ($6.35M diagnostic-lab software in the UK, 2025) and a comparable LIMS tender attracted one £202,652 bid, which is consistent with a thin specialist buyer population | `evidence/vetlab-en18029-conformance/2026-09-21-vetlab-market-and-buyer-economics.md` |
| Is this merely a feature of an established category? | Not established either way — it is a standards-conformance and maintained-data job adjacent to, but distinct from, PIMS/LIMS integration middleware | `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md` |

Because no check is a definite "already exists / already free / already a feature", the idea
is not killed at screening: it is desk-screened with a weak why-now and unknown buyer. The
single most important novelty risk — a free conformance suite published by a standards body
or consortium — is the first thing a later run should re-check.

## Distribution

- Route to the first 10 buyers without paid acquisition: hypothesised direct outreach to
  named PIMS/LIMS and laboratory-software vendors (VetXML member list is a ready-made target
  list) plus veterinary laboratory procurement channels. No vendor or lab has signalled
  interest; unvalidated.
- Evidence: `evidence/vetlab-en18029-conformance/2026-09-21-vet-interoperability-and-incumbents.md`

## Economics (assumptions labelled)

- Price hypothesis: per-vendor annual licence plus per-mapping or per-connection fee; no
  price evidence found (assumption).
- Cost drivers: maintaining reference lists and cross-walks per jurisdiction and vendor,
  building and updating test fixtures as the standard and VetXML evolve, supporting
  conformance attestations.
- Contribution margin at realistic scale: unknown; the diagnostic-laboratory software
  segment is small (UK $6.35M in 2025) and a maintained-data service is recurring cost, so
  the buyer population must include PIMS vendors and laboratories beyond the UK for the
  model to work. Not modelled with a real price.
- Evidence: `evidence/vetlab-en18029-conformance/2026-09-21-vetlab-market-and-buyer-economics.md`

## Founder fit

- Reach, skills, motivation (evidence only; `null` if unknown): `null` — no evidence about
  who would found or sell this; it would need standards/health-IT domain knowledge and
  reference-data curation capability.

## Adversarial case (strongest case this is wrong)

EN 18029 is a standard, not a mandate: without an EU/UK regulatory driver, no vendor has to
implement it, and nothing found shows any vendor intends to. The buyer population is tiny
and specialised — the UK diagnostic-laboratory software segment was only $6.35M in 2025, and
a comparable LIMS tender attracted a single bid — so a conformance toolkit may be a one-shot
consultancy rather than a product, or a feature that the few large PIMS vendors build
themselves (IDEXX, Antech, Zoetis already build bilateral integrations). Standards bodies,
the VetXML consortium or national veterinary associations could publish a free conformance
suite and reference lists, making the wedge worthless. The positive finding is only that no
such product was found, which is fragile. The why-now is weak, no buyer budget is evidenced,
and the reference-list service could require perpetual curation for a handful of customers.

## Strongest supporting case

A hard, dated, first-of-its-kind European standard published in April 2026 that explicitly
omits the code lists needed for exchange, in a vertical whose integration layer is closed
and fee-gated and whose existing products solve a different layer. The conformance and
maintained-reference-list job is structurally distinct from the already-contested delivery
seam that killed the parent idea. It is a genuine "standard before vendors implement it"
seam — but it is unproven and the why-now is weak.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| A PIMS/LIMS or lab vendor has a funded EN 18029/VetXML conformance need | Interview ≥5 vendors/labs; none names a funded need | untested |
| No free conformance suite or authoritative reference list will be published | Desk check of standards bodies, VetXML consortium and national associations; find a published free suite | untested |
| The buyer population is large enough for a product, not one-shot consultancy | Size the population of PIMS/LIMS/lab-software vendors and count bids needing conformance | untested |
| Reference-list curation can be funded by a recurring subscription | Price test against a named vendor | untested |

## Cheapest decisive experiment

- Assumption under test: buyers will fund EN 18029/VetXML conformance tooling before any
  mandate exists.
- Proposed test: desk check of standards bodies/consortia for free conformance suites,
  followed by short structured interviews with labs and PIMS/LIMS vendors about whether
  exchange conformance is a funded requirement and what they would pay.
- Pre-fixed decision rule: proceed to a paid-pilot test only if ≥2 of 5 named labs/PIMS
  vendors state a funded EN 18029/VetXML conformance need or commit to a paid pilot, and no
  free authoritative conformance suite is found; otherwise remain desk-screened/parked.
- Cost bound: 12 human-hours, £0, 21 calendar days.
- Status: **proposed — awaits human approval** (interviews require human contact).
- Link: `experiments/vetlab-en18029-conformance-buyer-wedge/plan.md`

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-21 | (new) discovered -> desk-screened | Promoted from observation O5 (seed `vetlab-standard-conformance`); no hard-filter `fail`; ≥1 dated problem source; full fresh research completed but buyer, wedge and adoption remain unknown | `ideas/vetlab-en18029-conformance/decision.md` |
