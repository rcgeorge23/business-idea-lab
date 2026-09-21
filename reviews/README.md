# reviews/ — independent review packages and outcomes

Review is repository-mediated: the reviewer works only from committed artefacts
and writes a response file here. Full policy in `method/review-policy.md`.

- **Request:** `reviews/<YYYY-MM-DD>-<slug>-review-request.md`, generated with
  `python3 scripts/build_review_request.py --slug <slug> --trigger "..." --transition "..."`.
- **Response:** `reviews/<YYYY-MM-DD>-<slug>-<reviewer>-<model>.md`, following
  `templates/review/response.md`.
- **States:** `not-required -> requested -> changes-requested | approved | killed`.
  History is append-only in `ideas/<slug>/scorecard.json` (`review.history`).
- The worker must respond to a `changes-requested` review explicitly at the
  start of its next run; it must never silently overwrite an outcome.

A review request is triggered by: proposing `validation-ready`; material method
or threshold changes; contradictory or low-confidence evidence carrying a high
score; material legal/privacy/trust/platform risk; an experiment above the
20-human-hour / £100 threshold; every fifth killed idea (false-negative audit);
or a human request.

A second model (ChatGPT) is **not** independent market validation. It can only
challenge the evidence chain, never supply demand evidence.
