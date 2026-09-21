"""Bounded public-source collectors (issue #9 Parts 2, 7 and 8).

Rules honoured here:
- Only documented, publicly accessible endpoints; no paid keys, no
  anti-bot bypass, no paywall circumvention. GitHub search optionally uses the
  repository's own automatically issued `GITHUB_TOKEN` (documented API
  authentication for higher rate limits, not an access-control bypass).
- Every network request is metered through ``Budget``; on any failure the
  collector records an honest access-failure status and returns no items.
- Collectors never raise for HTTP/transport errors.
"""
from __future__ import annotations

import json
import os
import socket
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from .budget import Budget, BudgetExceeded
from .util import read_jsonl, strip_html, truncate

USER_AGENT = (
    "business-idea-lab-painmine-spike/0.1 "
    "(+https://github.com/rcgeorge23/business-idea-lab; research; no auth)"
)

ENABLED_SOURCES = ("hn_algolia", "stack_exchange", "github_issues", "reddit_public_json")


RETRYABLE_HTTP_STATUS = (429, 500, 502, 503, 504)


def _retryable_exception(exc: Exception) -> bool:
    """Transient transport failures only; never retry programming errors."""
    return isinstance(exc, (urllib.error.URLError, TimeoutError, socket.timeout, ConnectionError))


def _error_kind(exc: Exception) -> str:
    if isinstance(exc, (TimeoutError, socket.timeout)):
        return "timeout"
    return "transport_error"


def http_get_json(
    url: str, budget: Budget, headers: dict[str, str] | None = None
) -> tuple[Any | None, dict]:
    """GET a public JSON document. Returns (data, status) and never raises.

    Every actual network request is metered through ``Budget``. Transient
    failures (timeouts, transport errors, HTTP 429/5xx) are retried up to
    ``budget.max_retries`` times; each retry is metered and counted separately.
    Status counters are explicit so reports can reconcile: ``http_requests``
    (attempts made), ``http_responses`` (responses received, including HTTP
    error responses), ``retries``, ``attempted`` and ``error_kind``.
    """
    if not budget.can_fetch():
        return None, {
            "ok": False,
            "url": url,
            "error": f"budget stopped: {budget.stop_reason or 'limit reached'}",
            "error_kind": "budget_prevented",
            "attempted": False,
            "http_requests": 0,
            "http_responses": 0,
            "retries": 0,
        }
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        merged.update(headers)
    request = urllib.request.Request(url, headers=merged)
    max_attempts = 1 + max(0, budget.max_retries)
    http_requests = 0
    http_responses = 0
    retries = 0
    last_status: dict = {}
    for attempt in range(max_attempts):
        budget.sleep_between_requests()
        try:
            budget.record_request()
        except BudgetExceeded as exc:
            return None, {
                "ok": False,
                "url": url,
                "error": str(exc),
                "error_kind": "budget_prevented",
                "attempted": http_requests > 0,
                "http_requests": http_requests,
                "http_responses": http_responses,
                "retries": retries,
            }
        http_requests += 1
        try:
            with urllib.request.urlopen(request, timeout=budget.request_timeout) as response:
                raw = response.read().decode("utf-8", "replace")
                status_code = response.status
            http_responses += 1
            budget.record_response()
        except urllib.error.HTTPError as exc:
            http_responses += 1
            budget.record_response()
            body = ""
            try:
                body = exc.read().decode("utf-8", "replace")[:300]
            except Exception:  # pragma: no cover - defensive
                pass
            last_status = {
                "ok": False,
                "url": url,
                "http_status": exc.code,
                "error": f"HTTP {exc.code}",
                "error_kind": "http_error",
                "body_excerpt": body,
                "attempted": True,
                "http_requests": http_requests,
                "http_responses": http_responses,
                "retries": retries,
            }
            if exc.code in RETRYABLE_HTTP_STATUS and attempt + 1 < max_attempts and budget.can_fetch():
                retries += 1
                budget.record_retry()
                continue
            return None, last_status
        except Exception as exc:  # noqa: BLE001 - access failures must be recorded, not raised
            last_status = {
                "ok": False,
                "url": url,
                "error": f"{type(exc).__name__}: {exc}",
                "error_kind": _error_kind(exc),
                "attempted": True,
                "http_requests": http_requests,
                "http_responses": http_responses,
                "retries": retries,
            }
            if _retryable_exception(exc) and attempt + 1 < max_attempts and budget.can_fetch():
                retries += 1
                budget.record_retry()
                continue
            return None, last_status
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            return None, {
                "ok": False,
                "url": url,
                "http_status": status_code,
                "error": f"invalid JSON: {exc}",
                "error_kind": "invalid_json",
                "attempted": True,
                "http_requests": http_requests,
                "http_responses": http_responses,
                "retries": retries,
            }
        return data, {
            "ok": True,
            "url": url,
            "http_status": status_code,
            "bytes": len(raw),
            "error_kind": None,
            "attempted": True,
            "http_requests": http_requests,
            "http_responses": http_responses,
            "retries": retries,
        }
    return None, last_status


def _raw_item(
    source_type: str,
    source_id: str,
    url: str,
    title: str,
    text: str,
    author: str | None,
    published_at: str | None,
    engagement: int = 0,
    extra: dict | None = None,
) -> dict:
    return {
        "source_type": source_type,
        "source_id": source_id,
        "url": url,
        "title": strip_html(title or ""),
        "text": strip_html(text or ""),
        "author": author,
        "published_at": published_at,
        "engagement": int(engagement or 0),
        "extra": extra or {},
    }


def fetch_hn(query: str, cap: int, budget: Budget) -> tuple[list[dict], dict]:
    url = (
        "https://hn.algolia.com/api/v1/search?"
        + urllib.parse.urlencode(
            {
                "query": query,
                "tags": "comment",
                "hitsPerPage": min(25, cap),
                "restrictSearchableAttributes": "comment_text",
            }
        )
    )
    data, status = http_get_json(url, budget)
    status["source_id"] = "hn_algolia"
    status["query"] = query
    items: list[dict] = []
    if not status.get("ok") or not isinstance(data, dict):
        status["items"] = 0
        return items, status
    for hit in data.get("hits", []):
        text = hit.get("comment_text") or ""
        if not text.strip():
            continue
        object_id = str(hit.get("objectID") or "")
        items.append(
            _raw_item(
                "hn_algolia",
                f"hn:{object_id}",
                f"https://news.ycombinator.com/item?id={object_id}",
                hit.get("story_title") or "",
                text,
                hit.get("author"),
                hit.get("created_at"),
                hit.get("points") or 0,
                {"story_id": hit.get("story_id"), "story_title": hit.get("story_title")},
            )
        )
    status["items"] = len(items)
    return items, status


SE_DEFAULT_SITE = "stackoverflow"


def _se_site_base(site: str) -> str:
    """Canonical web base for a Stack Exchange site id (used only as a fallback)."""
    if site in ("stackoverflow", "superuser", "serverfault"):
        return f"https://{site}.com"
    return f"https://{site}.stackexchange.com"


def fetch_stack_exchange(
    query: str, cap: int, budget: Budget, site: str = SE_DEFAULT_SITE
) -> tuple[list[dict], dict]:
    """Public API v2.3 search across one Stack Exchange site (no auth, read-only).

    ``site`` comes from the source options in ``sources.json`` so a run can
    rotate across the network (Stack Overflow, Web Applications, Money, ...)
    without extra requests. Item ids include the site because question ids are
    only unique within a site.
    """
    url = (
        "https://api.stackexchange.com/2.3/search/excerpts?"
        + urllib.parse.urlencode(
            {
                "order": "desc",
                "sort": "relevance",
                "q": query,
                "site": site,
                "pagesize": min(25, cap),
                "filter": "withbody",
            }
        )
    )
    # No Accept-Encoding override: urllib does not auto-decompress, and the SE
    # API returns plain JSON when the client does not request compression.
    data, status = http_get_json(url, budget)
    status["source_id"] = "stack_exchange"
    status["query"] = query
    status["site"] = site
    items: list[dict] = []
    if not status.get("ok") or not isinstance(data, dict):
        # Note: urllib does not auto-decompress gzip; retry without the header.
        status["items"] = 0
        return items, status
    for hit in data.get("items", []):
        text = strip_html(hit.get("body") or hit.get("excerpt") or "")
        if not text.strip():
            continue
        item_id = hit.get("answer_id") or hit.get("question_id")
        kind = "answer" if hit.get("answer_id") else "question"
        link = hit.get("link") or f"{_se_site_base(site)}/q/{hit.get('question_id')}"
        items.append(
            _raw_item(
                "stack_exchange",
                f"se:{site}:{hit.get('question_id')}:{kind}:{item_id}",
                link,
                hit.get("title") or "",
                text,
                hit.get("owner", {}).get("display_name") if isinstance(hit.get("owner"), dict) else None,
                hit.get("creation_date"),
                hit.get("score") or 0,
                {"tags": hit.get("tags", []), "is_answered": hit.get("is_answered"), "site": site},
            )
        )
    status["items"] = len(items)
    return items, status


def fetch_github(query: str, cap: int, budget: Budget) -> tuple[list[dict], dict]:
    url = (
        "https://api.github.com/search/issues?"
        + urllib.parse.urlencode(
            {
                "q": f"{query} in:body",
                "per_page": min(20, cap),
                "sort": "created",
                "order": "desc",
            }
        )
    )
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data, status = http_get_json(
        url, budget, headers=headers
    )
    status["source_id"] = "github_issues"
    status["query"] = query
    items: list[dict] = []
    if not status.get("ok") or not isinstance(data, dict):
        status["items"] = 0
        return items, status
    for issue in data.get("items", []):
        body = issue.get("body") or ""
        if not body.strip():
            continue
        repo = (issue.get("repository_url") or "").replace("https://api.github.com/repos/", "")
        number = issue.get("number")
        author = (issue.get("user") or {}).get("login")
        items.append(
            _raw_item(
                "github_issues",
                f"gh:{repo}#{number}",
                issue.get("html_url") or "",
                issue.get("title") or "",
                body,
                author,
                issue.get("created_at"),
                issue.get("comments") or 0,
                {"repo": repo, "labels": [lbl.get("name") for lbl in issue.get("labels", [])]},
            )
        )
    status["items"] = len(items)
    return items, status


def fetch_reddit(query: str, cap: int, budget: Budget) -> tuple[list[dict], dict]:
    url = (
        "https://www.reddit.com/search.json?"
        + urllib.parse.urlencode({"q": query, "limit": min(25, cap), "sort": "relevance", "raw_json": 1})
    )
    data, status = http_get_json(url, budget)
    status["source_id"] = "reddit_public_json"
    status["query"] = query
    items: list[dict] = []
    if not status.get("ok") or not isinstance(data, dict):
        status["items"] = 0
        return items, status
    children = ((data.get("data") or {}).get("children")) or []
    for child in children:
        post = child.get("data") or {}
        text = f"{post.get('title') or ''} {post.get('selftext') or ''}"
        if not text.strip():
            continue
        items.append(
            _raw_item(
                "reddit_public_json",
                f"reddit:{post.get('id')}",
                "https://www.reddit.com" + (post.get("permalink") or ""),
                post.get("title") or "",
                text,
                post.get("author"),
                post.get("created_utc"),
                post.get("score") or 0,
                {"subreddit": post.get("subreddit")},
            )
        )
    status["items"] = len(items)
    return items, status


DISCOURSE_DEFAULT_SITE = "discuss.python.org"


def fetch_discourse(
    query: str, cap: int, budget: Budget, site: str = DISCOURSE_DEFAULT_SITE
) -> tuple[list[dict], dict]:
    """Public Discourse search (buyer-side communities, no auth).

    Discourse instances expose a public ``/search.json`` endpoint. Only public
    read access is used: no authentication, no private endpoints. The class is
    disabled in sources.json until the owner has checked each site's terms and
    robots policy.
    """
    url = f"https://{site}/search.json?" + urllib.parse.urlencode({"q": query, "page": 1})
    data, status = http_get_json(url, budget)
    status["source_id"] = "discourse_public_json"
    status["query"] = query
    status["site"] = site
    items: list[dict] = []
    if not status.get("ok") or not isinstance(data, dict):
        status["items"] = 0
        return items, status
    topics = {t.get("id"): t for t in (data.get("topics") or []) if isinstance(t, dict)}
    for post in data.get("posts") or []:
        if not isinstance(post, dict):
            continue
        topic = topics.get(post.get("topic_id")) or {}
        title = topic.get("title") or post.get("topic_title") or ""
        text = post.get("blurb") or post.get("cooked") or ""
        if not str(text).strip():
            continue
        topic_id = post.get("topic_id")
        post_number = post.get("post_number") or post.get("id")
        items.append(
            _raw_item(
                "discourse_public_json",
                f"discourse:{site}:{topic_id}:{post_number}",
                f"https://{site}/t/{topic.get('slug') or 'topic'}/{topic_id}/{post_number}",
                title,
                text,
                post.get("username"),
                post.get("created_at"),
                post.get("reply_count") or 0,
                {"site": site, "topic_id": topic_id},
            )
        )
        if len(items) >= cap:
            break
    status["items"] = len(items)
    return items, status


COLLECTORS = {
    "hn_algolia": fetch_hn,
    "stack_exchange": fetch_stack_exchange,
    "github_issues": fetch_github,
    "reddit_public_json": fetch_reddit,
    "discourse_public_json": fetch_discourse,
}


def load_fixture_items(path: str) -> list[dict]:
    """Offline fixture items for tests/demos. Fixtures are never evidence.

    Returns every row unfiltered: extraction is responsible for rejecting empty
    or cue-free items, and tests assert those reject reasons.
    """
    return read_jsonl(path)


def _attempt_kwargs(source_id: str, options: dict, index: int) -> dict:
    """Per-attempt collector options, e.g. Stack Exchange site rotation.

    Rotating by query position spreads a family across the network without
    spending extra HTTP requests: attempt i uses sites[i % len(sites)].
    """
    if source_id == "stack_exchange":
        sites = options.get("sites") or []
        if sites:
            return {"site": sites[index % len(sites)]}
    return {}


def collect(
    queries: list[str],
    source_ids: list[str],
    budget: Budget,
    state=None,
    per_source_cap: int | None = None,
    source_options: dict[str, dict] | None = None,
) -> tuple[list[dict], list[dict]]:
    """Collect from each source for each query within the budget.

    ``source_options`` maps a source id to its configured options (see
    ``sources.json``); only options with an implemented meaning are used.
    Returns (items, statuses). Unknown source ids are recorded as failures.
    """
    items: list[dict] = []
    statuses: list[dict] = []
    per_source_cap = per_source_cap or budget.max_items_per_source
    source_options = source_options or {}
    counts_by_source: dict[str, int] = {}
    for source_id in source_ids:
        collector = COLLECTORS.get(source_id)
        if collector is None:
            statuses.append(
                {
                    "source_id": source_id,
                    "ok": False,
                    "error": "collector not implemented",
                    "error_kind": "collector_missing",
                    "attempted": False,
                    "http_requests": 0,
                    "http_responses": 0,
                    "retries": 0,
                    "items_returned": 0,
                    "items_accepted": 0,
                }
            )
            continue
        options = source_options.get(source_id) or {}
        for index, query in enumerate(queries):
            base = {
                "source_id": source_id,
                "query": query,
                "attempted": False,
                "http_requests": 0,
                "http_responses": 0,
                "retries": 0,
                "items_returned": 0,
                "items_accepted": 0,
            }
            if budget.stopped:
                base.update(
                    {
                        "ok": False,
                        "error": f"budget stopped: {budget.stop_reason}",
                        "error_kind": "budget_prevented",
                    }
                )
                statuses.append(base)
                continue
            if counts_by_source.get(source_id, 0) >= per_source_cap:
                base.update(
                    {"ok": False, "error": "per-source item cap reached", "error_kind": "per_source_item_cap"}
                )
                statuses.append(base)
                continue
            remaining = min(per_source_cap - counts_by_source.get(source_id, 0), budget.max_items_total - budget.items)
            if remaining <= 0:
                budget.stop("item cap reached")
                base.update({"ok": False, "error": "item cap reached", "error_kind": "item_cap"})
                statuses.append(base)
                continue
            fetched, status = collector(query, remaining, budget, **_attempt_kwargs(source_id, options, index))
            status.setdefault("source_id", source_id)
            status.setdefault("query", query)
            status.setdefault("attempted", True)
            status["items_returned"] = len(fetched)
            status["items"] = len(fetched)
            fresh = state.filter_new(fetched) if state is not None else fetched
            if state is not None:
                state.mark_seen(fetched)
            kept = fresh[:remaining]
            status["items_accepted"] = len(kept)
            statuses.append(status)
            counts_by_source[source_id] = counts_by_source.get(source_id, 0) + len(kept)
            budget.record_items(len(kept))
            items.extend(kept)
    return items, statuses


def _empty_source_summary() -> dict:
    return {
        "queries_attempted": 0,
        "queries_skipped": 0,
        "http_requests_initiated": 0,
        "http_responses_received": 0,
        "retries": 0,
        "items_returned": 0,
        "items_accepted": 0,
        "per_source_item_cap_reached": 0,
        "total_item_cap_reached": 0,
        "requests_prevented_budget": 0,
        "source_access_failures": 0,
        "errors": [],
    }


def summarise_statuses(statuses: list[dict]) -> dict:
    """Per-source ledger with distinct, reconcilable counters (issue #13).

    Distinguishes a source attempt, a query attempt, an HTTP request, an HTTP
    response, a retry, an item returned, an item accepted, an item cap, a
    request prevented by budget exhaustion and a source access failure. Item
    caps and budget stops are never counted as HTTP failures.
    """
    by_source: dict[str, dict] = {}
    for status in statuses:
        sid = status.get("source_id", "unknown")
        entry = by_source.setdefault(sid, _empty_source_summary())
        attempted = bool(status.get("attempted"))
        if attempted:
            entry["queries_attempted"] += 1
        else:
            entry["queries_skipped"] += 1
        entry["http_requests_initiated"] += int(status.get("http_requests") or 0)
        entry["http_responses_received"] += int(status.get("http_responses") or 0)
        entry["retries"] += int(status.get("retries") or 0)
        entry["items_returned"] += int(status.get("items_returned") or 0)
        entry["items_accepted"] += int(status.get("items_accepted") or 0)
        kind = status.get("error_kind")
        if kind == "per_source_item_cap":
            entry["per_source_item_cap_reached"] += 1
        elif kind == "item_cap":
            entry["total_item_cap_reached"] += 1
        elif kind == "budget_prevented":
            entry["requests_prevented_budget"] += 1
        elif not status.get("ok"):
            entry["source_access_failures"] += 1
        err = status.get("error")
        if err and err not in entry["errors"]:
            entry["errors"].append(err)
    return by_source


def build_ledger(statuses: list[dict], budget: Budget) -> dict:
    """Run-level ledger with totals and reconciliation against Budget (issue #13)."""
    sources = summarise_statuses(statuses)
    totals = _empty_source_summary()
    for entry in sources.values():
        for key in totals:
            if key == "errors":
                totals["errors"].extend(err for err in entry["errors"] if err not in totals["errors"])
            else:
                totals[key] += entry[key]
    reconciliation = {
        "http_requests_match_budget": totals["http_requests_initiated"] == budget.requests,
        "http_responses_within_requests": totals["http_responses_received"] <= totals["http_requests_initiated"],
        "items_accepted_match_budget": totals["items_accepted"] == budget.items,
        "items_returned_ge_accepted": totals["items_returned"] >= totals["items_accepted"],
        "hard_request_cap_respected": budget.requests <= budget.max_requests,
        "hard_item_cap_respected": budget.items <= budget.max_items_total,
        "budget_requests_used": budget.requests,
        "budget_items_collected": budget.items,
    }
    return {"sources": sources, "totals": totals, "reconciliation": reconciliation}
