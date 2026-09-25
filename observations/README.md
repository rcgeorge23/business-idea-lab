# Opportunity observations

Per-run opportunity-observation pools produced by the discovery funnel
(`method/discovery.md`, section "Opportunity-observation funnel", method 1.8.2).

- One file per run: `observations/<run-id>.md`, written from
  `templates/observation/pool.md`.
- A pool holds 15–20 materially distinct observations; each is triaged cheaply
  before at most three are promoted to full candidates.
- Every normal funnel run records at least one bounded latent-signal search pass,
  separating the behavior lens (what to look for) from the source class (where to look)
  and recording its focus/query, date and yield, including no-result or blocked
  searches. Sweep searches may be reused; the pass adds no signal or candidate quota.
- An empty search or absence of complaints is not evidence that the behavior is absent
  or present, and a behavior signal or inferred benefit is not demand evidence.
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

The run summary reports the pool counts, source mix, archetype mix, latent-signal search
pass and yield, triage outcomes and the promoted observations
(`templates/run/summary.md`).
