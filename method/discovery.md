# Discovery

Method version: see `method/VERSION`. This file defines how candidates are found,
screened for novelty, deduplicated, and how adjacent opportunities are preserved.

## The discontinuity test

The lab exists to find opportunities that a search for "problems" would miss. Every
candidate must be able to complete this sentence with a specific, dated, cited change:

> **This was not an attractive business three years ago, but it might be now because
> ______ changed.**

"Because the problem exists" is not an answer. "Because AI assistants became a
mass-market buying surface in 2024-2025" is an answer when tied to evidence. The change
need not be brand new; it must be *identifiable and material*, and the candidate must
explain why it creates or widens an opening now rather than at any time in the past.

Prefer changes that are hard to reverse, create urgency or compulsion, or invalidate an
incumbent's position. Reject candidates whose only "why now" is a general trend.

### Sources of change to investigate

| Class | Examples of what to look for |
|---|---|
| Legislation / regulation | Acts with commencement dates, statutory instruments, new reporting or record-keeping duties |
| Consultations / announced rules | Open consultations, confirmed future obligations, transition periods |
| New APIs / developer surfaces | Government or industry APIs newly opened, terms changed, rate limits lifted |
| New datasets | Registers, price/usage/registry data newly published or made machine-readable |
| Platform rule / pricing / access changes | Marketplace, app-store, search or social platform policy and pricing shifts |
| Incumbent disruption | Products discontinued, withdrawn, repriced, end-of-lifed, acquired and neglected |
| New technical capability | LLM/vision/document processing making an expensive human workflow newly automatable |
| Manual structured-data flows | Industries still re-keying between email, PDFs, spreadsheets and portals |
| Poor narrow incumbents | Verticals where the only software is expensive, dated or widely disliked |
| Mandated formats / submissions | New filings, e-invoicing, schemas, portals creating integration/adaptor needs |

A run need not cover every class, but it must search across several and record which
classes it searched in the run summary. Rotating deliberately across classes is
expected; repeatedly mining one class is a reason to justify the choice.

## Why now?

Every candidate records `why_now` in `ideas/index.json` and a "Why now?" section in its
dossier:

```json
"why_now": {
  "changed": "what changed, in one sentence",
  "changed_date": "YYYY-MM-DD or YYYY-MM or 'announced'",
  "evidence": ["evidence/<slug>/<file>.md or URL"],
  "why_it_matters": "why this materially improves the opportunity now",
  "competitors_responded": "none known | named incumbents already moved | unknown"
}
```

- `changed` and `why_it_matters` must be non-empty and specific.
- `evidence` must cite at least one dated source register entry or external URL.
- A missing or unevidenced why-now does not auto-kill. For a candidate whose
  evidence level is `Plausible` or `Promising` (pre-demand), it caps `differentiation`
  and `problem_severity_frequency` at 2 (see `method/scorecard.md`) and is a strong
  reason to reject a generic or crowded candidate at screening. The cap does not apply
  once there is `Demand evidence` or better (v1.2.0): an evergreen niche with real
  payment evidence is judged on that evidence, not on a missing discontinuity.

## Novelty / incumbent sanity check

Run this before deep research, and record the answers in the dossier. It is a screening
aid, not an automatic kill: a candidate that fails a check may still proceed with a
stated reason (for example, "three providers exist but all require an accountancy
practice to self-serve configuration we can remove").

1. Does this exact product already exist?
2. Are there multiple credible providers?
3. Is the proposed wedge already a standard feature of an incumbent?
4. Is an authoritative or free alternative already adequate?
5. Has a well-capitalised company already shown the unit economics are hostile (e.g. a
   category leader losing money at scale)?
6. Is this merely a feature of an established category rather than a standalone product?

## Duplicate detection

Before creating a candidate, check against every entry in `ideas/index.json` and every
seed in `seeds/index.json`:

- normalised title/slug collision => duplicate, do not create;
- same buyer AND same problem AND (same mechanism OR >= 3 shared fingerprint keywords)
  => duplicate unless the candidate states what is materially different;
- a variant of a killed idea that does not address the recorded kill reason => reject,
  and record the reason;
- a seed may only become a candidate after fresh research from scratch, with its own
  evidence and scorecard; it never inherits the parent's score or evidence level.

## Adjacent opportunity seeds

Rejections often surface a better-adjacent proposition (e.g. "discovery is commoditised
but application quality is not"). Preserve it as a seed so a later run can investigate
without resurrecting the killed idea:

- one file per seed under `seeds/<slug>.md`, one entry in `seeds/index.json`;
- record the parent idea, the observation, the evidence for it, and what would make it
  materially different from the parent;
- seeds carry **no** score, confidence or evidence level, and cannot be promoted without
  their own dossier, evidence and scorecard.

## Recording

- The run summary lists the source classes searched and what they yielded.
- The run summary states, for each generated candidate, whether its why-now is
  evidenced (`strong` | `weak` | `absent`).
- Rejected candidates keep their why-now analysis in the decision record.
