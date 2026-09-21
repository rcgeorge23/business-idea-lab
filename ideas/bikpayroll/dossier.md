# Dossier — `bikpayroll`

- **ID / slug:** `bikpayroll`
- **State:** `killed`
- **Evidence level:** Plausible
- **Owner:** human (not yet assigned)
- **Created:** 2026-09-21
- **Updated:** 2026-09-21
- **Source:** fresh (run `20260921T081223Z-normal`, method 1.3.0); killed by `bikpayroll-incumbent-capability` scan, 2026-09-21

## One-sentence proposition

A data bridge that collects, validates and reconciles third-party benefit-in-kind data (fleet/leasing, medical insurers, fuel cards) into SMEs' and payroll bureaus' pay cycles, so the April 2027 mandatory-payrolling mandate is met without manual re-keying.

## Why now?

- **What changed:** HMRC confirmed that from **6 April 2027** the most common benefits in kind (company cars, car/van fuel, employer-provided medical benefits) must be reported and taxed through payroll **in real time** rather than via the annual P11D, with the remaining benefits following on 6 April 2028. `The Income Tax (Pay As You Earn) (Amendment) Regulations 2026` (SI 2026/189, made 2026-09-14) removes the voluntary-registration route from 2027-28.
- **When:** policy paper 2026-07-13 (updated 2026-07-23); SI 2026-09-14; interim guidance 2025-11-26; first operative date 2027-04-06.
- **Evidence:** `evidence/bikpayroll/2026-09-21-mandatory-bik-payrolling.md`.
- **Why it materially improves the opportunity:** the mandate moves a recurring, data-dependent reporting obligation onto a large population of employers/payroll bureaus on a fixed date, and standardises the RTI fields (126 → 32, 18 to be built by developers).
- **Competitors responded:** **yes (post-scan, 2026-09-21)** — benefits platforms already absorb the seam (Zhoosh Benefits, The Electric Car Scheme, Zest, Zellis/Benefex) and IRIS sells a managed BiK payrolling service; payroll software itself still requires manual cash-equivalent entry (Sage, BrightPay). See `evidence/bikpayroll/2026-09-21-incumbent-capability-scan.md`.
- **Strength:** strong (dated primary legislation + imminent operative date).

Why-now sentence: *This was not an attractive business three years ago, but it might be now because HMRC mandated real-time payrolling of the most common benefits in kind from 6 April 2027, forcing third-party benefit data into every pay cycle.*

## Buyer

- **Primary hypothesis:** payroll bureaus and accountants serving SME clients that provide company cars/medical benefits, and SME employers (roughly 10–250 staff) with no benefits-administration platform.
- **Budget owner:** finance director / payroll manager (SME) or bureau principal. **Not evidenced** — the economic buyer is identifiable but no budget line or comparable spend has been observed.
- **Population signal:** HMRC states 3.5 million people will have BiK tax collected in real time; the affected employer population is large but uncounted here.

## Problem

From April 2027 an employer must have correct per-pay-period values for cars, fuel, vans and medical benefits and must report them through RTI. Those values originate outside payroll (fleet/leasing company, insurer, fuel-card provider) and today are typically reconciled annually at P11D time. The second-order operational seam is **getting provider data into the pay run each period and reconciling it** (mid-year car changes, insurer renewals, joining/leaving employees), not the tax calculation itself, which the payroll product will do.

## Mechanism / wedge

Assumed mechanism: an integration/ingestion layer (CSV/API) that normalises benefit-provider exports into each payroll product's incoming-BiK format, with validation and an exception queue; sold to bureaus (multi-employer) or directly to SMEs. Adjacent value: employee communications and forecasting the per-period Class 1A NIC cash-flow.

**Wedge status: fail (post-scan).** The `bikpayroll-incumbent-capability` scan (2026-09-21) found that named benefits platforms already ingest provider benefit data and emit per-period taxable payroll reports — Zhoosh Benefits for the medical-benefit seam (page dated 2026-08-04; "Payroll receives an employee-by-employee report that includes taxable values... without waiting for insurer invoices"), The Electric Car Scheme (API/SFTP monthly payroll inputs) and Zest (provider-to-payroll integrations), with Zellis/Benefex and IRIS's managed service as further named cases. Under the precommitted rule (≥2 platforms already ingest provider BiK data) `defensible_wedge = fail` and the idea is killed. The parties who own the data also retain the incentive to supply it, and payroll vendors already accept per-period BiK values.

## Novelty / incumbent sanity check

| Check | Result |
|---|---|
| Does an exact product already exist? | **Yes (post-scan).** Zhoosh Benefits markets the exact medical-benefit data → per-period taxable payroll report flow (2026-08-04); The Electric Car Scheme and Zest bridge provider data into payroll. |
| Are there multiple credible providers? | **Yes (post-scan).** Zhoosh, Zest, The Electric Car Scheme, plus Zellis/Benefex and IRIS's managed service; car-benefit calculation is commoditised via Comcar/DriveSmart APIs. |
| Is the wedge already a standard feature? | Contested → effectively yes: payroll products accept per-period BiK values, and benefits platforms now supply/calculate them. |
| Is a free/authoritative alternative adequate? | Partly — Bupa, Vitality and AXA already do true monthly reconciliation and Bupa/Vitality expose downloadable monthly bills; platform pricing not evidenced. |
| Is a well-capitalised company hostile to the unit economics? | Yes — payroll vendors and benefits platforms adjacent; benefits platforms (e.g. Benefex/Zellis-class) already own the data flow for larger employers. |
| Is it merely a feature of an established category? | Yes (post-scan) — the bridge is a feature of benefits-administration software or a managed payroll service, not a standalone wedge. |

**If any check fails, state the reason to continue anyway:** the checks now fail and the precommitted rule fired, so there is no reason to continue. The mandate remains real; the seam is already served.

## Distribution

Hypothesis: payroll-bureau associations, accountancy networks, payroll-software marketplaces, and content in accountant/payroll communities (CIPP, AccountingWEB). **No prospects tested; channel plausible but unproven** — `distribution` capped at 2.

## Economics (assumptions labelled)

- **Assumption:** price per employee per month (a few £) or per-employer flat fee (~£30–60/month for a 30-person employer).
- **Assumption:** gross margin software-like if ingestion is automated; **services-like and thin** if provider chasing is manual.
- **Assumption:** no material COGS beyond hosting/support.
- Modelled economics rest on untested inputs → `economics` capped at 2, low confidence.

## Founder fit

Unknown / null (no evidence recorded).

## Adversarial case

Recorded from the adversarial pass (`idea-critic`, 2026-09-21), which recommended **kill** and, on a strict evidence reading, permitted parking only if the wedge stays `unknown` and the candidate does not advance:

1. **The seam is a decade old.** Voluntary payrolling has existed since 2016; any employer who chose it already had to get per-period BiK values into RTI. Ten years with no dedicated third-party ingestion product is a market verdict, not an opportunity.
2. **The data owners can self-supply.** Fleet/leasing, insurers and fuel-card providers already hold the data and already give clients P11D-ready schedules; monthly/real-time is a frequency change on data they own, with retention/cross-sell upside. A bridge is disintermediated by the provider.
3. **Workflow owners are building toward it.** Payroll vendors are building the 18 new RTI fields; accepting a per-period import is the natural next step.
4. **Buyer budget is inferred from advisory content**, which is not demand. A £30–60/month item is hard for a bureau to justify as a new line.
5. **Distribution unknown** — the same unproven bureau/accountant channel recorded `unknown` on prior ideas.
6. **Service burden / margins risk** — provider chasing is status-chasing manual work.
7. **Window is closing, not opening** — incumbents have had ~10 months since draft legislation.
8. **Precedent cluster** — `vetcma`, `prsregister`, `propident`, `packproof`, `agentready` all died on `defensible_wedge`/category capture; `discovery.md` treats a recurring cluster as a signal.
9. **Gating dimensions weak:** problem and buyer budget both cap at 2 on current evidence; aggregate ~50.5, below the 65 threshold.

**Post-scan addendum (2026-09-21).** The `bikpayroll-incumbent-capability` scan confirmed the critic's case: the exact seam is productised (Zhoosh, 2026-08-04), two further platforms already bridge provider data into payroll, and three medical insurers already do true monthly reconciliation. The precommitted rule fired KILL and the idea is killed. The critic's inference that this is "a reporting-frequency change on data the provider already owns" is now evidenced.

## Strongest supporting case

A dated, primary-evidenced mandate with a hard operative date puts third-party benefit data into every pay period for a large population, on standardised fields, at a moment when many SMEs and bureaus have no benefits-administration layer. If (and only if) the capability scan shows neither providers nor payroll platforms supply/absorb the data, the ingestion-plus-reconciliation layer could be a durable, recurring, software-margin product with a clear pre-mandate sales window.

**Outcome (2026-09-21):** the scan tested exactly that condition and it failed — the bridge is already supplied by benefits platforms (and partly by insurers and a managed payroll service), so the conditional case for the idea does not open.

## Unresolved assumptions

| Assumption | Why it matters | How to resolve |
|---|---|---|
| Providers do not already supply machine-readable per-period benefit data free | Kills the wedge if false | **Resolved (partly false):** Bupa/Vitality/AXA true monthly reconciliation with downloadable monthly bills (broker evidence, format unspecified) |
| Payroll/benefits platforms do not already ingest provider BiK data | Kills the wedge if false | **Resolved (false):** Zhoosh, The Electric Car Scheme, Zest (plus Zellis/Benefex, IRIS managed service) |
| Bureaus/SMEs will pay for ingestion rather than absorb it manually | Missing gating dimension | Moot — no escalation experiment is proposed because the rule fired KILL |
| Provider chasing can be automated enough to protect margin | Economics | Not tested; moot after kill |
| Handler of payroll/medical-benefit data is acceptable risk | Trust/privacy | Not tested; moot after kill |

## Cheapest decisive experiment

`bikpayroll-incumbent-capability` — a desk-only capability scan with pre-fixed kill thresholds (see `experiments/bikpayroll-incumbent-capability/plan.md`). Cost bound £0, ≤6 human-hours, ≤3 calendar days. It directly falsifies the "unserved seam" claim; no external contact, spend or account is involved.

## Decision log (append-only)

| Date | Run | Decision | State | Note |
|---|---|---|---|---|
| 2026-09-21 | `20260921T081223Z-normal` | hold (park) | discovered → desk-screened | `defensible_wedge` unknown; adversarial pass recommended kill but the wedge cannot be failed on cited evidence. Not advanced toward validation-ready. Experiment proposed. |
| 2026-09-21 | `bikpayroll-incumbent-capability` (issue #5) | kill | desk-screened → killed | Precommitted scan rule fired: ≥2 payroll/benefits platforms already ingest provider BiK data (Zhoosh 2026-08-04, Zest; plus The Electric Car Scheme, Zellis/Benefex, IRIS managed service). `defensible_wedge = fail`; no escalation experiment (KILL branch excludes it). Kill #10 triggers the false-negative audit obligation. |
