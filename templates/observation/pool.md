# Opportunity-observation pool: <run-id>

- **Run:** <run-id>
- **Date:** <YYYY-MM-DD>
- **Method version:** 1.6.0
- **Pool size:** <n> (target 15–20)
- **Archetype mix:** change-driven <n> / persistent market failure <n>
- **Source mix:** regulatory <n> / non-regulatory <n>
- **Triage:** promoted <n> / rejected <n>

An observation is not an idea: it records an evidenced problem, workflow,
dissatisfaction, market failure or change without a product proposition. Rows are
not scored, carry no evidence level, and confer no inherited positive evidence on
any candidate later promoted from them (see `method/discovery.md`).

| ID | Observation (problem / workflow) | Buyer | Source class | Reg? | Archetype | Evidence (source, date) | Type | Incumbent / free-alternative check | Triage | Triage reason |
| -- | -------------------------------- | ----- | ----------- | ---- | --------- | ----------------------- | ---- | ---------------------------------- | ------ | ------------- |
| O1 |  |  |  |  | change / persistent |  | primary / practitioner / vendor / secondary |  | promote / reject |  |

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
