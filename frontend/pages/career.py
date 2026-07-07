import streamlit as st
import requests



st.title("💬 Career Chat")

question = st.chat_input(
    "Ask CareerPilot..."
)

if question:

    response = requests.post(

        f"{API}/chat",

        json={
            "question": question
        }

    )

    result = response.json()

    st.write(result["response"])
    st.divider()

st.caption(
    "🚀 CareerPilot AI | Built using FastAPI • LangGraph • Gemini • Streamlit"
)