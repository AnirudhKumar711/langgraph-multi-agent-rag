from company_rag import retrieve_answer

def company_agent(state):
    query = state["query"]
    result = retrieve_answer(query)
    return {"result": result}