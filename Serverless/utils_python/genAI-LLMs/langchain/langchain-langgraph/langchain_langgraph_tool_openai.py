
# https://www.youtube.com/watch?v=1Q_MDOWaljk
# pip install -U langgraph langchain-openai

# Annotated[int, runtime_check.Unsigned]
from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph = StateGraph(State)

@tool
def get_weather(location:str):
    """Call to get the current weather"""
    if location.lower in ["london"]:
        return "It's always rainy"
    else:
        return "It's a sunny day"
    
tools = [get_weather]

llm = ChatOpenAI(api_key="", model="gpt-4o")
llm_with_tools = llm.bind_tools(tools)

tool_node = ToolNode(tools)
graph.add_node(tool_node)


def prompt_node(state:State) -> State:
    new_message = llm_with_tools.invoke(state["messages"])
    return {"messages":[new_message]}

graph.add_node("prompt_node", prompt_node)


def conditional_edge(state:State) -> Literal["tool_node", "__end__"]:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tool_node"
    else:
        return "__end__"
    
graph.add_conditional_edges("prompt_node", conditional_edge)
graph.add_edge("tool_node", "prompt_node")
graph.set_entry_point("prompt_node")

app = graph.compile()
new_state = app.invoke({"messages":["What is the weather in london?"]})
print(new_state["messages"][-1].content)