def find_technologies(technologies, file_content):
    tech_found = []
    normalized_content = file_content.lower()
    for tech in technologies:
        if tech.lower() in normalized_content:
            tech_found.append(tech)
    return tech_found


def analyze_match(my_skills, result):
    matched_skills = [matched for matched in my_skills if matched in result]
    missing_skills = [missing for missing in result if missing not in my_skills]
    return matched_skills, missing_skills
