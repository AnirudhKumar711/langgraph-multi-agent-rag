# ✅ imports at top
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# load pdf
loader = PyPDFLoader("company_docs/company_policy.pdf")
documents = loader.load()

# split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

docs = splitter.split_documents(documents)
texts = [doc.page_content for doc in docs]

# embeddings
embeddings = model.encode(texts)

# FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def retrieve_answer(query):
    query_embedding = model.encode([query])

    D, I = index.search(query_embedding, k=3)

    results = [texts[i] for i in I[0]]
    return "\n\n".join(results)