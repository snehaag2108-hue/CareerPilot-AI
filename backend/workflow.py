from typing import TypedDict

from langgraph.graph import StateGraph, END

from backend.agents.router_agent import router_agent
from backend.agents.resume_agent import resume_agent
from backend.agents.career_agent import career_agent
from backend.agents.interview_agent import interview_agent
from backend.agents.roadmap_agent import roadmap_agent


class AgentState(TypedDict):
    user_input: str
    response: str
    agent: str


# ---------------- Router ----------------

def router_node(state: AgentState):

    selected = router_agent.route(state["user_input"])

    return {
        **state,
        "agent": selected
    }


# ---------------- Resume ----------------

def resume_node(state: AgentState):

    response = """
Please upload your resume in the Streamlit interface.
"""

    return {
        **state,
        "response": response
    }


# ---------------- Career ----------------

def career_node(state: AgentState):

    response = career_agent.suggest_career(
        skills="Python",
        interests=state["user_input"],
        experience="Engineering Student"
    )

    return {
        **state,
        "response": response
    }


# ---------------- Interview ----------------

def interview_node(state: AgentState):

    response = interview_agent.generate_questions(
        state["user_input"]
    )

    return {
        **state,
        "response": response
    }


# ---------------- Roadmap ----------------

def roadmap_node(state: AgentState):

    response = roadmap_agent.generate_roadmap(
        state["user_input"]
    )

    return {
        **state,
        "response": response
    }


builder = StateGraph(AgentState)

builder.add_node("router", router_node)
builder.add_node("resume", resume_node)
builder.add_node("career", career_node)
builder.add_node("interview", interview_node)
builder.add_node("roadmap", roadmap_node)

builder.set_entry_point("router")


def route(state: AgentState):
    return state["agent"]


builder.add_conditional_edges(
    "router",
    route,
    {
        "resume": "resume",
        "career": "career",
        "interview": "interview",
        "roadmap": "roadmap"
    }
)

builder.add_edge("resume", END)
builder.add_edge("career", END)
builder.add_edge("interview", END)
builder.add_edge("roadmap", END)

career_graph = builder.compile()