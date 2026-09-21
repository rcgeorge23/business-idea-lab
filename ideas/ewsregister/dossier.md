# EwsRegister: Exchange Web Services dependency discovery before the 2027 shutdown

- **ID / slug:** `ewsregister`
- **State:** `killed`
- **Evidence level:** `Plausible`
- **Owner:** worker
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** worker run `20260921T085149Z-normal`, fresh discontinuity hunt - source class
  "software shutdown / end-of-life / forced-migration gaps" (searched this run, overlapping the
  previous run's accounting-EOL scan)

## One-sentence proposition

> SMBs and the MSPs that manage them have hidden Exchange Web Services dependencies that will break
> at Microsoft's 2027 shutdown; we provide discovery and a maintained migration register at a low
> monthly price.

## Why now?

> This was not an attractive business three years ago, but it might be now because Microsoft
> announced the phased disablement of Exchange Web Services in Exchange Online with a hard 2027
> shutdown date.

- What changed: Microsoft begins tenant-by-tenant EWS disablement in Exchange Online on
  1 October 2026, with permanent shutdown on 1 April 2027; EWS is commonly embedded in backup jobs,
  archive connectors, public-folder workflows, scheduling apps and scripts.
- When it changed: announced for 1 October 2026 / 1 April 2027.
- Evidence (dated source): `evidence/ewsregister/2026-09-21-ews-retirement-and-usage-visibility.md`
  (ITECS 2026-08-20, citing Microsoft's plan and the `EWSEnabled` / `EWSAllowedAppIDs` controls).
- Why this materially improves the opportunity now: a dated, non-negotiable shutdown creates a
  window of forced action that did not exist before, and the dependency set is invisible by
  default.
- Have competitors already responded? Partly - Microsoft ships a free EWS usage report and tenant
  controls, and IT consultancies publish migration guidance; no dedicated discovery product was
  found, but none was needed for the incumbent position to be covered.
- Strength: `strong`

## Buyer

- Who exactly pays (role, company size, segment): assumed to be managed service providers and IT
  managers at SMBs running Microsoft 365.
- Who uses it: IT administrators and MSP technicians.
- Evidence: none for the buyer or its budget. Resolution is named in the scorecard `resolve_via`.

## Problem

- What is painful/frequent/expensive: silent EWS dependencies break at disablement; discovering them
  is manual and Microsoft's usage report covers only 7/30/90-day windows, aggregated weekly, so
  infrequent or seasonal applications can be missed.
- Current alternatives and their weaknesses: Microsoft's own free usage report and tenant controls;
  one-off consultancy migration projects; migration tooling from IT vendors.
- Evidence: `evidence/ewsregister/2026-09-21-ews-retirement-and-usage-visibility.md`.

## Mechanism / wedge

- What we would actually do: a tool that scans a tenant's EWS usage, maps it to business owners and
  vendors, and maintains a migration register with exceptions and expiry.
- Why it is defensible against the cheapest credible incumbent: it is not - Microsoft's usage report
  is authoritative and free, the gap it leaves is narrow, and the work is a one-shot project that
  MSPs already sell as consulting.
- Evidence: `evidence/ewsregister/2026-09-21-ews-retirement-and-usage-visibility.md`.

## Novelty / incumbent sanity check

| Check | Answer | Evidence |
|---|---|---|
| Does this exact product already exist? | No dedicated product found; Microsoft ships reporting + controls | evidence file, section 1 |
| Are there multiple credible providers? | Yes, in services form - MSPs/consultancies and Microsoft itself | ITECS 2026-08-20 |
| Is the wedge already a standard feature? | Discovery is available free via Microsoft's usage report | evidence file |
| Is a free/authoritative alternative already adequate? | Yes, for the core need | evidence file |
| Has a well-capitalised company shown hostile unit economics? | No evidence | - |
| Is this merely a feature of an established category? | Yes - Microsoft 365 migration services | evidence file |

If any check fails, state the reason to continue anyway: it was not continued. The candidate was
generated to test a previously underexplored class; it was killed once the free authoritative
alternative and one-shot nature of the work were established.

## Distribution

- Route to the first 10 buyers without paid acquisition: none evidenced. MSP communities are
  plausible but no prospects identified.
- Evidence: none.

## Economics (assumptions labelled)

- Price hypothesis (assumption): low monthly subscription or per-tenant scan fee.
- Cost drivers (assumption): support and continuous spec/tool maintenance against a one-shot need.
- Contribution margin at realistic scale: not modelled; a one-shot migration is a poor recurring
  subscription.

## Founder fit

- Reach, skills, motivation (evidence only; `null` if unknown): `null`.

## Adversarial case (strongest case this is wrong)

Nobody wants a discovery product here. The people who know a tenant has EWS dependencies are
Microsoft's own reports and the tenant's historical scripts; the free report plus a gateway/IP
blocking test answers the question in an afternoon. The affected population that cannot do this
itself (small SMBs) does not buy tools - it calls its MSP, and the MSP's incentive is to sell a
migration project, not a subscription. Microsoft is closing the visibility gap over time and offers
`EWSAllowedAppIDs` for exceptions. Any product is a thin wrapper over first-party data with a
one-shot market and a hard expiry date: by mid-2027 the entire opportunity is gone.

## Strongest supporting case

The deadline is real and dated, the dependency set is genuinely invisible, and MSPs will be
inundated with break-fix calls in late 2026; a per-tenant scanner could be sold through MSP
marketplaces before the window closes.

## Unresolved assumptions

| Assumption | How it could be falsified | Status |
|---|---|---|
| SMBs/MSPs would pay for discovery rather than use the free report | Ask 5 MSPs what they charge and what they use | unresolved |
| Microsoft's usage report is genuinely inadequate | Test against a tenant with infrequent EWS use | unresolved |
| A recurring product (not one-shot) is possible | Map the post-migration job | unresolved |

## Cheapest decisive experiment

- Assumption under test: the free authoritative alternative is adequate.
- Proposed test: none. The desk scan already disconfirmed the wedge; no experiment proposed.
- Pre-fixed decision rule: n/a.
- Cost bound: n/a (desk research, 0 human-hours, £0).
- Status: not proposed (idea killed)
- Link: none

## Decision log (append-only)

| Date | State change | Why | Link |
|---|---|---|---|
| 2026-09-21 | `discovered` -> `killed` | `defensible_wedge` fail: Microsoft's free EWS usage report and tenant controls cover the core need; work is one-shot migration services already served by MSPs and consultancies. | `ideas/ewsregister/decision.md` |
