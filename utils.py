def build_context(docs):
    context = ""
    for i, doc in enumerate(docs[:2]):
        context += f"[Doc{i}] {doc[:200]}\n"   # truncate
    return context


def validate_output(answer):
    if "[Doc" not in answer:
        return "⚠️ Missing citations.\n" + answer
    return answer