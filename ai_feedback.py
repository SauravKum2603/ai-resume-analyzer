import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_gpt_feedback(resume_text, job_desc):
    prompt = f"Compare this resume to the job description and suggest improvements:\n\nResume:\n{resume_text}\n\nJob Description:\n{job_desc}"

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # ✅ change to this if gpt-4 gives error
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error from OpenAI API: {e}"
