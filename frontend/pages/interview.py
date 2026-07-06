import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Interview Preparation",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 AI Interview Preparation")

st.write(
    "Generate interview questions, expected answers, and interview tips."
)

role = st.text_input(
    "Enter the Job Role",
    placeholder="Example: AI Engineer"
)

difficulty = st.selectbox(
    "Difficulty Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

if st.button("Generate Interview Questions"):

    if role == "":
        st.warning("Please enter a job role.")

    else:

        question = f"""
Generate {difficulty} interview questions for {role}.
Include:

1. Question
2. Expected Answer
3. Difficulty
4. Tips
"""

        with st.spinner("Generating Interview Questions..."):

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "question": question
                }
            )

        if response.status_code == 200:

            data = response.json()

            st.success(f"Agent Used: {data['agent']}")

            st.markdown(data["response"])

        else:

            st.error("Something went wrong.")
            st.divider()

st.caption(
    "🚀 CareerPilot AI | Built using FastAPI • LangGraph • Gemini • Streamlit"
)