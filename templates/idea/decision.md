# Decision record: <idea title>

- **Idea:** `<slug>`
- **Date:** YYYY-MM-DD
- **Run:** `<run-id or bootstrap>`
- **Decision:** advance | hold | kill | defer
- **State:** `<from>` -> `<to>`
- **Actor:** worker | human-owner

## What changed

<One paragraph: what was learned or decided this run.>

## Why now? (discovery gate)

- Archetype: `change-driven` | `persistent market failure` | `latent opportunity` | `search-led`
- What changed / when (search-led: record `not-required` and point to the search-intent evidence):
- Why it materially improves the opportunity:
- Strength: `strong` | `weak` | `absent` | `not-required`
- Search-led candidates only (v1.9.0): no contrived discontinuity is required. Summarise
  the search-intent evidence (exact seed queries, dated demand evidence, SERP check date)
  and link the scorecard `seo_assessment`. The missing-why-now cap does not apply, and the
  exemption is not a score bonus and relaxes no evidence requirement.
- Persistent-market-failure and latent-opportunity candidates only - persistence thesis
  (both limbs must be evidenced for the missing-why-now cap to lift; record `unknown`
  where not):
  - Limb 1, continued pain/workaround despite reachable alternatives: `pass` | `unknown` | `fail`
  - Limb 2, credible persistence mechanism: `pass` | `unknown` | `fail`
  - Net thesis quality: `strong` | `weak` | `absent`
- Latent-opportunity candidates only - the six admissibility fields from
  `method/discovery.md` archetype C, and confirmation that the value inference is an
  inference, not demand evidence. Cite dated evidence for factual observations, label
  unverified capability applications and buyer/payment claims as inference or
  assumption, and do not treat missing search results as evidence of non-consumption:
- If `weak` or `absent`: why the candidate was generated anyway, and why it was kept
  or rejected.

## Hard filters

| Filter | Status | Note |
|---|---|---|
| economic_buyer | unknown | |
| painful_frequent_or_budgeted | unknown | |
| non_paid_distribution | unknown | |
| defensible_wedge | unknown | |
| no_network_effects_needed | unknown | |
| plausible_margins | unknown | |
| acceptable_risk | unknown | |
| cheap_disconfirming_test | unknown | |
| not_all_optimistic | unknown | |
| seo_discoverable | unknown | |
| self_serve_purchase | unknown | |
| solo_operator_fit | unknown | |

Status values are `pass` | `unknown` | `fail`; see `method/scorecard.md`. `unknown`
entries name what would resolve them in the scorecard's `resolve_via`. The last three
filters are the founder-fit / self-service gates introduced in method 1.9.0; a `fail`
on any filter kills the candidate.

## Evidence considered

<Dated links to evidence register entries. Include anything that cut against the
decision.>

## Scores

<Weighted total, threshold, per-dimension summary; link `scorecard.json`. New cards use
schema v2 (weights 1.3.0); legacy schema-v1 cards keep their historic scores untouched.>

## Review

<Review status, request/response links, and how the worker responded to each point.>

## Reasons if killed

<Why; what evidence would have changed the decision; preserved for future reference.>

## False-negative audit (killed ideas only)

- Audited: yes/no
- Reviewer / date:
- Verdict:
- What new evidence would justify reopening:
