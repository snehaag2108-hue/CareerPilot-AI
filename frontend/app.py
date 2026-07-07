import streamlit as st

API_URL = "https://careerpilot-ai-zqs8.onrender.com"

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")

st.markdown("""
## Welcome to CareerPilot AI

Your Personal AI Career Mentor built using **Google Gemini**, **LangGraph**, **FastAPI**, and **Streamlit**.

### 🚀 Features

- 📄 ATS Resume Analysis
- 💼 AI Career Guidance
- 🗺️ Personalized Learning Roadmaps
- 🎤 AI Interview Preparation
- 🧠 Persistent User Memory
- 🤖 Multi-Agent Architecture

---

### 📚 How to Use

1. Open **Dashboard** to view your profile.
2. Upload your resume from **Resume Analyzer**.
3. Ask career-related questions in **Career Chat**.
4. Generate interview questions in **Interview Preparation**.
5. Create personalized learning plans in **Career Roadmap**.

---

### 🛠️ Technology Stack

- Python
- FastAPI
- Streamlit
- LangGraph
- Google Gemini
- PyMuPDF
- JSON Memory

---

### 🎯 Kaggle AI Agents Intensive Capstone

This project demonstrates:

- ✅ Multi-Agent System
- ✅ Tool Integration
- ✅ Memory Management
- ✅ Security Guardrails

Use the **sidebar** to navigate between pages.
""")

st.divider()

st.info("""
### 💡 Suggested Questions

• Review my resume

• Help me become an AI Engineer

• Generate interview questions for Data Scientist

• Create a roadmap for Machine Learning

• What skills should I learn for AI?

• How can I improve my resume?
""")

st.divider()

st.caption(
    "🚀 CareerPilot AI | Built using FastAPI • LangGraph • Gemini • Streamlit"
)