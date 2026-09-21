# Run summary: 20260921T065316Z-normal

- **Mode:** normal
- **Started / finished:** 2026-09-21T06:53:16Z / 2026-09-21T07:03:20Z
- **Agent / model:** idea-worker / opencode-go/deepseek-v4.1-flash
- **Method version:** 1.1.0
- **Input / output revision:** `f5a856db79393da10106dea6d193bc35c3605fe2` / `uncommitted`
- **Status:** success

## Source classes searched

| Source class | Searched? | What it yielded |
|---|---|---|
| Legislation / regulation | yes | EUDR, Belgium B2B e-invoicing, Companies House IDV (ECCTA 2023), EU AI Act Art 50, PPWR, Employment Rights Act 2025, MTD for Income Tax |
| Consultations / announced rules | yes | EU AI Act Code of Practice (10 Jun 2026) and Art 50 guidelines; PPWR delegated/implementing acts delayed to Q4 2026; HMRC MTD sign-up from Sep 2026 |
| New APIs / developer surfaces | yes (partial) | ACP/UCP agentic-commerce endpoints, WooCommerce MCP/Abilities API; not exhaustively mapped |
| New datasets | no | No qualifying new public dataset surfaced in the searches run; recorded as a gap |
| Platform rule / pricing / access changes | yes | Shopify Agentic Storefronts (free beyond standard processing), Stripe Agentic Commerce Suite, PayPal/ACP adoption; platform bundling is the key finding |
| Incumbent disruption | no | Not deliberately searched this run; recorded as a gap |
| New technical capability | yes | Agentic checkout/product feeds; C2PA/marking tooling; LLM-assisted compliance drafting |
| Manual structured-data flows | no | Not searched this run; recorded as a gap |
| Poor narrow incumbents | no | Not searched this run; recorded as a gap |
| Mandated formats / submissions | yes | Peppol BIS (Belgium), EUDR DDS via TRACES, PPWR DoC/labelling, MTD quarterly submissions |

## Why-now quality

| Candidate | Why now (one line) | Strength | Competitors responded |
|---|---|---|---|
| `agentready` | ACP (Sep 2025) and UCP (Jan 2026) opened agent-mediated checkout, and platforms began bundling it | strong | Yes — Shopify, Stripe, Google, WooCommerce, BigCommerce, Salesforce all shipping; bundled free |
| `packproof` | PPWR generally applies from 12 Aug 2026, adding labelling, DoC and PFAS duties for packaging placed on the EU market | strong | Yes — PPWR Copilot, PPWRify, PPWR Connect, Trace One already selling |
| `reasonable-steps` | Employment Rights Act 2025 ss.20-21 commence 30 Oct 2026: "all reasonable steps" plus a third-party harassment duty | strong | Partial — free Acas/EHRC guidance and paid Acas training; no dedicated low-cost SME tool evidenced |

## What advanced

| Idea | From | To | Why |
|---|---|---|---|
| `reasonable-steps` | `discovered` | `adversarially-researched` | Strong dated discontinuity and no hard-filter fail; parked at the pre-validation-ready state because the score is below threshold and the wedge/budget are still unknown |

No idea was advanced to `validation-ready` this run (0 of the 1 permitted advance).

## What was killed

| Idea | Reason | Preserved in |
|---|---|---|
| `agentready` | Hard-filter `defensible_wedge` = fail: the change is real but platforms bundle agentic checkout free, so a readiness wedge is commodity positioning | `ideas/agentready/` plus seed `agent-checkout-offplatform` |
| `packproof` | Hard-filter `defensible_wedge` = fail: multiple credible PPWR providers, including a cheap UK tier; feature of an established compliance-software category | `ideas/packproof/` plus seed `uk-epr-small-producer-tooling` |

These are kills #4 and #5 overall, which triggers the every-fifth-kill false-negative audit
(review policy trigger 6). The oldest un-audited kill (`shiftswap`) was self-audited by the
worker and an external audit request was raised.

## What failed or was skipped

- Several promising discontinuities were screened out before deep research because the
  novelty/incumbent check failed: Belgium B2B e-invoicing (crowded by access points and
  accounting platforms), Companies House ACSP verification (purpose-built cheap tools
  already exist), MTD for Income Tax (Sage/Xero/FreeAgent/Taxd/bridging), EU AI Act
  Article 50 (C2PA/watermarking vendors bundling), EUDR (repeated delays plus enterprise
  compliance vendors), and UK EPR (absorbed by compliance schemes).
- Untested source classes (incumbent disruption, poor narrow incumbents, manual
  structured-data flows, new datasets) were skipped to stay within the run budget; they
  remain the largest discovery gap.
- No experiment was run; both proposed experiments remain unapproved.

## Limits encountered

- Candidates generated: 3 / 3
- Unreviewed after run: 0 / 10
- Advances to validation-ready: 0 / 1
- Web lookups: 14 / 25
- Cost: not separately metered by the worker; no paid spend occurred. Steps and lookups
  stayed within the run bounds ($1.00 budget not knowingly approached).
- `method/calibration.md` still shows the v1.1.0 calibration as pending human/reviewer
  sign-off; it was not edited (routine run).

## Decisions needing human input

| Decision | Options | Deadline / trigger | Where recorded |
|---|---|---|---|
| Approve or decline the false-negative audit request and confirm the shiftswap kill | Confirm kill / reopen / commission audit | Before trust in kill practice is assumed | `reviews/2026-09-21-false-negative-audit-request.md` |
| Approve or decline `reasonable-steps-willingness` (and assess review trigger 4 legal/regulatory risk before any external testing) | Approve / amend / decline | Before any contact or spend | `experiments/reasonable-steps-willingness/plan.md` |
| Approve or decline the still-proposed `geonerd-demand-spike` | Approve / amend / decline | Before any contact or spend | `experiments/geonerd-demand-spike/plan.md` |
| Respond to the GeoNerd v2 review request | Approve / changes-requested / kill | Open since 2026-09-21 | `reviews/2026-09-21-geonerd-review-request-v2.md` |
| Respond to the method v1.1.0 review request | Approve / changes-requested | Open since 2026-09-21 | `reviews/2026-09-21-method-v1.1.0-review-request.md` |
| Update `method/calibration.md` status table | Human edit | Whenever convenient | `method/calibration.md` |

## Review queue after this run

| Idea | Review status | Request | Outstanding since |
|---|---|---|---|
| `geonerd` | requested | `reviews/2026-09-21-geonerd-review-request-v2.md` | 2026-09-21 |
| `shiftswap` | requested | `reviews/2026-09-21-false-negative-audit-request.md` | 2026-09-21 |
| (method) | requested | `reviews/2026-09-21-method-v1.1.0-review-request.md` | 2026-09-21 |
| `reasonable-steps` | not-required | — | — |

## Next run should

1. Work the untested source classes — incumbent disruption (product sunsets), poor narrow
   incumbents, and manual structured-data flows — since the regulation and platform
   classes are now well covered and mostly crowded.
2. Check whether any human response has arrived on the review queue; a `changes-requested`
   outcome must be answered explicitly and may change the GeoNerd or shiftswap records.
3. If the human approves either experiment, record approval and (only then) begin it; if
   not, look for a buyer-specific wedge inside an existing mandate rather than another
   broad compliance tool.

## Disallowed actions

No commits, pushes, issues, pull requests or other publication were made; nobody was
contacted; no money was spent; no external accounts were created; no commitments were
made; `method/` was not edited. Only proposed experiments were recorded.
