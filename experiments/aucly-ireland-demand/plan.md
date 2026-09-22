# Experiment plan: Ireland demand probe for Aucly (discriminating expansion test)

- **ID:** `aucly-ireland-demand`
- **Idea:** `aucly`
- **Created:** 2026-09-22
- **Status:** proposed
- **Approval:** required (human owner) — not yet granted
- **Source:** proposed by the 2026-09-22 locale-expansion assessment; refs
  `ideas/aucly/expansion-assessment.md`,
  `evidence/aucly/2026-09-22-locale-market-and-incumbents.md`,
  `evidence/aucly/2026-09-22-locale-regulation-and-tax.md`

## Central assumption

Unmet demand exists in Ireland for a flat-fee, no-commission, self-service school
auction tool **despite free or low-cost incumbents** (Fundraising Solutions zero
platform fee; iDonate.ie low transaction fees; GalaBid ROI), and a UK-run provider
can reach Irish primary-school PTAs without paid acquisition.

## Hypothesis

If 20 Irish primary-school PTA organisers are approached directly (publicly listed
organisational contact addresses, no paid advertising) with a locally relevant case
study and free-tier setup help, then at least 2 will launch a real auction within
30 days at zero paid spend, because the offer removes both setup friction and
commission.

## Test design

- **Population / sample:** 20 Irish primary-school PTAs / school fundraisers,
  recruited outside any existing customer or personal network. Organisational
  contact addresses only; no personal data beyond the organisational contact.
- **What participants see or do:** a short outreach message referencing a
  comparable real auction outcome and the free tier, offering hands-on setup; a
  15-minute call if they reply; a real auction if they proceed. The free tier is
  used deliberately so that no Irish VAT arises during the test.
- **Recruitment route:** direct outreach only. No paid traffic, no purchased lists,
  no scraping of personal data. Check the lawful basis for each contact before any
  message is sent; exclude contacts where a lawful basis is unclear.
- **Instrumentation (manual, recorded in results):** contacts attempted, bounces,
  replies, calls held, auctions configured, auctions launched, amount raised,
  free-tier vs paid tier, the platform the organiser used previously, and whether
  the organiser says they would run another auction next year.
- **Timebox:** 30 calendar days from approval, outreach spread over the first 14
  days.
- **Dependency / sequencing:** this probe is only informative **in combination with
  `aucly-channel-test`**. It must not be run as a substitute for it. See the
  decision rule below.
- **Deliberately NOT included:** paid acquisition, new product features, localised
  branding build-out, EUR pricing changes, SEO work, tax registration.

## Decision rule (fixed before running)

| Outcome | Verdict | Action |
|---|---|---|
| UK test fails AND ≥2 of 20 Irish contacts launch within 30 days at zero paid spend | expand-signal | The home failure may be market-specific; propose a small IE retention/pricing test before any build |
| UK test fails AND ≤1 of 20 Irish contacts launch | do-not-expand | Channel problem, not a geography problem; record and do not fund expansion |
| UK test succeeds | defer | Address the home market first; portability can be retested later on proven mechanics |
| 0 launches and the dominant objection is a satisfactory free platform | stop | Record the free-incumbent barrier as the reason; do not retry another locale on the same hypothesis |
| Outreach blocked by legal/permission constraints | record | Report as untested, not failed |

## Kill condition

Zero of the 20 Irish organisations launch an auction within 30 days and the
dominant response is that a free or low-cost platform already satisfies them — or
that they do not run auctions.

## Cost bound

- Money: GBP 0 (free tier avoids Irish VAT on paid tiers during the test)
- Human hours: 20
- Calendar days: 30

(At the review-policy threshold, not above it; a human owner must approve before
any contact, and no message may be sent until approval is recorded.)

## Risks and safeguards

- **No contact happens until the human owner records approval in
  `experiments/index.json`** (`approval.granted: true` with name and date) and in
  `experiments/aucly-ireland-demand/results.md`.
- Direct marketing compliance: organisational contacts only; lawful-basis check per
  contact under Irish ePrivacy/DPC guidance and the GDPR; no purchased lists;
  opt-out honoured immediately; unanswered contacts not chased more than once. A UK
  controller contacting Irish individuals may require an EEA representative under
  GDPR Article 27; confirm before sending.
- Charity-sector sensitivity: approach school/PTA organisational addresses, not
  individual parents; do not imply endorsement by the Charities Regulator.
- If the decision rule outcome is ambiguous, record it as ambiguous rather than
  reinterpreting the threshold after the fact.

## Results

Not yet run. Results will be recorded in
`experiments/aucly-ireland-demand/results.md` and applied mechanically to the
decision rule above.
