# Evidence: PRS Database 2026 rollout - shallow re-check of `prs-listing-precheck`

- **Idea / scope:** `prsregister` (seed `prs-listing-precheck`)
- **Register:** evidence
- **Source:** sources listed per claim below (URLs recorded)
- **Accessed / dated:** 2026-09-21
- **Credibility:** primary for the statutory instrument; credible secondary for law firm and
  platform write-ups; vendor marketing labelled

## Claim(s) supported

- The PRS Database regime is now a dated, regionally-phased duty with a fee and identifier
  obligations, and letting agents are given a role but no confirmed bulk/API route.
- Incumbents already contest the agent-facing compliance position: a lettings platform is building
  PRS support and a vendor already sells a flat-fee PRS compliance product.
- Agent CRM platforms already exchange the landlord/property/compliance data a pre-check would use.

## Exact detail

### 1. The statutory instrument (primary)

The Private Rented Sector Database Regulations 2026
(`https://www.legislation.gov.uk/ukdsi/2026/9780348286861/body`). Reported: regulation 1(2)/reg 3
comes into force on 15 December 2026, with other purposes on 15 September 2027; entries are made in
writing via a website or form; a letting agent or property manager may provide Part 2 Schedule 3
information on behalf of the person making a dwelling entry; entries must be updated within 28 days
of becoming out of date; registration is renewed every 12 months; a fee is payable before a dwelling
entry.

### 2. Rollout, fee and agent responsibilities (credible secondary)

Gowling WLG, "The PRS Database is coming"
(`https://gowlingwlg.com/en/insights-resources/articles/2026/the-prs-database-is-coming`), dated
2026-09-10: the "Register your rental property" service opens in the West Midlands on 15 December
2026, with all eligible England properties registered by 14 November 2027; £65 per property per
year; landlords must initiate registration even where a managing agent is appointed; agents can
upload certain information; operators are advised to agree responsibilities, controls and
timescales.

Goodlord, "The Government confirms Register Your Rental Property service..."
(`https://blog.goodlord.co/the-government-confirms-register-your-rental-property-service-what-landlords-and-letting-agents-need-to-know`),
dated 2026-09-10: regional rollout table (West Midlands open 15 Dec 2026 / deadline 14 Mar 2027;
East of England 15 Jan / 14 Apr 2027; East Midlands 15 Feb / 14 May 2027; South East 15 Mar /
14 Jun 2027; Yorkshire & Humber 15 Apr / 14 Jul 2027; North West 15 May / 14 Aug 2027; North East
15 Jun / 14 Sep 2027; London 15 Jul / 14 Oct 2027; South West 15 Aug / 14 Nov 2027); the landlord is
responsible for starting and ending registration; the agents' exact permitted inputs have not yet
been published, with guidance promised before launch; stated "At Goodlord, we're looking at how we
can support that process."

The Letting Industry Council, position paper PDF
(`https://www.thelettingsindustrycouncil.co.uk/_files/ugd/231fc4_d1ccca614e514e509b430687b9830ac3.pdf`):
recommends UPRN as the primary identifier, states the "need for APIs, bulk uploads and adequate
lead-in periods", strongly recommends system integration through APIs so agent CRM data transfers
directly, and asks that CSV bulk upload be available at MVP stage, with a minimum six-month lead-in
per region.

The Independent Landlord, PRS Database page (`https://theindependentlandlord.com/prs-database/`),
accessed 2026-09-21: "At present, it is not yet known whether there will be a bulk uploading method
or API for letting agents to use. If not, letting agents will need to painstakingly register each
property." Landlords and letting agents must not market or advertise without a valid Landlord
Registration Number and Property Registration Number; portals and agents have duties under the
Renters' Rights Act 2025 s82(1)/s82(2); the service is in beta testing.

### 3. Incumbents already in the agent-facing position

- Goodlord + Reapit (`https://goodlord.my.site.com/contactsupport/s/article/Reapit-integration-with-Goodlord`),
  Alto + Goodlord (`https://www.altosoftware.co.uk/integrations/goodlord/`), Goodlord CRM
  integrations (`https://www.goodlord.com/platform/integrations/crm-integrations`): Goodlord already
  imports/exports landlord, property, compliance-certificate and tenancy-document data with Reapit,
  Street and Alto - i.e. agent CRMs already hold the data a pre-check would validate.
- Proplio, "PRS Database registration: letting agents documents checklist"
  (`https://www.proplio.co/blog/prs-database-registration-letting-agents-documents-checklist`),
  dated 2026-05-04 (vendor marketing, partially inaccurate): sells a £29/month flat
  unlimited-properties compliance platform with CSV import and document expiry/reminder tracking;
  claims a £40-£80 per-property "going rate" for agents registering on landlords' behalf; also
  claims the database "went live... 1 May 2026", which contradicts the SI and the September 2026
  law-firm/platform evidence, so its claims are treated as unreliable.
- Other agent-facing guidance: selflandlord.com
  (`https://selflandlord.com/guides/property-portal-landlord-registration/`) and LLCR
  (`https://www.llcr.uk/articles/prs-database-what-landlords-need-to-register.html`).

## Why it is credible

The statutory instrument is primary and checkable. Gowling WLG and Goodlord are credible secondary
sources with detailed, consistent dates and fees. The TLIC and Independent Landlord items directly
evidence the unresolved bulk/API question. The Proplio claims are vendor marketing containing at
least one demonstrable error and are used only to show that a competitor markets the position.

## What it does NOT show

- Whether the registry will actually permit agents to bulk-register or integrate via API - guidance
  is explicitly still pending, so the "no bulk route" premise is unresolved, not proven.
- Whether portals (Rightmove/Zoopla) or agent CRM vendors will build listing pre-checks themselves.
- Any evidence of agent or portal willingness to pay a third party for a pre-check.
- No prospects, pricing evidence or market size.

## Links

- Used by: `seeds/prs-listing-precheck.md` (shallow re-check), `seeds/prs-self-managing-landlord.md`
