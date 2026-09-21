# Experiment queue

- **Prepared by:** worker
- **Date:** 2026-09-21
- **Method version:** 1.3.0
- **Source:** `experiments/index.json` (status as of 2026-09-21, after the
  `bikpayroll-incumbent-capability` scan completed)

No experiment listed as requiring approval has been started. Only desk research
and self-authorised desk scans have run.

## Queue

| Idea | Experiment | Purpose / central assumption | Cost / human time | Approval required | Recommendation | Reason |
| - | - | - | - | - | - | - |
| reasonable-steps | `reasonable-steps-willingness` | The Employment Rights Act 2025 "all reasonable steps" duty creates enough demand for a paid evidence tool. Ten niche employers must commit ≥ £12/mo and one non-network channel must sustain ≥ 5 conversations. | £20 + 10h, 7 days | Yes (human) | **Run now (first priority)** | Cheapest decisive test in the queue and the only candidate parked mainly on `unknown` filters rather than a `fail`; it resolves eight unknowns at once. |
| aucly | `aucly-channel-test` | Unpaid direct outreach can make real PTAs launch a real auction (≥ 2 of 20 within 30 days). | £0 + 20h, 30 days | Yes (human) | **Run now (second priority)** | Distribution is Aucly's binding constraint (45 GSC clicks, 2,333 visitors → 0 accounts). Zero spend, but requires lawful-basis review per contact before any outreach. |
| geonerd | `geonerd-demand-spike` | Five UK accountancy practices will commit ≥ £19/mo for AI-visibility monitoring after a scan. | £50 + 20h, 7 days | Yes (human) | **Defer** | Review v2 is outstanding and may change the proposition; run only after the human routes the review and approves. It would resolve four unknown hard filters. |
| bikpayroll | `bikpayroll-incumbent-capability` | Benefit providers/payroll platforms would not already ingest per-period BiK data, leaving a third-party bridge. | £0 + 6h, 3 days | No (desk scan) | **Completed — cancel as a queue item** | Scan finished 2026-09-21 and met the pre-committed KILL branch: ≥ 2 platforms already ingest provider BiK data. Idea moved to `killed`. |

## Notes

- The three live experiments all await **human approval**; nothing starts until
  approval is recorded in `experiments/index.json` (`approval.granted = true`
  with a human approver and date) and, for any outreach, a lawful-basis check.
- Recommended order reflects information per unit of cost and founder time, not
  expected attractiveness: `reasonable-steps-willingness` first,
  `aucly-channel-test` second, `geonerd-demand-spike` only after the GeoNerd
  review is routed.
- No experiment in this list may contact people, spend money, publish, create
  accounts or make commitments without the human owner's explicit approval.
