def route_query(state):
    query = state["query"].lower()

    if any(word in query for word in ["company", "policy", "leave", "salary", "work"]):
        route = "company"

    elif any(word in query for word in ["recommend", "suggest", "similar"]):
        route = "rag"

    else:
        route = "sql"

    return {"route": route}