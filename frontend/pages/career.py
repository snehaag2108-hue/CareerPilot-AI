import streamlit as st
import requests

# -----------------------------
# Backend API URL
# -----------------------------
API_URL = "https://careerpilot-ai-zqs8.onrender.com"

st.set_page_config(
    page_title="Career Chat",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Career Chat")

st.write("Ask CareerPilot anything about careers, skills, jobs, or learning paths.")

question = st.chat_input("Ask CareerPilot...")

if question:

    with st.spinner("Thinking..."):

        try:

            response = requests.post(
                f"{API_URL}/chat",
                json={"question": question},
                timeout=120
            )

            if response.status_code == 200:

                result = response.json()

                st.success(f"Agent Used: {result['agent']}")

                st.markdown(result["response"])

            else:

                st.error(f"Backend Error ({response.status_code})")
                st.write(response.text)

        except requests.exceptions.ConnectionError:

            st.error("❌ Could not connect to the backend API.")

        except requests.exceptions.Timeout:

            st.error("⏳ Request timed out. Please try again.")

        except Exception as e:

            st.error(f"Unexpected Error:\n\n{e}")

st.divider()

st.caption(
    "🚀 CareerPilot AI | Built using FastAPI • LangGraph • Gemini • Streamlit"
)