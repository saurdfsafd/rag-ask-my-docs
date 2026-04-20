from sentence_transformers import CrossEncoder

reranker = CrossEncoder("BAAI/bge-reranker-base")


def rerank(query, docs):
    pairs = [[query, doc] for doc in docs]
    scores = reranker.predict(pairs)

    ranked = [doc for _, doc in sorted(zip(scores, docs), reverse=True)]
    return ranked