import sys
from datetime import datetime

from analyzer import analyze_match, find_technologies
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
        print(f"{data['file']} - {data['match']}% - {data['analyzed_at']}")


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
        "file": sys.argv[2],
        "match": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "analyzed_at": datetime.now().isoformat(),
    }

    print(f"\nMatch: {match_percentage}%")
    print(f"Job analysis: {job_analysis}")

    save_analysis(job_analysis)


if len(sys.argv) >= 2:
    command = sys.argv[1]

    if command == "analyze":
        analyze()
    if command == "history":
        history()
