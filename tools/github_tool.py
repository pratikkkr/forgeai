import requests
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_issue(issue_url: str) -> dict:
    """
    Takes a GitHub issue URL and returns issue details.
    Example URL: https://github.com/owner/repo/issues/42
    """
    # Parse the URL
    parts = issue_url.rstrip("/").split("/")
    owner = parts[-4]
    repo = parts[-3]
    issue_number = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"GitHub API error: {response.status_code} - {response.text}")

    data = response.json()

    return {
        "title": data["title"],
        "body": data["body"],
        "state": data["state"],
        "author": data["user"]["login"],
        "labels": [label["name"] for label in data["labels"]],
        "url": issue_url
    }