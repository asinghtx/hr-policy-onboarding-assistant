# Product Requirements Document — HR Policy + Onboarding Assistant
Rebuilt for Python + Streamlit

| Field | Value |
|---|---|
| Product | HR Policy + Onboarding Assistant |
| Document type | Product Requirements Document (PRD) |
| Version | MVP1 – Python + Streamlit rebuild |
| Session fit | 2-hour Claude Code build workshop |
| Primary stack | Python, Streamlit, OpenRouter API, requests, pandas where needed |
| Deployment target | Streamlit Community Cloud, AWS, Azure, or Hostinger VPS |
| Data policy | Use synthetic examples only; do not use confidential or real personal data |

---

## 1. Product summary

The HR Policy + Onboarding Assistant helps employees, new hires, managers, and HR operations teams answer common policy and onboarding questions. In MVP1, a Streamlit app accepts pasted HR policy or onboarding guide text, employee context, and a question. It calls OpenRouter to generate an employee-friendly answer, policy basis, next steps, approvals or documents needed, escalation flag, and draft message to HR or a manager.

The MVP is intentionally lightweight: no HRMS integration, no employee database, and no policy repository. It demonstrates the employee-support workflow with synthetic policies only.

## 2. Target users

| User | Need | MVP value |
|---|---|---|
| New Employee | Understand first-week tasks, tools, payroll, and benefits setup. | Gets a clear checklist and point-of-contact guidance. |
| Existing Employee | Ask about leave, WFH, travel, reimbursement, probation, or benefits. | Gets a simple answer and next steps. |
| People Manager | Guide team members without searching policy PDFs. | Gets manager-friendly guidance and approval notes. |
| HR Operations Team | Reduce repetitive policy questions. | Gets a demo of policy-grounded self-service. |

## 3. Problem statement

Employees often struggle to find HR answers scattered across PDFs, intranet pages, onboarding emails, and manager notes. HR teams repeatedly answer questions about leave carry-forward, remote work, reimbursements, probation, benefits, travel policy, and new-hire tasks. A friendly AI assistant can improve self-service while keeping final approvals with HR and managers.

## 4. MVP goal

- Build a Streamlit app where users paste HR policy or onboarding text.
- Accept employee context such as role, department, location, employment type, and joining stage.
- Allow users to ask HR policy or onboarding questions.
- Generate a simple employee-friendly answer with policy basis, next steps, approvals, escalation flag, and draft message.
- Use synthetic policies and sample employee contexts only.

## 5. Non-goals for MVP1

- No real employee data, payroll data, performance data, health data, or HR documents.
- No leave approval, reimbursement approval, payroll update, benefits enrollment, or HRMS workflow automation.
- No legal employment advice or final HR decision-making.
- No authentication, role-based HR data access, or enterprise policy repository in MVP1.
- No storage of employee questions or generated answers.

## 6. MVP user flow in Streamlit

1. User opens Streamlit app and selects a sample policy or onboarding guide from the sidebar.
2. User chooses policy category: leave, WFH, reimbursement, travel, benefits, probation, onboarding, or general HR.
3. User enters employee context in simple fields.
4. User asks a question in natural language.
5. User clicks Get HR Guidance.
6. App calls OpenRouter and requests structured JSON output.
7. App displays answer, policy basis, next steps, approvals or documents, HR escalation flag, draft message, and disclaimer.
8. User downloads a Markdown answer or copies the draft message.

## 7. Core features and requirements

| Feature | Priority | Streamlit requirement |
|---|---|---|
| Policy / onboarding input | P0 | `st.text_area` for HR policy or onboarding guide. |
| Employee context fields | P0 | `st.text_input` and `st.selectbox` for role, location, employment type, department, tenure/joining stage. |
| Question input | P0 | `st.text_area` for employee question. |
| Sample policy loader | P0 | `st.selectbox` loads synthetic leave, WFH, reimbursement, and onboarding examples. |
| Employee-friendly answer | P0 | Plain-language response displayed first. |
| Policy basis | P0 | Relevant policy summary or excerpt shown separately. |
| Next steps | P0 | Checklist of actions, approvals, documents, or deadlines. |
| HR escalation flag | P0 | Visible True/False with reason. |
| Draft message | P1 | Draft email or chat message to HR or manager. |
| New-hire checklist mode | P1 | If onboarding category is selected, render first-week checklist. |
| Download answer | P1 | `st.download_button` exports Markdown. |

## 8. Streamlit screen design

| Area | Components | Behavior |
|---|---|---|
| Sidebar | Sample policy selector, policy category selector, privacy warning. | Prefills synthetic examples and reinforces no real employee data. |
| Employee context | Role, location, department, employment type, joining date/tenure. | Context helps tailor next steps without accessing HRMS. |
| Policy and question | Large policy textarea and question textarea inside `st.form`. | Submit triggers validation and model call. |
| Answer card | `st.success` or `st.info` with direct answer. | Employee sees simple answer first. |
| Details | Policy basis, next steps, approvals, escalation, draft message in expanders. | Keeps answer readable for demo. |
| Actions | Download Markdown, clear session. | No persistence. |

## 9. AI prompt contract

- Use only the provided HR policy or onboarding text.
- Be clear, practical, and employee-friendly.
- Do not approve leave, reimbursements, benefits, remote work, or employment changes.
- Do not provide legal employment advice.
- Escalate unclear or sensitive cases to HR.
- Avoid biased, discriminatory, or invasive language.
- Always include a human HR review disclaimer.

## 10. Suggested response schema

```json
{
  "answer": "string",
  "policy_basis": ["string"],
  "next_steps": ["string"],
  "documents_or_approvals_needed": ["string"],
  "hr_escalation_required": true,
  "escalation_reason": "string",
  "draft_message": "string",
  "onboarding_checklist": ["string"],
  "disclaimer": "string"
}
```

## 11. Synthetic data examples

| Scenario | Synthetic HR text | Question |
|---|---|---|
| Leave carry-forward | Employees receive 18 annual leave days per calendar year. Up to 5 unused annual leave days may be carried forward to the next year. Carry-forward leave must be used by March 31. | I have 8 unused leave days. How many can I carry forward? |
| Remote work | Employees may work from home up to 2 days per week with manager approval. Remote work from another city for more than 5 working days requires HR approval. | Can I work remotely from another city for 2 weeks? |
| Onboarding | New hires must complete identity verification, payroll setup, laptop configuration, security training, benefits enrollment, and manager introduction during the first week. | I am joining as a Product Analyst next Monday. What should I complete in my first week? |
| Reimbursement | Employees may claim business travel expenses with valid receipts. Meal reimbursement is capped at Rs 1,500 per day for domestic travel. Claims must be submitted within 15 days of travel completion. | I spent Rs 2,200 on meals during one day of domestic travel. How much can I claim? |

## Technical architecture: Python + Streamlit

The MVP is implemented as a single Streamlit application with a thin OpenRouter client. The app keeps all data in the current browser session and does not persist user inputs unless the team intentionally adds storage after MVP1.

| Layer | MVP choice | Notes |
|---|---|---|
| UI framework | Streamlit | Use `st.text_area`, `st.selectbox`, `st.form`, `st.button`, `st.expander`, `st.download_button`. |
| Language | Python 3.10+ | Fast to build, easy for data-heavy enterprise workflows, simple deployment. |
| AI API | OpenRouter Chat Completions | Call through `requests` using `OPENROUTER_API_KEY` from environment variables or `st.secrets`. |
| State handling | `st.session_state` | Store selected sample, latest result, and UI status only. |
| Structured output | JSON-first prompt | Ask the model for JSON and render it into Streamlit sections and tables. |
| Storage | None for MVP1 | No database; outputs are copy/download only. |
| Deployment | Streamlit Cloud / AWS / Azure / Hostinger VPS | Vercel is not the preferred direct host for Streamlit apps. |

### Recommended repository structure

```
hr-policy-onboarding-assistant/
  app.py
  requirements.txt
  README.md
  .env.example
  src/
    openrouter_client.py
    prompts.py
    sample_data.py
    ui_helpers.py
    response_parser.py
  tests/
    test_prompt_contract.py
    test_sample_data.py
```

### requirements.txt for MVP1

```
streamlit
requests
python-dotenv
pandas
```

### OpenRouter client pattern

The team should keep the model call in a small helper function and avoid putting API keys in the UI code. For deployed Streamlit apps, use `st.secrets`. For local development, use `.env` or environment variables.

```python
import os
import requests
import streamlit as st

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def get_api_key() -> str:
    return st.secrets.get("OPENROUTER_API_KEY") or os.getenv("OPENROUTER_API_KEY", "")

def call_openrouter(messages, model=None, temperature=0.2):
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY is not configured.")
    payload = {
        "model": model or os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
        "messages": messages,
        "temperature": temperature,
    }
    response = requests.post(
        OPENROUTER_URL,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
```

### Streamlit UI implementation pattern

```python
with st.form("analysis_form"):
    primary_text = st.text_area("Primary document or input", height=220)
    scenario = st.text_area("Scenario / question", height=140)
    submitted = st.form_submit_button("Generate analysis")

if submitted:
    with st.spinner("Generating structured analysis..."):
        result = generate_analysis(primary_text, scenario)
        st.session_state["latest_result"] = result

if "latest_result" in st.session_state:
    st.subheader("AI-generated result")
    render_result(st.session_state["latest_result"])
    st.download_button("Download Markdown", to_markdown(st.session_state["latest_result"]), "report.md")
```

## Deployment plan for Streamlit

| Option | When to use | Deployment notes |
|---|---|---|
| Streamlit Community Cloud | Fastest demo deployment | Push to GitHub, add secrets, deploy app.py. Best for workshop demos. |
| AWS | Enterprise-friendly hosting | Use EC2, App Runner, ECS, or Elastic Beanstalk. Store API key in environment or Secrets Manager. |
| Azure | Enterprise-friendly hosting | Use Azure App Service or Container Apps. Store API key in App Settings or Key Vault. |
| Hostinger VPS | Simple VPS deployment | Run Streamlit behind Nginx with systemd or Docker; configure HTTPS. |
| Vercel | Not recommended for direct Streamlit | Use only if building a separate web frontend; Streamlit itself is better hosted elsewhere. |

## 12. Acceptance criteria

- User can run locally with `streamlit run app.py`.
- App loads at least four synthetic HR/onboarding policies.
- User can enter employee context and ask a question.
- Output includes answer, policy basis, next steps, documents or approvals, HR escalation flag, draft message, and disclaimer.
- AI does not approve leave, reimbursements, benefits, remote work, or employment decisions.
- Output can be downloaded as Markdown.
- App is deployed and demo-ready.

## 13. Risks and guardrails

| Risk | Guardrail |
|---|---|
| AI gives legal employment advice | Prompt and UI state that output is informational and HR must confirm decisions. |
| AI approves requests | Use next-step language and require manager/HR approval where relevant. |
| Real employee data is entered | Use synthetic examples only and no storage. |
| Bias or discriminatory output | Prompt requires neutral, inclusive, policy-based language. |
| Ambiguous policy | Escalate to HR and list missing information. |

## 2-hour Streamlit build plan

| Time | Activity | Owner suggestion |
|---|---|---|
| 0–15 min | Create Streamlit app skeleton, requirements, and HR privacy disclaimer. | Developer 1 |
| 15–30 min | Build sample policy loader and employee context form. | Developer 1 + 2 |
| 30–55 min | Implement OpenRouter client and HR prompt template. | Developer 2 |
| 55–80 min | Render answer, policy basis, next steps, escalation, and draft message. | Developer 3 |
| 80–100 min | Add onboarding checklist handling and Markdown download. | Developer 3 |
| 100–115 min | Test four synthetic scenarios and tune tone. | Developer 4 |
| 115–120 min | Deploy and prepare demo script. | All |

## MVP testing checklist

- App launches locally with `streamlit run app.py`.
- `OPENROUTER_API_KEY` is read from environment variables or `st.secrets`.
- At least three synthetic sample scenarios load correctly.
- Empty inputs produce friendly validation messages instead of API calls.
- AI response is rendered into cards, tables, or expanders rather than a raw wall of text.
- Copy/download output works without storing data on the server.
- The app shows a clear disclaimer and human-review guardrail.
- Deployed URL works from another browser session.

## Demo and judging criteria

| Criteria | Weight | Evidence in demo |
|---|---|---|
| Working deployed Streamlit app | 30% | Public or shareable URL; no local-only demo. |
| Clear enterprise workflow | 20% | User can understand the business problem within 30 seconds. |
| Quality of AI output | 25% | Structured, grounded, specific, and useful. |
| Responsible AI guardrails | 10% | Disclaimers, missing information, and human review are visible. |
| UX clarity | 10% | Input form, sample loader, and output sections are easy to follow. |
| Synthetic data use | 5% | No real customer, employee, patient, vendor, or regulated data. |
