from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

movies = [
    "Inception is a sci-fi movie about dreams and mind bending",
    "Interstellar is about space exploration and black holes",
    "RRR is an Indian action drama",
    "Avengers is a superhero action movie",
    "Dangal is a sports drama based on wrestling"
]

embeddings = model.encode(movies)

def rag_agent(state):
    query = state["query"]

    query_embedding = model.encode([query])[0]
    similarities = np.dot(embeddings, query_embedding)
    best_idx = np.argmax(similarities)

    return {"result": movies[best_idx]}