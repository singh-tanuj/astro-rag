from qdrant_client.models import Distance, VectorParams

from app.vector_store.qdrant_client import get_qdrant_client


COLLECTION_NAME = "astro_chunks"
VECTOR_SIZE = 384


def main():
    client = get_qdrant_client()

    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE
        )
    )

    print(f"Collection created: {COLLECTION_NAME}")
    print(client.get_collections())

    client.close()


if __name__ == "__main__":
    main()