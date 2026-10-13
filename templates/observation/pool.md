# Search-intent observation pool: <run-id>

- **Run:** <run-id>
- **Date:** <YYYY-MM-DD>
- **Method version:** 1.9.0
- **Qualified hypothesis shortlist:** <n> (target 3–5; fewer when weak; zero is valid)
- **Archetype mix:** change-driven <n> / persistent market failure <n> / latent <n> / search-led <n>
- **Source mix:** regulatory <n> / non-regulatory <n>
- **Latent-signal search pass:** completed <yes/no>
- **Triage:** promoted <n> / rejected <n>

An observation is not an idea: it records an evidenced problem, workflow,
dissatisfaction, market failure or change without a product proposition. Rows are
not scored, carry no evidence level, and confer no inherited positive evidence on
any candidate later promoted from them (see `method/discovery.md`).

Discovery is search-intent-first (v1.9.0): exact seed query → job or task → existing
solutions → neglected sub-niche → paid self-service hypothesis. Never invent search
volumes, rankings, CPC, trends or difficulty: record `unknown` plus a low-cost next
check. Search volume alone is not proof of willingness to pay, and a blocked or
failed SERP check is not evidence that demand is absent.

## Qualified hypotheses (search-intent shortlist, v1.9.0)

One row per qualified hypothesis; aim for 3–5 per normal run, fewer when the
evidence is weak, and zero is a valid outcome. Competitor existence alone is never
treated as wedge failure; record the negative evidence actually checked.

| ID | Seed query / intent cluster | Job or task behind the query | Existing solutions (named; SERP date checked) | Neglected sub-niche and underserved wedge (evidence / negative evidence) | Paid self-service hypothesis | Source class (where) | Archetype | Demand evidence (source, date; volume only if credible) | Triage | Triage reason |
| -- | --------------------------- | ---------------------------- | -------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------- | -------------------- | --------- | -------------------------------------------------------- | ------ | ------------- |
| H1 |  |  |  |  |  |  | change / persistent / latent / search-led |  | promote / reject |  |

## Observations

| ID | Observation (problem / workflow) | Buyer | Source class (where) | Signal lens (latent only; what) | Reg? | Archetype | Evidence (source, date) | Type | Incumbent / free-alternative check | Triage | Triage reason |
| -- | -------------------------------- | ----- | -------------------- | ------------------------------- | ---- | --------- | ----------------------- | ---- | ---------------------------------- | ------ | ------------- |
| O1 |  |  |  |  |  | change / persistent / latent / search-led |  | primary / practitioner / vendor / secondary |  | promote / reject |  |

### Latent-opportunity observations (archetype C)

A latent observation is admissible only with all six fields below (see
`method/discovery.md` archetype C). Cite dated evidence for factual claims and label
each claim as an observation, inference or assumption; do not dress a plausible
mechanism or benefit as observed fact. Record one block per latent observation; a
latent observation missing any field is not admissible.

| Required field | Claim (label observation / inference / assumption) | Dated source(s) and observed evidence |
|---|---|---|
| Observation ID | | |
| Buyer/user and observed current behaviour or constraint | | |
| Newly possible capability and concrete mechanism | | |
| Why the buyer might value it despite not requesting it (inference) | | |
| Why now, or "no discontinuity known" | | |
| Existing substitute / status quo and competitors | | |
| Central falsifiable assumption and cheapest behavioural test | | |

## Latent-signal search pass (required in every normal run)

Record at least one deliberate, bounded search, including its yield even when there is
no usable result. The lens is **what behavior to look for**; the source class is
**where to look**. Searches made for the wider sweep may be reused. Do not fill every
lens or lens/source-class combination, and do not create a latent observation to satisfy
a quota. A no-result search or absence of complaints establishes neither that behavior
is absent nor that buyer demand exists.

| Behavior-signal lens (what) | Source class / source (where) | Focus or query | Search date | Yield (observation IDs, no usable result, or blocked/unavailable reason) |
|---|---|---|---|---|
| <e.g. repeated shadow work; delayed/skipped work; handoff/reconciliation; recurring manual service; newly feasible task> | <e.g. workflow instructions; job description; service scope/pricing; support discussion; release note; procurement> | | | |

## Promoted observations

| ID | Promoted to candidate | Why it was promoted |
| -- | --------------------- | ------------------- |
|  |  |  |

## Triage false-negative audit

Exactly one rejected observation is re-checked per normal funnel run, preferring
promising/high-ambiguity rejections (see `method/discovery.md`). Record it here and
in the run summary: observation selected; why; original triage reasoning; additional
evidence checked; upheld or overturned; implication for triage depth.

| Field | Value |
|---|---|
| Observation selected | |
| Why selected | |
| Original triage reasoning | |
| Additional evidence checked | |
| Outcome | upheld / overturned |
| Implication for triage depth | |

## Notes

- Evidence type meanings: **primary** (official documents, first-party data),
  **practitioner** (forums, communities, support threads, job ads, service
  pricing), **vendor** (vendor marketing, release notes), **secondary**
  (journalism, analyst summaries).
- A rejected observation with an adjacent insight becomes a seed under `seeds/`,
  never a candidate.
- "I could not establish why this persists" is an acceptable archetype-B answer
  and should be recorded as triage evidence.
- A latent-opportunity observation (archetype C) is admissible only with the six
  required fields above; "customers do not know they need it yet" is never a
  substitute for a buyer, mechanism, distribution route or falsifiable test.
- Every factual field in a latent block cites dated source evidence. The value claim is
  explicitly an inference; an unverified buyer, mechanism or willingness-to-pay claim is
  an assumption. Neither novelty nor inferred benefit is demand evidence or enough on
  its own to pass a hard filter or promote an observation.
- Any candidate promoted from a search-led hypothesis must carry a complete
  `seo_assessment` in its schema-v2 scorecard (see `method/scorecard.md`): exact seed
  queries and intent clusters, dated demand evidence, the SERP landscape with dates,
  qualitative organic entry feasibility, conversion mechanics, assumption-labelled
  traffic-to-revenue scenarios, SEO risks, and unknowns with low-cost next checks.
- Research promise, search opportunity and commercial validation are three distinct
  registers: an evidenced search opportunity is not validated demand, and a promising
  mechanism is not paid usage.
