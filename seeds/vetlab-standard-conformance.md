# Seed: DIN EN 18029 / VetXML exchange conformance tooling for veterinary lab and PIMS vendors

- **Seed ID / slug:** `vetlab-standard-conformance` / `vetlab-standard-conformance`
- **Origin idea:** `vetlab-bridge` (`killed`)
- **Recorded:** 2026-09-21
- **Status:** `promoted`

**This seed does not inherit any score, evidence level or hard-filter status from
`vetlab-bridge`.** The parent was killed on the `defensible_wedge` hard filter. A future
run must research this seed from scratch, including its own novelty check, evidence
register, hard filters and scorecard.

## Observation

DIN EN 18029:2026-04 (E), "Animal health diagnostic analyses – Electronic data exchange
in laboratory analysis", was published in April 2026, specifying request, result and
acknowledgement files plus a data dictionary. VetXML is adopted by only some UK PIMS
vendors and insurers, and the research found no evidence that any vendor has implemented
DIN EN 18029. Veterinary laboratories and PIMS/LIS vendors therefore face a conformance
and mapping burden against two overlapping exchange standards with no obvious
implementation/test tooling.

Source: `evidence/vetlab-bridge/2026-09-21-din-en-18029-standard.md`.

## Why it is materially different from the parent

The parent sold a results-delivery service to independent labs, competing directly with
shipping products (ManuCare, DataHub Vet) — and was killed for it. This seed has a
different buyer (PIMS/LIS and laboratory software vendors, plus labs that must attest
exchange conformance), a different mechanism (a conformance/test-fixture and
mapping-validation toolkit rather than an operated delivery channel), and its value
depends on standards adoption rather than on operating a network. It addresses the
parent's recorded kill reason (feature of an established integration category) by
selling to the implementers of a new standard instead of operating the integration.

## Evidence for the observation

- `evidence/vetlab-bridge/2026-09-21-din-en-18029-standard.md` — DIN catalogue record for
  DIN EN 18029:2026-04 (E); published April 2026.
- `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md` — live
  integration products and the absence of any conformance tooling among them.
- `ideas/vetlab-bridge/decision.md` — the parent's kill reasons and false-negative audit.

## What a later run should check first

- Whether any PIMS/LIS vendor, lab or insurer has publicly committed to DIN EN 18029 or
  VetXML adoption, and on what timetable (without adoption there is no buyer).
- Whether standards bodies, national veterinary associations or the vendors themselves
  publish free conformance suites or test fixtures that would make this a commodity.
- Whether the buyer count (veterinary PIMS/LIS vendors in the UK/EU) is large enough for a
  viable business, or whether this is a one-shot consultancy rather than a product.
- Whether a conformance toolkit can be sold before the standard is mandated anywhere.

## Outcome (append-only)

| Date | Outcome | Why | Link |
|---|---|---|---|
| 2026-09-21 | created | Surfaced during the `vetlab-bridge` kill; recorded as a non-inheriting adjacent opportunity | this file |
| 2026-09-21 | promoted | Full fresh research during run `20260921T100247Z-normal` produced candidate `vetlab-en18029-conformance` (observation O5); the candidate carries its own evidence, hard filters and 44.2/100 score and inherits nothing from `vetlab-bridge` | `ideas/vetlab-en18029-conformance/` |
