#!/usr/bin/env python3
"""Build a single self-contained HTML dashboard from the idea ledger.

Reads the machine-readable ledgers (ideas/index.json, ideas/<slug>/scorecard.json,
experiments/index.json, seeds/index.json, runs/index.jsonl, runs/<run-id>/run.json)
plus the discovery trail (intake/*.md, observations/*.md) and renders them as one
explorable HTML file. Stdlib only, no network, no external assets: the output is a
single file that opens in any browser.

The intake and observation sections are parsed from Markdown with a deliberately
small, tolerant parser: they surface the hypotheses and triage outcomes that never
became scored ideas, so early rejections stay visible. If a file does not match the
expected shape it is listed with a note rather than guessed at.

The dashboard renders only what the ledgers contain. Missing values are shown as
"unknown" / "not recorded" rather than guessed. Regenerating is idempotent: the
same inputs produce the same output.

Usage:
    python3 scripts/build_dashboard.py [--root DIR] [--out PATH] [--quiet]

Defaults: --root is the repository root (the parent of this script's directory),
--out is <root>/dashboard.html.
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from datetime import datetime, timezone

SCHEMA_VERSION = 1
THRESHOLD = 65

DIMENSION_ORDER = [
    "problem_severity_frequency",
    "buyer_budget_clarity",
    "evidence_strength",
    "distribution",
    "differentiation",
    "validation_speed_cost",
    "feasibility",
    "economics",
    "founder_fit",
    "risk",
]

DIMENSION_LABELS = {
    "problem_severity_frequency": "Problem severity / frequency",
    "buyer_budget_clarity": "Buyer budget clarity",
    "evidence_strength": "Evidence strength",
    "distribution": "Distribution",
    "differentiation": "Differentiation",
    "validation_speed_cost": "Validation speed / cost",
    "feasibility": "Feasibility",
    "economics": "Economics",
    "founder_fit": "Founder fit",
    "risk": "Risk",
}

GATING_DIMENSIONS = {
    "problem_severity_frequency",
    "buyer_budget_clarity",
    "evidence_strength",
}

HARD_FILTER_ORDER = [
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

HARD_FILTER_LABELS = {
    "economic_buyer": "Clear economic buyer",
    "painful_frequent_or_budgeted": "Painful / frequent / budgeted",
    "non_paid_distribution": "Non-paid distribution",
    "defensible_wedge": "Defensible wedge",
    "no_network_effects_needed": "No network effects needed",
    "plausible_margins": "Plausible margins",
    "acceptable_risk": "Acceptable risk",
    "cheap_disconfirming_test": "Cheap disconfirming test",
    "not_all_optimistic": "Not all-optimistic",
}

STATE_ORDER = [
    "validation-ready",
    "externally-tested",
    "validated",
    "iterate",
    "adversarially-researched",
    "desk-screened",
    "discovered",
    "killed",
]

STATE_LABELS = {
    "discovered": "Discovered",
    "desk-screened": "Desk-screened",
    "adversarially-researched": "Adversarially researched",
    "validation-ready": "Validation-ready",
    "externally-tested": "Externally tested",
    "validated": "Validated",
    "iterate": "Iterate",
    "killed": "Killed",
}

EVIDENCE_LEVEL_ORDER = [
    "Repeatability evidence",
    "Commercial evidence",
    "Demand evidence",
    "Validation-ready",
    "Promising",
    "Plausible",
]

# Controlled industry vocabulary. Must match INDUSTRIES in scripts/validate_repo.py.
# Ideas are grouped by this field; an idea with no industry renders as "unknown".
INDUSTRY_ORDER = [
    "accountancy-professional-services",
    "hospitality-leisure",
    "food-grocery",
    "ecommerce-retail",
    "packaging-manufacturing",
    "hr-employment",
    "education-charities",
    "veterinary",
    "property-lettings",
    "waste-environment",
    "payroll-benefits",
    "software-it",
    "healthcare-clinics",
]

INDUSTRY_LABELS = {
    "accountancy-professional-services": "Accountancy & professional services",
    "hospitality-leisure": "Hospitality & leisure",
    "food-grocery": "Food & grocery",
    "ecommerce-retail": "E-commerce & retail",
    "packaging-manufacturing": "Packaging & manufacturing",
    "hr-employment": "HR & employment",
    "education-charities": "Education & charities",
    "veterinary": "Veterinary",
    "property-lettings": "Property & lettings",
    "waste-environment": "Waste & environment",
    "payroll-benefits": "Payroll & benefits",
    "software-it": "Software & IT",
    "healthcare-clinics": "Healthcare & clinics",
}


def industry_label(value):
    """Human label for an industry slug; unknown/None renders honestly."""
    if value is None or value == "":
        return "unknown"
    return INDUSTRY_LABELS.get(value, str(value))



# --------------------------------------------------------------------------
# Loading
# --------------------------------------------------------------------------


def load_json(path, default=None):
    """Load JSON, returning default on missing or malformed files."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return default


def load_jsonl(path):
    """Load a JSONL file, skipping malformed lines."""
    rows = []
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    except (OSError, UnicodeDecodeError):
        return []
    return rows


def load_ledger(root):
    """Load every ledger the dashboard needs."""
    ideas_index = load_json(os.path.join(root, "ideas", "index.json"), {}) or {}
    experiments_index = load_json(os.path.join(root, "experiments", "index.json"), {}) or {}
    seeds_index = load_json(os.path.join(root, "seeds", "index.json"), {}) or {}
    runs = load_jsonl(os.path.join(root, "runs", "index.jsonl"))

    ideas = []
    for entry in ideas_index.get("ideas", []) or []:
        slug = entry.get("slug") or entry.get("id") or "unknown"
        scorecard_path = os.path.join(root, "ideas", slug, "scorecard.json")
        scorecard = load_json(scorecard_path, None)
        ideas.append({"entry": entry, "scorecard": scorecard})

    return {
        "ideas_index": ideas_index,
        "ideas": ideas,
        "experiments_index": experiments_index,
        "seeds_index": seeds_index,
        "runs": runs,
        "intake": load_intake(root),
        "observations": load_observations(root),
    }


# --------------------------------------------------------------------------
# Discovery trail (intake notes and observation pools)
# --------------------------------------------------------------------------

# A tolerant Markdown parser for the two discovery artefacts. Both are written to
# templates, so the shapes are stable, but the parser degrades to "listed, not
# parsed" rather than inventing structure when a file does not match.

_HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$")
_TABLE_ROW_RE = re.compile(r"^\|(.+)\|\s*$")
_TABLE_SEP_RE = re.compile(r"^\|[\s:|-]+\|\s*$")


def _read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return handle.read()
    except (OSError, UnicodeDecodeError):
        return None


def _split_table_row(line):
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [cell.strip() for cell in inner.split("|")]


def _parse_tables(text):
    """Return a list of tables; each table is {headers: [...], rows: [[...]]}."""
    tables = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if _TABLE_ROW_RE.match(line) and index + 1 < len(lines) and _TABLE_SEP_RE.match(lines[index + 1]):
            headers = _split_table_row(line)
            rows = []
            index += 2
            while index < len(lines) and _TABLE_ROW_RE.match(lines[index]):
                rows.append(_split_table_row(lines[index]))
                index += 1
            tables.append({"headers": headers, "rows": rows})
        else:
            index += 1
    return tables


def _strip_md(text):
    """Strip the light Markdown used in these files for plain-text display."""
    if text is None:
        return None
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", text)
    return text.strip()


def _section(text, heading_prefix):
    """Return the body of the first heading whose text starts with heading_prefix."""
    lines = text.splitlines()
    start = None
    level = None
    for index, line in enumerate(lines):
        match = _HEADING_RE.match(line)
        if match and match.group(2).strip().lower().startswith(heading_prefix.lower()):
            start = index + 1
            level = len(match.group(1))
            break
    if start is None or level is None:
        return ""
    body = []
    for line in lines[start:]:
        match = _HEADING_RE.match(line)
        if match and len(match.group(1)) <= level:
            break
        body.append(line)
    return "\n".join(body)


def load_intake(root):
    """Load intake notes: each file's title, header fields and hypothesis sections."""
    intake_dir = os.path.join(root, "intake")
    notes = []
    try:
        names = sorted(os.listdir(intake_dir))
    except OSError:
        return notes
    for name in names:
        if not name.endswith(".md") or name.lower() == "readme.md":
            continue
        path = os.path.join(intake_dir, name)
        text = _read_text(path)
        if text is None:
            continue
        lines = text.splitlines()
        title = None
        for line in lines:
            match = _HEADING_RE.match(line)
            if match and len(match.group(1)) == 1:
                title = _strip_md(match.group(2))
                break
        fields = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("- **") and ":**" in stripped:
                label, _, value = stripped[4:].partition(":**")
                fields.append((label.strip(), _strip_md(value.strip())))
        hypotheses = []
        for line in lines:
            match = _HEADING_RE.match(line)
            if not match:
                continue
            heading = _strip_md(match.group(2)) or ""
            if re.match(r"^(hypothesis|h\d+\b)", heading, re.IGNORECASE):
                body = _section(text, heading)
                hypotheses.append({"heading": heading, "body": body})
        notes.append(
            {
                "file": os.path.join("intake", name),
                "title": title or name,
                "fields": fields,
                "hypotheses": hypotheses,
                "parsed": bool(hypotheses),
            }
        )
    return notes


def load_observations(root):
    """Load observation pools: header metrics, observation rows and the audit."""
    obs_dir = os.path.join(root, "observations")
    pools = []
    try:
        names = sorted(os.listdir(obs_dir))
    except OSError:
        return pools
    for name in names:
        if not name.endswith(".md") or name.lower() == "readme.md":
            continue
        path = os.path.join(obs_dir, name)
        text = _read_text(path)
        if text is None:
            continue
        fields = []
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("- **") and ":**" in stripped:
                label, _, value = stripped[4:].partition(":**")
                fields.append((label.strip(), _strip_md(value.strip())))

        observations = []
        promoted = []
        audit = []
        for table in _parse_tables(text):
            headers = [h.lower() for h in table["headers"]]
            if headers and headers[0] == "id" and "observation" in " ".join(headers):
                for row in table["rows"]:
                    observations.append(dict(zip(table["headers"], row)))
            elif headers and headers[0] == "id" and "promoted" in " ".join(headers):
                for row in table["rows"]:
                    promoted.append(dict(zip(table["headers"], row)))
            elif headers and headers[0] == "field" and "record" in headers:
                for row in table["rows"]:
                    audit.append((row[0], row[1] if len(row) > 1 else ""))

        pools.append(
            {
                "file": os.path.join("observations", name),
                "run_id": name[:-3],
                "fields": fields,
                "observations": observations,
                "promoted": promoted,
                "audit": audit,
                "parsed": bool(observations),
            }
        )
    return pools


# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------


def esc(value):
    """HTML-escape a value, rendering missing values honestly."""
    if value is None:
        return '<span class="unknown">unknown</span>'
    if isinstance(value, bool):
        return "yes" if value else "no"
    text = str(value).strip()
    if not text:
        return '<span class="unknown">not recorded</span>'
    return html.escape(text)


def esc_raw(value):
    """HTML-escape a plain string (no unknown placeholder)."""
    if value is None:
        return ""
    return html.escape(str(value))


def fmt_score(value):
    if value is None:
        return '<span class="unknown">unknown</span>'
    try:
        return f"{float(value):.1f}"
    except (TypeError, ValueError):
        return esc(value)


def fmt_money(value):
    if value is None:
        return '<span class="unknown">unknown</span>'
    try:
        return f"${float(value):.4f}"
    except (TypeError, ValueError):
        return esc(value)


def fmt_int(value):
    if value is None:
        return '<span class="unknown">unknown</span>'
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return esc(value)


def count_by(items, key):
    counts = {}
    for item in items:
        value = item.get(key)
        if value is None:
            value = "unknown"
        counts[value] = counts.get(value, 0) + 1
    return counts


def ordered_counts(counts, order):
    """Return (label, count) pairs in a preferred order, then the rest."""
    seen = set()
    rows = []
    for key in order:
        if key in counts:
            rows.append((key, counts[key]))
            seen.add(key)
    for key in sorted(counts):
        if key not in seen:
            rows.append((key, counts[key]))
    return rows


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------


def render_stat_cards(ideas_index, ideas, experiments_index, seeds_index, runs):
    counts = ideas_index.get("counts", {}) or {}
    by_state = counts.get("by_state", {}) or {}
    total = counts.get("total", len(ideas))
    unreviewed = counts.get("unreviewed", 0)
    killed = counts.get("killed", by_state.get("killed", 0))

    experiments = experiments_index.get("experiments", []) or []
    seed_counts = seeds_index.get("counts", {}) or {}
    seed_by_status = seed_counts.get("by_status", {}) or {}

    scored = [
        item["entry"].get("score")
        for item in ideas
        if item["entry"].get("score") is not None
    ]
    best = max(scored) if scored else None
    above = sum(1 for s in scored if s is not None and s >= THRESHOLD)

    total_cost = 0.0
    cost_known = False
    for run in runs:
        value = run.get("cost_usd")
        if isinstance(value, (int, float)):
            total_cost += float(value)
            cost_known = True

    cards = [
        ("Ideas in ledger", fmt_int(total), f"{unreviewed} unreviewed"),
        ("Killed", fmt_int(killed), "preserved with reasons"),
        ("Best score", fmt_score(best), f"threshold {THRESHOLD}"),
        ("At/above threshold", fmt_int(above), "of scored ideas"),
        ("Experiments", fmt_int(len(experiments)), "proposed / completed"),
        ("Seeds", fmt_int(seed_counts.get("total", len(seeds_index.get("seeds", []) or []))), "non-inheriting"),
        ("Runs recorded", fmt_int(len(runs)), "in runs/index.jsonl"),
        ("Total run cost", fmt_money(total_cost) if cost_known else '<span class="unknown">unknown</span>', "sum of recorded runs"),
    ]

    out = ['<div class="cards">']
    for label, value, note in cards:
        out.append(
            '<div class="card">'
            f'<div class="card-value">{value}</div>'
            f'<div class="card-label">{esc_raw(label)}</div>'
            f'<div class="card-note">{esc_raw(note)}</div>'
            "</div>"
        )
    out.append("</div>")
    return "\n".join(out)


def render_bar_chart(title, rows, total):
    out = [f'<div class="chart"><h4>{esc_raw(title)}</h4>']
    if not rows:
        out.append('<p class="unknown">no data</p></div>')
        return "\n".join(out)
    for label, count in rows:
        pct = (count / total * 100) if total else 0
        out.append(
            '<div class="bar-row">'
            f'<span class="bar-label">{esc_raw(label)}</span>'
            '<span class="bar-track">'
            f'<span class="bar-fill" style="width:{pct:.1f}%"></span>'
            "</span>"
            f'<span class="bar-count">{count}</span>'
            "</div>"
        )
    out.append("</div>")
    return "\n".join(out)


def render_portfolio(ideas_index, ideas, experiments_index, seeds_index, runs):
    counts = ideas_index.get("counts", {}) or {}
    by_state = counts.get("by_state", {}) or {}
    total = counts.get("total", len(ideas)) or 1

    state_rows = ordered_counts(by_state, STATE_ORDER)
    state_rows = [(STATE_LABELS.get(k, k), v) for k, v in state_rows]

    level_counts = count_by([i["entry"] for i in ideas], "evidence_level")
    level_rows = ordered_counts(level_counts, EVIDENCE_LEVEL_ORDER)

    conf_counts = count_by([i["entry"] for i in ideas], "confidence")
    conf_rows = ordered_counts(conf_counts, ["high", "medium", "low"])

    experiments = experiments_index.get("experiments", []) or []
    exp_counts = count_by(experiments, "status")
    exp_rows = ordered_counts(exp_counts, ["proposed", "awaiting-approval", "approved", "running", "completed", "abandoned"])

    seed_counts = (seeds_index.get("counts", {}) or {}).get("by_status", {}) or {}
    seed_rows = ordered_counts(seed_counts, ["unexplored", "exploring", "promoted", "dropped"])

    industry_counts = count_by([i["entry"] for i in ideas], "industry")
    industry_rows = ordered_counts(industry_counts, INDUSTRY_ORDER)
    industry_rows = [(industry_label(k), v) for k, v in industry_rows]

    charts = [
        render_bar_chart("Ideas by state", state_rows, total),
        render_bar_chart("Ideas by industry", industry_rows, total),
        render_bar_chart("Ideas by evidence level", level_rows, total),
        render_bar_chart("Ideas by confidence", conf_rows, total),
        render_bar_chart("Experiments by status", exp_rows, max(len(experiments), 1)),
        render_bar_chart("Seeds by status", seed_rows, max(sum(seed_counts.values()), 1)),
    ]
    return '<div class="charts">' + "\n".join(charts) + "</div>"


def render_score_distribution(ideas):
    """A simple horizontal strip showing each idea's score against the threshold."""
    scored = [i for i in ideas if i["entry"].get("score") is not None]
    if not scored:
        return '<p class="unknown">No scored ideas.</p>'
    scored.sort(key=lambda i: i["entry"].get("score") or 0, reverse=True)
    out = ['<div class="score-strip">']
    for item in scored:
        entry = item["entry"]
        score = entry.get("score") or 0
        pct = min(max(score, 0), 100)
        cls = "score-high" if score >= THRESHOLD else ("score-mid" if score >= 50 else "score-low")
        out.append(
            '<div class="score-row">'
            f'<span class="score-name">{esc_raw(entry.get("title") or entry.get("slug"))}</span>'
            '<span class="score-track">'
            f'<span class="score-fill {cls}" style="width:{pct:.1f}%"></span>'
            f'<span class="score-threshold" style="left:{THRESHOLD}%"></span>'
            "</span>"
            f'<span class="score-value">{fmt_score(score)}</span>'
            "</div>"
        )
    out.append("</div>")
    out.append(
        f'<p class="hint">The vertical marker is the validation-ready threshold ({THRESHOLD}). '
        "Scores are desk-research scores, not market validation.</p>"
    )
    return "\n".join(out)


def render_dimensions(scorecard):
    if not scorecard:
        return '<p class="unknown">No scorecard recorded.</p>'
    dimensions = scorecard.get("dimensions", {}) or {}
    out = ['<table class="grid"><thead><tr>'
           "<th>Dimension</th><th>Weight</th><th>Score</th><th>Confidence</th>"
           "<th>Rationale</th><th>Evidence</th></tr></thead><tbody>"]
    for key in DIMENSION_ORDER:
        dim = dimensions.get(key)
        if not isinstance(dim, dict):
            out.append(
                f'<tr><td>{esc_raw(DIMENSION_LABELS.get(key, key))}</td>'
                '<td class="unknown">unknown</td><td class="unknown">unknown</td>'
                '<td class="unknown">unknown</td><td class="unknown">unknown</td>'
                '<td class="unknown">unknown</td></tr>'
            )
            continue
        gating = ' <span class="tag tag-gating">gating</span>' if key in GATING_DIMENSIONS else ""
        evidence = dim.get("evidence") or []
        evidence_html = ", ".join(f'<code>{esc_raw(e)}</code>' for e in evidence) if evidence else '<span class="unknown">none</span>'
        out.append(
            "<tr>"
            f'<td>{esc_raw(DIMENSION_LABELS.get(key, key))}{gating}</td>'
            f'<td>{esc(dim.get("weight"))}</td>'
            f'<td class="num">{esc(dim.get("score"))}</td>'
            f'<td>{esc(dim.get("confidence"))}</td>'
            f'<td class="rationale">{esc(dim.get("rationale"))}</td>'
            f'<td class="evidence">{evidence_html}</td>'
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def render_hard_filters(scorecard):
    if not scorecard:
        return '<p class="unknown">No scorecard recorded.</p>'
    filters = scorecard.get("hard_filters", {}) or {}
    out = ['<table class="grid"><thead><tr>'
           "<th>Hard filter</th><th>Status</th><th>Note</th><th>Resolve via</th>"
           "<th>Evidence</th></tr></thead><tbody>"]
    for key in HARD_FILTER_ORDER:
        flt = filters.get(key)
        if not isinstance(flt, dict):
            out.append(
                f'<tr><td>{esc_raw(HARD_FILTER_LABELS.get(key, key))}</td>'
                '<td class="unknown">unknown</td><td class="unknown">unknown</td>'
                '<td class="unknown">unknown</td><td class="unknown">unknown</td></tr>'
            )
            continue
        status = flt.get("status")
        status_cls = {
            "pass": "status-pass",
            "unknown": "status-unknown",
            "fail": "status-fail",
        }.get(str(status) if status is not None else "", "status-unknown")
        evidence = flt.get("evidence") or []
        evidence_html = ", ".join(f'<code>{esc_raw(e)}</code>' for e in evidence) if evidence else '<span class="unknown">none</span>'
        out.append(
            "<tr>"
            f'<td>{esc_raw(HARD_FILTER_LABELS.get(key, key))}</td>'
            f'<td><span class="status {status_cls}">{esc(status)}</span></td>'
            f'<td>{esc(flt.get("note"))}</td>'
            f'<td>{esc(flt.get("resolve_via"))}</td>'
            f'<td class="evidence">{evidence_html}</td>'
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def render_why_now(entry):
    why = entry.get("why_now") or {}
    if not why:
        return '<p class="unknown">No why-now recorded.</p>'
    evidence = why.get("evidence") or []
    evidence_html = ", ".join(f'<code>{esc_raw(e)}</code>' for e in evidence) if evidence else '<span class="unknown">none</span>'
    rows = [
        ("What changed", esc(why.get("changed"))),
        ("When", esc(why.get("changed_date"))),
        ("Why it matters", esc(why.get("why_it_matters"))),
        ("Strength", esc(why.get("strength"))),
        ("Competitors responded", esc(why.get("competitors_responded"))),
        ("Evidence", evidence_html),
    ]
    out = ['<table class="kv">']
    for label, value in rows:
        out.append(f"<tr><th>{esc_raw(label)}</th><td>{value}</td></tr>")
    out.append("</table>")
    return "\n".join(out)


def render_fingerprint(entry):
    fp = entry.get("fingerprint") or {}
    if not fp:
        return '<p class="unknown">No fingerprint recorded.</p>'
    keywords = fp.get("keywords") or []
    keyword_html = " ".join(f'<span class="tag">{esc_raw(k)}</span>' for k in keywords) if keywords else '<span class="unknown">none</span>'
    rows = [
        ("Buyer", esc(fp.get("buyer"))),
        ("Problem", esc(fp.get("problem"))),
        ("Mechanism", esc(fp.get("mechanism"))),
        ("Keywords", keyword_html),
    ]
    out = ['<table class="kv">']
    for label, value in rows:
        out.append(f"<tr><th>{esc_raw(label)}</th><td>{value}</td></tr>")
    out.append("</table>")
    return "\n".join(out)


def render_review(entry, scorecard):
    review = (scorecard or {}).get("review") or entry.get("review") or {}
    if not review:
        return '<p class="unknown">No review recorded.</p>'
    rows = [
        ("Status", esc(review.get("status"))),
        ("Requested from", esc(review.get("requested_from"))),
        ("Request path", esc(review.get("request_path"))),
        ("Response path", esc(review.get("response_path"))),
        ("Last reviewed revision", esc(review.get("last_reviewed_revision"))),
    ]
    out = ['<table class="kv">']
    for label, value in rows:
        out.append(f"<tr><th>{esc_raw(label)}</th><td>{value}</td></tr>")
    out.append("</table>")

    history = review.get("history") or []
    if history:
        out.append('<table class="grid"><thead><tr><th>Date</th><th>From</th><th>To</th><th>Actor</th><th>Reason</th></tr></thead><tbody>')
        for row in history:
            out.append(
                "<tr>"
                f'<td>{esc(row.get("date"))}</td>'
                f'<td>{esc(row.get("from"))}</td>'
                f'<td>{esc(row.get("to"))}</td>'
                f'<td>{esc(row.get("actor"))}</td>'
                f'<td>{esc(row.get("reason"))}</td>'
                "</tr>"
            )
        out.append("</tbody></table>")
    return "\n".join(out)


def render_experiment(entry, experiments_by_id):
    exp_ref = entry.get("experiment") or {}
    exp_id = exp_ref.get("id")
    exp = experiments_by_id.get(exp_id) if exp_id else None
    if not exp:
        if not exp_ref:
            return '<p class="unknown">No experiment recorded.</p>'
        rows = [
            ("ID", esc(exp_ref.get("id"))),
            ("Status", esc(exp_ref.get("status"))),
            ("Plan", esc(exp_ref.get("plan"))),
        ]
        approval = exp_ref.get("approval") or {}
        rows.append(("Approval required", esc(approval.get("required"))))
        rows.append(("Approval granted", esc(approval.get("granted"))))
        out = ['<table class="kv">']
        for label, value in rows:
            out.append(f"<tr><th>{esc_raw(label)}</th><td>{value}</td></tr>")
        out.append("</table>")
        return "\n".join(out)

    approval = exp.get("approval") or {}
    cost = exp.get("cost_bound") or {}
    rows = [
        ("ID", esc(exp.get("id"))),
        ("Status", esc(exp.get("status"))),
        ("Hypothesis", esc(exp.get("hypothesis"))),
        ("Central assumption", esc(exp.get("central_assumption"))),
        ("Kill condition", esc(exp.get("kill_condition"))),
        ("Decision rule", esc(exp.get("decision_rule"))),
        ("Cost bound (money)", esc(cost.get("money_gbp"))),
        ("Cost bound (hours)", esc(cost.get("human_hours"))),
        ("Cost bound (days)", esc(cost.get("calendar_days"))),
        ("Approval required", esc(approval.get("required"))),
        ("Approval granted", esc(approval.get("granted"))),
        ("Plan", esc(exp.get("plan"))),
        ("Results", esc(exp.get("results"))),
    ]
    out = ['<table class="kv">']
    for label, value in rows:
        out.append(f"<tr><th>{esc_raw(label)}</th><td>{value}</td></tr>")
    out.append("</table>")
    return "\n".join(out)


def render_idea(item, experiments_by_id):
    entry = item["entry"]
    scorecard = item["scorecard"]
    slug = entry.get("slug") or entry.get("id") or "unknown"
    title = entry.get("title") or slug
    state = entry.get("state")
    score = entry.get("score")
    aggregate = (scorecard or {}).get("aggregate") or {}
    meets = aggregate.get("meets_threshold")
    if meets is None and score is not None:
        meets = score >= THRESHOLD

    state_cls = "state-killed" if state == "killed" else "state-live"
    score_cls = "score-high" if (score or 0) >= THRESHOLD else ("score-mid" if (score or 0) >= 50 else "score-low")

    out = [f'<details class="idea" id="idea-{esc_raw(slug)}">']
    out.append(
        "<summary>"
        f'<span class="idea-title">{esc_raw(title)}</span>'
        f'<span class="tag {state_cls}">{esc(state)}</span>'
        f'<span class="tag">{esc(entry.get("evidence_level"))}</span>'
        f'<span class="tag tag-industry">{esc_raw(industry_label(entry.get("industry")))}</span>'
        f'<span class="idea-score {score_cls}">{fmt_score(score)}</span>'
        "</summary>"
    )
    out.append('<div class="idea-body">')

    meta_rows = [
        ("Slug", esc(slug)),
        ("Industry", esc_raw(industry_label(entry.get("industry")))),
        ("State", esc(state)),
        ("Evidence level", esc(entry.get("evidence_level"))),
        ("Score", fmt_score(score)),
        ("Threshold", fmt_int(aggregate.get("threshold", THRESHOLD))),
        ("Meets threshold", esc(meets)),
        ("Confidence", esc(entry.get("confidence"))),
        ("Discovered", esc(entry.get("discovered"))),
        ("Updated", esc(entry.get("updated"))),
        ("Dossier", esc((entry.get("paths") or {}).get("dossier"))),
        ("Decision record", esc((entry.get("paths") or {}).get("decision"))),
        ("Scorecard", esc((entry.get("paths") or {}).get("scorecard"))),
    ]
    out.append('<table class="kv">')
    for label, value in meta_rows:
        out.append(f"<tr><th>{esc_raw(label)}</th><td>{value}</td></tr>")
    out.append("</table>")

    out.append("<h4>Why now?</h4>")
    out.append(render_why_now(entry))

    out.append("<h4>Fingerprint</h4>")
    out.append(render_fingerprint(entry))

    out.append("<h4>Scorecard dimensions</h4>")
    out.append(render_dimensions(scorecard))

    out.append("<h4>Hard filters</h4>")
    out.append(render_hard_filters(scorecard))

    vetoes = (scorecard or {}).get("vetoes") or []
    out.append("<h4>Vetoes</h4>")
    if vetoes:
        out.append('<table class="grid"><thead><tr><th>Key</th><th>Note</th><th>Date</th></tr></thead><tbody>')
        for veto in vetoes:
            out.append(
                "<tr>"
                f'<td>{esc(veto.get("key"))}</td>'
                f'<td>{esc(veto.get("note"))}</td>'
                f'<td>{esc(veto.get("date"))}</td>'
                "</tr>"
            )
        out.append("</tbody></table>")
    else:
        out.append('<p class="unknown">No vetoes recorded.</p>')

    out.append("<h4>Review</h4>")
    out.append(render_review(entry, scorecard))

    out.append("<h4>Experiment</h4>")
    out.append(render_experiment(entry, experiments_by_id))

    out.append("</div></details>")
    return "\n".join(out)


def render_ideas(ideas, experiments_by_id):
    if not ideas:
        return '<p class="unknown">No ideas in the ledger.</p>'

    def sort_key(item):
        entry = item["entry"]
        state = entry.get("state")
        try:
            state_rank = STATE_ORDER.index(state)
        except ValueError:
            state_rank = len(STATE_ORDER)
        score = entry.get("score")
        return (state_rank, -(score if isinstance(score, (int, float)) else -1))

    def industry_rank(item):
        industry = item["entry"].get("industry")
        try:
            return INDUSTRY_ORDER.index(industry)
        except ValueError:
            return len(INDUSTRY_ORDER)

    # Group by industry (controlled vocabulary order, unknown last), then by the
    # existing state/score ordering within each group.
    groups: dict = {}
    for item in ideas:
        groups.setdefault(item["entry"].get("industry"), []).append(item)

    out = []
    for industry in sorted(groups, key=lambda k: (INDUSTRY_ORDER.index(k) if k in INDUSTRY_ORDER else len(INDUSTRY_ORDER))):
        members = sorted(groups[industry], key=sort_key)
        label = industry_label(industry)
        out.append(
            f'<h3 class="industry-heading" id="industry-{esc_raw(industry or "unknown")}">'
            f'{esc_raw(label)} <span class="industry-count">{len(members)}</span></h3>'
        )
        out.append("\n".join(render_idea(item, experiments_by_id) for item in members))
    return "\n".join(out)


def render_experiments_table(experiments_index):
    experiments = experiments_index.get("experiments", []) or []
    if not experiments:
        return '<p class="unknown">No experiments recorded.</p>'
    out = ['<table class="grid"><thead><tr>'
           "<th>ID</th><th>Idea</th><th>Status</th><th>Approval</th>"
           "<th>Cost bound</th><th>Hypothesis</th><th>Decision rule</th></tr></thead><tbody>"]
    for exp in experiments:
        approval = exp.get("approval") or {}
        cost = exp.get("cost_bound") or {}
        cost_text = ", ".join(
            f"{k}={v}" for k, v in [
                ("GBP", cost.get("money_gbp")),
                ("hours", cost.get("human_hours")),
                ("days", cost.get("calendar_days")),
            ] if v is not None
        ) or None
        approval_text = f"required={approval.get('required')}, granted={approval.get('granted')}"
        out.append(
            "<tr>"
            f'<td><code>{esc_raw(exp.get("id"))}</code></td>'
            f'<td>{esc(exp.get("idea_id"))}</td>'
            f'<td>{esc(exp.get("status"))}</td>'
            f'<td>{esc_raw(approval_text)}</td>'
            f'<td>{esc(cost_text)}</td>'
            f'<td class="rationale">{esc(exp.get("hypothesis"))}</td>'
            f'<td class="rationale">{esc(exp.get("decision_rule"))}</td>'
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def render_intake(intake):
    """Render owner-nominated intake notes and their hypotheses."""
    if not intake:
        return '<p class="unknown">No intake notes recorded.</p>'
    out = []
    for note in intake:
        out.append(f'<details class="idea" id="intake-{esc_raw(os.path.basename(note["file"])[:-3])}">')
        out.append(
            "<summary>"
            f'<span class="idea-title">{esc_raw(note["title"])}</span>'
            f'<span class="tag">{len(note["hypotheses"])} hypotheses</span>'
            f'<span class="tag tag-industry">intake</span>'
            "</summary>"
        )
        out.append('<div class="idea-body">')
        out.append(f'<p class="hint"><code>{esc_raw(note["file"])}</code> - unvalidated discovery input; carries no score, evidence level or hard-filter result.</p>')
        if note["fields"]:
            out.append('<table class="kv">')
            for label, value in note["fields"]:
                out.append(f"<tr><th>{esc_raw(label)}</th><td>{esc(value)}</td></tr>")
            out.append("</table>")
        if note["hypotheses"]:
            for hypothesis in note["hypotheses"]:
                out.append(f'<h4>{esc_raw(hypothesis["heading"])}</h4>')
                body = hypothesis["body"].strip()
                if body:
                    out.append(f'<div class="md-body">{esc(body)}</div>')
        else:
            out.append('<p class="unknown">No hypothesis sections parsed from this note.</p>')
        out.append("</div></details>")
    return "\n".join(out)


def render_observations(pools):
    """Render observation pools: header metrics, observations, promotions and audit."""
    if not pools:
        return '<p class="unknown">No observation pools recorded.</p>'
    out = []
    for pool in pools:
        out.append(f'<details class="idea" id="pool-{esc_raw(pool["run_id"])}">')
        out.append(
            "<summary>"
            f'<span class="idea-title">{esc_raw(pool["run_id"])}</span>'
            f'<span class="tag">{len(pool["observations"])} observations</span>'
            f'<span class="tag tag-industry">pool</span>'
            "</summary>"
        )
        out.append('<div class="idea-body">')
        out.append(f'<p class="hint"><code>{esc_raw(pool["file"])}</code> - observations are not scored and confer no inherited positive evidence.</p>')
        if pool["fields"]:
            out.append('<table class="kv">')
            for label, value in pool["fields"]:
                out.append(f"<tr><th>{esc_raw(label)}</th><td>{esc(value)}</td></tr>")
            out.append("</table>")
        if pool["observations"]:
            headers = list(pool["observations"][0].keys())
            out.append('<table class="grid"><thead><tr>')
            for header in headers:
                out.append(f"<th>{esc_raw(header)}</th>")
            out.append("</tr></thead><tbody>")
            for row in pool["observations"]:
                out.append("<tr>")
                for header in headers:
                    cell = row.get(header, "")
                    cls = ' class="rationale"' if header.lower() in ("observation", "triage reason", "incumbent / free-alternative check") else ""
                    out.append(f"<td{cls}>{esc(cell)}</td>")
                out.append("</tr>")
            out.append("</tbody></table>")
        else:
            out.append('<p class="unknown">No observation rows parsed from this pool.</p>')
        if pool["promoted"]:
            out.append("<h4>Promoted observations</h4>")
            headers = list(pool["promoted"][0].keys())
            out.append('<table class="grid"><thead><tr>')
            for header in headers:
                out.append(f"<th>{esc_raw(header)}</th>")
            out.append("</tr></thead><tbody>")
            for row in pool["promoted"]:
                out.append("<tr>" + "".join(f"<td>{esc(row.get(h, ''))}</td>" for h in headers) + "</tr>")
            out.append("</tbody></table>")
        if pool["audit"]:
            out.append("<h4>Triage false-negative audit</h4>")
            out.append('<table class="kv">')
            for label, value in pool["audit"]:
                out.append(f"<tr><th>{esc_raw(label)}</th><td>{esc(value)}</td></tr>")
            out.append("</table>")
        out.append("</div></details>")
    return "\n".join(out)


def render_seeds_table(seeds_index):
    seeds = seeds_index.get("seeds", []) or []
    if not seeds:
        return '<p class="unknown">No seeds recorded.</p>'
    out = ['<table class="grid"><thead><tr>'
           "<th>Slug</th><th>Title</th><th>Origin idea</th><th>Status</th>"
           "<th>Observation</th></tr></thead><tbody>"]
    for seed in seeds:
        out.append(
            "<tr>"
            f'<td><code>{esc_raw(seed.get("slug") or seed.get("id"))}</code></td>'
            f'<td>{esc(seed.get("title"))}</td>'
            f'<td>{esc(seed.get("origin_idea"))}</td>'
            f'<td>{esc(seed.get("status"))}</td>'
            f'<td class="rationale">{esc(seed.get("observation"))}</td>'
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def render_runs_table(runs):
    if not runs:
        return '<p class="unknown">No runs recorded.</p>'
    out = ['<table class="grid"><thead><tr>'
           "<th>Run</th><th>Mode</th><th>Status</th><th>Method</th>"
           "<th>Cost</th><th>Tokens</th><th>Validation</th><th>Summary</th>"
           "</tr></thead><tbody>"]
    for run in reversed(runs):
        status = run.get("status")
        status_cls = {
            "success": "status-pass",
            "failed": "status-fail",
            "invalid-output": "status-fail",
            "over-budget": "status-fail",
        }.get(status, "status-unknown")
        summary = run.get("summary")
        summary_html = f'<code>{esc_raw(summary)}</code>' if summary else '<span class="unknown">none</span>'
        out.append(
            "<tr>"
            f'<td><code>{esc_raw(run.get("run_id"))}</code></td>'
            f'<td>{esc(run.get("mode"))}</td>'
            f'<td><span class="status {status_cls}">{esc(status)}</span></td>'
            f'<td>{esc(run.get("method_version"))}</td>'
            f'<td class="num">{fmt_money(run.get("cost_usd"))}</td>'
            f'<td class="num">{fmt_int(run.get("tokens_total"))}</td>'
            f'<td>{esc(run.get("validation"))}</td>'
            f'<td>{summary_html}</td>'
            "</tr>"
        )
    out.append("</tbody></table>")
    return "\n".join(out)


def render_run_stats(runs):
    if not runs:
        return '<p class="unknown">No runs recorded.</p>'
    costs = [r.get("cost_usd") for r in runs if isinstance(r.get("cost_usd"), (int, float))]
    tokens = [r.get("tokens_total") for r in runs if isinstance(r.get("tokens_total"), (int, float))]
    statuses = count_by(runs, "status")
    rows = [
        ("Runs", fmt_int(len(runs))),
        ("Total cost", fmt_money(sum(costs)) if costs else '<span class="unknown">unknown</span>'),
        ("Mean cost", fmt_money(sum(costs) / len(costs)) if costs else '<span class="unknown">unknown</span>'),
        ("Max cost", fmt_money(max(costs)) if costs else '<span class="unknown">unknown</span>'),
        ("Total tokens", fmt_int(sum(tokens)) if tokens else '<span class="unknown">unknown</span>'),
        ("Statuses", ", ".join(f"{k}={v}" for k, v in sorted(statuses.items())) or None),
    ]
    out = ['<table class="kv">']
    for label, value in rows:
        out.append(f"<tr><th>{esc_raw(label)}</th><td>{value}</td></tr>")
    out.append("</table>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Page
# --------------------------------------------------------------------------


CSS = """
:root {
  --bg: #0f1115;
  --panel: #171a21;
  --panel-2: #1e222b;
  --border: #2a2f3a;
  --text: #e6e9ef;
  --muted: #9aa3b2;
  --accent: #6ea8fe;
  --good: #4ade80;
  --warn: #fbbf24;
  --bad: #f87171;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}
header {
  padding: 28px 32px 20px;
  border-bottom: 1px solid var(--border);
  background: linear-gradient(180deg, #1a1e27, #12151b);
}
header h1 { margin: 0 0 6px; font-size: 24px; }
header .sub { color: var(--muted); font-size: 13px; }
main { padding: 24px 32px 64px; max-width: 1400px; margin: 0 auto; }
section { margin-bottom: 40px; }
h2 {
  font-size: 18px;
  margin: 0 0 16px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--border);
}
h3 { font-size: 15px; margin: 24px 0 10px; color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
h4 { font-size: 14px; margin: 18px 0 8px; color: var(--accent); }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 12px; }
.card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
}
.card-value { font-size: 24px; font-weight: 600; }
.card-label { color: var(--muted); font-size: 12px; margin-top: 4px; text-transform: uppercase; letter-spacing: .04em; }
.card-note { color: var(--muted); font-size: 12px; margin-top: 2px; }
.charts { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
.chart {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 14px 16px;
}
.chart h4 { margin-top: 0; color: var(--text); }
.bar-row { display: flex; align-items: center; gap: 8px; margin: 6px 0; font-size: 13px; }
.bar-label { width: 150px; color: var(--muted); flex: none; }
.bar-track { flex: 1; height: 10px; background: var(--panel-2); border-radius: 5px; overflow: hidden; }
.bar-fill { display: block; height: 100%; background: var(--accent); }
.bar-count { width: 32px; text-align: right; flex: none; }
.score-strip { background: var(--panel); border: 1px solid var(--border); border-radius: 10px; padding: 14px 16px; }
.score-row { display: flex; align-items: center; gap: 10px; margin: 7px 0; font-size: 13px; }
.score-name { width: 260px; flex: none; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.score-track { flex: 1; height: 12px; background: var(--panel-2); border-radius: 6px; position: relative; overflow: hidden; }
.score-fill { display: block; height: 100%; }
.score-high { background: var(--good); }
.score-mid { background: var(--warn); }
.score-low { background: var(--bad); }
.score-threshold { position: absolute; top: -2px; bottom: -2px; width: 2px; background: var(--text); opacity: .7; }
.score-value { width: 48px; text-align: right; flex: none; }
.hint { color: var(--muted); font-size: 12px; margin-top: 10px; }
table.grid { width: 100%; border-collapse: collapse; font-size: 13px; background: var(--panel); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; }
table.grid th, table.grid td { text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }
table.grid thead th { background: var(--panel-2); color: var(--muted); font-weight: 600; font-size: 12px; text-transform: uppercase; letter-spacing: .03em; }
table.grid tr:last-child td { border-bottom: none; }
table.kv { width: 100%; border-collapse: collapse; font-size: 13px; }
table.kv th { text-align: left; width: 190px; color: var(--muted); font-weight: 500; padding: 5px 10px 5px 0; vertical-align: top; }
table.kv td { padding: 5px 0; }
.num { text-align: right; font-variant-numeric: tabular-nums; }
.rationale { color: var(--muted); }
.evidence code, code { background: var(--panel-2); border: 1px solid var(--border); border-radius: 4px; padding: 1px 5px; font-size: 12px; }
.unknown { color: var(--muted); font-style: italic; }
.tag { display: inline-block; background: var(--panel-2); border: 1px solid var(--border); border-radius: 999px; padding: 1px 9px; font-size: 11px; margin-right: 4px; color: var(--muted); }
.tag-gating { border-color: var(--accent); color: var(--accent); }
.tag-industry { border-color: var(--accent); color: var(--accent); }
.industry-heading { margin: 22px 0 10px; font-size: 15px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); border-bottom: 1px solid var(--border); padding-bottom: 6px; }
.industry-count { display: inline-block; background: var(--panel-2); border: 1px solid var(--border); border-radius: 999px; padding: 0 8px; font-size: 11px; color: var(--muted); margin-left: 6px; }
.state-killed { border-color: var(--bad); color: var(--bad); }
.state-live { border-color: var(--good); color: var(--good); }
.status { display: inline-block; border-radius: 999px; padding: 1px 9px; font-size: 11px; border: 1px solid var(--border); }
.status-pass { border-color: var(--good); color: var(--good); }
.status-unknown { border-color: var(--warn); color: var(--warn); }
.status-fail { border-color: var(--bad); color: var(--bad); }
details.idea { background: var(--panel); border: 1px solid var(--border); border-radius: 10px; margin-bottom: 10px; }
details.idea > summary { cursor: pointer; padding: 12px 16px; display: flex; align-items: center; gap: 10px; list-style: none; }
details.idea > summary::-webkit-details-marker { display: none; }
details.idea > summary::before { content: "\\25B8"; color: var(--muted); margin-right: 4px; }
details.idea[open] > summary::before { content: "\\25BE"; }
.idea-title { flex: 1; font-weight: 600; }
.idea-score { font-variant-numeric: tabular-nums; font-weight: 600; }
.idea-body { padding: 4px 16px 18px; border-top: 1px solid var(--border); }
.md-body { white-space: pre-wrap; font-size: 13px; color: var(--text); background: var(--panel-2); border: 1px solid var(--border); border-radius: 8px; padding: 10px 12px; margin: 6px 0 14px; }
footer { color: var(--muted); font-size: 12px; padding: 0 32px 40px; max-width: 1400px; margin: 0 auto; }
"""


def build_html(ledger, root):
    ideas_index = ledger["ideas_index"]
    ideas = ledger["ideas"]
    experiments_index = ledger["experiments_index"]
    seeds_index = ledger["seeds_index"]
    runs = ledger["runs"]

    experiments_by_id = {}
    for exp in experiments_index.get("experiments", []) or []:
        if exp.get("id"):
            experiments_by_id[exp["id"]] = exp

    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    method_version = ideas_index.get("method_version", "unknown")
    updated = ideas_index.get("updated", "unknown")

    parts = []
    parts.append("<!DOCTYPE html>")
    parts.append('<html lang="en"><head><meta charset="utf-8">')
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    parts.append("<title>business-idea-lab dashboard</title>")
    parts.append(f"<style>{CSS}</style>")
    parts.append("</head><body>")
    parts.append("<header>")
    parts.append("<h1>business-idea-lab dashboard</h1>")
    parts.append(
        f'<div class="sub">Method {esc_raw(method_version)} &middot; ledger updated {esc_raw(updated)} '
        f"&middot; generated {esc_raw(generated)} &middot; threshold {THRESHOLD}</div>"
    )
    parts.append("</header>")
    parts.append("<main>")

    parts.append('<section id="overview"><h2>Overview</h2>')
    parts.append(render_stat_cards(ideas_index, ideas, experiments_index, seeds_index, runs))
    parts.append("</section>")

    parts.append('<section id="portfolio"><h2>Portfolio statistics</h2>')
    parts.append(render_portfolio(ideas_index, ideas, experiments_index, seeds_index, runs))
    parts.append("</section>")

    parts.append('<section id="scores"><h2>Score distribution</h2>')
    parts.append(render_score_distribution(ideas))
    parts.append("</section>")

    parts.append('<section id="ideas"><h2>Ideas</h2>')
    parts.append('<p class="hint">Ideas are grouped by industry, then ordered by lifecycle state and score. Expand an idea to see its why-now, fingerprint, all ten scorecard dimensions, all nine hard filters, vetoes, review history and experiment.</p>')
    parts.append(render_ideas(ideas, experiments_by_id))
    parts.append("</section>")

    parts.append('<section id="experiments"><h2>Experiments</h2>')
    parts.append(render_experiments_table(experiments_index))
    parts.append("</section>")

    parts.append('<section id="intake"><h2>Intake (owner-nominated hypotheses)</h2>')
    parts.append('<p class="hint">Unvalidated discovery inputs. These carry no score, evidence level or hard-filter result, and are shown so early hypotheses stay visible even when they never become candidates.</p>')
    parts.append(render_intake(ledger.get("intake") or []))
    parts.append("</section>")

    parts.append('<section id="observations"><h2>Observation pools</h2>')
    parts.append('<p class="hint">Every observation swept in a funnel run, with its triage decision and reason. Observations are not scored; a rejection here is the record of why an idea was dropped early.</p>')
    parts.append(render_observations(ledger.get("observations") or []))
    parts.append("</section>")

    parts.append('<section id="seeds"><h2>Seeds</h2>')
    parts.append(render_seeds_table(seeds_index))
    parts.append("</section>")

    parts.append('<section id="runs"><h2>Runs</h2>')
    parts.append(render_run_stats(runs))
    parts.append(render_runs_table(runs))
    parts.append("</section>")

    parts.append("</main>")
    parts.append(
        '<footer>Generated by <code>scripts/build_dashboard.py</code> from the machine-readable ledgers. '
        "It renders only what the ledgers contain; missing values are shown as unknown. "
        "Scores are desk-research scores, not market validation.</footer>"
    )
    parts.append("</body></html>")
    return "\n".join(parts)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the idea-ledger HTML dashboard.")
    parser.add_argument("--root", default=None, help="repository root (default: parent of scripts/)")
    parser.add_argument("--out", default=None, help="output HTML path (default: <root>/dashboard.html)")
    parser.add_argument("--quiet", action="store_true", help="suppress the summary line")
    args = parser.parse_args(argv)

    root = os.path.abspath(args.root) if args.root else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_path = os.path.abspath(args.out) if args.out else os.path.join(root, "dashboard.html")

    ledger = load_ledger(root)
    document = build_html(ledger, root)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(document)

    if not args.quiet:
        ideas = ledger["ideas"]
        runs = ledger["runs"]
        print(
            f"dashboard: wrote {out_path} "
            f"({len(ideas)} ideas, {len(ledger['experiments_index'].get('experiments', []) or [])} experiments, "
            f"{len(ledger.get('intake') or [])} intake notes, "
            f"{len(ledger.get('observations') or [])} observation pools, "
            f"{len(ledger['seeds_index'].get('seeds', []) or [])} seeds, {len(runs)} runs)"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
