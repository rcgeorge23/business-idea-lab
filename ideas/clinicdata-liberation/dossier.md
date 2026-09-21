# ClinicData Liberation: productised data extraction and migration for no-export clinical software

- **ID / slug:** `clinicdata-liberation`
- **State:** `killed`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** worker run `20260921T091851Z-normal`, observation `O25` (fresh discovery)

## One-sentence proposition

> Clinic owners whose practice-management software is end-of-life or has no export path
> must migrate without losing clinical records; we provide a productised UI-level
> extraction, normalisation and document re-association service (fixed fee per
> migration), sold to migrating clinics and to the vendors receiving them. **Killed: a
> live vendor (ValueStreamAI) already sells the exact method, and receiving vendors give
> guided migration away, making this a feature of an established category.**

## Why now?

> This was not an attractive business three years ago, but it might be now because a
> cluster of clinical and practice-management platforms reaches end-of-life in 2026.

- What changed: BP Allied switches off 31 July 2026 (no updates, fixes or support);
  Cherwell Service Management reaches end-of-life 31 December 2026; on-premise RoboVet
  reached end-of-life and a UK practice migrated off it in June 2026.
- When it changed (or is due to change): 2026-07-31 (first switch-off), with a further
  date 2026-12-31. The BP Allied date is already past at the time of writing.
- Evidence (dated source), and why the change is real rather than a trend:
  `evidence/clinicdata-liberation/2026-09-21-eol-cluster-2026.md` (vendor switch-off
  notices and a migration case study). Caveat recorded: the three events are heterogeneous
  (allied health, enterprise ITSM, veterinary) and the addressable UK clinical population
  is unmeasured, so "cluster" is an interpretation, not a measured market.
- Why this materially improves the opportunity now: a fixed switch-off forces an action
  that clinics would otherwise defer.
- Have competitors already responded? Yes — ValueStreamAI sells UI-level extraction of
  no-export clinical systems at published bands; receiving vendors (Nookal, Upheal) ship
  guided migration and give it away in onboarding; enterprise archivists own the
  enterprise tier.
- Strength: `strong` (the dated events are real; the competitive response neutralises them)

## Buyer

- Who exactly pays (role, company size, segment): owner/manager of a small UK clinic
  facing a forced migration; second buyer is the receiving software vendor. The evidence
  for a paying buyer is a competitor's **published list bands** (£4k–12k, £12k–32k),
  which are inferred budget, not realised prices.
- Who uses it: practice staff (records continuity) and the receiving vendor's onboarding
  team.
- Evidence: `evidence/clinicdata-liberation/2026-09-21-no-export-extraction-and-pricing.md`

## Problem

- What is painful/frequent/expensive: the source system has no CSV/API/export in the
  target case; third-party extraction of a no-export system is sold at £4k–12k for a
  single registry, £12k–32k with clinical history and billing, £32k+ multi-site. The
  documented manual-workload figures (10–15 hours, 4–5 weeks of overlap, PDF-only notes,
  disconnected password-protected charts) come from a system that *does* export
  (SimplePractice), so they are indicative, not directly transferable to a no-export case.
- Current alternatives and their weaknesses: receiving-vendor guided imports handle
  whatever the source system exports and are given away free; at least one legacy product
  can alternatively be archived by reading its database backup (a commodity DBA-style job);
  enterprise archiving vendors serve the enterprise tier.
- Evidence: `evidence/clinicdata-liberation/2026-09-21-migration-pain-and-tooling.md`,
  `evidence/clinicdata-liberation/2026-09-21-no-export-extraction-and-pricing.md`

## Mechanism / wedge

- What we would actually do: a repeatable extraction toolkit that drives the legacy
  application's own UI inside the clinic's authenticated session, captures structured
  records and documents, normalises clients/charts, re-associates detached PDFs, and
  loads into the replacement system — priced at a fixed fee per migration.
- Why it is defensible against the cheapest credible incumbent: it is not. ValueStreamAI
  already sells this exact method, and receiving vendors give guided migration away as
  onboarding, so the "wedge" is a services skill rather than a durable asset.
- Evidence: `evidence/clinicdata-liberation/2026-09-21-no-export-extraction-and-pricing.md`

## Novelty / incumbent sanity check

| Check | Answer | Evidence |
|---|---|---|
| Does this exact product already exist? | Yes — ValueStreamAI sells UI-level extraction of no-export clinical systems at published bands | `evidence/clinicdata-liberation/2026-09-21-no-export-extraction-and-pricing.md` |
| Are there multiple credible providers? | Yes — ValueStreamAI, Nookal, Upheal, and enterprise archivists (Archive360, AvenDATA, Docbyte, Natuvion, SNP) | `evidence/clinicdata-liberation/2026-09-21-enterprise-archive-crowding.md` |
| Is the wedge already a standard feature? | Yes — receiving vendors bundle guided migration into onboarding and give it away | `evidence/clinicdata-liberation/2026-09-21-migration-pain-and-tooling.md` |
| Is a free/authoritative alternative already adequate? | Largely — the receiving vendor's guided import is free and covers the exported subset; a database-backup path is the documented alternative for one EOL system | `evidence/clinicdata-liberation/2026-09-21-eol-cluster-2026.md` |
| Has a well-capitalised company shown hostile unit economics? | Not shown for this niche, but the free-in-onboarding substitute removes the buyer regardless | `evidence/clinicdata-liberation/2026-09-21-migration-pain-and-tooling.md` |
| Is this merely a feature of an established category? | Yes — data migration services are an established category | `evidence/clinicdata-liberation/2026-09-21-enterprise-archive-crowding.md` |

If any check fails, state the reason to continue anyway: **no reason to continue.** A
live vendor already sells the exact method and the receiving vendor gives the substitute
away free, so `defensible_wedge` is a hard-filter failure. The idea is killed. It would
only be reopened if a desk check showed ≥3 named UK clinical systems with genuinely no
export path other than UI automation **and** ≥2 of 3 recent UK switchers paid a third
party rather than accept the receiving vendor's free guided migration.

## Distribution

- Route to the first 10 buyers without paid acquisition: content/SEO on
  "<product> end of life migration" queries; partnerships with receiving vendors as their
  migration arm; clinic-owner communities. No receiving vendor has signalled interest, and
  the receiving vendor is also a competitor for the switch — unvalidated.
- Evidence: `evidence/clinicdata-liberation/2026-09-21-eol-cluster-2026.md`

## Economics (assumptions labelled)

- Price hypothesis: fixed fee per migration in the documented £4k–12k single-registry
  band (assumption from a competitor's published bands, not realised prices).
- Cost drivers: hours per migration (extraction recipes amortise), data-protection
  overhead, re-association labour.
- Contribution margin at realistic scale: unknown; one-shot revenue with no retention
  unless a retention/archive service is added.

## Founder fit

- Reach, skills, motivation (evidence only; `null` if unknown): `null` — no evidence
  about who would found or sell this.

## Adversarial case (strongest case this is wrong)

Data migration is an established, crowded service category; the receiving vendor
performs the migration as part of onboarding and gives it away, which removes the buyer;
ValueStreamAI already sells exactly the UI-level extraction method; at least one legacy
product can alternatively be archived from its database backup; revenue is one-shot and
tied to a shrinking pool of EOL events, with no recurring retention; and UI-level
extraction of clinical records raises licence-term and data-protection questions. The
"wedge" is a services skill, not a durable asset. This should be killed, not parked.

## Strongest supporting case

A dated, forced-action window with a documented no-export reality and documented
third-party price bands. This is not enough: the mechanism is already sold, the free
in-onboarding substitute removes the buyer, and the buyer-behaviour evidence is
vendor-sourced.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| ≥3 named UK clinical systems have no export path other than UI automation | Desk check of 3 named systems; any export path found falsifies | untested (not tested — idea killed) |
| Clinics will pay a third party rather than accept the receiving vendor's free migration | Quote 3 recent switchers; find none who paid a third party | untested (not tested) |
| The extraction method is lawful under source-system licence terms in the UK | Obtain legal view on 2 representative licences | untested (not tested) |
| One-shot migrations can be made repeatable at acceptable margin | Time-box a dry-run extraction on 2 source systems | untested (not tested) |

## Cheapest decisive experiment

- Assumption under test: a defensible wedge exists (no shipping service already performs
  no-export extraction, and receiving vendors do not give an adequate substitute away).
- Proposed test: **desk-only** check of 3 named UK clinical systems for genuine export
  paths (including database-backup options) plus 3 switcher interviews on what they paid
  and to whom.
- Pre-fixed decision rule: proceed to a paid pilot only if ≥3 named systems have no export
  path other than UI automation **and** ≥2 of 3 switchers paid a third party or lost
  records they would have paid to recover; otherwise the idea stays killed.
- Cost bound: 6 human-hours, £0, 10 calendar days.
- Status: **not run — idea killed at the `defensible_wedge` hard filter.** Retained as
  the reopening test.
- Link: `ideas/clinicdata-liberation/decision.md`

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-21 | (new) discovered -> desk-screened -> adversarially-researched | Promoted from observation O25; full research completed | `ideas/clinicdata-liberation/decision.md` |
| 2026-09-21 | adversarially-researched -> killed | `defensible_wedge` hard-filter `fail` (ValueStreamAI already sells the exact UI-level extraction method; receiving vendors give guided migration away free; feature of an established category) and `not_all_optimistic` `fail`; independent adversarial review (idea-critic) recommended kill. Scored 49.5/100, below the 65 threshold | `ideas/clinicdata-liberation/decision.md` |
