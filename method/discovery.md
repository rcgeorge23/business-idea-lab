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
- A missing or unevidenced why-now does not auto-kill. For a **change-driven**
  candidate whose evidence level is `Plausible` or `Promising` (pre-demand), it caps
  `differentiation` and `problem_severity_frequency` at 2 (see `method/scorecard.md`)
  and is a strong reason to reject a generic or crowded candidate at screening. The cap
  does not apply once there is `Demand evidence` or better (v1.2.0): an evergreen niche
  with real payment evidence is judged on that evidence, not on a missing discontinuity.
- **Persistent-market-failure candidates are not required to fabricate a
  discontinuity (v1.6.0).** Instead they must carry an evidence-backed **persistence
  thesis** answering "why has this problem remained inadequately solved despite
  existing alternatives?". The cap is lifted only by the two-part requirement described
  under `### Two discovery archetypes`.

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
  existing category; and (v1.8.0) money-already-moving sources - job advertisements
  describing repetitive administrative work, service/agency pricing pages, public
  procurement and tender records, incumbent support forums and release notes, trade
  press reporting spend or staffing, and job descriptions for roles that exist only to
  bridge two systems.
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

## Opportunity-observation funnel

Discovery runs as a funnel, not as a search for three ideas:

> **15–20 raw opportunity observations → shallow triage → at most 3 full candidates
> → the existing rigorous evaluation.**

The funnel exists to search more of the opportunity space before committing research
budget to a candidate. It changes the *shape of discovery only*: scoring, threshold,
hard-filter semantics, evidence levels, lifecycle gates and the candidate/advancement
maxima are unchanged. Observations are not scored and carry no evidence level. The
15–20 pool size is retained **provisionally** pending several empirical runs (v1.6.0);
do not increase it.

### What counts as an observation

An observation is deliberately lighter than a business idea. It describes an evidenced
problem, workflow, dissatisfaction, market failure or change, without requiring a
polished product proposition. Acceptable shapes include:

- "Small firms in segment X repeatedly export data from system A and manually re-key
  it into system B."
- "Organisations in niche Y pay disproportionately high annual fees for software they
  use only a few times per year."
- "Users of incumbent Z repeatedly complain about a specific workflow that remains
  unresolved."
- "A repetitive professional service costing £N per case now appears technically
  automatable."
- "A platform/API/product change has created a new operational task for an
  identifiable buyer."
- "Buyers in segment X accept a costly routine as normal, and a newly available
  capability could change it" (a **latent-opportunity hypothesis** - see archetype C;
  admissible only with the six required fields).

Do not create scorecards or dossiers for observations.

### Observation record

A run records its pool in `observations/<run-id>.md` (template:
`templates/observation/pool.md`). Each observation records at minimum:

- a concise problem/workflow statement;
- the target user/buyer, if identifiable;
- the source class it came from;
- its evidence/source(s) and the evidence type — primary, practitioner/community,
  vendor, or secondary;
- why it may represent an opportunity;
- an obvious incumbent / free-alternative check;
- whether it is **change-driven**, a **persistent market failure**, or a **latent
  opportunity** (archetype C, which additionally requires the six admissibility fields);
- the triage outcome and reason.

Keep each row compact: the pool must fit comfortably inside one run's budget.

### Three discovery archetypes

**A. Change-driven.** Something changed and created or materially worsened the
problem: regulation, platform/API/pricing/access change, product end-of-life, a new
dataset, a new technical capability, market restructuring. These record a conventional
`why now?` per the section above.

**B. Persistent market failure.** No recent discontinuity is required. Examples: poor
or overpriced niche incumbent software; a narrow segment poorly served by products
built for larger customers; recurring spreadsheet/email/PDF/manual workflows; awkward
integration seams; expensive repetitive service work; persistent complaints about an
incumbent; pricing disproportionate to the narrow job being performed. For these
observations, replace a forced "why now?" with:

> **Why does this problem still persist despite existing alternatives?**

Possible answers: the market is too small for large vendors, incumbent lock-in,
fragmented buyers, legacy architecture, low vendor priority, a recent fall in
build/automation cost, or a narrow underserved segment. Do not invent a justification
the evidence does not support — "I could not establish why this persists" is an honest
and acceptable answer, and it is itself triage evidence.

A candidate promoted from archetype B still needs a `why_now` object in its index
entry. Record `strength: "absent"` when there is no favourable discontinuity, and put
the persistence thesis in `why_it_matters` and the decision record. Do not fabricate a
discontinuity to escape the cap.

**The missing-why-now cap is archetype-aware (v1.6.0).** The v1.2.0 cap on
`differentiation` and `problem_severity_frequency` at `Plausible`/`Promising` continues
to apply unchanged to **change-driven** candidates and lifts at `Demand evidence` or
better. For a **persistent-market-failure** candidate the cap may be lifted only by an
evidence-backed persistence thesis, and only where **both** of the following are
supported by cited evidence:

1. **Continued pain or workaround despite the alternatives.** The target buyer still
   pays, waits, re-keys, reconciles or works around the problem even though the
   alternatives named in the incumbent check exist and are reachable. Adequate
   evidence includes: repeated recent practitioner/community complaints about the same
   narrow workflow; a demonstrated manual workaround that persists despite incumbent
   availability; pricing, minimum-contract or implementation economics that
   systematically exclude the target segment; credible switching/data-access barriers
   combined with continuing pain; or products that technically offer a feature the
   target segment still cannot practically or economically use.
2. **A credible persistence mechanism.** A present-tense, evidence-supported
   explanation of *why* the market has not adequately resolved the problem for the
   specified segment: incumbent architecture/channel constraints that make the narrow
   job unattractive; vendor economics (minimum contract value, integration cost);
   fragmentation of the buyer population; or a recent fall in the cost of building the
   missing piece. Unsupported narratives such as "incumbents don't care about this
   niche" or "the market is too small" are **not** sufficient.

The persistence thesis is **not a scoring bonus**: it only allows the ordinary evidence
to be scored without the missing-why-now cap. Where the persistence evidence is absent,
weak or speculative, the cap stays. A persistence thesis never establishes
`buyer_budget_clarity`, `evidence_strength`, distribution or wedge, and it never
upgrades a hard filter: `defensible_wedge` still fails where credible incumbents
adequately occupy the exact proposed seam for the defined buyer. The existence of
competing products is not by itself adequate occupation - see `### Shallow triage`.

**C. Latent opportunity (v1.7.0).** Some worthwhile products change a behaviour the
buyer currently accepts as normal. The buyer may not discuss a "problem" because they
have not seen the alternative, so a sweep that only looks for articulated pain can
under-source or prematurely reject these hypotheses. This archetype is a **guarded
route**, not a relaxation of standards: "customers do not know they need it yet" is
**never** a blanket defence for an unevidenced idea, and it does not lift any score cap,
lower the threshold, redefine evidence levels or upgrade a hard filter.

An observation may be recorded as a latent-opportunity hypothesis only if it names all
of the following, each backed by dated observable evidence rather than model
imagination:

1. **The specific buyer/user and their current behaviour or constraint** - what they
   actually do today, observed (a costly routine treated as normal, a workaround in a
   neighbouring market, an accepted constraint), not inferred from a trend narrative.
2. **The newly possible experience or capability and a concrete mechanism** - how it
   changes time, cost, quality, access or outcomes, and by what means.
3. **Why the buyer might value the difference despite not requesting it** - the
   inference about value, labelled as inference, with the reasoning shown.
4. **Why now, or an honest statement that no discontinuity is known.** A latent
   hypothesis may have no favourable discontinuity; record `strength: "absent"` and do
   not fabricate one. The missing-why-now cap applies exactly as for archetype B unless
   an evidence-backed persistence thesis lifts it.
5. **The existing substitute / status quo and direct or adjacent competitors** - what
   the buyer uses instead today and what already exists.
6. **The central falsifiable assumption and the cheapest behavioural test** that could
   disconfirm it.

Source material for latent hypotheses is hypothesis-generating, not proof of demand:
observed adoption of adjacent tools, costly routines treated as normal, new
distribution or technical capabilities, workarounds in neighbouring markets, and
revealed behaviour when an alternative becomes available. Unsupported trend narratives
and AI-generated enthusiasm are not evidence.

**Evidence and gate semantics for latent hypotheses (v1.7.0).**

- Enough evidence to justify a **cheap test** need not include a pre-existing complaint
  or a search query for the proposed product. The admissibility test above is the bar
  for recording the observation and for proposing a test.
- **Demand and commercial validation still require real target-buyer behaviour**:
  payment, a pre-order, a meaningful commitment, or an approved experiment with a
  pre-declared decision rule. Interviews asking "would you use this?" and model opinions
  do **not** suffice, and a latent hypothesis never advances on plausibility.
- A latent hypothesis with **no buyer, no observable status quo, no plausible
  distribution route or no decisive affordable test** is still rejected or parked.
- Missing evidence stays `unknown` and is **never** upgraded to a hard-filter `pass`.
  Do not silently lift score caps, lower the 65 threshold or redefine evidence levels.
  If the scorecard cannot represent such a hypothesis honestly, that is a separate
  reviewable method change with regression evidence - not something a run may do.
- Expensive external validation, outreach, publication and spend still require human
  approval under `method/experiment-rules.md`.

A latent observation is recorded in the pool like any other, with its archetype marked
`latent` and the six admissibility fields present; it is triaged and promoted under the
same rules and limits as archetypes A and B. The archetype is a **subtype of discovery
sourcing**, not a new lifecycle state or evidence level.

### Bias the sweep toward ugly persistent problems

Method 1.5.0 deliberately aims meaningful search effort at:

- poor / expensive / unpopular narrow incumbent software;
- manual structured-data / spreadsheet / email / PDF re-keying workflows;
- awkward integrations between established systems.

Search practitioner and community evidence where feasible, not only vendor
announcements and generic technology news. Useful evidence includes user complaints
and reviews, practitioner forums and communities, support threads, trade/professional
discussions, job descriptions showing repetitive admin, consultancy/service pricing,
incumbent pricing/support/release notes, migration guides, and
spreadsheet/CSV/manual-submission instructions.

The source-class budget above still applies at candidate promotion. The observation
pool should itself make source diversity visible; do not create a second quota.

### Bias the sweep toward money already moving (v1.8.0)

Complaint forums are where problems are *discussed*; they are not where budgets are
*spent*. Six consecutive funnel runs (schools, open banking, trades, regulatory
changes and the general sweep) produced zero promotions, and the dominant rejection
reason was demonstrated occupation: every seam with real buyer pain already had at
least one mature incumbent, usually several, often with a free tier. The convergence
reviews recorded in `retrospectives/` escalated this to a sourcing/framing problem,
not a filter problem.

Method 1.8.0 therefore requires every normal funnel run to aim a meaningful share of
its search effort at **money-already-moving sources** - sources where a buyer is
already paying, hiring or procuring, rather than describing a problem:

- **job advertisements** that describe repetitive administrative work (a role whose
  duties are re-keying, reconciling, chasing or assembling documents is evidence that
  someone is paying a salary to do it);
- **service and agency pricing pages** (a consultancy or bureau charging for a manual
  process is evidence of an existing budget line);
- **public procurement and tender records** (a contract awarded for a manual or
  outsourced workflow is evidence of spend and of the buyer);
- **incumbent support forums and release notes** (repeated support threads about the
  same narrow workflow, or a feature the vendor keeps not shipping, are evidence of
  persistent unmet demand inside an existing budget);
- **trade and professional press** where it reports spend, pricing or staffing rather
  than product announcements;
- **job descriptions and org charts** showing a role that exists only to bridge two
  systems.

The point is not that these sources are better in general; it is that they carry
budget evidence that complaint forums do not. An observation sourced this way should
still record the costly event, the current workaround, frequency, the incumbent
response, the buyer and the reachable distribution, and it is still triaged and
scored under exactly the same rules. This is a sourcing bias, not a scoring change:
no cap is lifted, no threshold is lowered, no evidence level is redefined, and
`defensible_wedge` is unchanged.

A run that cannot find money-already-moving evidence for a seam should record that as
a finding rather than falling back to complaint-forum observations and calling them
equivalent. The run summary must state which money-already-moving sources were
searched and what they yielded, including unsuccessful searches.

### Shallow triage

Every observation gets a cheap first-pass triage before any candidate is promoted.
Triage eliminates observations where desk evidence already shows, for example:

- the exact solution is a standard incumbent feature of products the target buyer
  already owns or can readily adopt;
- an authoritative/free alternative adequately solves the job for the target buyer
  (technical availability to another, better-served segment does not count);
- credible vendors demonstrably and adequately occupy the exact proposed seam for the
  defined buyer/segment;
- the problem is obviously one-shot with no attractive economics (unless a service
  business is intentionally being considered);
- no plausible economic buyer exists;
- the observation is merely a feature request rather than a standalone or
  meaningfully differentiated opportunity;
- the apparent opportunity depends on network effects before value can be delivered.

**Competitor existence is not wedge failure (v1.6.0).** The bare presence of named
competitors is **not** sufficient grounds for triage rejection, and neither are vendor
claims without evidence of demonstrated capability. Ask whether the alternatives
actually leave a meaningful gap the proposition could win on - price, complexity,
segment accessibility, an incomplete solution, or one-shot economics where a recurring
need persists - and record the evidence either way. Enterprise availability is not the
same as accessibility to a narrow target niche; a product feature is not the same as a
complete solution. Where the evidence shows the seam is genuinely well served, triage
rejects and records why. The `defensible_wedge` hard filter is unchanged and still
fails where credible incumbents adequately occupy the exact seam.

Triage is **not** a replacement for the hard filters; it is a cheap way to avoid
spending full candidate-research effort on obvious dead ends. Record the negative
evidence and the reason for every rejection. An observation that fails triage but
contains an adjacent insight becomes a seed under `seeds/` rather than a candidate.

#### Triage false-negative audit (v1.6.0)

Triage makes most of the funnel's decisions, so every **normal funnel run** independently
re-checks **exactly one triage-rejected observation** afterwards. This is a cheap
sample, not a second triage pass:

- **Selection favours promising/high-ambiguity rejections**, not a uniform random draw:
  prefer an observation with relatively strong practitioner/problem evidence that was
  rejected because an incumbent, free alternative or crowded field appeared to occupy
  the seam. Record why it was selected.
- **The audit tests whether triage confused:**
  1. existence of competitors with adequate customer satisfaction;
  2. a feature with a complete solution;
  3. enterprise availability with accessibility to the target niche;
  4. vendor claims with demonstrated capability;
  5. one-shot migration/service availability with attractive recurring product
     economics.
- **Keep it cheap:** one observation and a bounded check roughly the cost of one
  observation; no full candidate research, no re-opening every rejection.
- **Record** in the run summary and the pool file: the observation selected; why it was
  selected; the original triage reasoning; the additional evidence checked; whether the
  rejection is upheld or overturned; and the implication for triage depth.
- **A single overturn does not automatically change the method.** Repeated overturns are
  a signal to review triage depth (and possibly sampling) in a later method review; note
  the pattern rather than reacting to one case.

### Promotion

At most **3** observations become full candidates. Favour observations with the
strongest combination of: credible problem evidence; an identifiable buyer; a
plausible route to payment; evidence that alternatives leave a meaningful gap; an
inexpensive path to falsification; and reasonable fit for a small/bootstrapped
business. Zero, one or two promotions are valid — never select candidates merely to
fill three slots, and never promote filler to satisfy the source-class budget.

Once promoted, a candidate goes through the **existing full process unchanged**:
fresh research, fingerprint/duplicate check, incumbent/novelty sanity check, evidence
register, hard filters, scorecard, adversarial review, lifecycle decision, and at most
one `validation-ready` advancement. Name the originating observation ID in the
candidate's decision record. Surviving triage confers **no** inherited positive
evidence of any kind.

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
- The run summary states which **money-already-moving sources** (v1.8.0) were searched
  and what they yielded, including unsuccessful searches, and whether the run found
  budget evidence or only complaint-forum evidence.
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
- A funnel run reports the observation pool: total observations, source-class
  distribution, change-driven vs persistent-market-failure split, the number rejected
  during shallow triage with the principal reasons, the observations promoted and why,
  the triage false-negative audit (see `### Shallow triage`), and the research cost /
  lookup usage where available. The pool itself is written to
  `observations/<run-id>.md` and is never treated as scored evidence.
- For every promoted persistent-market-failure candidate the decision record states
  whether its persistence thesis is evidenced (`strong` | `weak` | `absent`) and which
  two-part test it passed or failed; candidates that fail it score under the
  missing-why-now cap.
- A run that exercises the latent-opportunity route (archetype C) reports how many
  latent observations were found, triaged, promoted and rejected, and why. Zero
  promotions is an acceptable outcome. A latent observation that fails triage but
  contains an adjacent insight becomes a seed, like any other rejection.
