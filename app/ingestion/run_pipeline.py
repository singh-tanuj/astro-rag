import json
from pathlib import Path

from app.ingestion.clean_text import clean_text
from app.ingestion.chunk_documents import create_chunks


RAW_DIR = Path("data/raw")
OUTPUT_FILE = Path("data/processed/chunks.jsonl")


def process_file(file_path: Path) -> list[dict]:
    raw_text = file_path.read_text(encoding="utf-8", errors="ignore")
    cleaned_text = clean_text(raw_text)

    source_name = file_path.stem

    return create_chunks(
        text=cleaned_text,
        source=source_name
    )


def main():
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    all_chunks = []

    for file_path in RAW_DIR.glob("*.txt"):
        print(f"Processing: {file_path.name}")

        chunks = process_file(file_path)
        all_chunks.extend(chunks)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    print(f"Done. Total chunks created: {len(all_chunks)}")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()