# evidence/ — evidence registers

One directory per idea: `evidence/<slug>/`, containing one file per source or
research artefact, named `<YYYY-MM-DD>-<slug-of-source>.md` and following
`templates/evidence/entry.md`.

Rules (full policy in `method/evidence-policy.md`):

- Every material claim carries a source and a capture date.
- Separate evidence from assumptions and inference; label each explicitly.
- A positive score in `scorecard.json` links to at least one register file that
  exists in this directory.
- Unsourced claims get no score at all.
- Desk research is not demand evidence. Search volume, survey interest and
  model opinion are not demand evidence.
- Registers are append-only; supersede a claim by adding a new dated entry,
  never by deleting the old one.

Current registers:

- `geonerd/` — GeoNerd wedge, demand-validation plan, spike findings,
  competitive teardown (all internal desk research,
  `/home/richard/projects/geonerd` @ `327f02e`).
