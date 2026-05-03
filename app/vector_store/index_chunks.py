import json
from pathlib import Path

import numpy as np
from qdrant_client.models import PointStruct

from app.vector_store.qdrant_client import get_qdrant_client


CHUNKS_FILE = Path("data/processed/chunks.jsonl")
EMBEDDINGS_FILE = Path("data/processed/chunk_embeddings.npz")

COLLECTION_NAME = "astro_chunks"


def load_chunks():
    chunks = []
    with CHUNKS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))
    return chunks


def load_embeddings():
    data = np.load(EMBEDDINGS_FILE)
    return data["chunk_ids"], data["embeddings"]


def main():
    client = get_qdrant_client()

    chunks = load_chunks()
    chunk_ids, embeddings = load_embeddings()

    points = []

    for idx, chunk in enumerate(chunks):
        vector = embeddings[idx]

        payload = {
            "text": chunk["text"],
            "metadata": chunk["metadata"]
        }

        points.append(
            PointStruct(
                id=idx,
                vector=vector.tolist(),
                payload=payload
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"Inserted {len(points)} chunks into Qdrant")

    client.close()


if __name__ == "__main__":
    main()