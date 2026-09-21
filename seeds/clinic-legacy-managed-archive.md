# Seed: Managed read-only archive and retention for clinics that keep legacy clinical records

- **Seed ID / slug:** `clinic-legacy-managed-archive` / `clinic-legacy-managed-archive`
- **Origin idea:** `clinicdata-liberation` (`killed`)
- **Recorded:** 2026-09-21
- **Status:** `unexplored`

**This seed does not inherit any score, evidence level or hard-filter status from
`clinicdata-liberation`.** The parent was killed on the `defensible_wedge` hard filter. A
future run must research this seed from scratch, including its own novelty check,
evidence register, hard filters and scorecard.

## Observation

When a clinic retires an end-of-life clinical system it must keep historical clinical
records accessible for years. The parent's research found the documented alternative to
full re-migration is a purpose-built read-only archive that reads the source system's
database backup (Cherwell's documented option, via Synapse Software, at enterprise
prices), while enterprise archivists (Archive360, AvenDATA, Docbyte, Natuvion, SNP) serve
the enterprise tier. No UK small-clinic-tier managed archive product surfaced for clinics
that keep or must access legacy records after a switch.

Sources: `evidence/clinicdata-liberation/2026-09-21-eol-cluster-2026.md`,
`evidence/clinicdata-liberation/2026-09-21-enterprise-archive-crowding.md`.

## Why it is materially different from the parent

The parent sold one-shot migration and was killed because ValueStreamAI already sells the
exact extraction method and receiving vendors give guided migration away free. This seed
has a different buyer (clinics that are retiring, or have retired, a system and need
long-term read access; and the receiving vendors that would rather not store legacy
data), a different mechanism (hosted read-only archive with a retention schedule and
export-on-request rather than extraction/migration), and recurring subscription economics
rather than a one-shot fee. It addresses the parent's recorded kill reason (a services
skill masquerading as a moat) by selling an ongoing retention obligation instead.

## Evidence for the observation

- `evidence/clinicdata-liberation/2026-09-21-eol-cluster-2026.md` — the documented
  database-backup read-only archive alternative for a retired system, and the 2026 EOL set.
- `evidence/clinicdata-liberation/2026-09-21-enterprise-archive-crowding.md` — enterprise
  archivists occupy the enterprise tier, with a healthcare example at Docbyte.
- `ideas/clinicdata-liberation/decision.md` — the parent's kill reasons, including the
  database-backup alternative, and its false-negative audit.

## What a later run should check first

- Whether receiving PIMS vendors, NHS systems or records-management providers already
  provide free retention/read access for switched-off systems (which would remove the
  buyer).
- Whether clinics in the UK have a statutory or professional retention duty that creates a
  budget, and for how many years.
- Whether a read-only archive can be built for multiple niche source systems at acceptable
  cost, and whether the database-backup route is legally and contractually available.
- Whether this is a one-off setup fee with low retention or a genuine recurring
  subscription.

## Outcome (append-only)

| Date | Outcome | Why | Link |
|---|---|---|---|
| 2026-09-21 | created | Surfaced during the `clinicdata-liberation` kill; recorded as a non-inheriting adjacent opportunity | this file |
