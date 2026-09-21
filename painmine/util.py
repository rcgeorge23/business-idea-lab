"""Shared stdlib-only helpers for the painmine spike (issue #9)."""
from __future__ import annotations

import hashlib
import html
import json
import os
import re
import unicodedata
from datetime import datetime, timezone
from typing import Any, Iterable

ISO = "%Y-%m-%dT%H:%M:%SZ"

# Words with low discriminating power for pain-statement clustering/dedup.
# Deliberately excludes pain cues like "still", "manually", "hours".
STOPWORDS = {
    "a", "about", "after", "again", "all", "also", "am", "an", "and", "any",
    "are", "as", "at", "be", "because", "been", "before", "being", "but",
    "by", "can", "could", "did", "do", "does", "doing", "done", "for",
    "from", "get", "got", "had", "has", "have", "he", "her", "here", "him",
    "his", "how", "i", "if", "in", "into", "is", "it", "its", "just", "like",
    "me", "more", "most", "much", "my", "no", "not", "now", "of", "on",
    "one", "only", "or", "other", "our", "out", "over", "own", "same",
    "she", "should", "so", "some", "such", "than", "that", "the", "their",
    "them", "then", "there", "these", "they", "this", "those", "to", "too",
    "up", "us", "very", "was", "we", "were", "what", "when", "where",
    "which", "while", "who", "why", "will", "with", "would", "you", "your",
}


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def utcnow_iso() -> str:
    return utcnow().strftime(ISO)


def sha1_hex(text: str, length: int = 40) -> str:
    return hashlib.sha1((text or "").encode("utf-8", "replace")).hexdigest()[:length]


def slugify(text: str, maxlen: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:maxlen] or "x"


_TAG_RE = re.compile(r"<[^>]+>")


def strip_html(text: str) -> str:
    if not text:
        return ""
    text = _TAG_RE.sub(" ", str(text))
    text = html.unescape(text)
    # Markdown code fences / links degrade gracefully.
    text = re.sub(r"```[^`]*```", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def truncate(text: str, limit: int) -> str:
    text = text or ""
    if len(text) <= limit:
        return text
    return text[: max(1, limit - 1)].rstrip() + "\u2026"


def normalize_text(text: str) -> str:
    text = strip_html(text or "").lower()
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    return [t for t in normalize_text(text).split() if t not in STOPWORDS and len(t) > 1]


def shingles(tokens: Iterable[str], k: int = 5) -> set[str]:
    toks = list(tokens)
    if not toks:
        return set()
    if len(toks) < k:
        return {" ".join(toks)}
    return {" ".join(toks[i : i + k]) for i in range(len(toks) - k + 1)}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def read_json(path: str, default: Any = None) -> Any:
    if not os.path.exists(path):
        return default
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path: str, obj: Any) -> None:
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2, ensure_ascii=False, sort_keys=False)
        fh.write("\n")


def read_jsonl(path: str) -> list[dict]:
    rows: list[dict] = []
    if not os.path.exists(path):
        return rows
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: str, rows: Iterable[dict]) -> None:
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_jsonl(path: str, rows: Iterable[dict]) -> None:
    parent = os.path.dirname(os.path.abspath(path))
    os.makedirs(parent, exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def parse_date(value: Any) -> str | None:
    """Best-effort ISO-8601 UTC date parsing. Returns None when unknown."""
    if value in (None, "", 0):
        return None
    if isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(float(value), tz=timezone.utc).strftime(ISO)
        except (OverflowError, OSError, ValueError):
            return None
    text = str(value).strip()
    if not text:
        return None
    text = text.replace("Z", "+00:00")
    candidates = [text, text[:10], text[:19]]
    for cand in candidates:
        for fmt in (
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%dT%H:%M:%S",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d",
            "%Y/%m/%d",
        ):
            try:
                dt = datetime.strptime(cand, fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt.astimezone(timezone.utc).strftime(ISO)
            except ValueError:
                continue
    return None


def days_since(iso_date: str | None) -> int | None:
    if not iso_date:
        return None
    try:
        dt = datetime.strptime(iso_date.replace("Z", "+00:00"), "%Y-%m-%dT%H:%M:%S%z")
    except ValueError:
        try:
            dt = datetime.strptime(iso_date[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    return max(0, (utcnow() - dt).days)


def sentences(text: str) -> list[str]:
    cleaned = strip_html(text)
    parts = re.split(r"(?<=[.!?])\s+|\n+", cleaned)
    return [p.strip() for p in parts if p.strip()]


def first_sentence_containing(text: str, pattern: re.Pattern[str]) -> str | None:
    for sentence in sentences(text):
        if pattern.search(sentence):
            return sentence
    return None


def domain_of(url: str) -> str:
    match = re.match(r"https?://([^/]+)/?", url or "")
    if not match:
        return ""
    return match.group(1).lower().removeprefix("www.")


def load_limits(path: str) -> dict:
    return read_json(path, {}) or {}
