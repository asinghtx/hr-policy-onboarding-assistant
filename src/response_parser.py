"""Parse and normalize the AI's JSON response into a predictable shape."""

import json
import re

FALLBACK_DISCLAIMER = (
    "This is AI-generated informational guidance only. It is not a final HR "
    "decision or legal advice. Please confirm with HR or your manager."
)

ONBOARDING_STAGES = ("first_week", "day_30", "day_60", "day_90")

_DEFAULTS = {
    "answer": "",
    "policy_basis": [],
    "next_steps": [],
    "documents_or_approvals_needed": [],
    "hr_escalation_required": False,
    "escalation_reason": "",
    "draft_message": "",
    "onboarding_checklist": {stage: [] for stage in ONBOARDING_STAGES},
    "disclaimer": FALLBACK_DISCLAIMER,
}

_LIST_FIELDS = (
    "policy_basis",
    "next_steps",
    "documents_or_approvals_needed",
)


def _as_list(value):
    if isinstance(value, list):
        return value
    return [str(value)] if value else []


def _normalize_onboarding_checklist(value):
    if isinstance(value, dict):
        return {stage: _as_list(value.get(stage, [])) for stage in ONBOARDING_STAGES}
    if isinstance(value, list):
        return {
            "first_week": value,
            "day_30": [],
            "day_60": [],
            "day_90": [],
        }
    return {stage: [] for stage in ONBOARDING_STAGES}


def _extract_json_object(raw_text: str) -> str:
    match = re.search(r"\{.*\}", raw_text, re.DOTALL)
    return match.group(0) if match else raw_text


def parse_response(raw_text: str) -> dict:
    try:
        data = json.loads(_extract_json_object(raw_text))
    except (json.JSONDecodeError, TypeError):
        return {
            **_DEFAULTS,
            "answer": (
                "The assistant response could not be parsed. Please try "
                "rephrasing your question or contact HR directly."
            ),
            "hr_escalation_required": True,
            "escalation_reason": "AI response was not valid JSON.",
        }

    result = dict(_DEFAULTS)
    for key, default in _DEFAULTS.items():
        value = data.get(key, default)
        if key in _LIST_FIELDS:
            value = _as_list(value)
        result[key] = value

    result["onboarding_checklist"] = _normalize_onboarding_checklist(
        data.get("onboarding_checklist")
    )

    if not result["disclaimer"]:
        result["disclaimer"] = FALLBACK_DISCLAIMER

    return result
