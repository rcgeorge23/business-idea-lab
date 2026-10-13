# <Idea title>

- **ID / slug:** `<slug>`
- **Industry:** `<industry-slug>` (controlled vocabulary in `scripts/validate_repo.py`; grouped on the dashboard)
- **State:** `discovered`
- **Evidence level:** `Plausible`
- **Owner:** worker | human-owner
- **Created:** YYYY-MM-DD
- **Updated:** YYYY-MM-DD
- **Source:** how this candidate was generated (worker run ID or human)
- **Scorecard:** schema v2 / weights 1.3.0 (legacy schema v1 exists only for cards recorded before method 1.9.0)

## One-sentence proposition

> <Buyer> has <problem>; we provide <mechanism> at <price/business model>.

## Why now?

> This was not an attractive business three years ago, but it might be now because
> ___ changed.

- What changed:
- When it changed (or is due to change):
- Evidence (dated source), and why the change is real rather than a trend:
- Why this materially improves the opportunity now:
- Have competitors already responded?
- Strength: `strong` | `weak` | `absent` | `not-required` (search-led only)
- Archetype: `change-driven` | `persistent market failure` | `latent opportunity` | `search-led`

For search-led candidates (v1.9.0), no contrived discontinuity is required: record
`not-required`, point to the dated search-intent evidence in the SEO assessment below,
and note that the exemption removes the missing-why-now cap only — it is not a score
bonus and relaxes no evidence requirement.

For persistent-market-failure candidates, record the persistence thesis (it lifts the
missing-why-now cap only when both limbs are affirmatively evidenced - see
`method/discovery.md`):

- Continued pain or workaround despite alternatives that exist and are reachable for
  this buyer:
- Credible mechanism explaining why the market has not adequately resolved the problem
  for this segment:
- Persistence thesis quality: `strong` | `weak` | `absent`

For latent-opportunity candidates (archetype C), record the six admissibility fields
from `method/discovery.md`. Cite dated evidence for factual observations, label each
material claim as observation, inference or assumption, and state plainly that the value
inference is not demand evidence. A proposed capability or mechanism that is not yet
verified for this buyer must be labelled inference/assumption:

- Buyer/user and observed current behaviour or constraint (observation + dated source):
- Newly possible capability and concrete mechanism (dated capability evidence; label unverified application):
- Why the buyer might value it despite not requesting it (inference + evidence it rests on):
- Why now, or "no discontinuity known" (dated evidence or explicitly unknown):
- Existing substitute / status quo and competitors (dated evidence or explicitly unknown):
- Central falsifiable assumption and cheapest behavioural test (assumption, not fact):

## Buyer

- Who exactly pays (role, company size, segment):
- Who uses it:
- Evidence: [link]

## Problem

- What is painful/frequent/expensive:
- Current alternatives and their weaknesses:
- Evidence: [link]

## Mechanism / wedge

- What we would actually do:
- Why it is defensible against the cheapest credible incumbent:
- Evidence: [link]

## Novelty / incumbent sanity check

| Check | Answer | Evidence |
|---|---|---|
| Does this exact product already exist? | | |
| Are there multiple credible providers? | | |
| Is the wedge already a standard feature? | | |
| Is a free/authoritative alternative already adequate? | | |
| Has a well-capitalised company shown hostile unit economics? | | |
| Is this merely a feature of an established category? | | |

If any check fails, state the reason to continue anyway:

## SEO assessment (schema v2)

Never invent volumes, rankings, CPC, trends or difficulty. Record `unknown` plus a
low-cost next check wherever evidence is missing or a SERP check was blocked. Search
volume alone is not proof of willingness to pay.

- **Seed queries and intent clusters:** (exact query text; cluster label)
- **Demand evidence (dated):** (source + date; reported volume only where credible,
  otherwise `unknown`)
- **SERP landscape (checked YYYY-MM-DD):**

| Query | Page / competitor | Type (organic / ad / forum / gov / ai_answer / marketplace / other) | Notes |
|---|---|---|---|
| | | | |

- **AI overviews observed:** yes | no | unknown
- **Organic entry feasibility (qualitative, no false precision):** (assessment; what
  could plausibly rank; unknowns)
- **Conversion mechanics (self-service only):** (signup → payment → delivery path;
  requirements; no demos, calls or hand-holding)
- **Traffic-to-revenue scenarios (assumption-labelled):**
  - Assumptions label:
  - Conservative:
  - Modest:
  - Optimistic:
- **SEO risks:** AI overviews / zero-click; seasonality; platform dependency; other
- **Unknowns and low-cost next checks:** (item → next check)

## Distribution

- Organic search entry (primary channel; see SEO assessment):
- Route to the first buyers without paid acquisition or outreach:
- Evidence: [link]

## Economics (assumptions labelled)

- Price hypothesis (self-service pricing):
- Cost drivers:
- Pricing vs organic traffic economics (conversion assumptions labelled):
- Contribution margin at realistic scale:

## Founder fit

- Self-service fit: can the product be bought and delivered without calls, demos,
  onboarding or custom work? Evidence:
- Solo-operator burden: build complexity, maintenance, support, external
  dependencies, owner time:
- Reach, skills, motivation (evidence only; `null` if unknown):

## Adversarial case (strongest case this is wrong)

<Written deliberately to kill the idea. If the idea survives, say why.>

## Strongest supporting case

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|

## Cheapest decisive experiment

- Assumption under test:
- Proposed test:
- Pre-fixed decision rule:
- Cost bound:
- Status: proposed | awaiting-approval | approved | running | completed | abandoned
- Link: `experiments/<id>/plan.md`

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
