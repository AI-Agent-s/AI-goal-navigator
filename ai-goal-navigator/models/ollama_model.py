"""Ollama LLM configuration for the AI Goal Navigator."""

import os
from typing import List

import requests
from langchain_ollama import OllamaLLM

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


class MockResponse:
    """Simple mock response object."""
    def __init__(self, text: str):
        self.content = text


class MockLLM:
    """Mock LLM for development/testing when Ollama is unavailable."""
    
    def invoke(self, prompt: str) -> MockResponse:
        """Return a mock response based on the prompt."""
        # Generate contextual mock responses
        if "Analyze" in prompt or "analyze" in prompt:
            return MockResponse("**Goal Type:** Career Development\n**Required Skills:** Python, Systems Design\n**Timeline:** 6 months\n**Prerequisites:** Basic programming knowledge")
        elif "milestone" in prompt.lower() or "plan" in prompt.lower():
            return MockResponse("**Phase 1 (Weeks 1-4):** Learn fundamentals\n**Phase 2 (Weeks 5-8):** Build first project\n**Phase 3 (Weeks 9-12):** Advanced topics\n**Weekly Checkpoints:** Every Friday")
        elif "resource" in prompt.lower() or "suggest" in prompt.lower():
            return MockResponse("**Books:** Python Crash Course, Fluent Python\n**Courses:** CS50, FastAPI tutorial\n**Projects:** Build a CLI tool, REST API\n**Communities:** Python Discord, Reddit r/learnprogramming")
        elif "risk" in prompt.lower():
            return MockResponse("**Risk 1:** Time management - Work 40+ hours\n**Mitigation:** Schedule 1 hour daily\n**Risk 2:** Concept complexity\n**Mitigation:** Start with basics, practice daily")
        else:
            return MockResponse(f"Generated response for: {prompt[:50]}...")


def _available_models(base_url: str) -> List[str]:
    try:
        response = requests.get(f"{base_url}/api/tags", timeout=2)
        response.raise_for_status()
        models = response.json().get("models", [])
        return [model.get("name", "") for model in models if model.get("name")]
    except Exception:
        return []


def _select_model() -> str:
    preferred = os.getenv("OLLAMA_MODEL", "qwen3:8b")
    installed = set(_available_models(OLLAMA_BASE_URL))

    candidates = [
        preferred,
        "qwen3:8b",
        "llama3:latest",
        "phi3:latest",
        "phi3:mini",
    ]

    for candidate in candidates:
        if candidate in installed:
            return candidate

    # If Ollama is unreachable or list cannot be read, keep user's preferred model.
    return preferred


def _get_llm():
    """Initialize LLM, falling back to mock if Ollama unavailable."""
    use_real_ollama = os.getenv("USE_OLLAMA", "false").lower() in ("true", "1", "yes")
    
    if not use_real_ollama:
        print("[INFO] Using mock LLM (development mode). Set USE_OLLAMA=true to use real Ollama.")
        return MockLLM()
    
    try:
        # Check if Ollama is reachable
        requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=2)
        print(f"[OK] Connected to Ollama at {OLLAMA_BASE_URL}")
        return OllamaLLM(
            model=_select_model(),
            base_url=OLLAMA_BASE_URL,
            temperature=0.3,
        )
    except Exception as e:
        print(f"[WARNING] Ollama unavailable ({type(e).__name__}). Falling back to mock LLM.")
        return MockLLM()


llm = _get_llm()
