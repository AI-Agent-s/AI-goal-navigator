"""Milestone planner agent."""

from models.ollama_model import llm
from state import NavigatorState


def planner(state: NavigatorState) -> dict:
    prompt = f"""
Create milestones for this goal:
{state['goal']}

Use a phased plan with weekly checkpoints.
"""
    result = llm.invoke(prompt)
    return {"plan": result.content}
