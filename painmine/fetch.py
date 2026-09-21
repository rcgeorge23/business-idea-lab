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


def http_get_json(
    url: str, budget: Budget, headers: dict[str, str] | None = None
) -> tuple[Any | None, dict]:
    """GET a public JSON document. Returns (data, status) and never raises."""
    if not budget.can_fetch():
        return None, {"ok": False, "url": url, "error": f"budget stopped: {budget.stop_reason or 'limit reached'}"}
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        merged.update(headers)
    request = urllib.request.Request(url, headers=merged)
    budget.sleep_between_requests()
    try:
        budget.record_request()
    except BudgetExceeded as exc:
        return None, {"ok": False, "url": url, "error": str(exc)}
    try:
        with urllib.request.urlopen(request, timeout=budget.request_timeout) as response:
            raw = response.read().decode("utf-8", "replace")
            status_code = response.status
    except urllib.error.HTTPError as exc:
        body = ""
        try:
            body = exc.read().decode("utf-8", "replace")[:300]
        except Exception:  # pragma: no cover - defensive
            pass
        return None, {
            "ok": False,
            "url": url,
            "http_status": exc.code,
            "error": f"HTTP {exc.code}",
            "body_excerpt": body,
        }
    except Exception as exc:  # noqa: BLE001 - access failures must be recorded, not raised
        return None, {"ok": False, "url": url, "error": f"{type(exc).__name__}: {exc}"}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, {"ok": False, "url": url, "http_status": status_code, "error": f"invalid JSON: {exc}"}
    return data, {"ok": True, "url": url, "http_status": status_code, "bytes": len(raw)}


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


def fetch_stack_exchange(query: str, cap: int, budget: Budget) -> tuple[list[dict], dict]:
    url = (
        "https://api.stackexchange.com/2.3/search/excerpts?"
        + urllib.parse.urlencode(
            {
                "order": "desc",
                "sort": "relevance",
                "q": query,
                "site": "stackoverflow",
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
        link = hit.get("link") or (
            f"https://stackoverflow.com/q/{hit.get('question_id')}"
        )
        items.append(
            _raw_item(
                "stack_exchange",
                f"se:{hit.get('question_id')}:{kind}:{item_id}",
                link,
                hit.get("title") or "",
                text,
                hit.get("owner", {}).get("display_name") if isinstance(hit.get("owner"), dict) else None,
                hit.get("creation_date"),
                hit.get("score") or 0,
                {"tags": hit.get("tags", []), "is_answered": hit.get("is_answered")},
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


COLLECTORS = {
    "hn_algolia": fetch_hn,
    "stack_exchange": fetch_stack_exchange,
    "github_issues": fetch_github,
    "reddit_public_json": fetch_reddit,
}


def load_fixture_items(path: str) -> list[dict]:
    """Offline fixture items for tests/demos. Fixtures are never evidence.

    Returns every row unfiltered: extraction is responsible for rejecting empty
    or cue-free items, and tests assert those reject reasons.
    """
    return read_jsonl(path)


def collect(
    queries: list[str],
    source_ids: list[str],
    budget: Budget,
    state=None,
    per_source_cap: int | None = None,
) -> tuple[list[dict], list[dict]]:
    """Collect from each source for each query within the budget.

    Returns (items, statuses). Unknown source ids are recorded as failures.
    """
    items: list[dict] = []
    statuses: list[dict] = []
    per_source_cap = per_source_cap or budget.max_items_per_source
    counts_by_source: dict[str, int] = {}
    for source_id in source_ids:
        collector = COLLECTORS.get(source_id)
        if collector is None:
            statuses.append(
                {"source_id": source_id, "ok": False, "error": "collector not implemented", "items": 0}
            )
            continue
        for query in queries:
            if budget.stopped:
                statuses.append(
                    {
                        "source_id": source_id,
                        "query": query,
                        "ok": False,
                        "error": f"budget stopped: {budget.stop_reason}",
                        "items": 0,
                    }
                )
                continue
            if counts_by_source.get(source_id, 0) >= per_source_cap:
                statuses.append(
                    {
                        "source_id": source_id,
                        "query": query,
                        "ok": False,
                        "error": "per-source item cap reached",
                        "items": 0,
                    }
                )
                continue
            remaining = min(per_source_cap - counts_by_source.get(source_id, 0), budget.max_items_total - budget.items)
            if remaining <= 0:
                budget.stop("item cap reached")
                continue
            fetched, status = collector(query, remaining, budget)
            statuses.append(status)
            fresh = state.filter_new(fetched) if state is not None else fetched
            if state is not None:
                state.mark_seen(fetched)
            kept = fresh[:remaining]
            counts_by_source[source_id] = counts_by_source.get(source_id, 0) + len(kept)
            budget.record_items(len(kept))
            items.extend(kept)
    return items, statuses


def summarise_statuses(statuses: list[dict]) -> dict:
    """Compact per-source summary for the run report (Part 10)."""
    by_source: dict[str, dict] = {}
    for status in statuses:
        sid = status.get("source_id", "unknown")
        entry = by_source.setdefault(
            sid, {"requests": 0, "ok_requests": 0, "failed_requests": 0, "items": 0, "errors": []}
        )
        entry["requests"] += 1
        if status.get("ok"):
            entry["ok_requests"] += 1
        else:
            entry["failed_requests"] += 1
            err = status.get("error") or "unknown error"
            if err not in entry["errors"]:
                entry["errors"].append(err)
        entry["items"] += int(status.get("items") or 0)
    return by_source
