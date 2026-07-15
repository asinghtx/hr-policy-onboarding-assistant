"""Visual elements for the HR assistant: category badges and status pills.

Colors are taken as-is from the validated reference palette (categorical
order and status palette) rather than invented here.
"""

import streamlit as st

FONT_FAMILY = "system-ui, -apple-system, 'Segoe UI', sans-serif"
INK_PRIMARY = "#0b0b0b"
INK_SECONDARY = "#52514e"

# Fixed categorical order, matching sample_data.POLICY_CATEGORIES 1:1.
CATEGORY_META = {
    "Leave": {"color": "#2a78d6", "icon": "🌴"},
    "WFH": {"color": "#008300", "icon": "🏠"},
    "Reimbursement": {"color": "#e87ba4", "icon": "💳"},
    "Travel": {"color": "#eda100", "icon": "✈️"},
    "Benefits": {"color": "#1baf7a", "icon": "🩺"},
    "Probation": {"color": "#eb6834", "icon": "📋"},
    "Onboarding": {"color": "#4a3aa7", "icon": "🎉"},
    "General HR": {"color": "#e34948", "icon": "🏢"},
}

STATUS_GOOD = "#0ca30c"
STATUS_CRITICAL = "#d03b3b"

ONBOARDING_STAGE_LABELS = {
    "first_week": "First week",
    "day_30": "By day 30",
    "day_60": "By day 60",
    "day_90": "By day 90",
}


def category_label(category: str) -> str:
    meta = CATEGORY_META.get(category)
    return f"{meta['icon']} {category}" if meta else category


def render_category_badge(category: str):
    meta = CATEGORY_META.get(category)
    if not meta:
        return
    html = (
        f'<div style="display:inline-flex; align-items:center; gap:6px; '
        f'background:{meta["color"]}1a; border:1px solid {meta["color"]}55; '
        f'color:{INK_PRIMARY}; padding:4px 12px; border-radius:999px; '
        f'font-family:{FONT_FAMILY}; font-size:0.85rem; font-weight:600; '
        f'margin-bottom:0.5rem;">'
        f'<span style="font-size:1rem;">{meta["icon"]}</span>'
        f'<span>{category}</span>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)


def render_escalation_pill(hr_escalation_required: bool, reason: str):
    if hr_escalation_required:
        color, icon, label = STATUS_CRITICAL, "⚠️", "HR escalation required"
    else:
        color, icon, label = STATUS_GOOD, "✅", "No escalation needed"

    reason_html = (
        f'<div style="color:{INK_SECONDARY}; font-size:0.85rem;">{reason}</div>'
        if reason
        else ""
    )

    html = (
        f'<div style="display:flex; align-items:center; gap:8px; '
        f'background:{color}14; border:1px solid {color}55; border-radius:10px; '
        f'padding:10px 14px; margin:0.5rem 0; font-family:{FONT_FAMILY};">'
        f'<span style="font-size:1.1rem;">{icon}</span>'
        f'<div>'
        f'<div style="color:{INK_PRIMARY}; font-weight:600; font-size:0.95rem;">{label}</div>'
        f'{reason_html}'
        f'</div>'
        f'</div>'
    )
    st.markdown(html, unsafe_allow_html=True)
