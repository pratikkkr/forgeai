from tools.github_tool import get_issue
from agents.planner import plan_issue

# Step 1 - Fetch the issue
issue_url = "https://github.com/tiangolo/fastapi/issues/1"
print("🔍 Fetching GitHub issue...\n")
issue = get_issue(issue_url)
print(f"Title: {issue['title']}\n")

# Step 2 - Plan the fix
print("🧠 Planner Agent is thinking...\n")
plan = plan_issue(issue)
print("📋 PLAN:\n")
print(plan)