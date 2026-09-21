# Scorecard

Method version: see `method/VERSION`. Weights version: `1.2.0`.

Scores are integers 0-5 per dimension. Every score is linked to evidence; unsupported
dimensions score `null` and are excluded from the aggregate (see
`method/evidence-policy.md`). Confidence is recorded per dimension and separately as an
overall confidence.

**Scores measure demonstrated strength, not plausibility.** A coherent story, an analogy,
a spreadsheet of modelled economics or a competitor's existence does not establish that
this business works. The weights version separates three levels explicitly:

- a claim that is *plausible but undemonstrated* caps a dimension at **2**;
- a score of **3** requires affirmative evidence about this buyer and market;
- scores of **4-5** require independent evidence or primary signals.

## Dimensions and weights

| Key | Dimension | Weight | What a 3 ("adequate") looks like |
|---|---|---|---|
| `problem_severity_frequency` | Problem severity + frequency | 15 | Evidence that this named buyer experiences the problem frequently/costly; a market-context argument is only a 2 |
| `buyer_budget_clarity` | Buyer + budget clarity | 15 | Buyer identified AND evidence that this buyer already pays for comparable tools/services; an inferred budget is a 2 |
| `evidence_strength` | Evidence strength | 15 | Credible secondary evidence about this buyer/market, no fatal objection; category analogy is a 2 |
| `distribution` | Distribution | 10 | A credible non-paid route to the first 10 buyers WITH evidence the channel reaches them; a plausible channel list is a 2 |
| `differentiation` | Differentiation | 10 | An evidenced wedge the cheapest credible incumbent does not already offer; direct incumbent overlap caps this at 2 |
| `validation_speed_cost` | Validation speed + cost | 10 | A decisive test can be run in weeks and within a documented cost bound |
| `feasibility` | Feasibility | 5 | Buildable and operable by a small team with known technology; unproven collection/ops steps cap at 3 |
| `economics` | Economics | 10 | Plausible contribution margin at realistic density/scale, with assumptions stated and at least one input tested; modelled-only caps at 2 |
| `founder_fit` | Founder fit | 5 | The founder can credibly reach the buyer and do the work; evidence required (null if unknown) |
| `risk` | Legal/regulatory/platform/trust risk | 5 | Manageable risks with no veto-level exposure |

Score anchors: `0` = hostile or no basis; `1` = weak/no source; `2` = plausible but
undemonstrated (assumption, analogy, model); `3` = adequate, evidenced for this
buyer/market; `4` = strong, multiple independent sources or early primary signals;
`5` = exceptional, primary evidence.

Hard caps that must be applied and stated in the rationale:

- untested/modelled economics: `economics <= 2`, confidence `low`;
- direct incumbent already contests the wedge: `differentiation <= 2`;
- distribution channels plausible but no prospects produced: `distribution <= 2`;
- problem asserted by analogy: `problem_severity_frequency <= 2`;
- missing or unevidenced why-now at `Plausible`/`Promising`: `differentiation <= 2` and
  `problem_severity_frequency <= 2`. The cap is **archetype-aware (v1.6.0)**: it applies
  unchanged to change-driven candidates; for persistent-market-failure candidates it is
  lifted only by an evidence-backed persistence thesis meeting BOTH parts of the test in
  `method/discovery.md` (continued pain/workaround despite alternatives AND a credible
  persistence mechanism). A weak, absent or speculative persistence thesis leaves the
  cap in place; the thesis is not a scoring bonus;
- the wedge is a feature of an established category, not a product: the candidate fails
  the `defensible_wedge` hard filter (not just a score reduction).

Competitor existence is not adequate occupation. `differentiation <= 2` and a
`defensible_wedge` failure both require evidence that a credible alternative actually
occupies the exact proposed seam for the defined buyer - not merely that competing
products exist, are advertised, or ship an adjacent feature. Where such evidence exists,
the cap and the hard filter apply exactly as before.

No-score rule: `null` when no evidence exists for the dimension. A score is never
inferred from another dimension's evidence, and a score is never raised because a
hard-filter unknown "seems likely".

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
2. no hard filter `fail`
3. no active veto
4. the three gating dimensions are scored >= 3
5. at least 8 dimensions are scored
6. overall confidence is `medium` or `high`
7. review has been triggered (`review.status != not-required`) per `method/review-policy.md`
8. every `unknown` hard filter names the experiment measurement that will resolve it

The threshold was deliberately **not lowered** in v1.1.0 even though tightening the
rubric makes it harder to reach: moving a goalpost to preserve a previous score would
defeat the purpose. An honest desk-only idea now typically lands in the 45-60 range and
stays at `adversarially-researched`. That is not a verdict: a parked idea can still carry
a proposed experiment (see `method/lifecycle.md`), and external results are the route
back to `validation-ready` with a higher evidence level.

The aggregate never overrides a hard veto. A single veto-level finding kills or parks
the idea regardless of score.

## Confidence

- Per dimension: `high` | `medium` | `low` | `none` (when `null`).
- Overall confidence: the lowest confidence among scored gating dimensions, downgraded
  one step if more than two dimensions are unscored. Recorded in `scorecard.json` as
  `confidence`.
- Model outputs, analogies and vendor marketing are at most `low`; named secondary
  sources about the buyer/market are `medium`; primary evidence is `high`.

## Hard filters

Recorded in `scorecard.json` under `hard_filters`. Each filter has:

- `status`: `pass` | `unknown` | `fail`
- `note`: one line of reasoning
- `evidence`: list of sources that affirmatively support a `pass` (required non-empty
  for `pass`; empty otherwise)
- `resolve_via`: the cheap measurement or check that would settle an `unknown`
  (required non-empty for `unknown`)

Semantics (v1.1.0):

- **`pass`** means the available evidence affirmatively supports the filter. An
  assumption, an analogy, a coherent narrative or "the model can describe a wedge"
  cannot produce a pass - pass requires at least one cited source.
- **`unknown`** means plausible but not demonstrated. It is a legitimate state and may
  exist at any lifecycle state, but it contributes no positive evidence, must never be
  reported as resolved, and at `validation-ready` must be named in the experiment.
- **`fail`** means evidence materially contradicts the filter. Any `fail` kills the idea
  (or, if contested, parks it for review with the failure recorded).

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

## Worked example (GeoNerd, rescored under 1.1.0)

Weights 15/15/15/10/10/10/5/10/5/5. Scores: problem 2 (pain inferred, not evidenced),
buyer 3 (incumbent pricing to the same buyer is evidence of a budget line), evidence 2
(category analysis, no buyer evidence), distribution 2 (channels plausible, no
prospects), differentiation 2 (TendorAI/SearchScore already contest AI visibility for
UK accountants), validation speed/cost 4, feasibility 3 (manual test feasible, pipeline
unproven), economics 2 (modelled with untested density/cost), founder fit `null`, risk 3.

```
raw_points    = 6 + 9 + 6 + 4 + 4 + 8 + 3 + 4 + 3 = 47
scored_weight = 95
weighted_total = 47 / 95 * 100 = 49.5   -> below the 65 threshold
```

The earlier 65.3 was produced by scoring inferred pain, plausible distribution and
modelled economics as if they were demonstrated. Under 1.1.0 the honest result is 49.5,
so GeoNerd is parked at `adversarially-researched` rather than carried at
`validation-ready`; its proposed demand experiment remains the cheapest way to resolve
the unknowns. Founder fit stays `null` until real evidence about the actual founder
exists.
