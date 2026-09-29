import asyncio
import sys
from datetime import datetime

from analyzer import analyze_match, find_technologies
from api import fetch_data
from storage import load_analyses, save_analysis

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


def history():
    analyses = load_analyses()

    if not analyses:
        print("No job analyses found.")
        return

    for data in analyses:
        source = data.get("source", data.get("file", "Unknown"))
        print(f"{source} - {data['match']}% - {data['analyzed_at']}")


def analyze_content(content, source):
    result = find_technologies(technologies, content)
    matched_skills, missing_skills = analyze_match(my_skills, result)
    if result:
        match_percentage = round(len(matched_skills) / len(result) * 100)
    else:
        match_percentage = 0

    job_analysis = {
        "source": source,
        "match": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "analyzed_at": datetime.now().isoformat(),
    }
    return job_analysis


def display_analysis(job_analysis):
    print("====== JOB MATCH ======\n")
    print("Your skills:")
    if not job_analysis["matched_skills"]:
        print("None")
    else:
        for skill in job_analysis["matched_skills"]:
            print(f"✓ {skill}")

    print("\nMissing:")
    if not job_analysis["missing_skills"]:
        print("None")
    else:
        for missing in job_analysis["missing_skills"]:
            print(f"✗ {missing}")

    print(f"\nMatch: {job_analysis['match']}%")
    print(f"Job analysis: {job_analysis}")


def analyze():
    if len(sys.argv) < 3:
        print("Usage: python main.py <path_to_job_description_file>")
        sys.exit(1)

    try:
        with open(sys.argv[2], "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {sys.argv[2]}")
        sys.exit(1)

    job_analysis = analyze_content(content, sys.argv[2])
    display_analysis(job_analysis)
    save_analysis(job_analysis)


async def analyze_api():
    if len(sys.argv) < 3:
        print("Usage: python main.py analyze-api <url>")
        return

    data = await fetch_data(sys.argv[2])
    if not data:
        print("No data fetched.")
        return
    body = data.get("body")
    if not body:
        print("No body fetched")
        return

    job_analysis = analyze_content(body, sys.argv[2])
    save_analysis(job_analysis)
    display_analysis(job_analysis)


if len(sys.argv) >= 2:
    command = sys.argv[1]

    if command == "analyze-api":
        asyncio.run(analyze_api())
    if command == "analyze":
        analyze()
    if command == "history":
        history()
