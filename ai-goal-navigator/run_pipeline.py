"""Run the workflow with a mocked LLM and print JSON output."""
import json
from types import SimpleNamespace

import models.ollama_model as ollama_model
from graph.workflow import graph


class MockLLM:
    def invoke(self, prompt: str):
        prompt_lower = prompt.lower()
        if "analyze the goal" in prompt_lower:
            content = (
                "Goal Type: Career\n"
                "Required Skills: Python, ML fundamentals, Data Structures\n"
                "Expected Timeline: 6 months\n"
                "Prerequisites: Basic programming experience\n"
            )
        elif "create milestones" in prompt_lower:
            content = (
                "Phase 1 (Weeks 1-4): Fundamentals and Python refresher\n"
                "Phase 2 (Weeks 5-12): Core ML concepts and projects\n"
                "Weekly checkpoints: Learn X, implement Y, review Z\n"
            )
        elif "suggest resources" in prompt_lower:
            content = (
                "Books: Hands-On Machine Learning, Deep Learning with Python\n"
                "Courses: Andrew Ng ML, fast.ai Practical Deep Learning\n"
                "Projects: Kaggle starter projects, personal portfolio\n"
            )
        elif "analyze risks" in prompt_lower:
            content = (
                "Top risks: Burnout, scope creep, unclear goals\n"
                "Mitigation: Timeboxing, mentorship, measurable metrics\n"
            )
        elif "generate a final roadmap" in prompt_lower:
            content = (
                "30/60/90 Day Plan:\n30-day: Basics and small projects\n60-day: Intermediate projects and networking\n90-day: Portfolio and interview prep\n"
                "Weekly action list: 5-10 concrete tasks per week\n"
                "Success metrics: projects completed, interviews booked\n"
            )
        else:
            content = "(mock response)"

        return SimpleNamespace(content=content)


def main():
    # Replace the real llm with the mock
    ollama_model.llm = MockLLM()

    sample_goal = "Become an AI Engineer in 6 months"
    result = graph.invoke({"goal": sample_goal})

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
