from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.rag import generate_answer

app = FastAPI()

# 🔥 CORS (otherwise frontend cries)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

@app.get("/")
def health():
    return {"status": "The realm stands."}

@app.post("/query")
def query(q: Query):
    answer = generate_answer(q.question)
    return {"answer": answer}