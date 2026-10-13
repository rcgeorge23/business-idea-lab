# Discovery

Method version: see `method/VERSION`. This file defines how candidates are found,
screened for novelty, deduplicated, and how adjacent opportunities are preserved.

Discovery is **search-intent-first** (v1.9.0). A normal run starts from the exact
queries real people use to get a job done, identifies the underlying task, examines the
pages and products ranking for those queries, looks for a neglected sub-niche with an
evidenced underserved wedge, and forms a **paid self-service hypothesis** for it.
Organic search is the primary acquisition channel; purchase and delivery must be
self-service; and the operator is a solo, part-time developer who does not do sales
calls, demos, custom integration work or procurement.

The change/discontinuity route documented below remains fully valid as **one route**
(archetypes A, B and C), not the default: search-led hypotheses (archetype D) are part
of every normal sweep. Search volume alone never proves willingness to pay, and no
volume, ranking, CPC, trend or difficulty figure may be invented: missing evidence is
recorded as `unknown` with a low-cost next check.

## The discontinuity test

A **change-driven** candidate must be able to complete this sentence with a specific,
dated, cited change:

> **This was not an attractive business three years ago, but it might be now because
> ______ changed.**

"Because the problem exists" is not an answer. "Because AI assistants became a
mass-market buying surface in 2024-2025" is an answer when tied to evidence. The change
need not be brand new; it must be *identifiable and material*, and the candidate must
explain why it creates or widens an opening now rather than at any time in the past.

Prefer changes that are hard to reverse, create urgency or compulsion, or invalidate an
incumbent's position. Reject candidates whose only "why now" is a general trend.
Search-led candidates (archetype D, below) are exempt from this test: evergreen search
demand is evidenced by dated queries and SERPs, not by an invented discontinuity.

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
expected; repeatedly mining one class is a reason to justify the choice. Under v1.9.0
search-intent classes (query clusters and SERP page types) are searched every normal
run; the change classes in this table are rotated alongside them.

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
looking. The same scrutiny applies to search-led sub-niches (v1.9.0): check whether the
neglected wedge is an operational seam in what the ranking solutions cover, not a
surface variation of the same product.

## Why now? (v1.9.0)

Every candidate records `why_now` in `ideas/index.json` and a "Why now?" section in its
dossier:

```json
"why_now": {
  "changed": "what changed, in one sentence",
  "changed_date": "YYYY-MM-DD or YYYY-MM or 'announced'",
  "strength": "strong | weak | absent | not-required",
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
  under `### Four discovery archetypes (v1.9.0)`.
- **Search-led candidates (archetype D, v1.9.0) record `strength: "not-required"`.** An
  evergreen search-led niche does not need a contrived discontinuity: no change is
  recorded and none may be invented. The search-intent basis goes in `why_it_matters`
  and is cited in `evidence`, with the full dated query/SERP record in the scorecard's
  `seo_assessment`. The missing-why-now cap does not apply. This exemption removes the
  cap only - it is not a score bonus and it does not relax any evidence requirement.

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
   seed-only: fresh discovery (search-led or change-driven) remains required, and seeds
   that do not survive the shallow check stay seeds (update their status, or note in the
   run summary why they remain `unexplored`).
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
- Non-regulatory classes include (v1.9.0) search-intent evidence - named query clusters
  and live SERP gaps showing an underserved job; plus poor, expensive or unpopular
  narrow incumbent software; repetitive professional/service work newly automatable with
  current AI; software shutdown, end-of-life or forced-migration gaps; newly accessible
  APIs or datasets; awkward integrations between established systems; recurring
  spreadsheet/email/PDF/manual re-keying workflows; platform access, pricing or policy
  changes that create a new operational problem; underserved subsegments of an
  existing category; and (v1.8.0) money-already-moving sources - job advertisements
  describing repetitive administrative work, service/agency pricing pages, public
  procurement and tender records, incumbent support forums and release notes, trade
  press reporting spend or staffing, and job descriptions for roles that exist only to
  bridge two systems.
- A candidate "qualifies" for its source class because of where its primary discovery
  evidence came from (for a change-driven candidate, where its why-now came from). A
  search-led candidate sourced from query/SERP evidence qualifies as non-regulatory.
  Record the class and the reason in the run summary; a candidate whose primary
  evidence is a mandate counts against the regulatory slot even if it also has a
  second-order seam.
- **Never manufacture weak candidates to satisfy the budget.** Fewer than three
  candidates is a valid run; killing every candidate is a valid run; advancing
  nothing is a valid run. If a class was searched and yielded nothing, record that
  as a finding, including unsuccessful searches.
- If the budget cannot be satisfied honestly (for example, a run where no
  non-regulatory class yields anything worth registering), that is itself a
  convergence signal to report — not a reason to relax the rule or promote filler.

## Search-intent discovery funnel (v1.9.0)

Discovery runs as a search-intent funnel, not as a search for three ideas and no longer
against a 15-20 observation quota:

> **3-5 qualified hypotheses → shallow triage → at most 3 full candidates
> → the existing rigorous evaluation.**

A normal run produces a shortlist of 3-5 materially distinct qualified hypotheses —
fewer when the evidence is weak, and an honest zero is valid. If the sweep does not
support five qualified hypotheses, record the shortfall rather than manufacturing
filler. The funnel changes the *shape of discovery only*: scoring, threshold,
hard-filter semantics, evidence levels, lifecycle gates and the candidate/advancement
maxima are unchanged. Hypotheses are not scored and carry no evidence level.

Every qualified hypothesis follows one chain:

> **exact seed query/queries → the job/task behind the query → the existing solutions
> ranking for it → a neglected sub-niche → a paid self-service hypothesis.**

"Paid self-service" means the target buyer can find the product through organic search,
sign up, pay and use it without a demo, call or hand-holding, and a solo part-time
operator can deliver it at the modelled scale. A hypothesis that cannot produce a
coherent self-service purchase and delivery path is weak by definition and is triaged
out honestly (see `### Shallow triage`).

The funnel's steps:

1. **Sweep query-intent leads.** Aim for 3-5 qualified hypotheses; record only
   evidence-supported ones. Each hypothesis starts from exact seed queries and follows
   the chain above, recording at minimum the fields in `### Observation record (v1.9.0)`.
   Zero latent observations are valid; never manufacture filler.
2. **Shallow-triage every hypothesis.** Record negative evidence and the reason for
   every rejection. Competitor existence alone is never treated as wedge failure (see
   `### Shallow triage`).
3. **Promote at most 3 materially distinct candidates.** Each promotion names its
   originating observation ID, archetype, source class and why, and meets the
   source-class budget. No candidate inherits positive evidence from triage survival or
   from a seed (see `### Promotion`, `## Source-class budget`).
4. **Run the triage false-negative audit.** Exactly one rejected hypothesis per normal
   run is cheaply re-checked and recorded, favouring promising/high-ambiguity rejections
   (see `#### Triage false-negative audit (v1.6.0)`).

Every normal run also conducts a bounded latent-signal search pass as one lens within
the sweep (see `### Bounded latent-signal search pass (v1.8.2)`).

### What counts as an observation (v1.9.0)

An observation is deliberately lighter than a business idea and remains
evidence-cheap: no scorecard, dossier or evidence level is created for it. Under
v1.9.0 the normal pool is the run's shortlist of 3-5 qualified hypotheses, each
following the query-intent chain above. Record only hypotheses supported by the
evidence actually gathered; a compliant search that yields no qualified hypothesis is
recorded as such and is a valid run.

Acceptable shapes include:

- "People search `<exact query>` when they need to `<job>`; the pages ranking for it are
  A, B and C, and none serves `<sub-niche>`" (search-led, archetype D).
- "Small firms in segment X repeatedly export data from system A and manually re-key
  it into system B" (archetype B or C, when evidenced).
- "Organisations in niche Y pay disproportionately high annual fees for software they
  use only a few times per year" (archetype B).
- "A repetitive professional service costing £N per case now appears technically
  automatable" (archetype A or B).
- "A platform/API/product change has created a new operational task for an
  identifiable buyer" (archetype A).
- "Buyers in segment X accept a costly routine as normal, and a newly available
  capability could change it" (a **latent-opportunity hypothesis** - see archetype C;
  admissible only with the six required fields).

Do not create scorecards or dossiers for observations.

### Observation record (v1.9.0)

A run records its pool in `observations/<run-id>.md` (template:
`templates/observation/pool.md`). A qualified hypothesis records at minimum:

- the exact seed query/queries and the intent cluster they belong to;
- the job/task behind the query;
- dated demand evidence: named sources with dates; a reported volume only where a
  credible named source exists (tool and month), otherwise `unknown`;
- the live SERP landscape where checked: named pages/competitors with dates across
  organic, ads, forums, government, AI answers and marketplaces;
- the neglected sub-niche and why the wedge may be underserved, including the negative
  evidence found;
- the paid self-service hypothesis (who pays, for what, and at what point in the search
  journey);
- the source class it came from and, for a latent hypothesis, the behavior-signal lens;
- its archetype: change-driven, persistent market failure, latent opportunity, or
  search-led;
- the evidence/source(s) and evidence type — primary, practitioner/community, vendor,
  or secondary;
- an obvious incumbent / free-alternative check;
- the triage outcome and reason.

Keep each row compact: the pool must fit comfortably inside one run's budget. The full
evidence standard for search-led work is in `### SEO evidence standard (v1.9.0)`.

### SEO evidence standard (v1.9.0)

Search-led discovery is only as good as the evidence recorded for it. This standard
applies from the hypothesis record onward and, for promoted candidates, is captured in
the scorecard's required `seo_assessment` block (see `method/scorecard.md`).

- **Exact seed queries and intent clusters.** Record the literal query strings, grouped
  into the job/intent cluster they represent. A remembered or paraphrased query list is
  not evidence.
- **Demand evidence, dated.** Each demand claim names its source and date. Report a
  volume only where a credible named source exists (tool name and observation month);
  otherwise record `unknown`. Never invent volumes, rankings, CPC, trends or difficulty
  figures.
- **SERP landscape checks.** Record what was actually seen on the results page for the
  checked queries, with the check date: organic results, ads, forums, government pages,
  AI answers/overviews and marketplaces, naming the specific pages and competitors.
  Blocked or failed checks are recorded honestly as blocked/failed - never as absence
  of demand.
- **Organic entry feasibility (qualitative).** State how a new entrant could reach
  these results without false precision: is the SERP dominated by institutions,
  aggregators, stale or thin content that a small focused site could outserve? No
  invented difficulty scores or ranking predictions.
- **Conversion mechanics.** Describe the self-service path: search result → landing
  page → signup → payment → use, naming what the path requires (pricing page, free
  tool, trial) and anything that would block self-service (mandatory demo, onboarding
  call, custom setup).
- **Traffic-to-revenue scenarios are assumptions, not forecasts.** Record
  conservative/modest/optimistic narratives with an explicit assumptions label; never
  present them as expected outcomes and never invent traffic, conversion or revenue
  numbers.
- **SEO risks.** Record AI overviews / zero-click exposure, seasonality, platform/SERP
  dependency, and any other SEO-specific risk.
- **Unknowns with a next check.** Every unverified item is recorded as unknown with the
  cheapest low-touch check that would settle it.

Three rules constrain how this evidence may be used:

1. **Search volume alone is not proof of willingness to pay.** Queries show intent to
   solve something; they do not show that this buyer pays for this solution.
2. **A blocked or failed SERP check is recorded as such** and is never evidence that no
   competitor, demand or opportunity exists.
3. **Recommendations must be falsifiable at low cost.** If an SEO claim cannot be
   checked cheaply, or a hypothesis cannot name a cheap disconfirming test, it is
   parked, not promoted.

### Bounded latent-signal search pass (v1.8.2)

Every normal run conducts and records at least one deliberate, bounded search
pass for behavior that could motivate a latent-opportunity hypothesis. This is a search
instruction, not a requirement to find or register a latent observation. It may reuse
searches already made for the hypothesis sweep; do not duplicate work just to create a
separate count.

Keep two concepts separate:

| Search dimension | What it means | Examples |
|---|---|---|
| **Behavior-signal lens (what to look for)** | A pattern in current or newly possible behavior that may reveal an unarticulated benefit | Repeated shadow work or manual workarounds; work delayed, skipped or never attempted because of cost or complexity; handoffs, reconciliation, exceptions, duplicated effort or costs shifted to another party; recurring manual services or roles; a task newly feasible because of a capability or change |
| **Source class (where to look)** | The kind of public or otherwise permitted material that can evidence a lens | Public workflow artifacts or instructions (forms, spreadsheets, manuals, integration guides); job descriptions; service scopes and pricing; practitioner/community or support discussions; incumbent release notes; public procurement/tender records; trade or professional reporting |

Search one or more relevant lenses through appropriate source classes, within the run's
existing lookup and cost limits. There is no requirement to search every lens, every
source class, or every lens/source-class combination. Record the focus or query, date,
source class, lens, and yield. Mark searches that were unavailable or blocked and say
why; record a searched-but-empty result as **no usable result**, not as evidence that
the behavior or an unmet need does not exist. A pass that reuses another sweep search
must still identify its lens and yield in the pass log.

The pass may return no result, an isolated behavior signal, or a signal already well
served by alternatives. None creates a latent observation automatically. Absence of
complaints, searches, or results is not evidence of non-consumption; observed behavior
is a hypothesis-generating signal, not evidence of demand. A latent observation still
requires all six archetype-C fields below, and a plausible benefit or novelty claim
alone cannot establish demand, pass a hard filter, or justify promotion.

### Four discovery archetypes (v1.9.0)

Every hypothesis and candidate is labelled with exactly one archetype. The archetype is
a discovery-sourcing label: it is not a lifecycle state and not an evidence level. The
first three are the change/discontinuity routes; D is the v1.9.0 search-led route.

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

For **search-led** candidates (archetype D) the cap does not apply at all (v1.9.0):
evergreen search demand is expected and `why_now.strength: "not-required"` is recorded.
The exemption removes the cap only; it is not a scoring bonus.

**C. Latent opportunity (v1.7.0).** Some worthwhile products change a behaviour the
buyer currently accepts as normal. The buyer may not discuss a "problem" because they
have not seen the alternative, so a sweep that only looks for articulated pain can
under-source or prematurely reject these hypotheses. This archetype is a **guarded
route**, not a relaxation of standards: "customers do not know they need it yet" is
**never** a blanket defence for an unevidenced idea, and it does not lift any score cap,
lower the threshold, redefine evidence levels or upgrade a hard filter.

An observation may be recorded as a latent-opportunity hypothesis only if it names all
of the following. Factual claims must be backed by dated observable evidence; distinguish
those observations from labelled inferences and assumptions rather than presenting a
plausible mechanism or benefit as an observed fact:

1. **The specific buyer/user and their current behaviour or constraint** - what they
   actually do today, observed (a costly routine treated as normal, a workaround in a
   neighbouring market, an accepted constraint), not inferred from a trend narrative.
2. **The newly possible experience or capability and a concrete mechanism** - cite the
   dated evidence for the capability; label an unverified application or mechanism as
   inference or assumption. State how it could change time, cost, quality, access or
   outcomes, and by what means.
3. **Why the buyer might value the difference despite not requesting it** - the
   inference about value, labelled as inference, with the reasoning shown.
4. **Why now, or an honest statement that no discontinuity is known.** A latent
   hypothesis may have no favourable discontinuity; record `strength: "absent"` and do
   not fabricate one. Do not treat a search yielding no change as proof that no
   discontinuity exists. The missing-why-now cap applies exactly as for archetype B
   unless an evidence-backed persistence thesis lifts it.
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
- Expensive external validation, outreach, public-facing content publication outside
  repository maintenance, and spend still require human approval under
  `method/experiment-rules.md`.

A latent observation is recorded in the pool like any other, with its archetype marked
`latent` and the six admissibility fields present; it is triaged and promoted under the
same rules and limits as the other archetypes. The archetype is a **subtype of discovery
sourcing**, not a new lifecycle state or evidence level.

**D. Search-led (v1.9.0).** The default route under the 1.9.0 pivot. Dated query/SERP
evidence shows that people already search for a specific job, the pages ranking for
those queries leave a neglected sub-niche, and a paid self-service product could serve
it. This is an *intent-evidenced evergreen niche*: a discontinuity is neither required
nor invented, and `why_now.strength` is recorded as `not-required` with the search
evidence in the scorecard's `seo_assessment`.

The search-led route changes where the hypothesis comes from; it is not a shortcut and
not a score bonus. A search-led candidate must still satisfy all 12 hard filters -
including `seo_discoverable`, `self_serve_purchase` and `solo_operator_fit` - pass the
novelty/incumbent sanity check, and meet the same evidence requirements as any other
candidate (see `### SEO evidence standard (v1.9.0)`). Search volume alone is not proof
of willingness to pay, and a remembered or plausible query list without dated query/SERP
evidence does not score. The route removes the missing-why-now cap only: no filter is
relaxed, no evidence requirement is lowered, and no dimension is scored higher because
the niche is evergreen.

### Bias the sweep toward search intent (v1.9.0)

Search-intent-first is the primary sourcing bias. Point the sweep at the queries buyers
actually type for a job - "[job] software", "[task] tool", "[thing] template",
"alternative to [incumbent]", "[task] for [segment]" - and follow the chain to the
existing solutions and the neglected sub-niche. Record the exact query strings, not a
paraphrase. The other biases below sharpen which niches to query, but they never
replace query evidence; do not start from a change announcement and work backwards to a
product unless the change route (archetypes A/B) is genuinely the stronger evidence.
Runs may mix archetypes, and a run may be entirely search-led.

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

Method 1.8.0 therefore requires every normal run to aim a meaningful share of
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
`defensible_wedge` is unchanged. Under v1.9.0 it is a **secondary** sourcing bias
within search-intent-first discovery: use it to find which niches and queries are worth
the sweep, not as evidence by itself.

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
- the named queries show no self-service purchase intent or no reachable organic entry
  for a new entrant, and no neglected sub-niche is evidenced (v1.9.0);
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

Triage makes most of the funnel's decisions, so every **normal run** independently
re-checks **exactly one triage-rejected hypothesis** afterwards. This is a cheap
sample, not a second triage pass:

- **Selection favours promising/high-ambiguity rejections**, not a uniform random draw:
  prefer a hypothesis with relatively strong practitioner/problem or query/SERP evidence
  that was rejected because an incumbent, free alternative or crowded field appeared to
  occupy the seam. Record why it was selected.
- **The audit tests whether triage confused:**
  1. existence of competitors with adequate customer satisfaction;
  2. a feature with a complete solution;
  3. enterprise availability with accessibility to the target niche;
  4. vendor claims with demonstrated capability;
  5. one-shot migration/service availability with attractive recurring product
     economics.
- **Keep it cheap:** one hypothesis and a bounded check roughly the cost of one
  observation; no full candidate research, no re-opening every rejection.
- **Record** in the run summary and the pool file: the hypothesis selected; why it was
  selected; the original triage reasoning; the additional evidence checked; whether the
  rejection is upheld or overturned; and the implication for triage depth.
- **A single overturn does not automatically change the method.** Repeated overturns are
  a signal to review triage depth (and possibly sampling) in a later method review; note
  the pattern rather than reacting to one case.
- **Edge case:** if a run's triage rejected nothing (every shortlisted hypothesis was
  promoted), there is no rejection to sample. The run must state that explicitly rather
  than inventing one; this should be rare because the shortlist is 3-5 and promotion is
  capped at 3.

### Promotion

At most **3** observations become full candidates. Favour observations with the
strongest combination of: credible problem evidence; an identifiable buyer; a
plausible route to payment; evidence that alternatives leave a meaningful gap; an
inexpensive path to falsification; and reasonable fit for a small/bootstrapped
business. A search-led hypothesis additionally needs dated query/SERP evidence and a
credible self-service path. Zero, one or two promotions are valid — never select
candidates merely to fill three slots, and never promote filler to satisfy the
source-class budget.

Once promoted, a candidate goes through the **existing full process unchanged**:
fresh research, fingerprint/duplicate check, incumbent/novelty sanity check, evidence
register, the 12 hard filters, a schema-v2 scorecard, adversarial review, lifecycle
decision, and at most one `validation-ready` advancement. Name the originating
observation ID, the archetype, the source class and why in the candidate's decision
record, and record the second-order seam where one exists. Surviving triage confers
**no** inherited positive evidence of any kind.

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

For search-led candidates, an overlapping intent cluster with the same buyer and
problem counts as a duplicate signal under the same test.

## Adjacent opportunity seeds

Rejections often surface a better-adjacent proposition (e.g. "discovery is commoditised
but application quality is not"). Preserve it as a seed so a later run can investigate
without resurrecting the killed idea:

- one file per seed under `seeds/<slug>.md`, one entry in `seeds/index.json`;
- record the parent idea, the observation, the evidence for it, and what would make it
  materially different from the parent;
- seeds carry **no** score, confidence or evidence level, and cannot be promoted without
  their own dossier, evidence and scorecard.

## Recording (v1.9.0)

- The run summary lists the source classes searched (regulatory vs non-regulatory,
  successful and unsuccessful) and what they yielded.
- The run summary reports the hypothesis shortlist: shortlist size (3-5 target; fewer
  or zero valid), source mix, archetype split including search-led, the number rejected
  in shallow triage with the principal reasons, and the hypotheses promoted and why.
- The run summary records the triage false-negative audit: the rejected hypothesis
  selected, why, the original reasoning, the additional evidence checked, whether the
  rejection was upheld or overturned, and the implication for triage depth. A run whose
  triage rejected nothing must say so explicitly.
- Every normal run records a bounded latent-signal search pass in the observation pool
  and run summary: behavior lens/lenses, source class/classes, search focus or
  query, date, and yield, including no-result, blocked or unavailable searches. The
  pass has no hit, observation or candidate quota; its completion does not imply that a
  latent opportunity exists.
- The run summary states which **money-already-moving sources** (v1.8.0) were searched
  and what they yielded, including unsuccessful searches, and whether the run found
  budget evidence or only complaint-forum evidence.
- The run summary states, for each generated candidate, whether its why-now is evidenced
  (`strong` | `weak` | `absent` | `not-required`, the last for search-led candidates).
- The run summary states each candidate's provenance (`seed:<seed-slug>` or `fresh`),
  the source class it qualifies under and why, the originating observation ID, and,
  where a second-order seam exists, the seam the candidate addresses and why it was
  preferred to the obvious first-order product.
- The run summary states whether the source-class budget was satisfied and why.
- The run summary answers whether discovery appears to be converging on less obvious,
  better-defended opportunities, or repeatedly finding and rejecting the same class of
  candidate. A recurring cluster of `defensible_wedge` kills is a signal to review
  discovery — not to weaken the filter.
- Rejected candidates keep their why-now analysis in the decision record.
- The run summary confirms that no manufactured observations or candidates were added;
  zero promotions is a valid run.
- The pool itself is written to `observations/<run-id>.md` and is never treated as
  scored evidence.
- For every promoted persistent-market-failure candidate the decision record states
  whether its persistence thesis is evidenced (`strong` | `weak` | `absent`) and which
  two-part test it passed or failed; candidates that fail it score under the
  missing-why-now cap.
- The run summary reports counts of latent observations found, triaged, promoted and
  rejected, including zeros, and why. Zero latent observations or promotions are
  acceptable. A latent observation that fails triage but contains an adjacent insight
  becomes a seed, like any other rejection.
