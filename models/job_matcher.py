from utils.pdf_parser import extract_text_from_pdf
from utils.docx_parser import extract_text_from_docx
from utils.skill_matcher import extract_skills
from utils.text_similarity import calculate_similarity

def match_resume_with_jd(jd_text, resume_file_path, skill_list):
    if resume_file_path.endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_file_path)
    elif resume_file_path.endswith(".docx"):
        resume_text = extract_text_from_docx(resume_file_path)
    else:
        return {"error": "Unsupported file type"}

    sim_score = calculate_similarity(jd_text, resume_text)
    jd_skills = extract_skills(jd_text, skill_list)
    resume_skills = extract_skills(resume_text, skill_list)

    matched_skills = list(set(jd_skills) & set(resume_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))
    all_mandatory_present = len(missing_skills) == 0

    return {
        "match_percentage": round(sim_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "all_mandatory_skills_present": all_mandatory_present
    }
