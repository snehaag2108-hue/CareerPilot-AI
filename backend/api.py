from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from backend.workflow import career_graph
from backend.agents.resume_agent import resume_agent

app = FastAPI(
    title="CareerPilot AI",
    version="1.0"
)


class UserQuery(BaseModel):
    question: str


# -----------------------------------
# Home Endpoint
# -----------------------------------
@app.get("/")
def home():
    return {
        "message": "CareerPilot AI API is running!"
    }


# -----------------------------------
# Chat Endpoint
# -----------------------------------
@app.post("/chat")
def chat(query: UserQuery):

    result = career_graph.invoke(
        {
            "user_input": query.question,
            "response": "",
            "agent": ""
        }
    )

    return {
        "agent": result["agent"],
        "response": result["response"]
    }


# -----------------------------------
# Resume Upload & Analysis Endpoint
# -----------------------------------
@app.post("/resume")
async def analyze_resume(file: UploadFile = File(...)):

    # Create uploads folder if it doesn't exist
    os.makedirs("uploads", exist_ok=True)

    # Save uploaded PDF
    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Analyze the resume using Resume Agent
    result = resume_agent.analyze_resume(file_path)

    return {
        "status": "success",
        "filename": file.filename,
        "response": result
    }