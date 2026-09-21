# VetLab Bridge: veterinary diagnostics results interchange for independent labs and the long tail

- **ID / slug:** `vetlab-bridge`
- **State:** `killed`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** worker run `20260921T091851Z-normal`, observation `O17` (fresh discovery)

## One-sentence proposition

> Independent and regional veterinary diagnostic labs have no economic route to deliver
> results into the long-tail PIMS used by independent practices, so practice staff
> re-key values or attach PDFs; we provide a semantic results-interchange layer
> (any lab format in, PIMS-ready structured result out) sold to labs as a distribution
> channel at a per-practice monthly fee. **Killed: the mechanism is already sold by a
> live vendor and is a feature of the established PIMS/LIMS integration category.**

## Why now?

> This was not an attractive business three years ago, but it might be now because a
> European standard for veterinary laboratory data exchange was published in April 2026.

- What changed: DIN EN 18029:2026-04 (E) "Animal health diagnostic analyses – Electronic
  data exchange in laboratory analysis" was published, specifying request, result and
  acknowledgement files plus a data dictionary.
- When it changed (or is due to change): standard published 2026-04.
- Evidence (dated source), and why the change is real rather than a trend:
  `evidence/vetlab-bridge/2026-09-21-din-en-18029-standard.md` (DIN catalogue record).
  The source record shows publication only; it does not show that any PIMS or lab has
  implemented it.
- Why this materially improves the opportunity now: a published format could reduce the
  per-lab mapping burden (inference, not established); it does not create a buyer.
- Have competitors already responded? Yes — ManuCare already markets universal lab-result
  import ("zero copy-paste"); DataHub Vet normalises PIMS data; Bitwerx, Covetrus Connect,
  Covetrus LabLink and PupPilot occupy adjacent layers
  (`evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md`).
- Strength: `weak`

## Buyer

- Who exactly pays (role, company size, segment): hypothesised to be independent/regional
  veterinary diagnostic labs that want distribution into independent practices but cannot
  fund certified point-to-point integrations. No lab is named and no lab budget is
  evidenced; the "not the four large reference networks" count was unsourced (sources name
  IDEXX, Antech, Zoetis).
- Who uses it: practice staff and vets reading results in their existing PIMS.
- Evidence: `evidence/vetlab-bridge/2026-09-21-vet-interoperability-structural-gap.md`

## Problem

- What is painful/frequent/expensive: results arrive as PDFs by email/portal and are
  re-entered or attached by hand; practitioner evidence describes opening results
  separately and re-keying values for trend comparison. Frequency and population are not
  quantified by any cited source, so this remains documented pain rather than a measured
  cost.
- Current alternatives and their weaknesses: large-lab bilateral integrations serve only
  big labs and big PIMS; middleware (Bitwerx, Covetrus Connect, AllyDVM) solves
  connection/structural layers; ManuCare already imports any lab's results and DataHub Vet
  already normalises PIMS data into six long-tail systems.
- Evidence: `evidence/vetlab-bridge/2026-09-21-vet-interoperability-structural-gap.md`,
  `evidence/vetlab-bridge/2026-09-21-pims-api-openness-and-fees.md`,
  `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md`

## Mechanism / wedge

- What we would actually do: accept results in any lab format (DIN EN 18029, HL7, CSV,
  PDF), normalise to a canonical veterinary result model with analyte mapping, deliver
  structured results into the practice's existing PIMS, and route unmapped analytes to an
  exception queue.
- Why it is defensible against the cheapest credible incumbent: it is not. ManuCare
  already markets universal lab-result import with "zero copy-paste", and DataHub Vet
  already exposes a normalised veterinary data model into long-tail PIMS from the other
  end. The remaining difference — that labs rather than practices would pay — is a
  commercial hypothesis with no supporting evidence, not a technical or structural wedge.
- Evidence: `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md`

## Novelty / incumbent sanity check

| Check | Answer | Evidence |
|---|---|---|
| Does this exact product already exist? | Yes — ManuCare markets universal CSV/HL7 lab-result import into the patient case ("zero copy-paste"); DataHub Vet sells a normalised data model into six long-tail PIMS | `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md` |
| Are there multiple credible providers? | Yes — DataHub Vet, ManuCare, Bitwerx, Covetrus Connect, Covetrus LabLink, PupPilot, plus expanding IDEXX lab integrations | `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md` |
| Is the wedge already a standard feature? | Largely — lab import is becoming a standard PIMS feature and ManuCare already sells the import mechanism | `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md` |
| Is a free/authoritative alternative already adequate? | VetXML is already adopted by some UK PIMS vendors and insurers, and an embedded standard is effectively free to the practice | `evidence/vetlab-bridge/2026-09-21-vet-interoperability-structural-gap.md` |
| Has a well-capitalised company shown hostile unit economics? | Yes, in adjacent form — IDEXX owns a reference lab and the PIMS itself, so it can bundle result delivery at no incremental fee; $30–50/clinic/month access fees filter out small integrators | `evidence/vetlab-bridge/2026-09-21-pims-api-openness-and-fees.md` |
| Is this merely a feature of an established category? | Yes — PIMS/LIMS integration and middleware | `evidence/vetlab-bridge/2026-09-21-incumbent-bridges-and-lab-integrations.md` |

If any check fails, state the reason to continue anyway: **no reason to continue.** The
`defensible_wedge` check fails on the filed evidence (a live vendor already sells the
mechanism and it is a feature of an established category), which under
`method/scorecard.md` is a hard-filter failure, not merely a score reduction. The idea is
killed rather than parked. It would only be reopened if the desk capability check
described under "False-negative audit" showed that no shipping product performs semantic
lab-result delivery to the long-tail independent lab and no independent lab has any
sanctioned structured import route.

## Distribution

- Route to the first 10 buyers without paid acquisition: hypothesised direct outreach to
  independent/regional UK and IE labs and partnership with open PIMS programmes (Provet,
  Lupa, Digitail). No lab is named, and no partner signalled interest — unvalidated.
- Evidence: `evidence/vetlab-bridge/2026-09-21-pims-api-openness-and-fees.md`

## Economics (assumptions labelled)

- Price hypothesis: per-practice monthly fee paid by the lab (assumption; no price
  evidence found). Must clear the documented $30–50/clinic/month access-fee floor and
  still leave margin.
- Cost drivers: per-lab format mapping (one-off), per-PIMS connector (repeated),
  exception handling.
- Contribution margin at realistic scale: unknown; a low ACV against a repeated
  connector/mapping service burden is the central economic risk.

## Founder fit

- Reach, skills, motivation (evidence only; `null` if unknown): `null` — no evidence
  about who would found or sell this.

## Adversarial case (strongest case this is wrong)

ManuCare already markets the exact import mechanism and DataHub Vet already normalises
the data from the PIMS side, and both could extend toward labs faster than a new entrant
can build PIMS connectors across a long tail whose vendors charge $30–50 per clinic per
month. IDEXX is vertically integrated (reference lab plus ezyVet/Cornerstone/Neo plus
VetConnect/DataPoint) and can bundle result delivery at no incremental fee. The buyer is
weak: independent labs are small, price-sensitive and already live with PDF delivery.
DIN EN 18029 is a standard, not a mandate, and may be implemented inside PIMS/LIMS
vendors rather than by a third party. The market is small, the wedge is a feature of an
established category, and this should be killed, not parked.

## Strongest supporting case

A real, persistent, practitioner-evidenced workflow failure (manual re-entry/attachment
of results) and a dated European standard published in April 2026. This is not enough:
the failure is already being solved by shipping products, and no buyer-side evidence
exists.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| Independent labs will pay for a results-delivery channel | Interview ≥5 labs; none willing to fund a pilot | untested (not tested — idea killed) |
| A semantic mapping layer is feasible across the long tail | Prototype 2 lab formats into 2 PIMS; measure hours | untested (not tested) |
| DataHub Vet/ManuCare cannot close the semantic gap first | Desk capability check of both products | untested (not tested) |
| The $30–50/clinic/month access-fee floor does not make the model unviable | Model pricing against that floor with a partner PIMS | untested (not tested) |

## Cheapest decisive experiment

- Assumption under test: a defensible wedge exists (i.e. no shipping product performs
  semantic lab-result delivery to the long tail).
- Proposed test: **desk-only capability check** of ManuCare, DataHub Vet and the
  IDEXX/Covetrus bundles, plus a check of whether any UK/IE independent lab already has a
  sanctioned structured import route. This is the test that would have to pass before any
  buyer-side test is worth running.
- Pre-fixed decision rule: proceed to a paid-pilot test only if no shipping product
  performs semantic lab-result delivery to the long tail and ≥2 named independent labs
  have no sanctioned structured import route; otherwise the idea stays killed.
- Cost bound: 4 human-hours, £0, 7 calendar days.
- Status: **not run — idea killed at the `defensible_wedge` hard filter.** Retained as
  the reopening test.
- Link: `ideas/vetlab-bridge/decision.md`

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-21 | (new) discovered -> desk-screened -> adversarially-researched | Promoted from observation O17; full research completed | `ideas/vetlab-bridge/decision.md` |
| 2026-09-21 | adversarially-researched -> killed | `defensible_wedge` hard-filter `fail` (ManuCare already markets universal lab-result import; feature of an established category) and `not_all_optimistic` `fail`; independent adversarial review (idea-critic) recommended kill. Scored 47.4/100, below the 65 threshold | `ideas/vetlab-bridge/decision.md` |
