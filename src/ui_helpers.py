"""Streamlit rendering helpers for the HR assistant result."""

import streamlit as st

from src.visuals import (
    ONBOARDING_STAGE_LABELS,
    render_category_badge,
    render_escalation_pill,
)

_ONBOARDING_STAGE_LABELS = ONBOARDING_STAGE_LABELS
_ONBOARDING_STAGES = tuple(_ONBOARDING_STAGE_LABELS.keys())


def render_result(result: dict, category: str):
    render_category_badge(category)
    st.success(result["answer"] or "No answer generated.")

    render_escalation_pill(
        result["hr_escalation_required"], result["escalation_reason"]
    )

    with st.expander("Policy basis", expanded=False):
        _render_list(result["policy_basis"])

    with st.expander("Next steps", expanded=True):
        _render_list(result["next_steps"])

    with st.expander("Documents or approvals needed", expanded=False):
        _render_list(result["documents_or_approvals_needed"])

    checklist = result["onboarding_checklist"]
    if category == "Onboarding" and any(checklist.get(stage) for stage in _ONBOARDING_STAGES):
        with st.expander("30/60/90-day onboarding roadmap", expanded=True):
            for stage, label in _ONBOARDING_STAGE_LABELS.items():
                st.markdown(f"**{label}**")
                _render_list(checklist.get(stage, []))

    with st.expander("Draft message to HR / manager", expanded=False):
        st.text_area(
            "Draft message",
            value=result["draft_message"],
            height=140,
            label_visibility="collapsed",
        )

    st.caption(result["disclaimer"])


def _render_list(items):
    if not items:
        st.write("None provided.")
        return
    for item in items:
        st.markdown(f"- {item}")


def to_markdown(result: dict, category: str, question: str) -> str:
    lines = [
        "# HR Guidance Summary",
        "",
        f"**Category:** {category}",
        f"**Question:** {question}",
        "",
        "## Answer",
        result["answer"] or "N/A",
        "",
        "## Policy basis",
        _list_to_markdown(result["policy_basis"]),
        "",
        "## Next steps",
        _list_to_markdown(result["next_steps"]),
        "",
        "## Documents or approvals needed",
        _list_to_markdown(result["documents_or_approvals_needed"]),
        "",
        f"## HR escalation required: {result['hr_escalation_required']}",
        result["escalation_reason"] or "",
        "",
    ]

    checklist = result["onboarding_checklist"]
    if category == "Onboarding" and any(checklist.get(stage) for stage in _ONBOARDING_STAGES):
        lines += ["## 30/60/90-day onboarding roadmap", ""]
        for stage, label in _ONBOARDING_STAGE_LABELS.items():
            lines += [f"### {label}", _list_to_markdown(checklist.get(stage, [])), ""]

    lines += [
        "## Draft message",
        result["draft_message"] or "N/A",
        "",
        "## Disclaimer",
        result["disclaimer"],
    ]

    return "\n".join(lines)


def _list_to_markdown(items) -> str:
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)
