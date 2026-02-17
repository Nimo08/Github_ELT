from airflow.decorators import dag, task
from airflow.providers.standard.operators.empty import EmptyOperator
import pendulum
from datetime import datetime, timedelta
from api.repo_stats import get_repo, get_commits, get_pull_requests, get_forks, get_issues, save_to_json


# Define the local timezone
local_tz = pendulum.timezone("Africa/Nairobi")


# Default Args
default_args = {
    "owner": "dataengineers",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "data@engineers.com",
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
    "max_active_runs": 1,
    "dagrun_timeout": timedelta(hours=1),
    "start_date": datetime(2025, 1, 1, tzinfo=local_tz),
    # 'end_date': datetime(2030, 12, 31, tzinfo=local_tz),
}


@dag(
        start_date=datetime(2026,2,1),
        schedule="@daily",
        catchup=False,
        )
def github_extraction_dag():

    @task
    def extract_repo():
        return get_repo()

    @task
    def extract_commits():
        return get_commits()
    
    @task
    def extract_pull_requests():
        return get_pull_requests()
    
    @task
    def extract_issues():
        return get_issues()

    @task
    def extract_forks():
        return get_forks()

    @task
    def save_data(repos, commits, pull_requests, issues, forks):
        save_to_json(
            repos=repos,
            commits=commits,
            pull_requests=pull_requests,
            issues=issues,
            forks=forks,
        )


    # Define task dependencies
    repo_names = extract_repo()

    # Run extractions in parallel
    commits = extract_commits()
    pull_requests = extract_pull_requests()
    issues = extract_issues()
    forks = extract_forks()

    save_data(repos=repo_names,
              commits=commits,
              pull_requests=pull_requests,
              issues=issues,
              forks=forks)

github_extraction_dag()

