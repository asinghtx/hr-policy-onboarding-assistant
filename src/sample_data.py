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
}


def get_sample_names():
    return list(SAMPLE_POLICIES.keys())


def get_sample(name):
    return SAMPLE_POLICIES.get(name)
