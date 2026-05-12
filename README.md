# 🎬 Multi-Domain AI Assistant using LangGraph

A multi-agent AI system built using LangGraph that intelligently routes user queries between:

- 📊 SQL-based movie database search
- 🎬 Semantic movie recommendation system (RAG)
- 📄 PDF-based company document retrieval (RAG)

The project combines structured querying, semantic search, vector embeddings, and workflow orchestration into a single interactive Streamlit application.

---

# 🚀 Features

## ✅ SQL Agent
- Query movie database using natural language
- Filter by:
  - country
  - genre
  - ratings
- Dynamic SQL generation

### Example Queries
- Show movies from Japan
- Best action movies
- Top rated movies

---

## ✅ Movie Recommendation RAG
Uses sentence embeddings for semantic search.

### Example Queries
- Suggest movies about space
- Recommend superhero movies
- Movies related to dreams

---

## ✅ Company PDF RAG
Retrieves relevant information from PDF documents using embeddings and FAISS vector search.

### Example Queries
- What is leave policy?
- Explain salary policy
- What are working hours?

---

# 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| LangGraph | Multi-agent workflow orchestration |
| Streamlit | Web UI |
| SQLite | Movie database |
| Sentence Transformers | Embedding generation |
| FAISS | Vector similarity search |
| LangChain | PDF loading and text splitting |
| Pandas | Table formatting |

---

# 🏗️ System Architecture

```text
User → Streamlit UI → LangGraph Router
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    SQL Agent       Movie RAG       Company PDF RAG
        │                │                │
    SQLite DB      Embeddings      PDF + FAISS
