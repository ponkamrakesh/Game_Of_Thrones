import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTOR_PATH = os.path.join(BASE_DIR, "vectorstore")

all_docs = []

# 🔥 Load all files dynamically
for file in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, file)

    if file.endswith(".pdf"):
        loader = PyPDFLoader(path)
        docs = loader.load()
        all_docs.extend(docs)

    elif file.endswith(".txt"):
        loader = TextLoader(path)
        docs = loader.load()
        all_docs.extend(docs)

print(f"Loaded {len(all_docs)} documents")

# Split
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(all_docs)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en"
)

# Store
db = FAISS.from_documents(chunks, embeddings)
db.save_local(VECTOR_PATH)

print("Vector DB created from all files.")
