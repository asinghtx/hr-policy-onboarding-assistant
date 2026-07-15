"""Thin OpenRouter Chat Completions client.

Keep API keys out of UI code: use st.secrets when deployed, or a local
.env / environment variable when developing.
"""

import os

import requests
import streamlit as st

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-4o-mini"
REQUEST_TIMEOUT_SECONDS = 60


def get_api_key() -> str:
    try:
        secret_key = st.secrets.get("OPENROUTER_API_KEY")
    except Exception:
        secret_key = None
    return secret_key or os.getenv("OPENROUTER_API_KEY", "")


def call_openrouter(messages, model=None, temperature=0.2):
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not configured. Set it in .env for local "
            "development or in st.secrets for deployment."
        )

    payload = {
        "model": model or os.getenv("OPENROUTER_MODEL", DEFAULT_MODEL),
        "messages": messages,
        "temperature": temperature,
        "response_format": {"type": "json_object"},
    }

    response = requests.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
