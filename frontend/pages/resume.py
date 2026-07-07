import streamlit as st
import requests

# -----------------------------
# Backend API URL
# -----------------------------
API_URL = "https://careerpilot-ai-zqs8.onrender.com"

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume in PDF format and receive an AI-powered ATS analysis."
)

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

        try:

            response = requests.post(
                f"{API_URL}/resume",
                files=files,
                timeout=180
            )

            if response.status_code == 200:

                result = response.json()

                st.success("✅ Analysis Completed")

                st.markdown(result["response"])

            else:

                st.error(f"Backend Error ({response.status_code})")
                st.write(response.text)

        except requests.exceptions.ConnectionError:

            st.error("❌ Could not connect to the backend server.")

        except requests.exceptions.Timeout:

            st.error("⏳ The request timed out. Please try again.")

        except Exception as e:

            st.error(f"Unexpected Error:\n\n{e}")

st.divider()

st.caption(
    "🚀 CareerPilot AI | Built using FastAPI • LangGraph • Gemini • Streamlit"
)