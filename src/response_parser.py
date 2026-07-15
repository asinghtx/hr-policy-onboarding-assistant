"""Parse and normalize the AI's JSON response into a predictable shape."""

import json
import re

FALLBACK_DISCLAIMER = (
    "This is AI-generated informational guidance only. It is not a final HR "
    "decision or legal advice. Please confirm with HR or your manager."
)

_DEFAULTS = {
    "answer": "",
    "policy_basis": [],
    "next_steps": [],
    "documents_or_approvals_needed": [],
    "hr_escalation_required": False,
    "escalation_reason": "",
    "draft_message": "",
    "onboarding_checklist": [],
    "disclaimer": FALLBACK_DISCLAIMER,
}

_LIST_FIELDS = (
    "policy_basis",
    "next_steps",
    "documents_or_approvals_needed",
    "onboarding_checklist",
)


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
        if key in _LIST_FIELDS and not isinstance(value, list):
            value = [str(value)] if value else []
        result[key] = value

    if not result["disclaimer"]:
        result["disclaimer"] = FALLBACK_DISCLAIMER

    return result
