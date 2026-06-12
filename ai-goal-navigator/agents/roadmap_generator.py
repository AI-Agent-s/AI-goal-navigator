"""Final roadmap synthesis agent."""

from models.ollama_model import llm
from state import NavigatorState


def roadmap_agent(state: NavigatorState) -> dict:
    prompt = f"""
Generate a final roadmap from the following sections.

Goal Analysis:
{state.get('goal_analysis', '')}

Plan:
{state.get('plan', '')}

Resources:
{state.get('resources', '')}

Risks:
{state.get('risks', '')}

Output format:
1. 30/60/90 day plan
2. Weekly action list
3. Success metrics
"""
    result = llm.invoke(prompt)
    return {"roadmap": result.content}
