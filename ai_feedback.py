import streamlit as st
from openai import OpenAI

def get_gpt_feedback(resume_text, job_desc):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    prompt = f"""
    You are a professional career coach. A candidate submitted the following resume:\n\n{resume_text}\n\n
    They are applying for the following job:\n\n{job_desc}\n\n
    Provide specific, constructive feedback on how to improve their resume for this role.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
