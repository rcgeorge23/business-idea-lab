# Discovery

Method version: see `method/VERSION`. This file defines how candidates are found,
screened for novelty, deduplicated, and how adjacent opportunities are preserved.

## The discontinuity test

The lab exists to find opportunities that a search for "problems" would miss. Every
candidate must be able to complete this sentence with a specific, dated, cited change:

> **This was not an attractive business three years ago, but it might be now because
> ______ changed.**

"Because the problem exists" is not an answer. "Because AI assistants became a
mass-market buying surface in 2024-2025" is an answer when tied to evidence. The change
need not be brand new; it must be *identifiable and material*, and the candidate must
explain why it creates or widens an opening now rather than at any time in the past.

Prefer changes that are hard to reverse, create urgency or compulsion, or invalidate an
incumbent's position. Reject candidates whose only "why now" is a general trend.

### Sources of change to investigate

| Class | Examples of what to look for |
|---|---|
| Legislation / regulation | Acts with commencement dates, statutory instruments, new reporting or record-keeping duties |
| Consultations / announced rules | Open consultations, confirmed future obligations, transition periods |
| New APIs / developer surfaces | Government or industry APIs newly opened, terms changed, rate limits lifted |
| New datasets | Registers, price/usage/registry data newly published or made machine-readable |
| Platform rule / pricing / access changes | Marketplace, app-store, search or social platform policy and pricing shifts |
| Incumbent disruption | Products discontinued, withdrawn, repriced, end-of-lifed, acquired and neglected |
| New technical capability | LLM/vision/document processing making an expensive human workflow newly automatable |
| Manual structured-data flows | Industries still re-keying between email, PDFs, spreadsheets and portals |
| Poor narrow incumbents | Verticals where the only software is expensive, dated or widely disliked |
| Mandated formats / submissions | New filings, e-invoicing, schemas, portals creating integration/adaptor needs |

A run need not cover every class, but it must search across several and record which
classes it searched in the run summary. Rotating deliberately across classes is
expected; repeatedly mining one class is a reason to justify the choice.

## Second-order effects

A discontinuity usually invites an obvious first-order product: a compliance dashboard,
a checklist, a reminder service, a registration helper. That response is often quick to
build and equally quick for incumbents to absorb — the first 2026-mandate candidates
died exactly there (`vetcma`, `prsregister`, `propident`,
run `20260921T075410Z-normal`).

Before promoting a candidate, investigate what the change does to the *work around* the
obvious product. Look explicitly for a second-order problem:

| Second-order effect | What to look for |
|---|---|
| Manual handoffs between systems | Work that now has to move between two systems that do not talk |
| Duplicate entry / re-keying | The same data now entered into a new portal as well as the old system |
| Reconciliation | Money, quantities or records that must now be matched across sources |
| Evidence / document collection | New duties requiring per-case documents gathered and evidenced |
| Exception handling | Cases that do not fit the standard process and stall |
| Status chasing | Chasing counterparties, authorities or suppliers for progress |
| Awkward exports / imports | Formats that must be transformed by hand or via scripts |
| Mandated structured-data transformations | New schemas that must be derived from legacy records |
| Integration gaps between incumbents | Two incumbent tools whose overlap is now an operational seam |
| New workflow steps incumbents handle poorly | Steps grafted onto software not designed for them |
| Expensive human review newly automatable | Review work that current models can do or pre-screen |
| Underserved subsegments | Buyers for whom incumbent solutions are disproportionately costly or complex |

Prefer a candidate built on an awkward operational seam over a generic
dashboard/checklist/compliance product. The preference is not a requirement to invent a
second-order opportunity where the evidence does not support one: if the direct
first-order product is genuinely the best opportunity, record why the second-order
options were weaker. What is not acceptable is promoting the obvious product without
looking.

## Why now?

Every candidate records `why_now` in `ideas/index.json` and a "Why now?" section in its
dossier:

```json
"why_now": {
  "changed": "what changed, in one sentence",
  "changed_date": "YYYY-MM-DD or YYYY-MM or 'announced'",
  "evidence": ["evidence/<slug>/<file>.md or URL"],
  "why_it_matters": "why this materially improves the opportunity now",
  "competitors_responded": "none known | named incumbents already moved | unknown"
}
```

- `changed` and `why_it_matters` must be non-empty and specific.
- `evidence` must cite at least one dated source register entry or external URL.
- A missing or unevidenced why-now does not auto-kill. For a candidate whose
  evidence level is `Plausible` or `Promising` (pre-demand), it caps `differentiation`
  and `problem_severity_frequency` at 2 (see `method/scorecard.md`) and is a strong
  reason to reject a generic or crowded candidate at screening. The cap does not apply
  once there is `Demand evidence` or better (v1.2.0): an evergreen niche with real
  payment evidence is judged on that evidence, not on a missing discontinuity.

## Novelty / incumbent sanity check

Run this before deep research, and record the answers in the dossier. It is a screening
aid, not an automatic kill: a candidate that fails a check may still proceed with a
stated reason (for example, "three providers exist but all require an accountancy
practice to self-serve configuration we can remove").

1. Does this exact product already exist?
2. Are there multiple credible providers?
3. Is the proposed wedge already a standard feature of an incumbent?
4. Is an authoritative or free alternative already adequate?
5. Has a well-capitalised company already shown the unit economics are hostile (e.g. a
   category leader losing money at scale)?
6. Is this merely a feature of an established category rather than a standalone product?

## Seed-aware discovery

Seeds are an input to discovery, not a museum. At the start of every normal run, review
`seeds/index.json`:

1. List the seeds with status `unexplored` (and re-read any `exploring` ones).
2. Shallowly re-check the most relevant or promising seeds against current public
   evidence: has the discontinuity strengthened, weakened, or been captured by an
   incumbent? This is a short check, not a full dossier.
3. A seed may become a candidate only after the same research a fresh discovery would
   get: its own fingerprint, evidence register, hard filters and scorecard. It never
   inherits the parent idea's score, evidence level, hard-filter results or favourable
   assumptions.
4. Record provenance for every candidate: `seed:<seed-slug>` or `fresh`. A run is not
   seed-only: fresh discontinuity hunting remains required, and seeds that do not
   survive the shallow check stay seeds (update their status, or note in the run
   summary why they remain `unexplored`).
5. The candidate limit (3 per run) is unchanged; provenance does not add an allowance.

## Source-class budget

Repeated `defensible_wedge` failures across regulatory discontinuities are a sourcing
problem, not a filter problem. The following **discovery-only** budget therefore
applies to every normal run (v1.4.0):

> **At least 2 of the maximum 3 candidate slots must originate from non-regulatory
> source classes. At most 1 candidate may primarily originate from
> legislation/regulation. At least one previously underexplored non-regulatory source
> class must actually be searched.**

- The budget constrains where candidates come from. It confers **no scoring
  advantage**: weights, thresholds, hard-filter semantics, evidence levels, lifecycle
  gates and candidate/advancement limits are unchanged.
- Regulatory sources remain valid (legislation, consultations, statutory deadlines,
  mandated formats). They simply must not consume the discovery budget by default.
- Non-regulatory classes include: poor, expensive or unpopular narrow incumbent
  software; repetitive professional/service work newly automatable with current AI;
  software shutdown, end-of-life or forced-migration gaps; newly accessible APIs or
  datasets; awkward integrations between established systems; recurring
  spreadsheet/email/PDF/manual re-keying workflows; platform access, pricing or policy
  changes that create a new operational problem; underserved subsegments of an
  existing category.
- A candidate "qualifies" for its source class because of where its why-now came
  from. Record the class and the reason in the run summary; a candidate whose primary
  why-now is a mandate counts against the regulatory slot even if it also has a
  second-order seam.
- **Never manufacture weak candidates to satisfy the budget.** Fewer than three
  candidates is a valid run; killing every candidate is a valid run; advancing
  nothing is a valid run. If a class was searched and yielded nothing, record that
  as a finding.
- If the budget cannot be satisfied honestly (for example, a run where no
  non-regulatory class yields anything worth registering), that is itself a
  convergence signal to report — not a reason to relax the rule or promote filler.

## Duplicate detection

Before creating a candidate, check against every entry in `ideas/index.json` and every
seed in `seeds/index.json`:

- normalised title/slug collision => duplicate, do not create;
- same buyer AND same problem AND (same mechanism OR >= 3 shared fingerprint keywords)
  => duplicate unless the candidate states what is materially different;
- a variant of a killed idea that does not address the recorded kill reason => reject,
  and record the reason;
- a seed may only become a candidate after fresh research from scratch, with its own
  evidence and scorecard; it never inherits the parent's score or evidence level.

## Adjacent opportunity seeds

Rejections often surface a better-adjacent proposition (e.g. "discovery is commoditised
but application quality is not"). Preserve it as a seed so a later run can investigate
without resurrecting the killed idea:

- one file per seed under `seeds/<slug>.md`, one entry in `seeds/index.json`;
- record the parent idea, the observation, the evidence for it, and what would make it
  materially different from the parent;
- seeds carry **no** score, confidence or evidence level, and cannot be promoted without
  their own dossier, evidence and scorecard.

## Recording

- The run summary lists the source classes searched and what they yielded.
- The run summary states, for each generated candidate, whether its why-now is
  evidenced (`strong` | `weak` | `absent`).
- The run summary states each candidate's provenance (`seed:<seed-slug>` or `fresh`)
  and, where a second-order seam exists, the seam the candidate addresses and why it
  was preferred to the obvious first-order product.
- The run summary answers whether discovery appears to be converging on less obvious,
  better-defended opportunities, or repeatedly finding and rejecting the same class of
  candidate. A recurring cluster of `defensible_wedge` kills is a signal to review
  discovery — not to weaken the filter.
- Rejected candidates keep their why-now analysis in the decision record.
