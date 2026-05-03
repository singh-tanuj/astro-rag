from app.rag.qdrant_hybrid_retriever import qdrant_hybrid_retrieve
from app.guardrails.safety_filter import apply_safety_filter
from app.rag.llm_generator import generate_llm_answer

def generate_answer(query: str) -> dict:
    response = qdrant_hybrid_retrieve(query, top_k=3)
    results = response["results"]

    if not results:
        return {
            "query": query,
            "parsed_query": response["parsed"],
            "answer": "I could not find a reliable matching astrology reference for this query in the current knowledge base.",
            "sources": []
        }

    sources = []

    for result in results:
        payload = result.payload
        metadata = payload["metadata"]

        sources.append({
            "source": metadata.get("source"),
            "score": round(result.score, 3),
            "text": payload["text"],
            "metadata": metadata
        })

    context = "\n\n".join([source["text"] for source in sources])

    answer = generate_llm_answer(
        query=query,
        context=context
    )

    answer = apply_safety_filter(answer)

    return {
        "query": query,
        "parsed_query": response["parsed"],
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":
    response = generate_answer("mars in 11th house gains through friends")
    print(response)