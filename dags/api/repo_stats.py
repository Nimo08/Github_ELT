import json
import requests
from datetime import date, datetime

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


# Print the repo names on the terminal
def get_repo():
    
    try:
        org_name = "openai"
        url = f"https://api.github.com/orgs/{org_name}/repos"

        response = requests.get(url)

        response.raise_for_status()
        data = response.json()

        # repo_names = [repo["name"] for repo in data]

        # for name in repo_names:
        #     print(f" - {name}")
        
        return data
    
    except requests.exceptions.RequestException as e:
        raise e
    

# Get the repo commits
def get_commits():

    try:
        org_name = "openai"
        repo_name = "codex"
        url = f"https://api.github.com/repos/{org_name}/{repo_name}/commits"
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # commit_ids = [commit["sha"] for commit in data]

        # for author in commit_ids:
        #     print(f" - {author}")
        
        return data
    
    except requests.exceptions.RequestException as e:
        raise e

# Get pull requests
def get_pull_requests():

    try:
        org_name = "openai"
        repo_name = "codex"
        url = f"https://api.github.com/repos/{org_name}/{repo_name}/pulls"
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # pull_requests = [pull_request["title"] for pull_request in data]

        # for title in pull_requests:
        #     print(f" - {title}")
        
        return data

    except requests.exceptions.RequestException as e:
        raise e

# Get issues
def get_issues():

    try:
        org_name = "openai"
        repo_name = "codex"
        url = f"https://api.github.com/repos/{org_name}/{repo_name}/issues"
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # issues = [issue["state"] for issue in data]

        # for state in issues:
        #     print(f" - {state}")
        
        return data

    except requests.exceptions.RequestException as e:
        raise e
    
# Get forks
def get_forks():

    try:
        org_name = "openai"
        repo_name = "codex"
        url = f"https://api.github.com/repos/{org_name}/{repo_name}/forks"
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        forks = [fork["name"] for fork in data]

        # for name in forks:
        #     print(f" - {name}")
        
        return data

    except requests.exceptions.RequestException as e:
        raise e

# Save to json
def save_to_json(**data):

    for key, value in data.items():
        file_path = f"./data/github_{key}.{datetime.today()}.json"
        # try:
        with open(file_path, "w",encoding="utf-8") as json_file:
            json.dump(value, json_file, indent=4, ensure_ascii=False)
        
            # return data
        
        # except Exception as e:
        #     print(f"Error saving {key}: {e}")


if __name__ == "__main__":

    repos = get_repo()
    commits = get_commits()
    pull_requests = get_pull_requests()
    issues = get_issues()
    forks = get_forks()
    save_to_json(
        repos=repos,
        pull_requests=pull_requests,
        commits=commits,
        issues=issues,
        forks=forks)
