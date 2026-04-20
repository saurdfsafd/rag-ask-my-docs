from fastapi import FastAPI
from ingestion import process_documents, chunks
from retrieval import build_indices, hybrid_search
from reranker import rerank
from llm import generate_answer
from utils import build_context, validate_output

app = FastAPI()

# Initialize system
process_documents()
build_indices()

@app.get("/ask")
def ask(query: str):
    doc_ids = hybrid_search(query)
    docs = [chunks[i] for i in doc_ids]

    #reranked_docs = rerank(query, docs)[:5]
    reranked_docs = docs[:2]
    context = build_context(reranked_docs)

    answer = generate_answer(query, context)
    return {"answer": validate_output(answer)}