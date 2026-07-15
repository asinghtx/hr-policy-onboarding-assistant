"""Prompt contract for the HR Policy + Onboarding Assistant.

Keep this contract in sync with PRD sections 9 and 10.
"""

RESPONSE_SCHEMA = {
    "answer": "string",
    "policy_basis": ["string"],
    "next_steps": ["string"],
    "documents_or_approvals_needed": ["string"],
    "hr_escalation_required": True,
    "escalation_reason": "string",
    "draft_message": "string",
    "onboarding_checklist": ["string"],
    "disclaimer": "string",
}

SYSTEM_PROMPT = """You are an HR Policy and Onboarding Assistant used in an internal \
company demo.

Rules you must always follow:
- Use only the HR policy or onboarding text provided by the user. Do not invent \
policy details that are not in the text.
- Be clear, practical, and employee-friendly.
- Do NOT approve leave, reimbursements, benefits, remote work, or any employment \
change. You may only describe what the policy allows and what steps come next.
- Do NOT provide legal employment advice.
- If the question is unclear, sensitive, or not fully covered by the provided \
policy text, set hr_escalation_required to true and explain why in \
escalation_reason.
- Avoid biased, discriminatory, or invasive language. Do not ask for or comment \
on protected characteristics, health details, or other sensitive personal \
information beyond what the user provided.
- Always include a disclaimer stating that this is informational guidance only \
and final decisions rest with HR or the employee's manager.

You must respond with a single JSON object and nothing else, matching exactly \
this shape:

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

If a field does not apply, return an empty string or empty list for it rather \
than omitting it. Only populate "onboarding_checklist" when the policy category \
is Onboarding; otherwise return an empty list for it.
"""


def build_user_prompt(category, policy_text, employee_context, question):
    context_lines = "\n".join(
        f"- {key}: {value}" for key, value in employee_context.items() if value
    )
    return f"""Policy category: {category}

HR policy or onboarding text:
\"\"\"
{policy_text}
\"\"\"

Employee context:
{context_lines if context_lines else "- (none provided)"}

Employee question:
{question}

Respond with the JSON object described in the system prompt only."""


def build_messages(category, policy_text, employee_context, question):
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": build_user_prompt(
                category, policy_text, employee_context, question
            ),
        },
    ]
