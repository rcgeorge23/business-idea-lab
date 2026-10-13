# Scorecard

Method version: see `method/VERSION`. Current weights version: `1.3.0` (schema
version 2). Legacy weights version: `1.2.0` (schema version 1).

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

## Schema versions and migration (v1.9.0)

The 1.9.0 pivot adds two dimensions, three hard filters and a required
`seo_assessment` block. This is done as **schema version 2** so that historic
scorecards are preserved exactly as they were recorded:

| | Schema v1 (legacy) | Schema v2 (current) |
|---|---|---|
| `schema_version` | `1` | `2` |
| `weights_version` | `1.2.0` | `1.3.0` |
| method versions | `<= 1.8.2` | `>= 1.9.0` |
| dimensions | 10, weights sum 100 | 12, weights sum 100 |
| scored-dimension minimum | 8 of 10 | 9 of 12 |
| hard filters | 9 | 12 |
| `seo_assessment` | not present | required |
| `why_now.strength` | `strong` \| `weak` \| `absent` | also `not-required` |

Rules:

1. **Historic scorecards are never rewritten.** A scorecard recorded under an earlier
   method keeps its original `method_version`, `weights_version` and scores. Its
   aggregate was computed on the v1 table and is still recomputed on that table.
2. **New scorecards use schema v2.** A scorecard at schema v2 must record
   `weights_version` `1.3.0` and a `method_version` of 1.9.0 or later.
3. **A scorecard at schema v1 must record** `weights_version` `1.2.0` and a
   `method_version` no later than 1.8.2; a v1 card under a later method is an error
   (migrate the entry by recording a new v2 scorecard, not by editing the old one).
4. **Migration is by re-triage, not rewrite.** Owners may opt in to re-triaging a legacy
   idea under the v2 criteria (see `method/retriage.md`). A re-triage records a new,
   clearly labelled memo or scorecard in addition to the historic one; the old scorecard
   and decision record remain untouched and auditable.
5. `weights_version` identifies the scoring table used; the ledger's aggregate for each
   entry is always recomputed against the table that its own card names.

## Dimensions and weights (schema v2, weights 1.3.0)

| Key | Dimension | Weight | What a 3 ("adequate") looks like |
|---|---|---|---|
| `problem_severity_frequency` | Problem severity + frequency | 12 | Evidence that this named buyer experiences the problem frequently/costly; a market-context argument is only a 2 |
| `buyer_budget_clarity` | Buyer + budget clarity | 12 | Buyer identified AND evidence that this buyer already pays for comparable tools/services; an inferred budget is a 2 |
| `evidence_strength` | Evidence strength | 12 | Credible secondary evidence about this buyer/market, no fatal objection; category analogy is a 2 |
| `seo_discoverability` | SEO-led discoverability | 14 | At least one dated, named query cluster with SERP evidence and a credible organic entry path for a new entrant; demand evidence beyond search volume alone. A plausible query list without SERP evidence is a 2 |
| `self_service_fit` | Self-service fit | 10 | A credible self-serve purchase and delivery path (signup, self-guided onboarding, payment, no mandatory demo/call/hand-holding), evidenced by comparable products' mechanics or a concrete product design; any required hand-holding caps at 2 |
| `distribution` | Other non-paid distribution | 5 | A credible non-search, non-paid route to the first buyers WITH evidence the channel reaches them; a plausible channel list is a 2 |
| `founder_fit` | Founder fit | 10 | The solo, part-time founder can credibly build, operate, support and maintain it at the modelled scale; build complexity, owner time, support burden and external dependencies evidenced; unknown is `null` |
| `economics` | Economics | 8 | Plausible contribution margin at realistic density/scale, with assumptions stated and at least one input tested; modelled-only caps at 2; pricing vs traffic economics (conversion assumptions) stated as assumptions |
| `validation_speed_cost` | Validation speed + cost | 7 | A decisive test can be run in weeks and within a documented cost bound |
| `feasibility` | Feasibility | 3 | Buildable and operable by a small team with known technology; unproven collection/ops steps cap at 3 |
| `differentiation` | Differentiation | 3 | An evidenced wedge the cheapest credible incumbent does not already offer; direct incumbent overlap caps this at 2. Deliberately downweighted at idea stage for narrow self-serve products |
| `risk` | Legal/regulatory/platform/trust risk | 4 | Manageable risks with no veto-level exposure |

Score anchors: `0` = hostile or no basis; `1` = weak/no source; `2` = plausible but
undemonstrated (assumption, analogy, model); `3` = adequate, evidenced for this
buyer/market; `4` = strong, multiple independent sources or early primary signals;
`5` = exceptional, primary evidence.

`seo_discoverability` and `self_service_fit` are deliberately prominent: under the
1.9.0 acquisition constraint, organic search is the primary distribution channel and
self-service purchase/delivery is a hard operating requirement. A candidate that cannot
be found on search or cannot be bought without a human is killed by the corresponding
hard filter regardless of its aggregate.

Hard caps (schema v2) that must be applied and stated in the rationale:

- untested/modelled economics: `economics <= 2`, confidence `low`;
- direct incumbent already contests the wedge: `differentiation <= 2`;
- distribution channels plausible but no prospects produced: `distribution <= 2`;
- problem asserted by analogy: `problem_severity_frequency <= 2`;
- **missing why-now** (archetypes A/B/C only): at `Plausible`/`Promising`,
  `differentiation <= 2` and `problem_severity_frequency <= 2`. The cap is
  **archetype-aware (v1.6.0)**: unchanged for change-driven candidates; for
  persistent-market-failure candidates lifted only by an evidence-backed persistence
  thesis meeting BOTH parts of the test in `method/discovery.md`; a weak, absent or
  speculative thesis leaves the cap in place; the thesis is not a scoring bonus;
- **search-led candidates are exempt from the missing-why-now cap** (archetype D,
  v1.9.0): evergreen search demand does not require a contrived discontinuity. The
  exemption is not a bonus: a search-led candidate with no dated query/SERP evidence
  simply scores `seo_discoverability` `null` or 2 and gains nothing. `why_now.strength`
  is recorded as `not-required` for these candidates, with the search-intent evidence
  living in `seo_assessment`;
- the wedge is a feature of an established category, not a product: the candidate fails
  the `defensible_wedge` hard filter (not just a score reduction).

Competitor existence is not adequate occupation. `differentiation <= 2` and a
`defensible_wedge` failure both require evidence that a credible alternative actually
occupies the exact proposed seam for the defined buyer - not merely that competing
products exist, are advertised, or ship an adjacent feature. Where such evidence exists,
the cap and the hard filter apply exactly as before. A narrow existing category with
evidenced search intent and an underserved sub-niche may survive despite competitors,
provided the underserved wedge is evidenced rather than assumed.

No-score rule: `null` when no evidence exists for the dimension. A score is never
inferred from another dimension's evidence, and a score is never raised because a
hard-filter unknown "seems likely".

**Latent-opportunity hypotheses (v1.7.0).** A candidate promoted from a latent
observation (archetype C in `method/discovery.md`) is scored under exactly the same
rules as any other candidate. The latent route changes *where observations come from*,
not how they are scored: it does not lift a cap, lower the 65 threshold, redefine
evidence levels, or upgrade a hard filter. A latent hypothesis with no buyer, no
observable status quo, no plausible distribution or no decisive affordable test is
rejected or parked like any other observation, and "the buyer does not know they need
it yet" is never a substitute for evidence.

**Search-led scoring note (v1.9.0).** A search-led candidate (archetype D) is scored on
demonstrated search demand and entry feasibility, not on novelty. The distinct registers
stay separate: a **research promise** (the evidence exists somewhere and can be
checked), a **search opportunity** (dated queries and SERPs showing reachable, unmet
intent), and **commercial validation** (behavioural evidence that buyers pay). Only the
last is commercial evidence; the first two never substitute for it. Search volume alone,
even when credibly sourced, is never proof of willingness to pay and never justifies a
`buyer_budget_clarity` score above 2 on its own.

## `seo_assessment` (required, schema v2)

Every schema-v2 scorecard records a structured `seo_assessment`. It documents what was
actually checked, dated, and what remains unknown. Fields whose evidence does not exist
are recorded as `unknown`/empty-and-listed in `unknowns` - never invented, and never
populated with estimated volumes, rankings, CPC or difficulty figures.

```json
{
  "seed_queries": [
    {
      "query": "exact query text",
      "intent_cluster": "short label for the job/intent",
      "demand_evidence": [
        {"source": "named source or URL", "date": "YYYY-MM-DD",
         "volume_reported": "optional string, only with a credible named source and date",
         "notes": "what this shows"}
      ]
    }
  ],
  "serp_landscape": {
    "checked_date": "YYYY-MM-DD",
    "queries_checked": ["exact query strings actually checked"],
    "pages": [
      {"url": "https://...", "type": "organic|ad|forum|gov|ai_answer|marketplace|other",
       "notes": "who ranks and why it matters"}
    ],
    "ai_overview_observed": "yes|no|unknown"
  },
  "organic_entry_feasibility": {
    "assessment": "qualitative judgement, no false precision",
    "notes": "why a new entrant could/could not reach these results",
    "unknowns": ["what is not known"]
  },
  "conversion_mechanics": {
    "path": "search result -> landing page -> self-service signup -> payment -> use",
    "requirements": ["what the path requires (pricing page, free tool, trial, ...)"],
    "notes": "anything blocking self-service"
  },
  "traffic_to_revenue_scenarios": {
    "assumptions_label": "explicitly labelled assumptions (e.g. 'assumed; untested')",
    "conservative": "low-case narrative with assumptions",
    "modest": "middle-case narrative with assumptions",
    "optimistic": "high-case narrative with assumptions"
  },
  "seo_risks": {
    "zero_click_ai": "AI overviews / zero-click exposure",
    "seasonality": "seasonal demand notes",
    "platform_dependency": "platform/SERP dependency notes",
    "other": "any other SEO risk"
  },
  "unknowns": [
    {"item": "what is unverified", "next_check": "cheapest low-touch way to check it"}
  ]
}
```

Validation rules:

- `seed_queries` is non-empty; each query needs `query`, `intent_cluster` and a
  non-empty `demand_evidence` list. Each `demand_evidence` entry needs a `source` and a
  `date`; `volume_reported` is optional but, if present, must be a non-empty string that
  names its measurement basis (for example a tool name and month). A failed or blocked
  check is recorded honestly as an entry whose `source` describes the check attempted.
- `serp_landscape` needs `checked_date`, a non-empty `queries_checked` list and
  `ai_overview_observed`; `pages` may be empty only when the SERP could not be read,
  which must then appear in `unknowns`.
- `organic_entry_feasibility`, `conversion_mechanics`, `traffic_to_revenue_scenarios`
  and `seo_risks` are required with the fields shown. Scenarios are narratives with an
  explicit `assumptions_label`; no invented traffic, conversion or revenue numbers.
- `unknowns` lists every unverified item with a low-cost next check. An empty list is
  allowed only when nothing material is unverified.
- No invented volumes, rankings, CPC, trends or difficulty scores anywhere in this
  block. Search volume alone is not proof of willingness to pay.

## Aggregate

```
raw_points      = sum(weight * score / 5)      over scored dimensions
scored_weight   = sum(weight)                  over scored dimensions
weighted_total  = round(raw_points / scored_weight * 100, 1)
```

Normalisation by `scored_weight` means unscored dimensions neither help nor punish, but
they are reported and they cap confidence. At least **9 of 12** dimensions must be
scored for a `validation-ready` proposal under schema v2 (8 of 10 under legacy v1);
`problem_severity_frequency`, `buyer_budget_clarity` and `evidence_strength` must always
be scored and must each be >= 3.

## Threshold for `validation-ready`

An idea may be proposed for `validation-ready` only if all of:

1. `weighted_total >= 65`
2. no hard filter `fail`
3. no active veto
4. the three gating dimensions are scored >= 3
5. at least 9 of 12 dimensions are scored (schema v2; 8 of 10 under legacy v1)
6. overall confidence is `medium` or `high`
7. review has been triggered (`review.status != not-required`) per `method/review-policy.md`
8. every `unknown` hard filter names the experiment measurement that will resolve it

The threshold was deliberately **not lowered** when the rubric was tightened; moving a
goalpost to preserve a previous score would defeat the purpose. An honest desk-only idea
typically lands in the 45-62 range and stays at `adversarially-researched`. That is not a
verdict: a parked idea can still carry a proposed experiment (see `method/lifecycle.md`),
and external results are the route back to `validation-ready` with a higher evidence
level.

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

The nine legacy filters (schema v1, and still present in schema v2):

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

Schema v2 adds three founder-fit/self-service gates:

| Key | Filter | Fails when |
|---|---|---|
| `seo_discoverable` | The buyer can be reached through organic search for a named job/query | No dated search evidence, or the SERP is effectively closed to a new entrant |
| `self_serve_purchase` | The product can be bought, onboarded and used without a demo, call or hand-holding | The credible path requires sales contact, demos, custom setup or ongoing hand-holding |
| `solo_operator_fit` | A solo, part-time founder can build, operate, support and maintain it at the modelled scale | Build complexity, support burden, external dependencies or owner time are incompatible with solo part-time operation |

All three are hard filters: `fail` kills; `unknown` needs a `resolve_via` and, at
`validation-ready`, must be named in the experiment. A `pass` requires cited evidence -
for `seo_discoverable` that means dated query/SERP evidence from `seo_assessment`, not
a plausible query list.

Legacy scorecards (schema v1) are validated against the nine legacy filters only; the
three new gates apply to new candidates and to opt-in re-triage memos.

## Vetoes

`vetoes` is a list of `{key, note, date}`. Any active veto overrides the aggregate and
forces `killed` or `adversarially-researched` (parked) with the reason recorded.

## Worked example (synthetic, schema v2)

A search-led micro-SaaS candidate (synthetic calibration fixture: "shop-floor
checklist app" style candidate, no real market claims). Scores: problem 3, buyer 3,
evidence 3, seo discoverability 3 (one dated query cluster and SERP snapshot, entry
plausible but unproven), self-service fit 4, distribution 2 (community channels
plausible, no prospects), founder fit 4, economics 2 (modelled; cap), validation 4,
feasibility 4, differentiation 2 (adjacent incumbent), risk 4. Search-led archetype:
missing-why-now cap does not apply.

```
raw_points    = 7.2 + 7.2 + 7.2 + 8.4 + 8.0 + 2.0 + 8.0 + 3.2 + 5.6 + 2.4 + 1.2 + 3.2 = 63.6
scored_weight = 100
weighted_total = 63.6   -> below the 65 threshold; parked at adversarially-researched
```

The candidate is not killed by any filter but is not carried either: the cheapest
next step is a cheap behavioural check on the search route, not more desk modelling.

## Legacy schema v1 (weights 1.2.0) - preserved

Historic scorecards use ten dimensions: `problem_severity_frequency` 15,
`buyer_budget_clarity` 15, `evidence_strength` 15, `distribution` 10,
`differentiation` 10, `validation_speed_cost` 10, `feasibility` 5, `economics` 10,
`founder_fit` 5, `risk` 5. Minimum 8 of 10 dimensions scored; hard filters are the nine
listed above; `seo_assessment` does not exist. The legacy missing-why-now cap and
persistence-thesis rule (v1.6.0) apply as recorded in the historic cards.

Legacy worked example (GeoNerd, rescored under 1.1.0, weights 15/15/15/10/10/10/5/10/5/5):
problem 2, buyer 3, evidence 2, distribution 2, differentiation 2, validation 4,
feasibility 3, economics 2, founder fit `null`, risk 3 → raw 47, scored_weight 95,
`weighted_total` 49.5, parked. This example is historical and is not rescored under v2.
