import streamlit as st
import pandas as pd
from graph import graph

st.title("🎬 Multi-Domain AI Assistant")

# --- Initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Chat input ---
query = st.chat_input("Ask your question...")

if query:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": query})

    # Get response
    response = graph.invoke({"query": query})
    result = response["result"]

    # Detect source
    source = "Unknown"

    if isinstance(result, list):
        source = "📊 SQL Database"

    elif isinstance(result, str):
        if "leave" in query.lower() or "policy" in query.lower() or "salary" in query.lower():
            source = "📄 Company PDF"
        else:
            source = "🎬 Movie RAG"

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": result,
        "source": source
    })

# --- Display chat history ---
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        # --- USER ---
        if msg["role"] == "user":
            st.write(msg["content"])

        # --- ASSISTANT ---
        else:
            result = msg["content"]

            # SQL table
            if isinstance(result, list) and len(result) > 0 and isinstance(result[0], tuple):

                col_count = len(result[0])

                if col_count == 3:
                    df = pd.DataFrame(result, columns=["Title", "Genre", "Rating"])
                elif col_count == 2:
                    df = pd.DataFrame(result, columns=["Title", "Rating"])
                else:
                    df = pd.DataFrame(result)

                st.dataframe(df)

            # Text output
            else:
                st.write(result)

            # Show source
            if "source" in msg:
                st.caption(f"Source: {msg['source']}")