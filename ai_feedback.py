import os
from openai import OpenAI

def get_gpt_feedback(resume_text, job_desc):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # ✅ Don't hardcode here

    prompt = f"""
    You are a resume expert. Analyze the following resume and job description. 
    Give feedback on how well they match, and suggest improvements.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
