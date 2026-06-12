"""Shared LangGraph state for the AI Goal Navigator."""

from typing import TypedDict


class NavigatorState(TypedDict, total=False):
    goal: str
    goal_analysis: str
    plan: str
    resources: str
    risks: str
    roadmap: str
