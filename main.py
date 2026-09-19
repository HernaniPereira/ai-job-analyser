import json
import sys
from datetime import datetime

from analyzer import analyze_match, find_technologies

technologies = [
    "Python",
    "FastAPI",
    "Docker",
    "Azure",
    "LLM",
    "RAG",
    "React",
]

my_skills = [
    "React Native",
    "TypeScript",
    "React",
    "Git",
    "Jest",
    "Python",
]


if len(sys.argv) < 2:
    print("Usage: python main.py <path_to_job_description_file>")
    sys.exit(1)


try:
    with open(sys.argv[1], "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")
    sys.exit(1)


result = find_technologies(technologies, content)
matched_skills, missing_skills = analyze_match(my_skills, result)

print("====== JOB MATCH ======\n")
print("Your skills:")
if not matched_skills:
    print("None")
else:
    for skill in matched_skills:
        print(f"✓ {skill}")


print("\nMissing:")
if not missing_skills:
    print("None")
else:
    for missing in missing_skills:
        print(f"✗ {missing}")


if result:
    match_percentage = round(len(matched_skills) / len(result) * 100)
else:
    match_percentage = 0

job_analysis = {
    "file": sys.argv[1],
    "match": match_percentage,
    "matched_skills": matched_skills,
    "missing_skills": missing_skills,
    "analyzed_at": datetime.now().isoformat(),
}

print(f"\nMatch: {match_percentage}%")
print(f"Job analysis: {job_analysis}")

try:
    with open("jobs.json", "r") as jobs_file:
        jobs = json.load(jobs_file)
except (FileNotFoundError, json.JSONDecodeError):
    jobs = []

jobs.append(job_analysis)

with open("jobs.json", "w") as jobs_file:
    json.dump(jobs, jobs_file, indent=2)
