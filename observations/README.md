# Opportunity observations

Per-run opportunity-observation pools produced by the discovery funnel
(`method/discovery.md`, section "Opportunity-observation funnel", method 1.6.0).

- One file per run: `observations/<run-id>.md`, written from
  `templates/observation/pool.md`.
- A pool holds 15–20 materially distinct observations; each is triaged cheaply
  before at most three are promoted to full candidates.
- Each normal funnel run re-checks exactly one triage-rejected observation (favouring
  promising/high-ambiguity rejections) as a sampled false-negative audit, recorded in
  the pool file and the run summary.
- Observations are **not** ideas. They carry no score, confidence, evidence level
  or lifecycle state, and surviving triage confers no inherited positive evidence
  on any candidate.
- Promoted candidates go through the existing full evaluation unchanged; their
  decision records name the originating observation ID.
- Rejected observations with an adjacent insight become non-inheriting seeds under
  `seeds/`, never candidates.

The run summary reports the pool counts, source mix, archetype mix, triage
outcomes and the promoted observations (`templates/run/summary.md`).
