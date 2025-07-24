def extract_skills(text, skill_list):
    text = text.lower()
    found_skills = [skill for skill in skill_list if skill.lower() in text]
    return found_skills
