from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition

from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq

from config import GROQ_API_KEY
from ai.state import AgentState

from ai.tools import (
    log_interaction,
    edit_interaction,
    search_interaction,
    summarize_interaction,
    followup_reminder,
)

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)

tools = [
    log_interaction,
    edit_interaction,
    search_interaction,
    summarize_interaction,
    followup_reminder,
]

llm = llm.bind_tools(tools)

tool_node = ToolNode(tools)


def chatbot(state: AgentState):

    messages = [
        SystemMessage(
            content="""
You are an AI CRM assistant for Healthcare Professionals.

Use the available tools whenever appropriate.

Available tools:
- log_interaction
- edit_interaction
- search_interaction
- summarize_interaction
- followup_reminder
"""
        )
    ] + state["messages"]

    response = llm.invoke(messages)

    return {
        "messages": [response]
    }


builder = StateGraph(AgentState)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", tool_node)

builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

builder.add_edge("tools", "chatbot")

builder.add_edge("chatbot", END)

graph = builder.compile()