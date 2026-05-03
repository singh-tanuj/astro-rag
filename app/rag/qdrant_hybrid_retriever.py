from app.rag.model_store import get_model
from qdrant_client.models import Filter, FieldCondition, MatchValue

from app.rag.query_parser import parse_query
from app.vector_store.qdrant_client import get_qdrant_client


COLLECTION_NAME = "astro_chunks"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def build_qdrant_filter(planet: str | None, house: str | None):
    conditions = []

    if planet:
        conditions.append(
            FieldCondition(
                key="metadata.planets",
                match=MatchValue(value=planet)
            )
        )

    if house:
        conditions.append(
            FieldCondition(
                key="metadata.houses",
                match=MatchValue(value=house)
            )
        )

    if not conditions:
        return None

    return Filter(must=conditions)


def qdrant_hybrid_retrieve(query: str, top_k: int = 3):
    parsed = parse_query(query)

    planet = parsed.get("planet")
    house = parsed.get("house")

    client = get_qdrant_client()
    model = get_model()

    query_vector = model.encode(
        query,
        normalize_embeddings=True
    ).tolist()

    qdrant_filter = build_qdrant_filter(planet, house)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        query_filter=qdrant_filter,
        limit=top_k
    ).points

    client.close()

    return {
        "query": query,
        "parsed": parsed,
        "results": results
    }


if __name__ == "__main__":
    response = qdrant_hybrid_retrieve("mars in 11th house gains through friends")

    print("\nQUERY:", response["query"])
    print("PARSED:", response["parsed"])

    print("\nQDRANT HYBRID RESULTS:\n")

    for result in response["results"]:
        print("Score:", round(result.score, 3))
        print("Text:", result.payload["text"])
        print("Metadata:", result.payload["metadata"])
        print("---")