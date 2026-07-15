import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.prompts import SYSTEM_PROMPT, build_messages, build_user_prompt
from src.response_parser import parse_response


def test_system_prompt_forbids_approvals_and_legal_advice():
    lowered = SYSTEM_PROMPT.lower()
    assert "do not" in lowered or "not approve" in lowered
    assert "legal" in lowered
    assert "disclaimer" in lowered


def test_build_messages_includes_policy_and_question():
    messages = build_messages(
        "Leave",
        "Employees get 18 leave days.",
        {"Role": "Engineer"},
        "How many days do I get?",
    )
    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"
    assert "18 leave days" in messages[1]["content"]
    assert "How many days do I get?" in messages[1]["content"]


def test_build_user_prompt_omits_empty_context_values():
    prompt = build_user_prompt(
        "WFH", "policy text", {"Role": "", "Department": "Sales"}, "question?"
    )
    assert "Department: Sales" in prompt
    assert "Role:" not in prompt


def test_parse_response_valid_json():
    raw = '{"answer": "You can carry forward 5 days.", "hr_escalation_required": false}'
    result = parse_response(raw)
    assert result["answer"] == "You can carry forward 5 days."
    assert result["hr_escalation_required"] is False
    assert result["disclaimer"]


def test_parse_response_invalid_json_escalates():
    result = parse_response("not json at all")
    assert result["hr_escalation_required"] is True
    assert result["answer"]


def test_parse_response_normalizes_non_list_fields():
    raw = '{"answer": "ok", "next_steps": "Talk to HR"}'
    result = parse_response(raw)
    assert result["next_steps"] == ["Talk to HR"]
