from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "got_book.pdf")
VECTOR_PATH = os.path.join(BASE_DIR, "vectorstore")

loader = PyPDFLoader(DATA_PATH)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en"
)

db = FAISS.from_documents(chunks, embeddings)
db.save_local(VECTOR_PATH)

print("Vector DB created successfully.")