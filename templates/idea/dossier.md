# <Idea title>

- **ID / slug:** `<slug>`
- **Industry:** `<industry-slug>` (controlled vocabulary in `scripts/validate_repo.py`; grouped on the dashboard)
- **State:** `discovered`
- **Evidence level:** `Plausible`
- **Owner:** worker | human-owner
- **Created:** YYYY-MM-DD
- **Updated:** YYYY-MM-DD
- **Source:** how this candidate was generated (worker run ID or human)

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
- Strength: `strong` | `weak` | `absent`
- Archetype: `change-driven` | `persistent market failure` | `latent opportunity`

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

## Distribution

- Route to the first 10 buyers without paid acquisition:
- Evidence: [link]

## Economics (assumptions labelled)

- Price hypothesis:
- Cost drivers:
- Contribution margin at realistic scale:

## Founder fit

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
