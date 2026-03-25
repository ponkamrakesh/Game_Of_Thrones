from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq
from app.config import GROQ_API_KEY
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
VECTOR_PATH = os.path.join(BASE_DIR, "vectorstore")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en"
)

db = FAISS.load_local(
    VECTOR_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are a Maester of the Citadel.

Speak in a Game of Thrones tone:
- Medieval
- Wise
- Slightly dramatic

Rules:
- Only use given context
- If unknown: "The records of the realm are unclear..."
"""

def generate_answer(query: str):
    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query}"
            }
        ],
        temperature=0.7
    )

    return completion.choices[0].message.content