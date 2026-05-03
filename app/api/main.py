from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.answer_generator import generate_answer


app = FastAPI(title="Astro RAG API")


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {"message": "Astro RAG API is running"}


@app.post("/ask")
@app.post("/ask")
def ask_question(request: QueryRequest):
    return generate_answer(request.query)