import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer

from app.rag.query_parser import parse_query


CHUNKS_FILE = Path("data/processed/chunks.jsonl")
EMBEDDINGS_FILE = Path("data/processed/chunk_embeddings.npz")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_chunks() -> list[dict]:
    chunks = []

    with CHUNKS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))

    return chunks


def load_embeddings():
    data = np.load(EMBEDDINGS_FILE)
    return data["chunk_ids"], data["embeddings"]


def metadata_matches(chunk: dict, planet: str | None, house: str | None) -> bool:
    metadata = chunk["metadata"]

    if planet and planet not in metadata.get("planets", []):
        return False

    if house and house not in metadata.get("houses", []):
        return False

    return True


def hybrid_retrieve(query: str, top_k: int = 3) -> list[dict]:
    parsed = parse_query(query)

    planet = parsed.get("planet")
    house = parsed.get("house")

    chunks = load_chunks()
    chunk_ids, embeddings = load_embeddings()

    model = SentenceTransformer(MODEL_NAME)
    query_embedding = model.encode([query], normalize_embeddings=True)[0]

    scored_results = []

    for idx, chunk in enumerate(chunks):
        if not metadata_matches(chunk, planet, house):
            continue

        score = float(np.dot(query_embedding, embeddings[idx]))

        scored_results.append({
            "score": score,
            "chunk": chunk
        })

    scored_results.sort(key=lambda x: x["score"], reverse=True)

    return scored_results[:top_k]


if __name__ == "__main__":
    query = "mars in 11th house gains through friends"

    results = hybrid_retrieve(query)

    print("\nQUERY:", query)
    print("\nHYBRID RESULTS:\n")

    for result in results:
        print("Score:", round(result["score"], 3))
        print("Chunk ID:", result["chunk"]["chunk_id"])
        print("Text:", result["chunk"]["text"])
        print("Metadata:", result["chunk"]["metadata"])
        print("---")