# Experiment plan: Direct unpaid outreach channel test for Aucly

- **ID:** `aucly-channel-test`
- **Idea:** `aucly`
- **Created:** 2026-09-21
- **Status:** proposed
- **Approval:** required (human owner) — not yet granted
- **Source:** proposed during the issue #3 Aucly calibration; refs
  `evidence/aucly/2026-09-21-seo-and-acquisition.md`,
  `evidence/aucly/2026-09-21-live-auctions-and-customers.md`

## Central assumption

UK primary-school PTAs, schools and small charities will launch a real auction
through direct, unpaid outreach supported by an existing case study and free
setup help — i.e. early distribution does not require paid acquisition.

## Hypothesis

If 20 UK primary-school PTA organisers are approached directly (publicly listed
organisational contact addresses, no paid advertising) with the Furzedown case
study (44 lots, 63 bidders, £2,265 raised) and an offer to configure their
auction at no fee, then at least 2 will launch a real auction within 30 days,
because the case study is concrete proof from a comparable organisation and the
main friction (setup) is removed.

## Test design

- **Population / sample:** 20 UK primary-school PTAs / small school
  fundraisers, recruited outside the founder's existing customer or personal
  network. Organisational contact addresses only (e.g. published PTA/school
  office addresses); no personal data beyond the organisational contact.
- **What participants see or do:** a short outreach message linking the
  Furzedown case study and the free-tier pricing page, offering hands-on setup;
  a 15-minute call if they reply; a real auction if they proceed.
- **Recruitment route:** direct outreach only. No paid traffic, no purchased
  lists, no scraping of personal data. Check lawful basis for each contact
  (PECR/UK GDPR) before any message is sent; exclude contacts where a lawful
  basis is unclear.
- **Instrumentation (manual, recorded in results):** contacts attempted,
  bounces, replies, calls held, auctions configured, auctions launched, items
  sold, amount raised, free-tier vs paid tier, and whether the organiser says
  they would run another auction next year.
- **Timebox:** 30 calendar days from approval, outreach spread over the first
  14 days.
- **Deliberately NOT included:** paid acquisition, new product features,
  branding work, SEO changes, retention beyond one auction cycle.

## Decision rule (fixed before running)

| Outcome | Verdict | Action |
|---|---|---|
| ≥2 of 20 contacts launch a real auction within 30 days at zero paid spend | proceed | Record as demand+distribution evidence and propose a retention/pricing follow-up test |
| Exactly 1 launch, or several serious conversations blocked by setup effort rather than willingness | iterate | One more outreach round with a revised offer/segment (e.g. charities rather than PTAs) |
| 0 launches and the dominant objection is incumbent satisfaction, no need, or the effort/benefit ratio | stop | Record and stop; do not invest further in this channel without new evidence |
| Outreach is blocked by legal/permission constraints before it can run | record | Do not proceed; report as untested rather than failed |

## Kill condition

Zero of the 20 organisations launch an auction within 30 days and the dominant
response is that they already use a satisfactory platform, do not run auctions,
or see no benefit — or the founder's time per launch is so high that the
channel cannot be repeated without paid help.

## Cost bound

- Money: GBP 0
- Human hours: 20
- Calendar days: 30

(At the review-policy threshold, not above it; a human owner must approve before
any contact, and no message may be sent until approval is recorded.)

## Risks and safeguards

- **No contact happens until the human owner records approval in
  `experiments/index.json`** (`approval.granted: true` with name and date) and
  in `experiments/aucly-channel-test/results.md`.
- Direct marketing compliance: organisational contacts only; PECR/UK GDPR
  lawful-basis check per contact; no purchased lists; opt-out honoured
  immediately; unanswered contacts not chased more than once.
- The case study names Furzedown Primary PTA, which is already published by
  Aucly; no new customer is named without permission.
- If the decision rule outcome is ambiguous, record it as ambiguous rather than
  reinterpreting the threshold after the fact.

## Results

Not yet run. Results will be recorded in
`experiments/aucly-channel-test/results.md` and applied mechanically to the
decision rule above.
