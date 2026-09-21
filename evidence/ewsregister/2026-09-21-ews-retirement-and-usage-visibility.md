# Evidence: Exchange Web Services retirement and remaining EOL/migration deadlines

- **Idea / scope:** `ewsregister`
- **Register:** evidence
- **Source:** ITECS and other sources listed per claim below (URLs recorded)
- **Accessed / dated:** 2026-09-21
- **Credibility:** credible secondary for the EWS plan; vendor/consultancy secondary for the rest

## Claim(s) supported

- Microsoft is disabling Exchange Web Services (EWS) in Exchange Online from 1 October 2026 and
  shutting it down permanently on 1 April 2027.
- EWS dependencies are commonly hidden in backup jobs, archive connectors, public-folder workflows,
  scheduling apps and scripts, and Microsoft's own usage reporting is time-windowed and aggregated.
- Microsoft provides tenant controls that can enable/disable EWS and restrict allowed apps.
- Several unrelated 2026 end-of-life and forced-migration deadlines fall in the same window.

## Exact detail

### 1. EWS retirement timeline and visibility gap (credible secondary)

ITECS, "EWS retirement: SMB Microsoft 365 migration plan"
(`https://itecsonline.com/post/ews-retirement-smb-microsoft-365-migration-plan`), dated 2026-08-20.
Reported: Microsoft begins phased, tenant-by-tenant disablement of EWS in Exchange Online on
1 October 2026, with permanent shutdown on 1 April 2027. EWS usage is described as commonly buried in
backup jobs, archive connectors, public-folder workflows, older scheduling applications and scripts.
Microsoft's EWS usage report is said to cover only 7/30/90-day windows and to aggregate weekly, so
infrequent or seasonal applications can be missed. Tenant controls named: `EWSEnabled` and
`EWSAllowedAppIDs`. Open Graph parity gaps are said to include public-folder import/export and
in-place archive scenarios. The article recommends maintaining an "EWS migration register" with
business and technical owners, vendor product-version evidence, expiring exceptions and restore
validation.

### 2. Concurrent 2026 EOL / forced-migration deadlines (context)

- ITECS (2026-08-20, above) reports Microsoft's EWS disablement/shutdown dates.
- TheSMBHub, "Google retires DSA for AI Max"
  (`https://www.thesmbhub.com/news/google-retires-dsa-ai-max-migration-2026/`), dated 2026-04-15:
  Google announced on 15 April 2026 that Dynamic Search Ads are retired in favour of AI Max for
  Search; upgrade tools late April 2026; voluntary migration May-August 2026; remaining legacy
  search campaigns auto-upgraded September 2026; AI Max performance is said to depend on clean
  conversion tracking (including offline/enhanced conversions that require CRM integration) and
  first-party audience feeds.
- Rand Group, "Sage BusinessVision end of life"
  (`https://www.randgroup.com/insights/sage/sage-businessvision-end-of-life-what-users-need-to-know/`),
  dated 2026-09-15: Sage BusinessVision reaches end of life on 31 December 2026 (no updates, patches,
  payroll or support; final payroll update July 2026; final T4/T5018 year-end update).
- ERP Software Blog, "Dynamics GP end of life"
  (`https://erpsoftwareblog.com/2026/07/dynamics-gp-end-of-life-business-central-migration-deadline/`),
  dated 2026-07-24: Dynamics GP new subscription sales ended 1 April 2026; mainstream enhancement,
  tax and support end 31 December 2029; security patching ends 30 April 2031.
- Beancount, "QuickBooks Desktop 2023 support ended"
  (`https://beancount.io/blog/2026/08/16/quickbooks-desktop-2023-support-ended-migration-checklist`),
  dated 2026-08-16: QuickBooks Desktop 2023 support ended 31 May 2026 - payroll tax tables frozen,
  bank feeds off, e-file/e-pay/direct deposit off, security patches ended.
- DotSquares, "Navigating end-of-life SKUs and legacy systems 2026"
  (`https://www.dotsquares.com/press-and-events/tech/navigating-end-of-life-skus-and-legacy-systems-2026`),
  dated 2026-09-19: a 2026 EOL wave including MySQL 8.0, Node.js 20, Exchange Server 2016/2019,
  SQL Server 2016, SharePoint Server 2016/2019, Project Online (service stops 30 September 2026),
  Office LTSC 2021 and the final Windows Server 2012 ESU window; endoflife.date is cited as tracking
  459 products.

## Why it is credible

The EWS timeline is reported by an IT consultancy that works on Microsoft 365 migrations, quoting
Microsoft's own published plan and tenant controls; the specific control names and dates are
checkable by any tenant admin. The remaining EOL items are vendor/consultancy blogs and are used
only as context for the breadth of forced migrations in the same period.

## What it does NOT show

- No evidence that SMBs or MSPs would pay a third party for EWS dependency *discovery*, as opposed
  to buying a migration project or using Microsoft's free usage report and controls.
- No pricing, procurement, buyer interviews or count of affected organisations.
- The claim that Microsoft's usage report misses infrequent applications is a consultancy assertion
  about report windows, not a measured failure rate.
- The 2026 EOL wave is a list of unrelated deadlines, not a single opportunity; it does not show
  that any of them lacks an adequate incumbent response.

## Links

- Used by: `ideas/ewsregister/scorecard.json#problem_severity_frequency`,
  `#buyer_budget_clarity`, `#evidence_strength`, `#differentiation`, `#economics`,
  `#defensible_wedge`, `#cheap_disconfirming_test`
