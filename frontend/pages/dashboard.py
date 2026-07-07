import streamlit as st
import json

API_URL = "https://careerpilot-ai-zqs8.onrender.com"

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 CareerPilot Dashboard")

st.write("Welcome to your AI Career Dashboard.")

st.divider()

# -------------------- Metrics --------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📄 Resume Score",
        value="90/100",
        delta="+5"
    )

with col2:
    st.metric(
        label="💼 Career Goal",
        value="AI Engineer"
    )

with col3:
    st.metric(
        label="🎯 Career Readiness",
        value="82%"
    )

st.divider()

# -------------------- Progress --------------------

st.subheader("📈 Progress")

st.write("Resume Quality")
st.progress(90)

st.write("Career Readiness")
st.progress(82)

st.write("Interview Preparation")
st.progress(75)

st.write("Learning Roadmap")
st.progress(60)

st.divider()

# -------------------- Features --------------------

st.subheader("🚀 Project Features")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Resume Analysis")
    st.success("✅ Career Guidance")
    st.success("✅ AI Interview Preparation")
    st.success("✅ Personalized Roadmaps")

with col2:
    st.success("✅ Multi-Agent System")
    st.success("✅ Gemini Integration")
    st.success("✅ FastAPI Backend")
    st.success("✅ LangGraph Workflow")

st.divider()

# -------------------- Memory --------------------

st.subheader("🧠 Saved User Memory")

try:
    with open("data/user_memory.json", "r") as f:
        memory = json.load(f)

    st.json(memory)

except:
    st.info("No saved memory found.")

st.divider()

# -------------------- Tips --------------------

st.subheader("💡 Career Tips")

st.info("""
✔ Keep your resume to one page.

✔ Build at least 3 strong projects.

✔ Practice coding daily.

✔ Improve communication skills.

✔ Learn Git & GitHub.

✔ Prepare for behavioral interviews.

✔ Keep updating your LinkedIn profile.
""")

st.divider()

st.caption(
    "🚀 CareerPilot AI | Dashboard | Built using FastAPI • LangGraph • Gemini • Streamlit"
)