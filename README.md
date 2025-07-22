
# 📄 AI Resume Analyzer (Streamlit Version)

Deployable AI resume analyzer that compares your resume with job descriptions and provides GPT-3.5 powered suggestions.

## 🛠 Tech Stack
- Streamlit
- OpenAI GPT
- pdfplumber
- scikit-learn

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file:
```
OPENAI_API_KEY=your_openai_key_here
```

3. Start the app:
```bash
streamlit run streamlit_app.py
```

## 🌐 Deploy on Streamlit Cloud
- Upload this repo to GitHub
- Connect it at https://streamlit.io/cloud
- Set `streamlit_app.py` as the main file
- Add secret: `OPENAI_API_KEY`
