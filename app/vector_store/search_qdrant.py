from sentence_transformers import SentenceTransformer

from app.vector_store.qdrant_client import get_qdrant_client


COLLECTION_NAME = "astro_chunks"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def search_qdrant(query: str, top_k: int = 3):
    client = get_qdrant_client()
    model = SentenceTransformer(MODEL_NAME)

    query_vector = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    results = client.query_points(
    collection_name=COLLECTION_NAME,
    query=query_vector,
    limit=top_k
).points

    client.close()
    return results


if __name__ == "__main__":
    results = search_qdrant("mars gains friends network")

    for result in results:
        print("\n--- MATCH ---")
        print("Score:", round(result.score, 3))
        print("Text:", result.payload["text"])
        print("Metadata:", result.payload["metadata"])