from app.rag.query_parser import parse_query
from app.rag.metadata_search import search_by_metadata


def run_pipeline(query: str):
    parsed = parse_query(query)

    planet = parsed.get("planet")
    house = parsed.get("house")

    results = search_by_metadata(planet=planet, house=house)

    print("\nQUERY:", query)
    print("PARSED:", parsed)

    print("\nRESULTS:\n")

    for r in results:
        print("---")
        print("Chunk:", r["chunk_id"])
        print("Text:", r["text"])
        print("Metadata:", r["metadata"])


if __name__ == "__main__":
    run_pipeline("mars in 11th house")