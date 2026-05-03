import re
from app.ingestion.enrich_metadata import enrich_metadata


def split_into_paragraphs(text: str) -> list[str]:
    """
    Splits text into paragraphs using double line breaks.
    """
    paragraphs = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paragraphs if p.strip()]


def create_chunks(text: str, source: str) -> list[dict]:
    """
    Creates chunks based on paragraphs (better for astrology content)
    """

    paragraphs = split_into_paragraphs(text)
    chunks = []

    for i, para in enumerate(paragraphs):
        metadata = enrich_metadata(para, source)

        chunks.append({
            "chunk_id": f"{source}_chunk_{i+1}",
            "text": para,
            "metadata": metadata
        })

    return chunks