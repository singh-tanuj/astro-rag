import json
from pathlib import Path


CHUNKS_FILE = Path("data/processed/chunks.jsonl")


def load_chunks() -> list[dict]:
    chunks = []

    with CHUNKS_FILE.open("r", encoding="utf-8") as f:
        for line in f:
            chunks.append(json.loads(line))

    return chunks


def search_by_metadata(
    planet: str | None = None,
    house: str | None = None
) -> list[dict]:

    chunks = load_chunks()
    results = []

    for chunk in chunks:
        metadata = chunk["metadata"]

        planet_match = True
        house_match = True

        if planet:
            planet_match = planet.title() in metadata.get("planets", [])

        if house:
            house_match = house in metadata.get("houses", [])

        if planet_match and house_match:
            results.append(chunk)

    return results


if __name__ == "__main__":
    results = search_by_metadata(planet="Mars", house="11")

    for result in results:
        print("\n--- MATCH ---")
        print("Chunk ID:", result["chunk_id"])
        print("Text:", result["text"])
        print("Metadata:", result["metadata"])