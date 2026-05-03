import json
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer


CHUNKS_FILE = Path("data/processed/chunks.jsonl")
OUTPUT_FILE = Path("data/processed/chunk_embeddings.npz")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_chunks() -> list[dict]:
    chunks = []

    with CHUNKS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))

    return chunks


def main():
    chunks = load_chunks()

    texts = [chunk["text"] for chunk in chunks]
    chunk_ids = [chunk["chunk_id"] for chunk in chunks]

    print(f"Loaded chunks: {len(chunks)}")
    print(f"Loading embedding model: {MODEL_NAME}")

    model = SentenceTransformer(MODEL_NAME)

    print("Generating embeddings...")
    embeddings = model.encode(texts, normalize_embeddings=True)

    np.savez(
        OUTPUT_FILE,
        chunk_ids=np.array(chunk_ids),
        embeddings=embeddings
    )

    print(f"Saved embeddings to: {OUTPUT_FILE}")
    print(f"Embedding shape: {embeddings.shape}")


if __name__ == "__main__":
    main()