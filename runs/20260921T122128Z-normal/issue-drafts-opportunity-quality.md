# Draft issues: opportunity quality (not yet filed)

Written 2026-09-21 by the `idea-worker` agent. The agent cannot create GitHub
issues (hard boundary: no publication). These are ready to paste into the
tracker. Status column reflects what was implemented locally in the same
session; all code changes are left uncommitted for human review.

Context: two Method 1.6 sweeps hit their 15-20 observation targets, but nearly
every triage rejection was "a credible incumbent already occupies this seam"
(garage management, dental PMS, pharmacy PMR, customs/broker re-keying, freight
booking re-keying, insurance bordereaux, EHR-to-EDC transcription, portal
listing syndication). The trawl finds real pain; it finds pain that is already
monetised. The four surviving ideas are low/medium confidence and two of the
four are regulation-derived.

## 1. Reseed query families around spend and seams, not generic pain

**Problem.** `painmine/sources.json` families ask for complaint chatter
(`"wish it integrated with"`, `"is there software that"`, `"double entry" excel
process`), which pulls feature requests and accounting-philosophy posts. The
widely-discussed pains are the served ones.

**Change.** Rewrite the three existing families around spend, workarounds and
named-system seams; add two families (`d_paid_workaround`, `e_unserved_seam`)
covering money-for-humans and vendor-refusal language.

**Acceptance.** Existing family keys remain non-empty (tests); `--family all`
merges every family; new families include at least one spend phrase and one
vendor-refusal phrase; no query references a single vendor's product name.

## 2. Add a paid-workaround cue group to deterministic extraction

**Problem.** `extract.py` looks for pain, not spend. "We pay a VA to re-key this"
and "it's a feature request" score the same.

**Change.** New `paid_workaround` cue group (strong): `we pay`, `paying
someone`, `hired a/an`, `outsourced`, `per seat/user/licence`, `minimum
contract/term`, `annual contract`, `data entry staff/agency`. Add it to
`GROUP_WEIGHTS` (2) and `STRONG_GROUPS`, and to the vendor-marketing
first-person exemption.

**Acceptance.** Signals whose only strong cue is a paid-workaround phrase are
extracted rather than rejected as `no_pain_cue`; existing extraction tests pass
or are updated with cited reasons; confidence still bounded at 0.9.

## 3. Add a non-regulatory buyer-side source class (Discourse)

**Problem.** Only three usable sources; Reddit is blocked at the edge; Stack
Exchange's literal queries mostly matched Stack Overflow. The mined population
is builders, not buyers.

**Change.** `fetch_discourse(query, cap, budget, site)` against a public
Discourse `/search.json` endpoint, site-configurable via
`sources.json` class `options.sites` (same pattern as Stack Exchange rotation),
item ids `discourse:<site>:<topic_id>:<post_id>`.

**Acceptance.** Collector is unit-tested with a mocked payload; class entry
documents access, rate limits and the owner decision on terms/robots before it
is enabled; no authentication, no scraping of non-public endpoints.

**Status note.** Collector + tests + class entry implemented; class left
**disabled** pending the owner's terms/robots check for each site.

## 4. Feed painmine observation pools into the Method run

**Problem.** painmine is input-only (issue #12) and `scripts/prompts/lab-run.md`
never mentions it. The mined clusters and the Method sweeps are two disconnected
loops.

**Change.** Prompt section telling the run to read the most recent
`observations/<run-id>.md` pool as pre-swept, cited observation inputs, to
re-triage them itself (including its own sampled false-negative audit), and to
record provenance. Observations remain inputs, never candidates.

**Acceptance.** Prompt states observations carry no score/evidence level and
cannot consume the three-candidate limit; the run still performs its own sweep
and triage; no method/ files change.

## 5. Cross-run restatements must not collapse a cluster to nothing

**Problem.** Re-running against accumulated state yields 0 clusters: restatements
are marked `duplicate_of` a prior-run signal id and therefore excluded from
clustering, while the prior members are not in the run, so nothing reaches
`min_cluster_size`.

**Change.** In `cluster.py`, treat cross-run restatements
(`duplicate_scope == "previous-run"`) as clusterable members while still
excluding them from `independent_sources`, so cumulative evidence can hold a
cluster together without inflating independence.

**Acceptance.** A run whose fresh signals plus restatements reach the minimum
cluster size produces a cluster with a lineage match; `independent_sources`
counts only genuinely independent evidence; exact/near link counts and state
semantics unchanged; deterministic tests cover the case.

## 6. Carrying prior-run evidence into clustering (follow-up, not implemented)

To let a cluster survive a run that only returns a single restatement, load the
state's stored signals for matched clusters as evidence-only inputs. Bigger
change; propose only after #5 is reviewed.
