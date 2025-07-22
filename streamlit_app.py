
import os
import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def calculate_similarity(resume_text, jd_text):
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100
    return round(score, 2)

def get_gpt_feedback(resume_text, jd_text):
    prompt = f"""
    Analyze the resume and job description below and provide 3 improvement suggestions.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}

    Suggestions:
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI Resume Analyzer")
st.markdown("Upload your resume and paste a job description to get a match score and AI suggestions.")

resume_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])
jd_text = st.text_area("Paste Job Description", height=200)

if st.button("Analyze") and resume_file and jd_text:
    with st.spinner("Processing..."):
        resume_text = extract_text_from_pdf(resume_file)
        score = calculate_similarity(resume_text, jd_text)
        feedback = get_gpt_feedback(resume_text, jd_text)

        st.success(f"✅ Resume Match Score: {score}%")
        st.markdown("### 💡 GPT Suggestions")
        st.markdown(f"```text\n{feedback}\n```")
