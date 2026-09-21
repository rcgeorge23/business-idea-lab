#!/usr/bin/env python3
"""Validate the business-idea-lab ledger.

Stdlib only. Exit code 0 when the repository is valid, 1 when there are errors.

Usage:
    python3 scripts/validate_repo.py [--root DIR] [--json] [--queue] [--quiet]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCHEMA_VERSION = 1
WEIGHTS_VERSION = "1.0.0"

DIMENSIONS = {
    "problem_severity_frequency": 15,
    "buyer_budget_clarity": 15,
    "evidence_strength": 15,
    "distribution": 10,
    "differentiation": 10,
    "validation_speed_cost": 10,
    "feasibility": 5,
    "economics": 10,
    "founder_fit": 5,
    "risk": 5,
}
GATING_DIMENSIONS = {"problem_severity_frequency", "buyer_budget_clarity", "evidence_strength"}
MIN_SCORED_DIMENSIONS = 8
THRESHOLD = 65
MIN_GATING_SCORE = 3

HARD_FILTERS = [
    "economic_buyer",
    "painful_frequent_or_budgeted",
    "non_paid_distribution",
    "defensible_wedge",
    "no_network_effects_needed",
    "plausible_margins",
    "acceptable_risk",
    "cheap_disconfirming_test",
    "not_all_optimistic",
]
FILTER_STATUSES = {"pass", "fail", "defer", "unknown"}

STATES = {
    "discovered",
    "desk-screened",
    "adversarially-researched",
    "validation-ready",
    "externally-tested",
    "validated",
    "iterate",
    "killed",
}
ADVANCED_STATES = {"validation-ready", "externally-tested", "validated", "iterate"}
EVIDENCE_LEVELS = {
    "Plausible",
    "Promising",
    "Validation-ready",
    "Demand evidence",
    "Commercial evidence",
    "Repeatability evidence",
}
CONFIDENCES = {"none", "low", "medium", "high"}
REVIEW_STATUSES = {"not-required", "requested", "changes-requested", "approved", "killed"}
REVIEW_TRANSITIONS = {
    ("not-required", "requested"),
    ("requested", "changes-requested"),
    ("requested", "approved"),
    ("requested", "killed"),
    ("changes-requested", "requested"),
    ("changes-requested", "approved"),
    ("changes-requested", "killed"),
    ("approved", "requested"),
    ("killed", "requested"),
}
EXPERIMENT_STATUSES = {"proposed", "awaiting-approval", "approved", "running", "completed", "abandoned"}
LIMITS = {
    "max_unreviewed_before_generation_stops": 10,
    "max_new_candidates_per_run": 3,
    "max_validation_ready_advances_per_run": 1,
}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def load_json(report: Report, path: Path, label: str):
    if not path.exists():
        report.error(f"{label}: missing file {path}")
        return None
    try:
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        report.error(f"{label}: invalid JSON in {path}: {exc}")
        return None


def as_dict(report: Report, value, label: str) -> dict:
    if not isinstance(value, dict):
        report.error(f"{label}: expected an object")
        return {}
    return value


def require_keys(report: Report, obj: dict, keys: list[str], label: str) -> bool:
    ok = True
    for key in keys:
        if key not in obj:
            report.error(f"{label}: missing required key '{key}'")
            ok = False
    return ok


def check_dated(report: Report, value, label: str) -> None:
    import re

    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        report.error(f"{label}: expected a YYYY-MM-DD date, got {value!r}")


def resolve_path(root: Path, ref: str) -> Path | None:
    if ref.startswith(("http://", "https://")):
        return None
    return root / ref


def check_evidence_refs(report: Report, root: Path, refs, label: str) -> None:
    if not isinstance(refs, list):
        report.error(f"{label}: evidence must be a list")
        return
    for ref in refs:
        if not isinstance(ref, str) or not ref.strip():
            report.error(f"{label}: evidence entries must be non-empty strings")
            continue
        path = resolve_path(root, ref)
        if path is not None and not path.exists():
            report.error(f"{label}: evidence path does not exist: {ref}")


def recompute_aggregate(report: Report, dimensions: dict, label: str) -> dict:
    scored_weight = 0
    raw = 0.0
    scored_dims = 0
    for key, weight in DIMENSIONS.items():
        dim = dimensions.get(key)
        if not isinstance(dim, dict):
            continue
        score = dim.get("score")
        if score is None:
            continue
        scored_weight += weight
        raw += weight * score / 5.0
        scored_dims += 1
    weighted_total = round(raw / scored_weight * 100, 1) if scored_weight else None
    return {
        "scored_weight": scored_weight,
        "raw_weighted_points": round(raw, 1),
        "weighted_total": weighted_total,
        "scored_dimensions": scored_dims,
    }


def check_scorecard(report: Report, root: Path, slug: str, entry: dict, method_version: str) -> dict | None:
    path = root / "ideas" / slug / "scorecard.json"
    label = f"ideas/{slug}/scorecard.json"
    sc = load_json(report, path, label)
    if sc is None:
        return None
    sc = as_dict(report, sc, label)
    if not require_keys(
        report,
        sc,
        ["schema_version", "method_version", "weights_version", "idea_id", "slug", "title",
         "state", "updated", "dimensions", "hard_filters", "vetoes", "aggregate", "confidence",
         "review", "experiment"],
        label,
    ):
        return sc

    if sc.get("schema_version") != SCHEMA_VERSION:
        report.error(f"{label}: schema_version must be {SCHEMA_VERSION}")
    if sc.get("method_version") != method_version:
        report.error(f"{label}: method_version {sc.get('method_version')!r} != {method_version!r}")
    if sc.get("weights_version") != WEIGHTS_VERSION:
        report.error(f"{label}: weights_version must be {WEIGHTS_VERSION}")
    if sc.get("slug") != slug or sc.get("idea_id") != slug:
        report.error(f"{label}: slug/idea_id must match directory name '{slug}'")
    if sc.get("state") != entry.get("state"):
        report.error(f"{label}: state {sc.get('state')!r} != ideas/index.json state {entry.get('state')!r}")
    if sc.get("state") not in STATES:
        report.error(f"{label}: illegal state {sc.get('state')!r}")
    if sc.get("confidence") not in CONFIDENCES:
        report.error(f"{label}: illegal confidence {sc.get('confidence')!r}")

    # Dimensions
    dims = as_dict(report, sc.get("dimensions"), label)
    for key, weight in DIMENSIONS.items():
        dim = dims.get(key)
        if not isinstance(dim, dict):
            report.error(f"{label}: dimensions.{key} missing or not an object")
            continue
        if dim.get("weight") != weight:
            report.error(f"{label}: dimensions.{key}.weight must be {weight}")
        score = dim.get("score")
        if score is not None and (not isinstance(score, int) or isinstance(score, bool) or not 0 <= score <= 5):
            report.error(f"{label}: dimensions.{key}.score must be null or an integer 0-5, got {score!r}")
        confidence = dim.get("confidence")
        if confidence not in CONFIDENCES:
            report.error(f"{label}: dimensions.{key}.confidence must be one of {sorted(CONFIDENCES)}")
        if score is None and confidence != "none":
            report.error(f"{label}: dimensions.{key} is unscored but confidence is {confidence!r} (must be 'none')")
        if score is not None and confidence == "none":
            report.error(f"{label}: dimensions.{key} is scored but confidence is 'none'")
        if score:  # a positive score requires evidence
            refs = dim.get("evidence")
            if not refs:
                report.error(f"{label}: dimensions.{key} scored {score} with no evidence")
        check_evidence_refs(report, root, dim.get("evidence", []), f"{label}: dimensions.{key}")
    extra = set(dims) - set(DIMENSIONS)
    if extra:
        report.error(f"{label}: unknown dimensions: {sorted(extra)}")

    # Hard filters
    filters = as_dict(report, sc.get("hard_filters"), label)
    for key in HARD_FILTERS:
        item = filters.get(key)
        if not isinstance(item, dict):
            report.error(f"{label}: hard_filters.{key} missing or not an object")
            continue
        if item.get("status") not in FILTER_STATUSES:
            report.error(f"{label}: hard_filters.{key}.status must be one of {sorted(FILTER_STATUSES)}")
    extra = set(filters) - set(HARD_FILTERS)
    if extra:
        report.error(f"{label}: unknown hard filters: {sorted(extra)}")

    # Vetoes
    vetoes = sc.get("vetoes", [])
    if not isinstance(vetoes, list):
        report.error(f"{label}: vetoes must be a list")
        vetoes = []
    for veto in vetoes:
        if not isinstance(veto, dict) or not veto.get("key"):
            report.error(f"{label}: each veto needs a 'key'")
        elif "date" in veto:
            check_dated(report, veto.get("date"), f"{label}: veto {veto.get('key')}")

    # Aggregate
    agg = as_dict(report, sc.get("aggregate"), label)
    computed = recompute_aggregate(report, dims, label)
    for key in ("scored_weight", "raw_weighted_points", "weighted_total"):
        if agg.get(key) != computed[key]:
            report.error(
                f"{label}: aggregate.{key} is {agg.get(key)!r}, computed {computed[key]!r}"
            )
    if agg.get("threshold") != THRESHOLD:
        report.error(f"{label}: aggregate.threshold must be {THRESHOLD}")
    expected_meets = computed["weighted_total"] is not None and computed["weighted_total"] >= THRESHOLD
    if bool(agg.get("meets_threshold")) != expected_meets:
        report.error(f"{label}: aggregate.meets_threshold is {agg.get('meets_threshold')!r}, computed {expected_meets}")

    # State-dependent rules
    state = sc.get("state")
    statuses = {k: (filters.get(k) or {}).get("status") for k in HARD_FILTERS}
    fails = [k for k, v in statuses.items() if v == "fail"]
    unknowns = [k for k, v in statuses.items() if v in {"unknown", "defer"}]

    if fails and state != "killed":
        report.error(f"{label}: hard filters failed ({', '.join(fails)}) but state is {state!r} (must be 'killed')")
    if unknowns and state not in {"discovered", "killed"}:
        report.error(
            f"{label}: hard filters unresolved ({', '.join(unknowns)}) but state is {state!r} (must be 'discovered' or 'killed')"
        )
    if not fails and not unknowns and state == "discovered":
        report.warn(f"{label}: all hard filters pass but state is still 'discovered'")
    if vetoes and state not in {"killed", "adversarially-researched"}:
        report.error(f"{label}: vetoes present but state is {state!r} (must be 'killed' or 'adversarially-researched')")

    if state in ADVANCED_STATES:
        if computed["weighted_total"] is None or computed["weighted_total"] < THRESHOLD:
            report.error(f"{label}: state {state!r} requires weighted_total >= {THRESHOLD}")
        if computed["scored_dimensions"] < MIN_SCORED_DIMENSIONS:
            report.error(
                f"{label}: state {state!r} requires >= {MIN_SCORED_DIMENSIONS} scored dimensions "
                f"(have {computed['scored_dimensions']})"
            )
        for key in GATING_DIMENSIONS:
            score = (dims.get(key) or {}).get("score")
            if score is None or score < MIN_GATING_SCORE:
                report.error(f"{label}: state {state!r} requires dimensions.{key} score >= {MIN_GATING_SCORE}")
        if sc.get("confidence") not in {"medium", "high"}:
            report.error(f"{label}: state {state!r} requires overall confidence medium or high")
        if fails:
            report.error(f"{label}: state {state!r} has failed hard filters")
        if vetoes:
            report.error(f"{label}: state {state!r} has active vetoes")
        review = sc.get("review") or {}
        if review.get("status") == "not-required":
            report.error(f"{label}: state {state!r} requires review.status != 'not-required'")
    if state == "killed" and (sc.get("review") or {}).get("status") not in {None, "not-required", "killed", "requested", "changes-requested"}:
        report.error(f"{label}: killed idea has impossible review.status")
    if (sc.get("review") or {}).get("status") == "killed" and state != "killed":
        report.error(f"{label}: review.status 'killed' requires state 'killed'")
    if entry.get("evidence_level") not in EVIDENCE_LEVELS:
        report.error(f"ideas/index.json: invalid evidence_level for {slug}: {entry.get('evidence_level')!r}")
    if state in {"externally-tested", "validated", "iterate"}:
        if (sc.get("review") or {}).get("status") != "approved":
            report.error(f"{label}: state {state!r} requires review.status 'approved'")
        exp = sc.get("experiment") or {}
        if not exp.get("results"):
            report.error(f"{label}: state {state!r} requires recorded experiment results")
        elif not (root / str(exp.get("results"))).exists():
            report.error(f"{label}: experiment results file missing: {exp.get('results')}")

    # Review block
    review = as_dict(report, sc.get("review"), label)
    status = review.get("status")
    if status not in REVIEW_STATUSES:
        report.error(f"{label}: review.status must be one of {sorted(REVIEW_STATUSES)}")
    history = review.get("history", [])
    if not isinstance(history, list):
        report.error(f"{label}: review.history must be a list")
        history = []
    if status == "not-required" and history:
        report.error(f"{label}: review.status is 'not-required' but history is not empty")
    if status != "not-required" and not history:
        report.error(f"{label}: review.status {status!r} requires non-empty review.history")
    previous = None
    for i, item in enumerate(history):
        if not isinstance(item, dict):
            report.error(f"{label}: review.history[{i}] must be an object")
            continue
        for key in ("date", "from", "to", "actor", "reason"):
            if key not in item:
                report.error(f"{label}: review.history[{i}] missing '{key}'")
        check_dated(report, item.get("date"), f"{label}: review.history[{i}].date")
        pair = (item.get("from"), item.get("to"))
        if pair not in REVIEW_TRANSITIONS:
            report.error(f"{label}: illegal review transition {pair}")
        if item.get("actor") not in {"worker", "human-owner", "reviewer", "bootstrap"}:
            report.error(f"{label}: review.history[{i}].actor must be worker|human-owner|reviewer|bootstrap")
        previous = item.get("to")
    if history and previous != status:
        report.error(f"{label}: review.history ends at {previous!r} but review.status is {status!r}")
    if status != "not-required":
        request_path = review.get("request_path")
        if not request_path:
            report.error(f"{label}: review.status {status!r} requires review.request_path")
        elif not (root / str(request_path)).exists():
            report.error(f"{label}: review request file missing: {request_path}")

    # Experiment reference
    exp = sc.get("experiment") or {}
    if exp.get("id"):
        if not exp.get("plan"):
            report.error(f"{label}: experiment.id set but experiment.plan is empty")
        elif not (root / str(exp.get("plan"))).exists():
            report.error(f"{label}: experiment plan file missing: {exp.get('plan')}")
        if exp.get("status") not in EXPERIMENT_STATUSES | {"none"}:
            report.error(f"{label}: illegal experiment.status {exp.get('status')!r}")
        if exp.get("results") and not (root / str(exp.get("results"))).exists():
            report.error(f"{label}: experiment results file missing: {exp.get('results')}")
    return sc


def check_index(report: Report, root: Path, index: dict, method_version: str) -> list[dict]:
    label = "ideas/index.json"
    if index.get("schema_version") != SCHEMA_VERSION:
        report.error(f"{label}: schema_version must be {SCHEMA_VERSION}")
    if index.get("method_version") != method_version:
        report.error(f"{label}: method_version {index.get('method_version')!r} != {method_version!r}")
    limits = index.get("limits") or {}
    for key, value in LIMITS.items():
        if limits.get(key) != value:
            report.warn(f"{label}: limits.{key} is {limits.get(key)!r}, expected {value}")
    ideas = index.get("ideas")
    if not isinstance(ideas, list):
        report.error(f"{label}: ideas must be a list")
        return []

    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    seen_titles: set[str] = set()
    by_state: dict[str, int] = {}
    unreviewed = 0

    for entry in ideas:
        entry = as_dict(report, entry, label)
        if not require_keys(
            report,
            entry,
            ["id", "slug", "title", "state", "discovered", "updated", "evidence_level", "score",
             "confidence", "fingerprint", "paths", "review", "experiment"],
            f"{label}: idea entry",
        ):
            continue
        slug = entry.get("slug")
        if not isinstance(slug, str) or not slug:
            report.error(f"{label}: idea slug must be a non-empty string")
            continue
        if slug in seen_slugs:
            report.error(f"{label}: duplicate slug '{slug}'")
        seen_slugs.add(slug)
        idea_id = entry.get("id")
        if idea_id in seen_ids:
            report.error(f"{label}: duplicate id {idea_id!r}")
        if isinstance(idea_id, str):
            seen_ids.add(idea_id)
        title_key = str(entry.get("title", "")).strip().lower()
        if title_key in seen_titles:
            report.error(f"{label}: duplicate title {entry.get('title')!r}")
        seen_titles.add(title_key)
        if entry.get("state") not in STATES:
            report.error(f"{label}: illegal state for {slug}: {entry.get('state')!r}")
            continue
        by_state[entry["state"]] = by_state.get(entry["state"], 0) + 1
        if entry["state"] == "discovered":
            unreviewed += 1
        check_dated(report, entry.get("discovered"), f"{label}: {slug}.discovered")
        check_dated(report, entry.get("updated"), f"{label}: {slug}.updated")

        fp = as_dict(report, entry.get("fingerprint"), f"{label}: {slug}.fingerprint")
        for key in ("buyer", "problem", "mechanism"):
            if not isinstance(fp.get(key), str) or not fp.get(key, "").strip():
                report.error(f"{label}: {slug}.fingerprint.{key} must be a non-empty string")
        if not isinstance(fp.get("keywords"), list) or not fp.get("keywords"):
            report.error(f"{label}: {slug}.fingerprint.keywords must be a non-empty list")

        paths = as_dict(report, entry.get("paths"), f"{label}: {slug}.paths")
        expected = {
            "dir": f"ideas/{slug}",
            "dossier": f"ideas/{slug}/dossier.md",
            "decision": f"ideas/{slug}/decision.md",
            "scorecard": f"ideas/{slug}/scorecard.json",
        }
        for key, value in expected.items():
            if paths.get(key) != value:
                report.error(f"{label}: {slug}.paths.{key} must be '{value}'")
            elif not (root / value).exists():
                report.error(f"{label}: {slug}.paths.{key} points at missing file {value}")

        review = as_dict(report, entry.get("review"), f"{label}: {slug}.review")
        if review.get("status") not in REVIEW_STATUSES:
            report.error(f"{label}: {slug}.review.status invalid: {review.get('status')!r}")
        if review.get("status") != "not-required":
            if not review.get("path"):
                report.error(f"{label}: {slug}.review.path required when status is {review.get('status')!r}")
            elif not (root / str(review.get("path"))).exists():
                report.error(f"{label}: {slug}.review.path missing: {review.get('path')}")

        exp = as_dict(report, entry.get("experiment"), f"{label}: {slug}.experiment")
        if exp.get("id") and exp.get("status") not in EXPERIMENT_STATUSES:
            report.error(f"{label}: {slug}.experiment.status invalid: {exp.get('status')!r}")

        sc = check_scorecard(report, root, slug, entry, method_version)
        if sc is not None:
            if entry.get("score") != (sc.get("aggregate") or {}).get("weighted_total"):
                report.error(
                    f"{label}: {slug}.score {entry.get('score')!r} != scorecard weighted_total "
                    f"{(sc.get('aggregate') or {}).get('weighted_total')!r}"
                )
            if entry.get("confidence") != sc.get("confidence"):
                report.error(
                    f"{label}: {slug}.confidence {entry.get('confidence')!r} != scorecard confidence "
                    f"{sc.get('confidence')!r}"
                )

    # Orphan idea directories
    ideas_dir = root / "ideas"
    if ideas_dir.is_dir():
        for child in sorted(ideas_dir.iterdir()):
            if child.is_dir() and child.name not in seen_slugs:
                report.error(f"ideas/: orphan directory with no index entry: {child.name}")

    # Counts
    counts = as_dict(report, index.get("counts"), f"{label}: counts")
    if counts.get("total") != len(ideas):
        report.error(f"{label}: counts.total {counts.get('total')!r} != {len(ideas)} ideas")
    if counts.get("unreviewed") != unreviewed:
        report.error(f"{label}: counts.unreviewed {counts.get('unreviewed')!r} != computed {unreviewed}")
    if counts.get("by_state") != by_state:
        report.error(f"{label}: counts.by_state {counts.get('by_state')!r} != computed {by_state!r}")
    if counts.get("killed") != by_state.get("killed", 0):
        report.error(f"{label}: counts.killed {counts.get('killed')!r} != {by_state.get('killed', 0)}")
    if unreviewed > LIMITS["max_unreviewed_before_generation_stops"]:
        report.error(
            f"{label}: {unreviewed} unreviewed ideas exceeds the limit of "
            f"{LIMITS['max_unreviewed_before_generation_stops']}; generation must stop"
        )
    elif unreviewed >= 8:
        report.warn(f"{label}: {unreviewed} unreviewed ideas (limit 10)")
    killed = by_state.get("killed", 0)
    if killed and killed % 5 == 0:
        report.warn(f"{label}: {killed} killed ideas; a false-negative audit is due (every 5th kill)")
    return ideas


def check_experiments(report: Report, root: Path, method_version: str, slugs: set[str]) -> dict:
    path = root / "experiments" / "index.json"
    label = "experiments/index.json"
    data = load_json(report, path, label)
    if data is None:
        return {}
    data = as_dict(report, data, label)
    if data.get("schema_version") != SCHEMA_VERSION:
        report.error(f"{label}: schema_version must be {SCHEMA_VERSION}")
    if data.get("method_version") != method_version:
        report.error(f"{label}: method_version {data.get('method_version')!r} != {method_version!r}")
    experiments = data.get("experiments")
    if not isinstance(experiments, list):
        report.error(f"{label}: experiments must be a list")
        return {}
    seen: set[str] = set()
    by_id: dict[str, dict] = {}
    for exp in experiments:
        exp = as_dict(report, exp, label)
        exp_id = exp.get("id")
        if not isinstance(exp_id, str) or not exp_id:
            report.error(f"{label}: experiment id must be a non-empty string")
            continue
        if exp_id in seen:
            report.error(f"{label}: duplicate experiment id '{exp_id}'")
        seen.add(str(exp_id))
        by_id[str(exp_id)] = exp
        if exp.get("idea_id") not in slugs:
            report.error(f"{label}: experiment {exp_id} references unknown idea {exp.get('idea_id')!r}")
        if exp.get("status") not in EXPERIMENT_STATUSES:
            report.error(f"{label}: experiment {exp_id} illegal status {exp.get('status')!r}")
        for key in ("hypothesis", "central_assumption", "kill_condition", "decision_rule"):
            if not isinstance(exp.get(key), str) or not exp.get(key, "").strip():
                report.error(f"{label}: experiment {exp_id} missing '{key}'")
        check_dated(report, exp.get("created"), f"{label}: {exp_id}.created")
        check_dated(report, exp.get("updated"), f"{label}: {exp_id}.updated")
        plan = exp.get("plan")
        if not plan or not (root / str(plan)).exists():
            report.error(f"{label}: experiment {exp_id} plan file missing: {plan!r}")
        results = exp.get("results")
        if results and not (root / str(results)).exists():
            report.error(f"{label}: experiment {exp_id} results file missing: {results!r}")
        approval = as_dict(report, exp.get("approval"), f"{label}: {exp_id}.approval")
        if not isinstance(approval.get("required"), bool):
            report.error(f"{label}: experiment {exp_id}.approval.required must be a boolean")
        if not isinstance(approval.get("granted"), bool):
            report.error(f"{label}: experiment {exp_id}.approval.granted must be a boolean")
        if approval.get("granted"):
            if not approval.get("granted_by") or not approval.get("granted_date"):
                report.error(f"{label}: experiment {exp_id} approved but granted_by/granted_date missing")
            check_dated(report, approval.get("granted_date"), f"{label}: {exp_id}.approval.granted_date")
        if exp.get("status") in {"approved", "running", "completed"} and not approval.get("granted"):
            report.error(f"{label}: experiment {exp_id} status {exp.get('status')!r} requires approval.granted")
        if exp.get("status") == "completed" and not results:
            report.error(f"{label}: experiment {exp_id} completed but results path is empty")
        bound = as_dict(report, exp.get("cost_bound"), f"{label}: {exp_id}.cost_bound")
        for key in ("money_gbp", "human_hours", "calendar_days"):
            if not isinstance(bound.get(key), (int, float)) or isinstance(bound.get(key), bool):
                report.error(f"{label}: experiment {exp_id}.cost_bound.{key} must be a number")
        if bound.get("human_hours", 0) > 20 or bound.get("money_gbp", 0) > 100:
            report.warn(
                f"{label}: experiment {exp_id} exceeds the review threshold "
                "(20 human-hours / GBP 100); a review request is required before approval"
            )
    return by_id


def check_runs(report: Report, root: Path, method_version: str) -> None:
    path = root / "runs" / "index.jsonl"
    if not path.exists():
        report.warn("runs/index.jsonl: missing (no runs recorded yet)")
        return
    seen: set[str] = set()
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            run = json.loads(line)
        except json.JSONDecodeError as exc:
            report.error(f"runs/index.jsonl:{lineno}: invalid JSON: {exc}")
            continue
        if not isinstance(run, dict):
            report.error(f"runs/index.jsonl:{lineno}: expected an object")
            continue
        for key in ("run_id", "mode", "status", "started_at", "agent", "model", "method_version", "validation", "summary"):
            if key not in run:
                report.error(f"runs/index.jsonl:{lineno}: missing '{key}'")
        run_id = run.get("run_id")
        if run_id in seen:
            report.error(f"runs/index.jsonl:{lineno}: duplicate run_id {run_id!r}")
        if isinstance(run_id, str):
            seen.add(run_id)
        if run.get("mode") not in {"normal", "dry-run", "smoke"}:
            report.error(f"runs/index.jsonl:{lineno}: illegal mode {run.get('mode')!r}")
        if run.get("status") not in {"success", "failed", "invalid-output", "over-budget"}:
            report.error(f"runs/index.jsonl:{lineno}: illegal status {run.get('status')!r}")
        if run.get("method_version") != method_version:
            report.error(f"runs/index.jsonl:{lineno}: method_version mismatch")
        if run.get("validation") not in {"pass", "fail", "not-run"}:
            report.error(f"runs/index.jsonl:{lineno}: illegal validation {run.get('validation')!r}")
        summary = run.get("summary")
        if summary and not (root / str(summary)).exists():
            report.warn(f"runs/index.jsonl:{lineno}: summary file missing: {summary}")


def run(root: Path, quiet: bool = False) -> Report:
    report = Report()
    version_file = root / "method" / "VERSION"
    if not version_file.exists():
        report.error("method/VERSION missing")
        method_version = "unknown"
    else:
        method_version = version_file.read_text(encoding="utf-8").strip()
        if not method_version:
            report.error("method/VERSION is empty")

    index = load_json(report, root / "ideas" / "index.json", "ideas/index.json")
    slugs: set[str] = set()
    if index is not None:
        index = as_dict(report, index, "ideas/index.json")
        ideas = check_index(report, root, index, method_version)
        slugs = {
            str(i.get("slug"))
            for i in ideas
            if isinstance(i, dict) and isinstance(i.get("slug"), str)
        }
        check_experiments(report, root, method_version, slugs)
    check_runs(report, root, method_version)
    return report


def queue(root: Path) -> int:
    index_path = root / "ideas" / "index.json"
    if not index_path.exists():
        print("No ideas/index.json found.", file=sys.stderr)
        return 1
    index = json.loads(index_path.read_text(encoding="utf-8"))
    ideas = index.get("ideas", [])
    rows = []
    for entry in ideas:
        if not isinstance(entry, dict):
            continue
        review = entry.get("review") or {}
        status = review.get("status")
        if status and status != "not-required":
            rows.append((entry.get("slug"), entry.get("state"), status, review.get("path")))
    killed = sum(1 for e in ideas if isinstance(e, dict) and e.get("state") == "killed")
    unreviewed = sum(1 for e in ideas if isinstance(e, dict) and e.get("state") == "discovered")
    print("Review queue")
    print("------------")
    if not rows:
        print("(empty)")
    for slug, state, status, path in rows:
        print(f"- {slug:<24} state={state:<22} review={status:<17} {path or ''}")
    print()
    print(f"Unreviewed ideas: {unreviewed} / {LIMITS['max_unreviewed_before_generation_stops']}")
    print(f"Killed ideas: {killed} (false-negative audit due every 5th kill)")
    if killed and killed % 5 == 0:
        print("  -> audit due now")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="repository root (default: current directory)")
    parser.add_argument("--json", action="store_true", help="print machine-readable result to stdout")
    parser.add_argument("--queue", action="store_true", help="print the review queue and exit")
    parser.add_argument("--quiet", action="store_true", help="suppress warnings in human output")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if args.queue:
        return queue(root)

    report = run(root)
    result = {
        "status": "pass" if not report.errors else "fail",
        "errors": report.errors,
        "warnings": report.warnings,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for warning in report.warnings:
            if not args.quiet:
                print(f"WARN: {warning}")
        for error in report.errors:
            print(f"ERROR: {error}")
        print(
            f"{result['status'].upper()}: {len(report.errors)} error(s), "
            f"{len(report.warnings)} warning(s) in {root}"
        )
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
