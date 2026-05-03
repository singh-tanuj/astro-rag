import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer


CHUNKS_FILE = Path("data/processed/chunks.jsonl")
EMBEDDINGS_FILE = Path("data/processed/chunk_embeddings.npz")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_chunks():
    chunks = []
    with CHUNKS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    return chunks


def load_embeddings():
    data = np.load(EMBEDDINGS_FILE)
    return data["chunk_ids"], data["embeddings"]


def cosine_similarity(a, b):
    return np.dot(a, b)


def semantic_search(query: str, top_k: int = 3):
    print(f"\nQuery: {query}")

    model = SentenceTransformer(MODEL_NAME)

    query_embedding = model.encode([query], normalize_embeddings=True)[0]

    chunk_ids, embeddings = load_embeddings()
    chunks = load_chunks()

    scores = []

    for idx, emb in enumerate(embeddings):
        score = cosine_similarity(query_embedding, emb)
        scores.append((score, idx))

    scores.sort(reverse=True)

    print("\nTop Results:\n")

    for score, idx in scores[:top_k]:
        chunk = chunks[idx]
        print("Score:", round(score, 3))
        print("Text:", chunk["text"])
        print("Metadata:", chunk["metadata"])
        print("---")


if __name__ == "__main__":
    semantic_search("mars gains friends network")