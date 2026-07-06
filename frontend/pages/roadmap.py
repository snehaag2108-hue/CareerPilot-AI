import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Career Roadmap",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ AI Career Roadmap")

goal = st.text_input(
    "Career Goal",
    placeholder="Example: Become an AI Engineer"
)

months = st.selectbox(
    "Roadmap Duration",
    [
        "3 Months",
        "6 Months",
        "12 Months"
    ]
)

if st.button("Generate Roadmap"):

    if goal == "":
        st.warning("Please enter your goal.")

    else:

        prompt = f"""
Create a detailed {months} roadmap for

{goal}

Include:

• Skills

• Projects

• Courses

• Certifications

• Interview Preparation

• Timeline
"""

        with st.spinner("Creating Roadmap..."):

            response = requests.post(
                f"{API_URL}/chat",
                json={
                    "question": prompt
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
