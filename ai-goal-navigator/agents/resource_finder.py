"""Learning resource recommendation agent."""

from models.ollama_model import llm
from state import NavigatorState


def resource_agent(state: NavigatorState) -> dict:
    prompt = f"""
Suggest resources for this goal:
{state['goal']}

Include:
- Books
- Courses
- Projects to build
- Communities to join
"""
    result = llm.invoke(prompt)
    return {"resources": result.content}
