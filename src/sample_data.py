"""Synthetic HR policy and onboarding samples for the workshop demo.

All text below is fictional and for demo purposes only. Do not replace
with real employee data or confidential company policy.
"""

POLICY_CATEGORIES = [
    "Leave",
    "WFH",
    "Reimbursement",
    "Travel",
    "Benefits",
    "Probation",
    "Onboarding",
    "General HR",
]

EMPLOYMENT_TYPES = ["Full-time", "Part-time", "Contractor", "Intern"]

JOINING_STAGES = [
    "Pre-joining",
    "First week",
    "First month",
    "Probation (1-6 months)",
    "Confirmed employee",
]

SAMPLE_POLICIES = {
    "Leave carry-forward": {
        "category": "Leave",
        "policy_text": (
            "Employees receive 18 annual leave days per calendar year. "
            "Up to 5 unused annual leave days may be carried forward to the "
            "next year. Carry-forward leave must be used by March 31."
        ),
        "sample_question": "I have 8 unused leave days. How many can I carry forward?",
    },
    "Remote work": {
        "category": "WFH",
        "policy_text": (
            "Employees may work from home up to 2 days per week with manager "
            "approval. Remote work from another city for more than 5 working "
            "days requires HR approval."
        ),
        "sample_question": "Can I work remotely from another city for 2 weeks?",
    },
    "Onboarding first week": {
        "category": "Onboarding",
        "policy_text": (
            "New hires must complete identity verification, payroll setup, "
            "laptop configuration, security training, benefits enrollment, "
            "and manager introduction during the first week."
        ),
        "sample_question": (
            "I am joining as a Product Analyst next Monday. "
            "What should I complete in my first week?"
        ),
    },
    "Travel reimbursement": {
        "category": "Reimbursement",
        "policy_text": (
            "Employees may claim business travel expenses with valid receipts. "
            "Meal reimbursement is capped at Rs 1,500 per day for domestic "
            "travel. Claims must be submitted within 15 days of travel "
            "completion."
        ),
        "sample_question": (
            "I spent Rs 2,200 on meals during one day of domestic travel. "
            "How much can I claim?"
        ),
    },
    "International travel approval": {
        "category": "Travel",
        "policy_text": (
            "Employees traveling for business must book travel through the "
            "approved travel portal at least 5 business days in advance. "
            "International travel requires VP approval regardless of trip "
            "length. Travel insurance is provided automatically for trips "
            "over 3 days."
        ),
        "sample_question": (
            "I'm traveling internationally for a 2-day conference next week. "
            "Do I need VP approval?"
        ),
    },
    "Adding a dependent to benefits": {
        "category": "Benefits",
        "policy_text": (
            "Employees are eligible for group health insurance from day one "
            "of employment. Dependents can be added within 30 days of joining "
            "or during the annual open enrollment window in November. Adding "
            "a dependent outside these windows requires a qualifying life "
            "event such as marriage or birth of a child."
        ),
        "sample_question": (
            "I got married last month. Can I add my spouse to my health "
            "insurance now?"
        ),
    },
    "Leave accrual during probation": {
        "category": "Probation",
        "policy_text": (
            "New employees serve a probation period of 3 months from their "
            "joining date. Probation may be extended once by up to 3 months "
            "at the manager's discretion. Employees on probation accrue 1 "
            "paid leave day per month; unused probation leave does not carry "
            "forward past confirmation."
        ),
        "sample_question": (
            "I'm on probation and have been here 6 weeks. How many leave "
            "days have I accrued so far?"
        ),
    },
    "Updating work location": {
        "category": "General HR",
        "policy_text": (
            "Employees may request a change to their registered work "
            "location, job title, or reporting manager through the HR "
            "portal. Any change to compensation or designation requires "
            "manager and HR Business Partner approval and takes effect from "
            "the start of the next payroll cycle."
        ),
        "sample_question": (
            "I want to update my work location in the system. What do I "
            "need to do?"
        ),
    },
}


def get_sample_names():
    return list(SAMPLE_POLICIES.keys())


def get_sample(name):
    return SAMPLE_POLICIES.get(name)
