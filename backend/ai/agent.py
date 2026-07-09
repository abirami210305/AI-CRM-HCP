from langchain_core.messages import HumanMessage
from ai.graph import graph


def run_agent(user_message: str):

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content=user_message)
            ]
        }
    )

    return result["messages"][-1].content