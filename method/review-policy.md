# Review Policy

Method version: see `method/VERSION`.

Reviews are how a second model (ChatGPT) and the human owner oversee the worker. Reviews
happen through committed artefacts, not shared chat. The reviewer must be able to work
from the repository alone.

## When a review is required

Trigger a review request when any of these is true:

1. An idea is proposed for `validation-ready`.
2. Scoring weights, evidence rules, or lifecycle thresholds change materially.
3. A high score rests on contradictory or low-confidence evidence.
4. There is material legal, regulatory, privacy, trust, safety or platform risk.
5. A proposed experiment exceeds 20 human-hours or GBP 100 projected effort.
6. Every 5th killed idea (false-negative audit; sample the oldest un-audited one).
7. The human owner asks.

## When a review is not required

Routine formatting, source capture, obvious hard-filter rejections, dossier updates that
do not change state or scores, and unchanged low-activity runs do not need a review
request. The worker proceeds and records normally.

## States

```
not-required -> requested -> changes-requested | approved | killed
```

- `not-required`: no trigger applies.
- `requested`: worker wrote the review request and set it in `scorecard.json#review`.
  Only the worker/human may set this.
- `changes-requested`: reviewer requires more evidence or a correction. The worker MUST
  respond in the next run: address each point with new evidence or a documented
  concession; never overwrite the review.
- `approved`: the reviewer agrees with the proposal. This is a gate, not validation: it
  still does not permit external action without human approval.
- `killed`: the reviewer's case is strong enough that the idea should stop. The worker
  moves the idea to `killed` (or raises a new, evidence-backed review request disputing
  it; the disagreeing state is recorded, and the idea does not advance until resolved).

Every state change appends to `scorecard.json#review.history`:

```json
{
  "date": "YYYY-MM-DD",
  "from": "not-required",
  "to": "requested",
  "actor": "worker | human-owner | reviewer",
  "reviewer": "chatgpt",
  "model": "gpt-5.x or null",
  "reason": "why",
  "revision": "git sha or commit",
  "artefacts": ["path", "..."]
}
```

History is append-only. Reviews are also preserved as files in `reviews/` (see below).

## Request package

`scripts/build_review_request.py` generates `reviews/<date>-<slug>-review-request.md`
containing, for the idea under review:

- the lifecycle state and proposed transition;
- score and confidence per dimension, with the aggregate and threshold;
- hard-filter results and any vetoes;
- dated evidence links (path + one-line summary);
- the strongest supporting case and the strongest disconfirming case;
- unresolved assumptions;
- the cheapest decisive experiment with its pre-fixed decision rule;
- the machine-readable review block (`scorecard.json#review`);
- explicit instructions for the reviewer and where to write the response.

The worker must not paraphrase away inconvenient evidence; disconfirming findings appear
in the package.

## Response files

Reviewer responses are saved as `reviews/<date>-<slug>-<reviewer>-<model>.md`
(example: `2026-09-20-geonerd-chatgpt.md`) using `templates/review/response.md`. The
human owner (or the worker transcribing the reviewer's exact text) records:

- verdict (`changes-requested` | `approved` | `killed`);
- reviewer, provider/model, date, reviewed revision;
- per-point reasoning, including any evidence the reviewer checked;
- the condition that would change the verdict.

The worker then updates `scorecard.json#review.status` and `review.history`, and
`ideas/index.json` if the state changes. The worker's response to each point is written
in the next run summary and, where relevant, the dossier.

## False-negative audits

Killed ideas are sampled: every 5th kill triggers an audit by the reviewer, which asks
whether the kill was correct and what evidence would have changed it. The audit result
is recorded in the killed idea's decision record (`## False-negative audit`). An idea
may return to `desk-screened` only via a new decision record with genuinely new
evidence, not via re-argument.

## Reviewer independence

The reviewer is never market validation. A second model's agreement is a quality signal
about the reasoning, nothing more. No state beyond `validation-ready` is reachable
without real-world evidence recorded under `experiments/`.
