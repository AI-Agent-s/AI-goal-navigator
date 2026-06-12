"""Safer runner that injects a mocked models.ollama_model before importing the workflow."""
import sys
import types
import json


class MockLLM:
    def invoke(self, prompt: str):
        p = prompt.lower()
        if "analyze the goal" in p:
            return types.SimpleNamespace(content="Goal Type: Career\nRequired Skills: Python, ML fundamentals\nExpected Timeline: 6 months\n")
        if "create milestones" in p:
            return types.SimpleNamespace(content="Phase 1: Weeks 1-4 - basics\nPhase 2: Weeks 5-12 - projects\n")
        if "suggest resources" in p:
            return types.SimpleNamespace(content="Books: Hands-On ML; Courses: Andrew Ng; Projects: portfolio")
        if "analyze risks" in p:
            return types.SimpleNamespace(content="Top risks: burnout, scope creep\nMitigation: timeboxing, mentors")
        if "generate a final roadmap" in p:
            return types.SimpleNamespace(content="30/60/90 Day Plan:\n30-day: basics\n60-day: projects\n90-day: portfolio\nWeekly actions and metrics")
        return types.SimpleNamespace(content="(mock)")


def main():
    mock_mod = types.ModuleType("models.ollama_model")
    mock_mod.llm = MockLLM()

    # Inject before importing agents to avoid real LLM initialization
    sys.modules["models.ollama_model"] = mock_mod

    # Import agents directly and run them in sequence to avoid langgraph dependency
    from agents.goal_analyzer import goal_analyzer
    from agents.planner import planner
    from agents.resource_finder import resource_agent
    from agents.risk_analyzer import risk_agent
    from agents.roadmap_generator import roadmap_agent

    state = {"goal": "Become an AI Engineer in 6 months"}

    ga = goal_analyzer(state)
    state.update(ga)

    pl = planner(state)
    state.update(pl)

    rs = resource_agent(state)
    state.update(rs)

    rk = risk_agent(state)
    state.update(rk)

    rd = roadmap_agent(state)
    state.update(rd)

    print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()
