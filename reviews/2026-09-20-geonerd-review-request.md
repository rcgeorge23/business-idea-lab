# Review request: GeoNerd: AI visibility digest for UK accountancy practices

- **Idea:** `geonerd`
- **Date:** 2026-09-20
- **Trigger:** proposed for validation-ready (bootstrap seed)
- **State:** `validation-ready`
- **Proposed transition:** not-required -> requested
- **Reviewed revision:** `327f02e`
- **Requested from:** ChatGPT (independent reviewer; not market validation)

## What the reviewer must decide

Whether `not-required -> requested` is justified by the evidence in this repository, or whether the idea should receive `changes-requested` or be `killed`.

## State and scores

| Dimension | Weight | Score | Confidence | Evidence |
|---|---|---|---|---|
| problem_severity_frequency | 15 | 3 | medium | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| buyer_budget_clarity | 15 | 3 | medium | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| evidence_strength | 15 | 3 | medium | `evidence/geonerd/2026-09-20-spike-findings.md` |
| distribution | 10 | 3 | medium | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| differentiation | 10 | 3 | medium | `evidence/geonerd/2026-09-20-competitive-teardown.md` |
| validation_speed_cost | 10 | 4 | high | `evidence/geonerd/2026-09-20-demand-validation-plan.md` |
| feasibility | 5 | 4 | medium | `evidence/geonerd/2026-09-20-spike-findings.md` |
| economics | 10 | 4 | medium | `evidence/geonerd/2026-09-20-wedge-strategy.md` |
| founder_fit | 5 | unscored | none | - |
| risk | 5 | 3 | medium | `evidence/geonerd/2026-09-20-competitive-teardown.md` |

- Weighted total: **65.3 / 100** (threshold 65, meets_threshold=True)
- Scored weight: 95 / 100
- Overall confidence: **medium**
- Evidence level: `Validation-ready`
- Vetoes: none

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | pass | Practice owner/partner is the decision maker; £19.99/mo is a small purchase against the value of one client. |
| painful_frequent_or_budgeted | pass | Assumed painful and recurring by analogy with search visibility tracking; desk evidence only (assumption A2). |
| non_paid_distribution | pass | Directory outreach, professional communities, SEO and a benchmark report are credible non-paid routes (assumption A4). |
| defensible_wedge | pass | Vertical depth + honest measurement + plain-language actions versus free checkers and £299/mo done-for-you services. |
| no_network_effects_needed | pass | Market-level prompt set is usable by a single customer; benchmarks improve with density but are not required for value. |
| plausible_margins | pass | Modelled contribution positive at >=10 customers per market at £19.99/mo; cost model untested. |
| acceptable_risk | pass | No personal data beyond submitted email; claims about AI answers are reproducible and disclaimered. |
| cheap_disconfirming_test | pass | £50 / 20 human-hours / 1-week demand spike with a pre-fixed decision rule can falsify the central assumption. |
| not_all_optimistic | pass | Stop rules fire on 0/5 commitments and on incumbent satisfaction; iterate path is defined. |

## Strongest supporting case

- Accountancy is dense in shared AI buying questions, the buyer is identifiable
  and reachable through non-paid professional communities, and the incumbent
  landscape leaves a genuine gap between free checkers and £299/mo
  done-for-you services. A £19.99/mo decision aid is a rounding error against
  the value of one new client, and the "honest measurement" angle is a credible
  response to documented UI/API noise (6–24% brand overlap).

## Strongest disconfirming case

- The wedge may be an artefact of desk research. TendorAI already sells AI
  visibility to UK accountants and SearchScore has audited 1,038 UK accountancy
  firms; if either satisfies even two of five interviewed practices, the stop
  rule fires. Owners may treat the free scan as a one-off curiosity and never
  pay monthly ("nice to know, not worth £20"). The honest-measurement
  positioning may actively reduce perceived value by admitting the number is
  noisy. If collection costs land at the top of the modelled range or API
  proxies are indefensible, unit economics fail at any reachable density. None
  of these has been tested.

## Unresolved assumptions

- A1: owners/partners of 1–20-staff practices will personally pay ≥£19/mo for a
  monthly digest.
- A2: AI invisibility is a felt, frequent problem for them (not merely
  interesting when shown).
- A3: the free scan creates enough pull to yield ≥25% email capture.
- A4: at least one non-paid channel produces conversations with non-network
  practices.
- A5: collection cost stays ≤£95/market/month at launch, or an API-equivalent
  proxy is defensible.
- A6: the contractor/IR35 specialism is the right beachhead rather than "small
  practice serving local SMEs".
- A7: monthly cadence matches the buyer's decision rhythm.

## Cheapest decisive experiment

The 1-week demand spike in `experiments/geonerd-demand-spike/plan.md`: five
conversations with target practices, a manual scan for each, a within-subject
£9/£19/£29 price ladder, and a pre-fixed decision rule (≥2 of 5 commit at
≥£19/mo **and** ≥25% email capture **and** ≥1 non-network conversation).
Estimated bound: £50, 20 human-hours, 7 calendar days — at the review
threshold, not above it. Falsification target: A1 and A3.

## Experiment register

- `geonerd-demand-spike` status=`proposed` approval.granted=`False` plan=`experiments/geonerd-demand-spike/plan.md` results=`none`
  - Central assumption: Owner-partners of 1-20-staff UK accountancy practices will pay at least £19/month for a monthly AI visibility digest after seeing a free scan.
  - Kill condition: Zero of five interviewed practices make any concrete commitment at any price, or the dominant reaction is 'interesting but I would not pay' after the iterate week, or interviewed practices already pay for a satisfying incumbent.

## Decision record

Initial ledger entry. GeoNerd was seeded from the existing research repository
`/home/richard/projects/geonerd` @ `327f02e` as a single bootstrap idea at
`validation-ready`, with an independent review requested and the demand
validation spike registered as a proposed experiment. No worker run has been
executed against this repository yet.

## Machine-readable review block

```json
{
  "status": "requested",
  "requested_from": "ChatGPT (independent reviewer)",
  "request_path": "reviews/2026-09-20-geonerd-review-request.md",
  "last_reviewed_revision": null,
  "history": [
    {
      "date": "2026-09-20",
      "from": "not-required",
      "to": "requested",
      "actor": "bootstrap",
      "reason": "Bootstrap seed at validation-ready under issue #1; independent review requested because the idea is proposed at an advanced state."
    }
  ]
}
```

## Instructions to the reviewer

1. Work only from the repository artefacts listed below. Do not fetch or assume outside data.
2. Attack the weakest link: unsupported inference, convenience evidence, mis-scored dimension, premature advancement, missed legal/platform risk, or a hard filter that should have failed.
3. State a verdict: `changes-requested`, `approved`, or `killed`.
4. For each finding, give the evidence checked and the condition that would change the verdict.
5. Write the response as `reviews/2026-09-20-geonerd-<reviewer>-<model>.md` following `templates/review/response.md`.
6. A second model is not market validation. Agreement is not demand evidence and cannot advance the idea beyond `validation-ready`.

## Artefacts for review

- `ideas/geonerd/dossier.md`
- `ideas/geonerd/scorecard.json`
- `ideas/geonerd/decision.md`
- `evidence/geonerd/`
- `experiments/index.json`
- `ideas/index.json`

