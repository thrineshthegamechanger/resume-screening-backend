from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import shutil
import os
from models.job_matcher import match_resume_with_jd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/match_bulk")
async def match_multiple_resumes(
    jd_text: str = Form(...),
    mandatory_skills: str = Form(...),
    resumes: List[UploadFile] = File(...)
):
    skills_list = [s.strip() for s in mandatory_skills.split(",")]
    results = []

    for resume in resumes:
        temp_file = f"temp_{resume.filename}"
        with open(temp_file, "wb") as f:
            shutil.copyfileobj(resume.file, f)

        match_result = match_resume_with_jd(jd_text, temp_file, skills_list)
        match_result["filename"] = resume.filename
        results.append(match_result)

        os.remove(temp_file)

    return {"results": results}
