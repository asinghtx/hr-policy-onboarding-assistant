# HR Policy + Onboarding Assistant

A Streamlit demo app that answers HR policy and onboarding questions using
synthetic HR text, employee context, and an OpenRouter-backed LLM. Built for
a 2-hour Claude Code workshop — see `PRD_HR_Policy_Onboarding_Assistant.md`
for the full product spec.

**Demo only.** No real employee, payroll, health, or performance data. No
storage, no authentication, no HRMS integration. Outputs are informational
only — HR and managers make the final call.

## Setup

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and set your OpenRouter key:

   ```
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   OPENROUTER_MODEL=openai/gpt-4o-mini
   ```

## Run locally

```bash
streamlit run app.py
```

Open the local URL Streamlit prints (default `http://localhost:8501`).

## Run tests

```bash
pip install pytest
pytest tests/
```

## Project structure

```
app.py                       Streamlit UI and orchestration
src/
  openrouter_client.py       Thin OpenRouter Chat Completions client
  prompts.py                 System prompt contract + message builder
  sample_data.py             Synthetic HR policy/onboarding samples
  response_parser.py         Parses and normalizes the model's JSON output
  ui_helpers.py               Renders results, builds Markdown export
tests/
  test_prompt_contract.py
  test_sample_data.py
```

## Deployment

Recommended for the workshop: [Streamlit Community Cloud](https://streamlit.io/cloud).

1. Push this repo to GitHub (do not commit `.env`).
2. Create a new app on Streamlit Community Cloud pointing at `app.py`.
3. In the app's Secrets settings, add:
   ```
   OPENROUTER_API_KEY = "..."
   OPENROUTER_MODEL = "openai/gpt-4o-mini"
   ```

AWS, Azure, and Hostinger VPS are also viable (see the PRD's deployment
plan). Vercel is not recommended for hosting Streamlit directly.
