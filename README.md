# ForgeAI 🔥
### Autonomous Software Engineering Agent

> Give it a GitHub issue. It plans, codes, tests, and raises a PR. Autonomously.

---

## What is ForgeAI?

ForgeAI is a multi-agent AI system that autonomously resolves GitHub issues.
A user pastes a GitHub issue URL and ForgeAI kicks off a pipeline of specialized
AI agents that read, plan, code, test, review, and raise a Pull Request — with
zero human intervention.

---

## Agent Pipeline

| Agent | Role |
|---|---|
| 🧠 Planner Agent | Reads the issue, creates a step-by-step fix plan |
| 💻 Coder Agent | Writes the actual code changes |
| 🧪 Tester Agent | Writes and runs unit tests |
| 🔍 Reviewer Agent | Reviews code like a senior developer |
| 📬 PR Agent | Raises a GitHub PR with description and labels |

---

## Tech Stack

- **AI** — Google Gemini API
- **Backend** — FastAPI
- **Frontend** — React + TypeScript
- **Vector DB** — ChromaDB
- **Infra** — Docker, Redis

---

## Status

🚧 Currently in active development — Phase 1 (Core Agent Loop)