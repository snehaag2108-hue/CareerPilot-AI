# 🚀 CareerPilot AI

> An Intelligent Multi-Agent Career Guidance System built using **Google Gemini**, **LangGraph**, **FastAPI**, and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![LangGraph](https://img.shields.io/badge/LangGraph-AI-purple)

---

# 📌 Project Overview

CareerPilot AI is a multi-agent AI application that helps students and professionals make informed career decisions.

The system analyzes resumes, provides career guidance, generates personalized learning roadmaps, creates interview questions, and remembers user preferences through a persistent memory system.

This project was developed for the **Kaggle 5-Day AI Agents Intensive Capstone Project**.

---

# 🎯 Problem Statement

Many students struggle with:

- Building ATS-friendly resumes
- Choosing the right career path
- Preparing for interviews
- Identifying missing skills
- Creating structured learning roadmaps

CareerPilot AI solves these challenges using specialized AI agents.

---

# ✨ Features

### 📄 Resume Analyzer

- Upload PDF Resume
- ATS-style Resume Review
- Resume Score
- Strengths & Weaknesses
- Missing Skills
- Suggested Improvements

---

### 💼 Career Guidance

- Personalized Career Advice
- Best Career Paths
- Salary Insights
- Required Skills
- Certifications
- Project Suggestions

---

### 🎤 Interview Preparation

- Role-specific Interview Questions
- Expected Answers
- Interview Tips
- Difficulty Levels

---

### 🗺️ Career Roadmap

- Month-wise Learning Plan
- Recommended Courses
- Projects
- Certifications
- Interview Preparation Timeline

---

### 🧠 Memory Management

The application remembers:

- Career Goal
- Skills
- Interests
- Experience
- Previous User Preferences

Memory is stored in JSON format for personalization.

---

### 🛡️ Security Guardrails

The application includes:

- Prompt validation
- Unsafe prompt detection
- Harmful request blocking

---

# 🤖 Multi-Agent Architecture

The project uses multiple AI agents.

## Router Agent

Routes user requests to the appropriate specialized agent.

---

## Resume Agent

- Reads PDF Resume
- Uses Gemini for Resume Analysis

---

## Career Agent

Provides personalized career guidance.

---

## Interview Agent

Generates interview questions.

---

## Roadmap Agent

Creates customized learning roadmaps.

---

# 🏗️ Architecture

```
                    User
                      │
              Streamlit Frontend
                      │
               HTTP Requests
                      │
                FastAPI Backend
                      │
             LangGraph Workflow
                      │
               Router Agent
      ┌─────────┬─────────┬─────────┐
      │         │         │         │
 Resume   Career   Interview   Roadmap
  Agent     Agent      Agent      Agent
      │
 ┌────┴───────────────┐
 │                    │
PDF Reader       Gemini API
      │
      ▼
 Memory Management
```

---

# 🛠️ Tech Stack

### Programming Language

- Python 3.10

### Backend

- FastAPI

### Frontend

- Streamlit

### LLM

- Google Gemini

### AI Framework

- LangGraph

### PDF Processing

- PyMuPDF

### Memory

- JSON Storage

### API

- REST API

---

# 📂 Project Structure

```
CareerPilot-AI/

│

├── backend/

│ ├── agents/

│ ├── tools/

│ ├── api.py

│ ├── workflow.py

│ ├── config.py

│

├── frontend/

│ ├── app.py

│ └── pages/

│ ├── dashboard.py

│ ├── resume.py

│ ├── career.py

│ ├── interview.py

│ ├── roadmap.py

│ └── about.py

│

├── uploads/

├── data/

├── requirements.txt

├── README.md

└── .env
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/CareerPilot-AI.git
```

Go inside the project

```bash
cd CareerPilot-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# ▶️ Run the Backend

```bash
uvicorn backend.api:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶️ Run the Frontend

```bash
streamlit run frontend/app.py
```

---

# 📸 Application Pages

- Home
- Dashboard
- Resume Analyzer
- Career Chat
- Interview Preparation
- Career Roadmap
- About

---

# 📚 Kaggle Capstone Requirements

| Requirement         | Status |
| ------------------- | ------ |
| Multi-Agent System  | ✅     |
| Tool Integration    | ✅     |
| Memory Management   | ✅     |
| Security Guardrails | ✅     |
| FastAPI Backend     | ✅     |
| Streamlit Frontend  | ✅     |
| Gemini Integration  | ✅     |
| LangGraph Workflow  | ✅     |

---

# 🚀 Future Enhancements

- Authentication
- Database Support
- Conversation History
- LLM Router
- Vector Database Memory
- Resume Comparison
- PDF Career Report Export
- LinkedIn Profile Analysis

---

# 👩‍💻 Author

**Sneha Agarwal**

Built as part of the **Kaggle 5-Day AI Agents Intensive Capstone Project (2026)**.

---

# 📄 License

This project is intended for educational purposes and the Kaggle AI Agents Intensive Capstone submission.
