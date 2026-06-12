# 🧭 AI Goal Navigator

An Agentic AI-powered planning assistant that transforms career goals and startup ideas into structured roadmaps using multiple AI agents and LangGraph workflows.

## 🚀 Overview

AI Goal Navigator helps users convert ambitious goals into actionable execution plans.

Whether you want to:

- Become an AI Engineer
- Crack a Product-Based Company Interview
- Launch a Startup
- Build a SaaS Product
- Learn Data Science

The system analyzes the goal, creates milestones, recommends resources, identifies risks, and generates a complete roadmap.

---

## ✨ Features

### 🎯 Goal Analysis Agent
Analyzes the user's goal and extracts:

- Goal Type
- Required Skills
- Timeline
- Prerequisites
- Constraints

### 📋 Planning Agent
Creates:

- Milestones
- Weekly Checkpoints
- Learning Phases
- Execution Strategy

### 📚 Resource Recommendation Agent
Suggests:

- Online Courses
- Books
- Communities
- Projects
- Learning Resources

### ⚠️ Risk Analysis Agent
Identifies:

- Common Challenges
- Skill Gaps
- Potential Blockers
- Mitigation Strategies

### 🛣️ Roadmap Generation Agent
Combines all outputs into:

- 30-Day Plan
- 60-Day Plan
- 90-Day Plan
- Weekly Action Items
- Success Metrics

---

## 🏗️ Architecture

```text
User Goal
    │
    ▼
Goal Analyzer Agent
    │
    ▼
Planning Agent
    │
    ▼
Resource Finder Agent
    │
    ▼
Risk Analyzer Agent
    │
    ▼
Roadmap Generator Agent
    │
    ▼
Final Personalized Roadmap
```

---

## 🧠 Tech Stack

- Python
- LangGraph
- LangChain
- Streamlit
- Ollama
- Qwen 3 / Llama 3 Models

---

## 📂 Project Structure

```text
ai-goal-navigator/
│
├── agents/
│   ├── goal_analyzer.py
│   ├── planner.py
│   ├── resource_finder.py
│   ├── risk_analyzer.py
│   └── roadmap_generator.py
│
├── graph/
│   └── workflow.py
│
├── models/
│   └── ollama_model.py
│
├── state.py
├── app.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ai-goal-navigator.git
cd ai-goal-navigator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🦙 Setup Ollama

Install Ollama:

https://ollama.com

Pull a model:

```bash
ollama pull qwen3:8b
```

or

```bash
ollama pull llama3
```

Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run the Application

Launch Streamlit:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 💡 Example Input

```text
Become an AI Engineer in 6 months
```

### Output

- Goal Analysis
- Milestone Plan
- Recommended Resources
- Risk Assessment
- 30/60/90 Day Roadmap

---

## 🎯 Use Cases

### Career Planning

- AI Engineer
- Data Scientist
- Software Engineer
- Product Manager

### Startup Planning

- SaaS Products
- AI Startups
- Mobile Applications
- Web Platforms

### Skill Development

- Machine Learning
- Data Science
- Full Stack Development
- Cloud Computing

---

## 📈 Future Improvements

- Internet Resource Search
- YouTube Course Recommendations
- Resume Analyzer
- Job Matching System
- Progress Tracking Dashboard
- Multi-Goal Planning
- Export Roadmaps to PDF

---

## 🎓 Learning Outcomes

This project demonstrates:

- Agentic AI Systems
- Multi-Agent Collaboration
- LangGraph Workflows
- State Management
- AI Planning Systems
- Streamlit Deployment

---

## 👨‍💻 Author

**Tejdeep Munjampally**

B.Tech Student | AI Engineer | Software Developer

GitHub: https://github.com/tejdeepmunjampally
