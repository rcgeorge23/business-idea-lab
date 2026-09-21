# Scorecard

Method version: see `method/VERSION`. Weights version: `1.0.0`.

Scores are integers 0-5 per dimension. Every score is linked to evidence; unsupported
dimensions score `null` and are excluded from the aggregate (see
`method/evidence-policy.md`). Confidence is recorded per dimension and separately as an
overall confidence.

## Dimensions and weights

| Key | Dimension | Weight | What a 3 ("adequate") looks like |
|---|---|---|---|
| `problem_severity_frequency` | Problem severity + frequency | 15 | The problem is recurring and costly enough that a named buyer should already spend money somewhere |
| `buyer_budget_clarity` | Buyer + budget clarity | 15 | A specific role owns the problem and a plausible existing budget line exists (not proven) |
| `evidence_strength` | Evidence strength | 15 | Credible secondary evidence, no fatal objection; no primary evidence |
| `distribution` | Distribution | 10 | A credible route to the first 10 buyers that does not require paid acquisition |
| `differentiation` | Differentiation | 10 | A stated wedge against the cheapest credible incumbent that is more than price |
| `validation_speed_cost` | Validation speed + cost | 10 | A decisive test can be run in weeks and within a documented cost bound |
| `feasibility` | Feasibility | 5 | Buildable and operable by a small team with known technology; no heroics |
| `economics` | Economics | 10 | Plausible contribution margin at realistic density/scale, with assumptions stated |
| `founder_fit` | Founder fit | 5 | The founder can credibly reach the buyer and do the work; evidence required (null if unknown) |
| `risk` | Legal/regulatory/platform/trust risk | 5 | Manageable risks with no veto-level exposure |

Score anchors: `0` = hostile or no basis; `1` = weak; `2` = below the bar;
`3` = adequate/plausible; `4` = strong; `5` = exceptional, primary evidence.

No-score rule: `null` when no evidence exists for the dimension. A score is never
inferred from another dimension's evidence.

## Aggregate

```
raw_points      = sum(weight * score / 5)      over scored dimensions
scored_weight   = sum(weight)                  over scored dimensions
weighted_total  = round(raw_points / scored_weight * 100, 1)
```

Normalisation by `scored_weight` means unscored dimensions neither help nor punish, but
they are reported and they cap confidence. At least 8 of 10 dimensions must be scored
for a `validation-ready` proposal; `problem_severity_frequency`, `buyer_budget_clarity`
and `evidence_strength` must always be scored and must each be >= 3.

## Threshold for `validation-ready`

An idea may be proposed for `validation-ready` only if all of:

1. `weighted_total >= 65`
2. all hard filters `pass` (no `fail`, `defer` or `unknown`)
3. no active veto
4. the three gating dimensions are scored >= 3
5. at least 8 dimensions are scored
6. overall confidence is `medium` or `high`
7. review has been triggered (`review.status != not-required`) per `method/review-policy.md`

The aggregate never overrides a hard veto. A single veto-level finding kills or parks
the idea regardless of score.

## Confidence

- Per dimension: `high` | `medium` | `low` | `none` (when `null`).
- Overall confidence: the lowest confidence among scored gating dimensions, downgraded
  one step if more than two dimensions are unscored. Recorded in `scorecard.json` as
  `confidence`.

## Hard filters

Recorded in `scorecard.json` under `hard_filters`, each with `status`
(`pass` | `fail` | `defer` | `unknown`) and a one-line note:

| Key | Filter |
|---|---|
| `economic_buyer` | There is a clear economic buyer |
| `painful_frequent_or_budgeted` | Evidence of a painful/frequent problem or an existing budget |
| `non_paid_distribution` | A credible route to early buyers without paid acquisition |
| `defensible_wedge` | Not commodity positioning; a defensible wedge exists |
| `no_network_effects_needed` | Value exists before network effects |
| `plausible_margins` | Plausible margins; no disproportionate service burden |
| `acceptable_risk` | Legal/regulatory/privacy/trust/platform risk is acceptable |
| `cheap_disconfirming_test` | A cheap test capable of disconfirming evidence exists |
| `not_all_optimistic` | Viability does not require every optimistic assumption to be true |

## Vetoes

`vetoes` is a list of `{key, note, date}`. Any active veto overrides the aggregate and
forces `killed` or `adversarially-researched` (parked) with the reason recorded.

## Worked example (GeoNerd, bootstrap seed)

Weights 15/15/15/10/10/10/5/10/5/5. Scores: problem 3, buyer 3, evidence 3,
distribution 3, differentiation 3, validation speed/cost 4, feasibility 4, economics 4,
founder fit `null` (no evidence), risk 3.

```
raw_points    = 9 + 9 + 9 + 6 + 6 + 8 + 4 + 8 + 3 = 62
scored_weight = 95
weighted_total = 62 / 95 * 100 = 65.3   -> meets the 65 threshold
```

Founder fit is excluded rather than scored, and overall confidence is capped at
`medium`. (`founder_fit` is intentionally `null` until evidence about the actual founder
exists; the human owner can supply it.)
