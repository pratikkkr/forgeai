from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def plan_issue(issue: dict) -> str:
    prompt = f"""
You are ForgeAI's Planner Agent — a senior software engineer.

You have been given a GitHub issue. Your job is to create a clear,
step-by-step plan to resolve this issue.

ISSUE TITLE: {issue['title']}
ISSUE AUTHOR: {issue['author']}
ISSUE BODY:
{issue['body']}

Respond with:
1. A brief understanding of the issue (2-3 lines)
2. A numbered step-by-step plan to fix it (be specific and technical)
3. Files that will likely need to be created or modified
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.choices[0].message.content