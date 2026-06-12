"""Goal analysis agent."""

from models.ollama_model import llm
from state import NavigatorState


def goal_analyzer(state: NavigatorState) -> dict:
    prompt = f"""
Analyze the goal.

Goal:
{state['goal']}

Extract:
1. Goal Type
2. Required Skills
3. Expected Timeline
4. Prerequisites and constraints
"""
    result = llm.invoke(prompt)
    return {"goal_analysis": result.content}
