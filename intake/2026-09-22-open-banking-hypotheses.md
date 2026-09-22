# Owner-nominated intake — five narrow open-banking workflow hypotheses

- **Recorded:** 2026-09-22
- **Source:** GitHub issue #18 (owner-nominated), plus desk research recorded below
- **Status:** unvalidated discovery leads. This is input to discovery, not a Method
  1.6 observation pool or a batch of scored ideas. Nothing here carries a score,
  confidence or evidence level, and nothing here is exempt from the source-class
  budget or the normal funnel.

## How to read this file

Each hypothesis records: the buyer/job hypothesis; the source URLs and dates
checked; the provider and regulatory position; the disconfirming incumbent
evidence found; the overlaps with existing ledger entries; and the key unknowns.
A provider's first-party claim establishes an **offering**, not uptake or
satisfaction. Adoption of open-banking infrastructure (16m+ UK users, payments
+53% in 2025) is **not** evidence of an underserved buyer.

Regulatory note applying to all five: account information services (AIS) and
payment initiation services (PIS) are regulated activities under the Payment
Services Regulations 2017, supervised by the FCA. Any product that reads bank
data or initiates payments must either be authorised or operate through an
authorised provider; a partnership does not remove the underlying obligations.
None of these hypotheses has been checked against a specific regulatory
perimeter beyond the general position below.

---

## H1 — PTA / community-group cross-channel event reconciliation (highest priority)

**Buyer/job hypothesis.** A PTA or community-group treasurer runs an event that
collects money through several channels at once — bank transfers, card payments,
cash, an auction, and a fundraising platform — and must match the proceeds to the
event, account for each channel, and report to a committee. The job is the
close-out and reconciliation, not the collection.

**Sources checked.**
- Open Banking Limited case study, "Open banking in the community: Parentkind and
  BOPP" (openbanking.org.uk, published 2022-07-20). BOPP launched 2021 and works
  with SMEs, sole traders, the education sector, charities and community groups.
  Parentkind signed an initial three-year deal with BOPP for payment services with
  an exclusive discounted service to members. The case study states: "There's a
  handy dashboard which allows the PTA to see all the payments it's received,
  which means it's easy to reconcile events, and see who paid how much and for
  what event." PTAs collected several thousand payments; some several hundred BOPP
  payments a year; one PTA over GBP 4,000; PTAs average 20 BOPP payments/month at
  an average transaction of GBP 7.48.
- BOPP pricing (bopp.io): "Minimum 5p, maximum 50p per transaction." BOPP partners
  page lists MyT (small businesses), Parentkind (PTAs) and Charity Digital
  (charities replacing cash donations, GiftAid capture).
- Parentkind blog (2026-06-03): HMRC closed its free CT600 online filing service on
  31 March 2026, so PTAs (especially Gift Aid-registered ones) receiving an HMRC
  notice must file Corporation Tax returns using compatible commercial software;
  paper only with a "reasonable excuse"; penalties may apply even for nil returns.
  Parentkind says this "introduces additional cost and complexity".
- ParentSquare (US, 2026-08-04) launched centralised reporting for district-wide
  payment visibility — evidence that cross-school payment reconciliation is a
  recognised product category.

**Provider/regulatory position.** BOPP is an authorised provider offering payment
links, QR codes and a reconciliation dashboard to PTAs via Parentkind. A new
entrant would either need its own authorisation or to build on an authorised
provider's rails. The Parentkind/BOPP arrangement is exclusive and discounted to
Parentkind members, which is a distribution advantage an outsider does not have.

**Disconfirming incumbent evidence.** The exact "reconcile events, see who paid
how much and for what event" job is already described as solved by BOPP's
dashboard in the Parentkind case study. Parentkind is the umbrella body for PTAs
in England and Wales and bundles the service to its members. ParentSquare shows
the category is recognised and being productised elsewhere.

**Overlaps.** Aucly (flat-fee auction platform for UK schools/PTAs/charities,
adversarially-researched, 60.0, why_now strength absent) is the closest ledger
entry; issue #17's school-software sweep is the closest recent pool. Aucly could
be one input to a cross-channel close-out product, not the whole product.

**Key unknowns.** Whether any cross-channel close-out exception remains unsolved
once BOPP's dashboard is in place (e.g. cash, auction proceeds, a second
fundraising platform, or committee reporting); whether the treasurer is the payer
or the committee/PTA is; whether a PTA would pay a third party when Parentkind
bundles a discounted service; and whether the CT600 filing change creates a
separate, better-evidenced job.

**Cheapest falsifying test (not run).** Ask a small number of PTA treasurers to
describe their last event close-out and show the artefacts they produced; a
proceed signal would be a treasurer describing a reconciliation step that BOPP's
dashboard does not cover and that they currently do by hand.

---

## H2 — Invoice-to-bank exception reconciliation for one SME vertical

**Buyer/job hypothesis.** An SME in a specific vertical receives repeated deposits
that do not match invoices one-to-one — partial payments, split invoices,
ambiguous references, lump sums from a payment provider covering many orders, or
over/underpayments — and must resolve the exceptions by hand before the ledger is
correct.

**Sources checked.**
- QuickBooks Community threads (2026-02-23, 2026-03-06, 2020-11-18) document
  practitioner pain: bulk deposits that cannot be matched to invoices marked as
  paid; lump-sum deposits from payment providers covering many orders;
  over/underpayments and credit memos that cannot be matched to a single net
  deposit (e.g. Store 1 +USD 100, Store 2 +USD 100, Store 3 -USD 100 = USD 100
  deposit); workarounds involving expense transactions, journal entries and manual
  clearing.
- SAP Ariba documentation defines a taxonomy of invoice exception types (unmatched
  invoice, PO variance, partial invoicing, receiving, tax, payment terms) with
  manual exception-handling workflows and escalation to supervisors.
- Sage Intacct supports partial matching of bank transactions (state "Partially
  matched", remaining-to-match field).
- Ledge (ledge.co/solutions/automated-reconciliation/invoices) already sells this:
  "connects directly to your banks, ERP, and payment systems, and matching
  payments, whether partial, batched, or inconsistently referenced, to the correct
  open invoices. Ledge resolves common exceptions like missing remittance data or
  overpayments using embedded logic and AI, reducing manual intervention."

**Provider/regulatory position.** Bank feeds are a standard feature of Xero,
QuickBooks and Sage; open banking is the feed mechanism, not the product. A
reconciliation product reads bank data (AIS) and may initiate payments (PIS), so
the same authorisation question applies.

**Disconfirming incumbent evidence.** Ledge already markets exactly the described
job — partial, batched and inconsistently referenced payments matched to open
invoices, with exception resolution. Sage Intacct and SAP Ariba ship partial
matching and exception workflows. Xero and QuickBooks ship bank feeds and rules.

**Overlaps.** None in the ledger directly; the closest prior work is the
reconciliation-tooling observation O19 in observations/20260922T060326Z-normal.md
(rejected: Xero/QuickBooks bank rules, Dext, AutoEntry, Hubdoc, NetSuite and the
AI reconciliation field occupy it).

**Key unknowns.** Which single named vertical has an exception pattern the
incumbents demonstrably fail to resolve; whether the buyer is the SME's
bookkeeper or an outsourced accountant; and whether the exception volume is large
enough to justify a standalone product rather than a feature of the accounting
system the SME already owns.

**Cheapest falsifying test (not run).** Pick one vertical and read its
practitioner forums for repeated, dated complaints about a specific exception
type that Ledge/Sage/Xero do not resolve; a proceed signal would be a named
vertical with recurring complaints and a visible workaround.

---

## H3 — Data-minimal evidence collection for a narrow financial-support scheme

**Buyer/job hypothesis.** A grant, bursary or financial-support provider must
review applicants' bank statements to assess eligibility or affordability, and
the review is costly, slow and intrusive; a consent-based, caseworker-friendly
evidence product could replace the manual statement review.

**Sources checked.**
- Thirdfort (help.thirdfort.com, updated 2026-07-14) uses Open Banking to obtain
  3, 6 or 12 months of read-only bank statements for verification, authorised on
  both the FCA and Open Banking Registers — an existing consented-data evidence
  product.
- Open Banking Limited written evidence to the Financial Inclusion Strategy
  committee (Dec 2025): open banking is a consent-based framework for sharing
  current account data and initiating payments; providers design services for
  people with variable incomes and thin credit files; for SMEs improved visibility
  leads to better access to SME lending.
- OBIE written evidence (CAF0055): Nationwide provided GBP 3m funding for "Open
  Banking for Good", pairing fintechs with debt and money charities; open banking
  enables debt advice charities to automate affordability assessments.
- HM Treasury "Access to Banking Services Review: Call for Evidence" ran 8 June to
  20 July 2026.
- DWP has started Pension Credit case reviews asking selected claimants for recent
  bank statements (Daily Record, 2026-08-24) — evidence that bank-statement
  evidence collection is a live, growing administrative burden.

**Provider/regulatory position.** Reading applicant bank data is AIS. The
safeguarding, consent-pressure, accessibility, vulnerable-applicant and fairness
questions are material and would need specialist review; no live applicant bank
data may be used during desk screening.

**Disconfirming incumbent evidence.** Blackbullion already supports student
funding with open banking; PayPoint/AperiData already supports Citizens Advice
debt assessments; Thirdfort already sells consented statement retrieval for
verification. The "Open Banking for Good" programme already paired fintechs with
debt and money charities.

**Overlaps.** None in the ledger. The vulnerable-buyer and consent questions make
this the highest-risk hypothesis of the five.

**Key unknowns.** Which single scheme has a costly bank-statement review that is
not already served; whether the provider would pay for a third-party evidence
product rather than use its existing process; and whether the fairness and
consent risks can be managed acceptably.

**Cheapest falsifying test (not run).** Identify one scheme and read its published
assessment guidance and any practitioner discussion of the review burden; a
proceed signal would be a named scheme with a documented, costly manual statement
review and no existing consented-data product.

---

## H4 — Flexible collection / arrears workflow for one niche biller (watchlist)

**Buyer/job hypothesis.** A biller in a niche with variable or seasonal amounts
(e.g. energy, insurance, utilities, telecoms) loses money to Direct Debit
failures and involuntary churn, and a constrained variable recurring payment
could recover some of it.

**Sources checked.**
- GoCardless Recurring Pay by Bank (gocardless.com/payments/recurring-pay-by-bank,
  published 2026-08-25): same-day settlement, no chargebacks, "100% UK bank
  coverage", intelligent routing between Pay by Bank and Direct Debit, balance
  checks that catch insufficient funds before collection, automatic retries at no
  extra cost; sector maximums: financial services GBP 450, insurance GBP 85,
  energy/utilities GBP 200, telecommunications GBP 120.
- GoCardless blog (2026-06-02): the UK Payments Initiative (UKPI) scheme went
  live, paving the way for Recurring Pay by Bank; cards comprise 84% of UK retail
  spending by turnover and cost businesses GBP 1.5bn in fees through the
  Visa/Mastercard duopoly; GoCardless research: 89% of recurring-revenue
  businesses believe the technology would significantly improve cash flow, 91%
  expect reduced operational costs, 49% intend to be early adopters, 38% of
  consumers open to trying recurring Pay by Bank rising to 60% of Gen Z; first
  recurring open banking transaction completed March 2026 for Jellyfish Energy;
  GoCardless has 100,000+ businesses.
- GoCardless Direct Debit failure data (guides/posts/why-payments-fail): average
  UK Direct Debit failure rate ~2.9% across 55,000 customers and 52m transactions;
  insufficient funds is >80% of failures (2.38% of the 2.9%); mandate cancelled
  ~15%; payments over USD 250 fail 4.1-5% vs 2.6-3% for USD 0-250; ~30% of churn
  is involuntary; retry success rate over 75%.
- Fintech Times (2026-04-11) and Open Banking Expo (2026-04-02): GoCardless
  research "Revolutionising Recurring Revenue" surveyed 489 UK recurring-revenue
  business leaders; legacy payment rails cost merchants an average 3.5% of total
  monthly revenue; 9 in 10 see commercial VRPs as the way forward.

**Provider/regulatory position.** Initiating payments is PIS; commercial VRP is a
developing scheme with per-sector maximums and evolving coverage. GoCardless
already offers recurring Pay by Bank with routing and retries.

**Disconfirming incumbent evidence.** GoCardless already sells the described
capability at scale (100,000+ businesses) with intelligent routing, balance checks
and automatic retries. The Direct Debit failure data is GoCardless's own, and it
is the incumbent's marketing case for its own product.

**Overlaps.** None in the ledger.

**Key unknowns.** Whether any niche biller has a Direct Debit failure/support cost
that GoCardless's existing product does not already address; whether scheme
coverage and economics make a standalone product viable; and whether the buyer
would switch from an incumbent already integrated into their billing stack.

**Cheapest falsifying test (not run).** For one named biller niche, establish the
actual Direct Debit failure and support cost and whether GoCardless's existing
product already covers it; a proceed signal would be a documented cost the
incumbent product does not address.

---

## H5 — Case-specific bank-data evidence pack for a specialist SME lender or mortgage broker (lower priority)

**Buyer/job hypothesis.** A specialist lender or mortgage broker needs
borrower-specific bank-data evidence that existing consented-data products still
leave as a manual gap.

**Sources checked.** The FCA open-finance roadmap
(https://www.fca.org.uk/publications/corporate-documents/open-finance-roadmap)
prioritises SME lending and mortgages as future use cases. No further research was
done this session; the roadmap is a statement of intent, not proof of a gap.

**Provider/regulatory position.** Reading borrower bank data is AIS; regulated
advice boundaries apply to brokers. Not yet assessed in detail.

**Disconfirming incumbent evidence.** Not yet gathered. The roadmap itself shows
the FCA expects existing and new providers to serve these use cases.

**Overlaps.** None in the ledger.

**Key unknowns.** Whether any borrower segment has a manual evidence gap that
existing consented-data products do not cover; whether the buyer is the lender,
the broker or the borrower; and whether the regulated-advice boundary constrains
the product.

**Cheapest falsifying test (not run).** Read one specialist lender's or broker's
published evidence requirements and check whether an existing consented-data
product already satisfies them; a proceed signal would be a named requirement no
existing product covers.

---

## Prior art and deduplication

- **Aucly** (flat-fee auction platform for UK schools/PTAs/charities) is the
  closest ledger entry to H1. H1 is materially different only if it addresses
  cross-channel close-out across several collection channels rather than auctions
  alone; that difference is not yet evidenced.
- **Issue #17** (school software) is the closest recent sweep; H1 must not
  duplicate its broader school-software observations.
- **O19** in observations/20260922T060326Z-normal.md (reconciliation tooling
  quality gap) was rejected because Xero/QuickBooks bank rules, Dext, AutoEntry,
  Hubdoc, NetSuite and the AI reconciliation field occupy it. H2 must show a
  specific exception pattern those do not resolve.
- No existing seed or idea covers H3, H4 or H5.

## What a later run should check first

1. H1: whether a PTA treasurer's last event close-out contains a step BOPP's
   dashboard does not cover.
2. H2: whether one named vertical has recurring, dated complaints about a specific
   exception type that Ledge/Sage/Xero do not resolve.
3. H3: whether one named scheme has a documented, costly manual statement review
   with no existing consented-data product.
4. H4: whether one named biller niche has a Direct Debit failure/support cost that
   GoCardless's existing product does not address.
5. H5: whether one specialist lender's or broker's evidence requirement is not
   covered by an existing consented-data product.

## Boundaries

No bank data was accessed, no consent flow was run, no prospect was contacted, no
pilot was started, no money was spent and no public claim was made. Any external
conversation, access to financial information, consent flow, pilot or expenditure
requires the human owner's approval under method/experiment-rules.md.
