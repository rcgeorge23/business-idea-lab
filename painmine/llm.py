"""Optional DeepSeek-via-OpenCode-Go inference (issue #9 inference requirement).

Hard rules implemented here:
- The provider/model is exactly what ``limits.json`` says
  (``opencode-go`` / ``opencode-go/deepseek-v4.1-flash`` by default). There is
  no automatic fallback to any other provider.
- Spend is disabled by default (``llm.enabled == false``). It is only ever
  enabled by an explicit owner decision; every call is metered by ``Budget``.
- Authentication comes from the environment (``OPENCODE_API_KEY``) or the
  standard OpenCode credentials file. Credentials are never printed or written
  into artefacts.
- Non-interactive invocation uses ``opencode run --format json``; if the
  provider is unavailable the call fails safely with a recorded reason.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
from typing import Any

from .budget import Budget
from .util import truncate

AUTH_FILE_HINT = os.path.join("~", ".local", "share", "opencode", "auth.json")


def estimate_tokens(text: str) -> int:
    return max(1, len(text or "") // 4)


def scan_usage(obj: Any, acc: dict | None = None) -> dict:
    """Recursively find provider-reported cost/token fields in an event stream."""
    if acc is None:
        acc = {"cost": 0.0, "input": 0, "output": 0, "reasoning": 0, "cache_read": 0, "cache_write": 0}
    if isinstance(obj, dict):
        for key, value in obj.items():
            lower = key.lower()
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                if lower == "cost":
                    acc["cost"] = max(acc["cost"], float(value))
                elif lower in ("input", "input_tokens", "prompt_tokens", "inputTokens"):
                    acc["input"] = max(acc["input"], int(value))
                elif lower in ("output", "output_tokens", "completion_tokens", "outputTokens"):
                    acc["output"] = max(acc["output"], int(value))
                elif lower in ("reasoning", "reasoning_tokens"):
                    acc["reasoning"] = max(acc["reasoning"], int(value))
                elif lower in ("cache_read", "cache_read_input_tokens"):
                    acc["cache_read"] = max(acc["cache_read"], int(value))
                elif lower in ("cache_write", "cache_write_input_tokens", "cache_creation_input_tokens"):
                    acc["cache_write"] = max(acc["cache_write"], int(value))
            elif isinstance(value, (dict, list)):
                scan_usage(value, acc)
    elif isinstance(obj, list):
        for item in obj:
            scan_usage(item, acc)
    return acc


def collect_text(obj: Any, out: list[str] | None = None) -> str:
    """Collect assistant text from an OpenCode JSON event stream."""
    if out is None:
        out = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            lower = key.lower()
            if lower in ("text", "content") and isinstance(value, str) and value.strip():
                out.append(value)
            elif isinstance(value, (dict, list)):
                collect_text(value, out)
    elif isinstance(obj, list):
        for item in obj:
            collect_text(item, out)
    return "\n".join(out)


def extract_json_blob(text: str) -> Any | None:
    """Find and parse the first balanced JSON object/array in free text."""
    if not text:
        return None
    start = min((i for i in (text.find("{"), text.find("[")) if i != -1), default=-1)
    if start == -1:
        return None
    stack: list[str] = []
    in_string = False
    escaped = False
    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char in "{[":
            stack.append(char)
        elif char in "}]":
            if not stack:
                return None
            opening = stack.pop()
            if (opening, char) not in {("{", "}"), ("[", "]")}:
                return None
            if not stack:
                try:
                    return json.loads(text[start : index + 1])
                except json.JSONDecodeError:
                    return None
    return None


def parse_event_stream(stdout: str) -> list[dict]:
    events: list[dict] = []
    for line in (stdout or "").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


class OpenCodeGo:
    """Bounded, non-interactive OpenCode Go client. Never falls back providers."""

    def __init__(self, limits: dict, budget: Budget) -> None:
        cfg = limits.get("llm", {})
        self.provider = str(cfg.get("provider", "opencode-go"))
        self.model = str(cfg.get("model", "opencode-go/deepseek-v4.1-flash"))
        self.agent = str(cfg.get("agent", "painmine-extractor"))
        self.timeout = int(cfg.get("timeout_seconds_per_call", 180))
        self.max_output_tokens = int(cfg.get("max_output_tokens_per_call", 1200))
        self.binary = os.environ.get("OPENCODE_BIN") or shutil.which("opencode") or ""
        self.budget = budget

    # ------------------------------------------------------------- status
    def auth_status(self) -> tuple[bool, str]:
        if os.environ.get("OPENCODE_API_KEY"):
            return True, "auth=env:OPENCODE_API_KEY"
        auth_path = os.path.expanduser(AUTH_FILE_HINT)
        if not os.path.exists(auth_path):
            return False, (
                "no OPENCODE_API_KEY secret and no OpenCode credentials file; "
                "set OPENCODE_API_KEY (or OPENCODE_AUTH_JSON) in the workflow secrets"
            )
        try:
            with open(auth_path, "r", encoding="utf-8") as handle:
                data = json.load(handle)
            if isinstance(data, dict) and any("opencode" in str(key).lower() for key in data):
                return True, "auth=opencode credentials file"
            return False, "credentials file present but has no opencode entry"
        except Exception as exc:  # noqa: BLE001 - report, never leak
            return False, f"cannot read credentials file: {type(exc).__name__}"

    def available(self) -> tuple[bool, str]:
        if not self.budget.llm_enabled:
            return False, "llm disabled by limits.json (llm.enabled=false); owner approval required"
        if not self.binary or (not os.path.exists(self.binary) and shutil.which(self.binary) is None):
            return False, "opencode binary not found (set OPENCODE_BIN or install opencode)"
        ok, auth_reason = self.auth_status()
        if not ok:
            return False, auth_reason
        return True, f"{auth_reason}; provider={self.provider}; model={self.model}"

    # ------------------------------------------------------------ invoke
    def run(self, prompt: str, agent: str | None = None) -> dict:
        ok, reason = self.available()
        meta = {"provider": self.provider, "model": self.model, "agent": agent or self.agent}
        if not ok:
            return {"ok": False, "error": reason, **meta}
        est_input = estimate_tokens(prompt)
        allowed, why = self.budget.can_llm(est_input, self.max_output_tokens)
        if not allowed:
            return {"ok": False, "error": why, **meta}
        command = [
            self.binary,
            "run",
            "--model",
            self.model,
            "--agent",
            agent or self.agent,
            "--format",
            "json",
            prompt,
        ]
        environment = {**os.environ, "NO_COLOR": "1"}
        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                env=environment,
                cwd=os.getcwd(),
            )
        except subprocess.TimeoutExpired:
            self.budget.stop(f"model call exceeded {self.timeout}s timeout")
            return {"ok": False, "error": f"timeout after {self.timeout}s", **meta}
        except Exception as exc:  # noqa: BLE001
            return {"ok": False, "error": f"{type(exc).__name__}: {exc}", **meta}

        events = parse_event_stream(completed.stdout)
        usage = scan_usage(events)
        self.budget.record_llm(usage["cost"], usage["input"], usage["output"])
        text = collect_text(events).strip()
        return {
            "ok": completed.returncode == 0 and bool(text),
            "text": text,
            "events": len(events),
            "cost_usd": usage["cost"],
            "tokens": usage,
            "stderr_tail": truncate(completed.stderr or "", 400),
            "error": "" if completed.returncode == 0 else f"opencode exit {completed.returncode}",
            **meta,
        }
