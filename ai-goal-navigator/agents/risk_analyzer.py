"""Risk and blocker analysis agent."""

from models.ollama_model import llm
from state import NavigatorState


def risk_agent(state: NavigatorState) -> dict:
    prompt = f"""
Analyze risks and blockers for this goal:
{state['goal']}

Provide:
- Top risks
- Why each risk matters
- Mitigation steps
"""
    result = llm.invoke(prompt)
    return {"risks": result.content}
