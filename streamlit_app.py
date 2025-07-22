
import os
import streamlit as st
import pdfplumber
from dotenv import load_dotenv
from resume_parser import extract_text_from_pdf
from match_engine import calculate_similarity
from ai_feedback import get_gpt_feedback

load_dotenv()

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer")

st.write("Upload your resume and paste a job description to get a match score and AI-powered suggestions.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description Here", height=200)

if st.button("Analyze"):
    if resume_file and job_desc:
        resume_text = extract_text_from_pdf(resume_file)
        score = calculate_similarity(resume_text, job_desc)
        feedback = get_gpt_feedback(resume_text, job_desc)

        st.markdown(f"### ✅ Match Score: `{score}%`")
        st.markdown("### 💡 GPT Suggestions:")
        st.success(feedback)
    else:
        st.warning("Please upload a resume and enter job description.")
