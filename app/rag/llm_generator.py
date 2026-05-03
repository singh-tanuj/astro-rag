import ollama


def generate_llm_answer(query: str, context: str) -> str:
    prompt = f"""
    You are a Vedic astrology assistant.

    Answer the question using ONLY the context provided below.
    If a detail is not explicitly present in the context, do not mention it.
    Do not add examples, terminology, or concepts from your general astrology knowledge.
    Do not make absolute or guaranteed predictions.
    Use cautious language such as "may indicate", "can suggest", or "is traditionally associated with".

    Context:
    {context}

    Question:
    {query}

    Return:
    1. Short summary
    2. Detailed explanation using only the context
    3. Important caveat

    """

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]