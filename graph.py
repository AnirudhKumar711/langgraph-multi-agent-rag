from langgraph.graph import StateGraph
from typing import TypedDict

from router import route_query
from sql_agent import sql_agent
from rag_agent import rag_agent
from company_agent import company_agent

class GraphState(TypedDict):
    query: str
    route: str
    result: object

builder = StateGraph(GraphState)

builder.add_node("router", route_query)
builder.add_node("sql", sql_agent)
builder.add_node("rag", rag_agent)
builder.add_node("company", company_agent)

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "sql": "sql",
        "rag": "rag",
        "company": "company"
    }
)

builder.set_finish_point("sql")
builder.set_finish_point("rag")
builder.set_finish_point("company")

graph = builder.compile()