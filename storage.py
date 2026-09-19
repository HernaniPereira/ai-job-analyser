import json


def save_analysis(job_analysis):
    try:
        with open("jobs.json", "r") as jobs_file:
            jobs = json.load(jobs_file)
    except (FileNotFoundError, json.JSONDecodeError):
        jobs = []

    jobs.append(job_analysis)

    with open("jobs.json", "w") as jobs_file:
        json.dump(jobs, jobs_file, indent=2)


def load_analyses():
    try:
        with open("jobs.json", "r") as jobs_file:
            jobs = json.load(jobs_file)
    except (FileNotFoundError, json.JSONDecodeError):
        jobs = []
    return jobs
