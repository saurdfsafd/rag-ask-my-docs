from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

model = SentenceTransformer("BAAI/bge-small-en")

chunks = []
embeddings = None

def load_documents():
    with open("data/sample.txt", "r", encoding="utf-8") as f:
        return f.read()


def process_documents():
    global chunks, embeddings
    text = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)
    embeddings = model.encode(chunks)

    return chunks, embeddings