"""Deterministic pain-signal extraction (issue #9 Part 3, step 2).

Preference order from the issue: deterministic/query-based retrieval first,
then cheap model OR deterministic extraction. This module is the deterministic
extractor: cue regexes, named-system lexicon, role/industry inference, bounded
confidence. It labels every signal with its provenance so an auditor can see
exactly which patterns fired. An LLM extractor exists in ``llm.py`` behind an
explicit spend gate and is never used automatically.
"""
from __future__ import annotations

import re
from typing import Any

from .schema import make_signal
from .util import (
    first_sentence_containing,
    strip_html,
    truncate,
    utcnow_iso,
)

EXTRACTOR_VERSION = "0.1.0"

CUE_GROUPS: dict[str, list[str]] = {
    "manual": [
        r"\bmanual(ly)?\b",
        r"\bby hand\b",
        r"\bstill (do|does|doing|use|using|rely|copy|paste|type|enter)\b",
        r"\bhand[- ]?enter\w*\b",
        r"\bcopy[- ]?(and[- ])?paste\b",
        r"\bre-?key(ing|ed|s)?\b",
        r"\bre-?type\b",
        r"\bdouble[- ]?entry\b",
        r"\bdata entry\b",
    ],
    "workaround": [
        r"\bwork[- ]?around\b",
        r"\bwe use (excel|a spreadsheet|google sheets|airtable|notion)\b",
        r"\bspreadsheet(s)?\b",
        r"\bexport\w* .{0,40}\b(import|into|csv)\b",
        r"\b(copy|paste|move|transfer)\w* .{0,30}\b(into|from|between)\b",
        r"\bwe'?ve (built|made) (a|our own)\b",
        r"\bjuggling\b",
    ],
    "time_cost": [
        r"\b(takes?|spend|spent|waste|costs?) (me|us|the team)? ?\d+\s*(hours?|hrs?|days?|weeks?|minutes?|mins?)\b",
        r"\b\d+\s*(hours?|hrs?|days?|weeks?)\s*(a|per|each)\s*(day|week|month|year)\b",
        r"\bhours (every|each|a) (day|week|month)\b",
        r"\bfull[- ]time (job|role)\b",
        r"\b(so much|too much) time\b",
    ],
    "money_cost": [
        r"[$£€]\s?\d[\d,.]*",
        r"\b\d[\d,.]*\s*(usd|gbp|eur|dollars?|pounds?|euros?)\b",
        r"\bwe pay (someone|a|for|an?\b)",
        r"\bpaying (for|someone)\b",
        r"\b(expensive|pricey|costly|rip[- ]?off|overpriced)\b",
        r"\b(subscription|licen[cs]e|licensing) (cost|fee|is|are)\b",
        r"\bper (seat|user|month) pricing\b",
    ],
    # Paid workarounds are the strongest evidence that a problem already has a
    # budget: someone is paying a human or a tool to absorb it. Added 2026-09-21
    # because extraction previously looked for pain, not spend.
    "paid_workaround": [
        r"\bwe pay (a|an|someone|people|staff|a va|a virtual assistant)\b",
        r"\bpaying (a|an|someone|people|staff|a va)\b",
        r"\b(hired|employ|employing|took on) (a|an|someone|staff|a va|a virtual assistant)\b",
        r"\boutsourc\w*\b",
        r"\bvirtual assistant\b",
        r"\bdata entry (staff|agency|team|person|clerk)\b",
        r"\bper (seat|user|licen[cs]e) (pricing|fee|cost)\b",
        r"\b(minimum|annual|12[- ]month|two[- ]year) (contract|term|commitment)\b",
        r"\bwe'?re locked in(to)?\b",
    ],
    "dissatisfaction": [
        r"\b(frustrat\w*|annoy\w*|hate|painful|nightmare|mess|shambles)\b",
        r"\bdoesn'?t (work|support|integrate|handle|do)\b",
        r"\bdoes not (work|support|integrate|handle|do)\b",
        r"\bcan'?t (believe|find|get|export|import|sync)\b",
        r"\bno (good )?(option|alternative|solution|tool)\b",
        r"\btoo expensive\b",
        r"\bswitching (from|away)\b",
        r"\b(cancel|ditch|leave|leaving|migrat)\w* (our|the|from)\b",
    ],
    "integration": [
        r"\bintegrat\w*\b",
        r"\bsync(hronis|hroniz|ed|ing)?\w*\b",
        r"\b(export|import)\w*\b",
        r"\bapi\b",
        r"\bwebhook\w*\b",
        r"\bzapier\b",
        r"\bmake\.com\b",
        r"\b(csv|xlsx)\b",
        r"\bconnector\w*\b",
        r"\bplugins?\b",
    ],
    "frequency": [
        r"\bevery (day|week|month|morning|friday|monday)\b",
        r"\b(daily|weekly|monthly|quarterly|annually)\b",
        r"\beach (day|week|month|quarter)\b",
        r"\bper (day|week|month|year)\b",
        r"\b(end of (the )?(month|week|quarter|year))\b",
    ],
    "automation_wish": [
        r"\bis there (a|any|some) (tool|software|app|service|way)\b",
        r"\blooking for (a|an|some|recommendations?)\b",
        r"\bany(one)? (know|recommend|suggest)\w*\b",
        r"\bi wish (it|there|they|my)\b",
        r"\bwish .{0,40}\bintegrat\w*\b",
        r"\bthere (has to|must) be a better way\b",
        r"\balternative to\b",
    ],
}

_COMPILED: dict[str, list[tuple[str, re.Pattern[str]]]] = {
    group: [(pattern, re.compile(pattern, re.IGNORECASE)) for pattern in patterns]
    for group, patterns in CUE_GROUPS.items()
}

# Group weights for the "best pain sentence" score. First-hand workaround and
# concrete cost clues are weighted highest because they are the strongest
# evidence of real, costly pain.
GROUP_WEIGHTS = {
    "manual": 2,
    "workaround": 2,
    "time_cost": 2,
    "money_cost": 2,
    "paid_workaround": 2,
    "dissatisfaction": 1,
    "integration": 1,
    "frequency": 1,
    "automation_wish": 1,
}

STRONG_GROUPS = {
    "manual",
    "workaround",
    "time_cost",
    "money_cost",
    "paid_workaround",
    "dissatisfaction",
    "automation_wish",
}

SYSTEM_NAMES = [
    "Excel", "Google Sheets", "Airtable", "Notion", "SharePoint", "Microsoft Access",
    "SQL Server", "MySQL", "PostgreSQL", "Salesforce", "HubSpot", "Pipedrive", "Zoho",
    "Microsoft Dynamics", "NetSuite", "SAP", "Oracle", "Workday", "Xero", "QuickBooks",
    "Sage", "MYOB", "FreeAgent", "Wave", "FreshBooks", "KashFlow", "ClearBooks",
    "Quickfile", "Jira", "Asana", "Monday.com", "Trello", "ClickUp", "Basecamp",
    "Slack", "Microsoft Teams", "Outlook", "Gmail", "Zendesk", "Freshdesk", "Intercom",
    "ServiceNow", "Shopify", "WooCommerce", "Magento", "BigCommerce", "Amazon Seller Central",
    "Stripe", "PayPal", "Square", "GoCardless", "DocuSign", "Power BI", "Tableau",
    "Looker", "Zapier", "Make.com", "Power Automate", "Mailchimp", "Klaviyo",
    "Hootsuite", "Buffer", "Canva", "Figma", "Harvest", "Toggl", "Clockify",
    "Deputy", "Rotaready", "Xero Projects", "Sage 50", "Sage 200", "QuickBooks Online",
]

_SYSTEM_RE = {
    name: re.compile(r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])", re.IGNORECASE)
    for name in SYSTEM_NAMES
}

# Most specific role first; the first match wins.
ROLE_PATTERNS: list[tuple[str, str]] = [
    (r"\b(book-?keep\w*)\b", "Bookkeeper"),
    (r"\b(accountant|accounting|accountancy|payroll)\b", "Accountant"),
    (r"\b(practice manager|clinic manager)\b", "Practice manager (clinic/health)"),
    (r"\b(e-?commerce|online store|shopify|woocommerce|amazon seller)\b", "E-commerce operator"),
    (r"\b(estate agent|lettings|property manager|landlord)\b", "Property/lettings professional"),
    (r"\b(solicitor|lawyer|legal|conveyanc\w*|paralegal)\b", "Legal professional"),
    (r"\b(recruit\w*|talent acquisition|people ops)\b", "Recruiter/HR"),
    (r"\b(warehouse|logistics|fulfilment|fulfillment|stock control|inventory manager)\b", "Warehouse/logistics operator"),
    (r"\b(construction|builder|contractor|plumber|electrician|tradesman)\b", "Construction/trade operator"),
    (r"\b(restaurant|cafe|catering|hospitality|hotel)\b", "Hospitality operator"),
    (r"\b(salon|barber|spa|hairdress\w*)\b", "Salon/spa operator"),
    (r"\b(teacher|school|tutor|academy|university)\b", "Education administrator"),
    (r"\b(charity|non-?profit|volunteer)\b", "Charity administrator"),
    (r"\b(operations? manager|ops manager|head of operations)\b", "Operations manager"),
    (r"\b(office manager)\b", "Office manager"),
    (r"\b(procurement|buyer|purchasing)\b", "Procurement/purchasing"),
    (r"\b(freelanc\w*|self-?employed|sole[- ]?traders?)\b", "Sole trader/freelancer"),
    (r"\b(small business|small company|small firm|smb)\b", "Small business owner/operator"),
    (r"\b(developer|software engineer|devops|programmer)\b", "Software developer"),
    (r"\b(admin\w*|assistant|secretar\w*)\b", "Administrator"),
    (r"\b(hr|human resources)\b", "HR/recruiter"),
]

ORG_PATTERNS: list[tuple[str, str]] = [
    (r"\b(accountancy practice|accounting firm|bookkeeping (firm|practice))\b", "Accountancy practice"),
    (r"\b(law firm|solicitors|legal practice)\b", "Law firm"),
    (r"\b(estate agency|letting agency)\b", "Estate/letting agency"),
    (r"\b(chartiy|charity|non-?profit)\b", "Charity/non-profit"),
    (r"\b(e-?commerce (business|store|company)|online store)\b", "E-commerce business"),
    (r"\b(manufactur\w*|factory|production)\b", "Manufacturer"),
    (r"\b(wholesale|distributor)\b", "Wholesaler/distributor"),
    (r"\b(saas (company|startup)|software company)\b", "Software company"),
    (r"\b(agency|agencies)\b", "Agency"),
    (r"\b(school|academy|college)\b", "School/college"),
    (r"\b(clinic|practice|surgery|dental|dentist)\b", "Clinic/health practice"),
    (r"\b(restaurant|cafe|hotel)\b", "Hospitality business"),
    (r"\b(construction (company|firm)|builder|contractor)\b", "Construction firm"),
    (r"\b(landlord|property portfolio)\b", "Landlord/property portfolio"),
    (r"\b(small business|small company|our business|my business)\b", "Small business"),
]

VENDOR_MARKETING = [
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\bbook a demo\b",
        r"\brequest a demo\b",
        r"\bstart your free trial\b",
        r"\bour (platform|solution|software|product) (helps|enables|allows|is)\b",
        r"\bwe'?re excited to announce\b",
        r"\btrusted by \d+\b",
        r"\bpricing (plans?|page)\b",
    )
]

FIRST_PERSON = re.compile(r"\b(i|we|our|my|us)\b", re.IGNORECASE)


def matched_groups(text: str) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for group, patterns in _COMPILED.items():
        hits = [pattern for pattern, regex in patterns if regex.search(text)]
        if hits:
            found[group] = hits
    return found


def named_systems(text: str) -> list[str]:
    return sorted({name for name, regex in _SYSTEM_RE.items() if regex.search(text)})


def infer_role(text: str) -> str | None:
    for pattern, label in ROLE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return label
    return None


def infer_org(text: str) -> str | None:
    for pattern, label in ORG_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return label
    return None


def _best_sentence(text: str) -> str:
    best, best_score = "", 0
    for sentence in re.split(r"(?<=[.!?])\s+|\n+", strip_html(text)):
        sentence = sentence.strip()
        if len(sentence) < 15:
            continue
        groups = matched_groups(sentence)
        score = sum(GROUP_WEIGHTS.get(g, 1) for g in groups)
        if groups.get("manual") or groups.get("workaround"):
            score += 1
        if score > best_score:
            best, best_score = sentence, score
    return best


def _statement_from(text: str) -> str:
    """Build the pain statement: best cue sentence, widened if very short."""
    sentence = _best_sentence(text)
    if not sentence:
        return ""
    if len(sentence) < 60:
        all_sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", strip_html(text)) if s.strip()]
        for idx, candidate in enumerate(all_sentences):
            if candidate == sentence and idx + 1 < len(all_sentences):
                sentence = f"{sentence} {all_sentences[idx + 1]}".strip()
                break
    return truncate(sentence, 400)


def _first_clue(text: str, group: str) -> str | None:
    for pattern, regex in _COMPILED[group]:
        sentence = first_sentence_containing(text, regex)
        if sentence:
            return truncate(sentence, 300)
    return None


# Auto-generated digest/roundup posts (e.g. "AI CLI Tools Digest", "Ecosystem
# Digest", "Hot Issues (Top 10 by Community Signal)") are long, keyword-dense
# and match almost every query, but they are machine-written summaries of other
# people's issues, not a buyer describing their own work. They were the source
# of the construction/trade false-positive cluster in the 2026-09-21 quality
# run, so they are rejected before cue matching.
DIGEST_MARKERS = [
    re.compile(r"\b(community|ecosystem|weekly|daily)\s+digest\b", re.IGNORECASE),
    re.compile(r"\bhot issues\b.*\bcommunity signal\b", re.IGNORECASE),
    re.compile(r"\bcross[- ]tool comparison\b", re.IGNORECASE),
    re.compile(r"\bgenerated:\s*\d{4}-\d{2}-\d{2}", re.IGNORECASE),
    re.compile(r"\btools covered:\s*\d+", re.IGNORECASE),
    re.compile(r"\bno new releases in the last 24 hours\b", re.IGNORECASE),
]


def _is_digest_post(text: str) -> bool:
    """True for auto-generated digest/roundup posts, which are not buyer pain."""
    hits = sum(1 for regex in DIGEST_MARKERS if regex.search(text))
    return hits >= 2


def _is_vendor_marketing(text: str, groups: dict[str, list[str]]) -> bool:
    vendor_hits = sum(1 for regex in VENDOR_MARKETING if regex.search(text))
    # Only cues that describe the buyer's own labour or dissatisfaction can
    # exempt vendor copy. money_cost and paid_workaround are excluded because
    # their patterns also fire on vendor phrasing ("we pay attention to
    # detail", "outsourced teams love us"), which would let marketing copy
    # masquerade as first-person pain.
    first_person_pain = bool(FIRST_PERSON.search(text)) and bool(
        set(groups) & {"manual", "workaround", "time_cost", "dissatisfaction", "automation_wish"}
    )
    return vendor_hits >= 2 and not first_person_pain


def confidence_for(groups: dict[str, list[str]], systems: list[str], role: str | None) -> float:
    score = 0.15 + 0.12 * len(groups)
    if systems:
        score += 0.08
    if role:
        score += 0.08
    if groups.get("frequency"):
        score += 0.05
    return round(min(0.9, score), 2)


def extract_signal(item: dict, limits: dict) -> tuple[dict | None, str]:
    """Extract one signal. Returns (signal | None, reject_reason)."""
    text = strip_html(item.get("text") or "")
    if not text:
        return None, "empty_text"
    if _is_digest_post(text):
        return None, "digest_post"
    groups = matched_groups(text)
    if _is_vendor_marketing(text, groups):
        return None, "vendor_marketing_only"
    if not set(groups) & STRONG_GROUPS:
        return None, "no_pain_cue"
    statement = _statement_from(text)
    min_chars = int(limits.get("extract", {}).get("min_statement_chars", 60))
    if len(statement) < min_chars:
        return None, "statement_too_short"
    systems = named_systems(text)
    role = infer_role(text)
    workaround = _first_clue(text, "workaround") or _first_clue(text, "manual")
    published = item.get("published_at")
    signal = make_signal(
        source_type=item.get("source_type", ""),
        source_id=item.get("source_id", ""),
        source_url=item.get("url", ""),
        retrieved_at=item.get("retrieved_at") or utcnow_iso(),
        published_at=published if isinstance(published, str) and published else None,
        source_author=item.get("author"),
        target_role=role,
        organisation_hint=infer_org(text),
        task=truncate(_best_sentence(text) or statement, 200),
        pain_statement=statement,
        current_workaround=workaround,
        named_systems=systems,
        frequency_clue=_first_clue(text, "frequency"),
        time_cost_clue=_first_clue(text, "time_cost"),
        money_cost_clue=_first_clue(text, "money_cost"),
        dissatisfaction_clue=_first_clue(text, "dissatisfaction"),
        integration_clue=_first_clue(text, "integration"),
        confidence=confidence_for(groups, systems, role),
        extraction_provenance={
            "method": "deterministic-cues",
            "version": EXTRACTOR_VERSION,
            "cue_groups": sorted(groups.keys()),
            "patterns_matched": sorted({p for hits in groups.values() for p in hits}),
            "model": None,
            "prompt_hash": None,
        },
        raw_excerpt=truncate(text, int(limits.get("extract", {}).get("max_raw_excerpt_chars", 600))),
    )
    return signal, ""


def extract_many(items: list[dict], limits: dict) -> tuple[list[dict], list[dict]]:
    """Extract signals from raw items; returns (signals, rejections)."""
    signals: list[dict] = []
    rejects: list[dict] = []
    for item in items:
        if not item.get("retrieved_at"):
            item = {**item, "retrieved_at": utcnow_iso()}
        signal, reason = extract_signal(item, limits)
        if signal is None:
            rejects.append(
                {"source_id": item.get("source_id"), "reason": reason, "source_type": item.get("source_type")}
            )
        else:
            signals.append(signal)
    return signals, rejects
