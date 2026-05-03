FORBIDDEN_PHRASES = [
    "you will die",
    "death is certain",
    "divorce is certain",
    "you will never marry",
    "you will definitely become rich",
    "guaranteed wealth",
    "fatal",
    "doomed"
]


def apply_safety_filter(answer: str) -> str:
    lower = answer.lower()

    for phrase in FORBIDDEN_PHRASES:
        if phrase in lower:
            return (
                "The generated response contained an unsafe or overly deterministic astrology claim. "
                "Please rephrase the query or consult a qualified professional for sensitive matters."
            )

    return answer