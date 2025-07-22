import openai
import os

def get_gpt_feedback(resume_text, job_desc):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""You are a career coach. Analyze the resume text below and compare it to the job description.
Provide specific improvement suggestions.

Resume:
{resume_text}

Job Description:
{job_desc}

Suggestions:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
