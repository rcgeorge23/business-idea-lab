# Experiment plan: One-week demand validation spike for the GeoNerd wedge

- **ID:** `geonerd-demand-spike`
- **Idea:** `geonerd`
- **Created:** 2026-09-20
- **Status:** proposed
- **Approval:** required (human owner) — not yet granted
- **Source:** adapted from `/home/richard/projects/geonerd/docs/demand-validation-plan.md` @ `327f02e`

## Central assumption

Owner-partners of 1–20-staff UK accountancy practices will pay at least
£19/month for a monthly AI visibility digest after seeing a free scan.

## Hypothesis

If five target practices are shown a manually-produced scan report and walked
through a within-subject £9/£19/£29 price ladder, then at least two will make a
concrete commitment at ≥£19/mo, because one new client is worth far more than
the subscription and the report names specific, actionable gaps.

## Test design

- **Population / sample:** 5 UK accountancy practices, 1–20 staff, owner or
  partner is the decision maker, contractor/IR35 or small-practice specialism;
  ≥3 of 5 recruited outside the founder's personal network.
- **What participants see or do:** a one-page scan report (12 highest-intent
  prompts, one ChatGPT consumer-UI run each, brands and cited sources recorded),
  a 15–20 minute scripted interview, and the £9/£19/£29 price ladder with a
  commitment question.
- **Recruitment route:** public directories (ICAEW/ACCA find-an-accountant,
  Google Maps), a community post of the aggregate benchmark, referral request at
  the end of each conversation. No paid acquisition.
- **Instrumentation:** the ten events defined in the source plan
  (`landing_view`, `scan_start`, `scan_complete`, `report_open`, `email_submit`,
  `call_booked`, `call_held`, `commitment`, `return_scan`, `digest_open`),
  recorded from the first visitor; verbatim quotes for price reactions and
  objections.
- **Timebox:** 7 calendar days, per the day-by-day schedule in the source plan.
- **Deliberately NOT included:** automated measurement pipeline validation,
  retention beyond 30 days, CAC, any paid traffic, any product build.

## Decision rule (fixed before running)

| Outcome | Verdict | Action |
|---|---|---|
| ≥2/5 commit at ≥£19/mo **and** ≥25% of scan completers submit email **and** ≥1 non-network channel produces a conversation | proceed | Prepare an MVP proposal for human review; no build without approval |
| Exactly 1 commitment, or consistent £9 choice, or email capture works but no conversations | iterate | One more week with revised positioning/price/report |
| 0/5 commit at any price, or "interesting but wouldn't pay" persists, or incumbents already satisfy participants | stop | Record and close the spike; do not build |

## Kill condition

Zero of five practices make any concrete commitment at any price — or the
dominant reaction after the iterate week is "interesting but I would not pay" —
or the interviewed practices already pay for an incumbent that satisfies them.

## Cost bound

- Money: GBP 50
- Human hours: 20
- Calendar days: 7

(At the review-policy threshold, not above it; a human owner must approve before
any execution.)

## Risks and safeguards

- **No contact, spend, publication or account creation happens until the human
  owner records approval in `experiments/index.json`** (`approval.granted: true`
  with name and date) and in `experiments/geonerd-demand-spike/results.md`.
- Personal-relationship participants are disclosed and excluded from the
  decision gate; ≥3 of 5 conversations must be non-network.
- Instrumentation records no PII beyond the email a participant submits.
- The report is presented as a sample of one run with a stated noise caveat; no
  precision is claimed.
- If the decision rule outcome is ambiguous, record it as ambiguous rather than
  reinterpreting the threshold after the fact.

## Results

Not yet run. Results will be recorded in
`experiments/geonerd-demand-spike/results.md` and applied mechanically to the
decision rule above.
