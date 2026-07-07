import streamlit as st
import requests

API_URL = "https://careerpilot-ai-zqs8.onrender.com"

st.title("📄 Resume Analyzer")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if resume:

    files = {
        "file": (
            resume.name,
            resume.getvalue(),
            "application/pdf"
        )
    }

    with st.spinner("Analyzing Resume..."):

        response = requests.post(
            f"{API}/resume",
            files=files
        )

        result = response.json()

    st.success("Analysis Completed")

    st.write(result["response"])
    st.divider()

st.caption(
    "🚀 CareerPilot AI | Built using FastAPI • LangGraph • Gemini • Streamlit"
)