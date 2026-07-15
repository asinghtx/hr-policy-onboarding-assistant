import streamlit as st
from dotenv import load_dotenv

from src.openrouter_client import call_openrouter
from src.prompts import build_messages
from src.response_parser import parse_response
from src.sample_data import (
    EMPLOYMENT_TYPES,
    JOINING_STAGES,
    POLICY_CATEGORIES,
    get_sample,
    get_sample_names,
)
from src.ui_helpers import render_result, to_markdown
from src.visuals import CATEGORY_META, category_label

load_dotenv()

st.set_page_config(
    page_title="HR Policy + Onboarding Assistant", page_icon="🧭", layout="centered"
)

st.markdown(
    """
    <style>
      .block-container { padding-top: 2rem; padding-bottom: 3rem; }
      div[data-testid="stExpander"] {
          border: 1px solid rgba(11,11,11,0.08);
          border-radius: 12px;
      }
      div[data-testid="stForm"] {
          border: 1px solid rgba(11,11,11,0.08);
          border-radius: 14px;
          padding: 1.25rem;
      }
      .hr-hero {
          background: linear-gradient(135deg, #2a78d6 0%, #4a3aa7 100%);
          border-radius: 16px;
          padding: 1.75rem 2rem;
          margin-bottom: 1.5rem;
          color: #ffffff;
      }
      .hr-hero h1 {
          margin: 0 0 0.35rem 0;
          font-size: 1.75rem;
          color: #ffffff;
      }
      .hr-hero p {
          margin: 0;
          color: rgba(255,255,255,0.9);
          font-size: 0.95rem;
      }
    </style>
    """,
    unsafe_allow_html=True,
)


def generate_guidance(category, policy_text, employee_context, question):
    messages = build_messages(category, policy_text, employee_context, question)
    raw_text = call_openrouter(messages)
    return parse_response(raw_text)


st.markdown(
    """
    <div class="hr-hero">
        <h1>🧭 HR Policy + Onboarding Assistant</h1>
        <p>Demo only — uses synthetic HR policies. Do not paste real employee,
        payroll, health, or performance data.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("Sample data")
    sample_name = st.selectbox(
        "Load a synthetic policy",
        ["(none)"] + get_sample_names(),
        format_func=lambda name: name
        if name == "(none)"
        else f"{CATEGORY_META[get_sample(name)['category']]['icon']} {name}",
    )

    st.divider()
    st.warning(
        "⚠️ Privacy: this demo does not store data. Use synthetic examples "
        "only — never enter real employee or confidential information."
    )

sample = get_sample(sample_name) if sample_name != "(none)" else None
sample_key = sample_name if sample else "none"

st.subheader("Employee context")
col1, col2 = st.columns(2)
with col1:
    role = st.text_input("Role / job title")
    department = st.text_input("Department")
    location = st.text_input("Location")
with col2:
    employment_type = st.selectbox("Employment type", EMPLOYMENT_TYPES)
    joining_stage = st.selectbox("Joining stage / tenure", JOINING_STAGES)
    category = st.selectbox(
        "Policy category",
        POLICY_CATEGORIES,
        index=POLICY_CATEGORIES.index(sample["category"]) if sample else 0,
        key=f"category_{sample_key}",
        format_func=category_label,
    )

with st.form("hr_question_form"):
    policy_text = st.text_area(
        "HR policy or onboarding guide text",
        value=sample["policy_text"] if sample else "",
        height=200,
        placeholder="Paste the relevant HR policy or onboarding guide text here...",
        key=f"policy_text_{sample_key}",
    )
    question = st.text_area(
        "Employee question",
        value=sample["sample_question"] if sample else "",
        height=100,
        placeholder="e.g. How many leave days can I carry forward?",
        key=f"question_{sample_key}",
    )
    submitted = st.form_submit_button("Get HR Guidance")

if submitted:
    if not policy_text.strip() or not question.strip():
        st.error(
            "Please provide both the HR policy/onboarding text and a question "
            "before requesting guidance."
        )
    else:
        employee_context = {
            "Role": role,
            "Department": department,
            "Location": location,
            "Employment type": employment_type,
            "Joining stage / tenure": joining_stage,
        }
        with st.spinner("Generating HR guidance..."):
            try:
                result = generate_guidance(
                    category, policy_text, employee_context, question
                )
                st.session_state["latest_result"] = result
                st.session_state["latest_category"] = category
                st.session_state["latest_question"] = question
            except Exception as exc:
                st.error(f"Could not generate guidance: {exc}")

if "latest_result" in st.session_state:
    st.subheader("HR Guidance")
    render_result(
        st.session_state["latest_result"], st.session_state["latest_category"]
    )

    markdown_output = to_markdown(
        st.session_state["latest_result"],
        st.session_state["latest_category"],
        st.session_state["latest_question"],
    )
    col_a, col_b = st.columns(2)
    with col_a:
        st.download_button(
            "Download answer as Markdown",
            markdown_output,
            file_name="hr_guidance.md",
            mime="text/markdown",
        )
    with col_b:
        if st.button("Clear session"):
            for key in ("latest_result", "latest_category", "latest_question"):
                st.session_state.pop(key, None)
            st.rerun()
