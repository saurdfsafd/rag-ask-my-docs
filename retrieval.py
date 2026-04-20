from rank_bm25 import BM25Okapi
import faiss
import numpy as np
from ingestion import chunks, embeddings, model

bm25 = None
index = None


def build_indices():
    global bm25, index

    tokenized_docs = [doc.split() for doc in chunks]
    bm25 = BM25Okapi(tokenized_docs)

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))


def hybrid_search(query, top_k=10):
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    query_emb = model.encode([query])
    _, vec_indices = index.search(query_emb, top_k)

    scores = {}

    for i, score in enumerate(bm25_scores):
        scores[i] = score * 0.5

    for rank, idx in enumerate(vec_indices[0]):
        scores[idx] += (1 / (rank + 1)) * 0.5

    ranked = sorted(scores, key=scores.get, reverse=True)
    return ranked[:top_k]