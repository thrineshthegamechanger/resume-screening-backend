from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from model.job_matcher import match_resume_to_jd

app = FastAPI()

@app.get("/")
def root():
    return {"status": "App is running"}

@app.post("/match_bulk")
async def match_bulk(
    jd_file: UploadFile = File(...),
    resumes: List[UploadFile] = File(...),
    mandatory_skills: str = Form(...)
):
    skills = [s.strip() for s in mandatory_skills.split(",") if s.strip()]
    results = match_resume_to_jd(jd_file, resumes, skills)
    return {"results": results}