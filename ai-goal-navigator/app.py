"""Streamlit app for AI Goal Navigator."""

import streamlit as st

from graph.workflow import graph

st.set_page_config(page_title="AI Goal Navigator", page_icon="🧭", layout="wide")

st.title("AI Goal Navigator")
st.caption("Agentic planning assistant for career goals and startup ideas")

goal = st.text_area(
    "Enter Career Goal or Startup Idea",
    placeholder="Example: Become an AI Engineer in 6 months",
    height=120,
)

if st.button("Generate Roadmap", type="primary"):
    if not goal.strip():
        st.warning("Please enter a goal first.")
    else:
        with st.spinner("Running agents: analysis -> planning -> resources -> risks -> roadmap"):
            result = graph.invoke({"goal": goal.strip()})

        st.subheader("Final Roadmap")
        st.markdown(result.get("roadmap", "No roadmap was generated."))

        with st.expander("Goal Analysis"):
            st.markdown(result.get("goal_analysis", ""))

        with st.expander("Plan"):
            st.markdown(result.get("plan", ""))

        with st.expander("Resources"):
            st.markdown(result.get("resources", ""))

        with st.expander("Risks"):
            st.markdown(result.get("risks", ""))
