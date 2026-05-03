import re


PLANETS = [
    "sun", "moon", "mars", "mercury", "jupiter",
    "venus", "saturn", "rahu", "ketu"
]

HOUSES = {
    "1st": "1", "first": "1",
    "2nd": "2", "second": "2",
    "3rd": "3", "third": "3",
    "4th": "4", "fourth": "4",
    "5th": "5", "fifth": "5",
    "6th": "6", "sixth": "6",
    "7th": "7", "seventh": "7",
    "8th": "8", "eighth": "8",
    "9th": "9", "ninth": "9",
    "10th": "10", "tenth": "10",
    "11th": "11", "eleventh": "11",
    "12th": "12", "twelfth": "12"
}

SIGNS = [
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]

TOPIC_KEYWORDS = {
    "career": ["career", "profession", "work", "job", "authority"],
    "wealth": ["wealth", "money", "gains", "income", "profit"],
    "marriage": ["marriage", "spouse", "wife", "husband", "relationship"],
    "health": ["health", "disease", "illness", "sickness"],
    "education": ["education", "learning", "intelligence", "study"],
    "children": ["children", "son", "daughter", "offspring"],
    "network": ["friends", "network", "circle", "elder siblings"],
    "spirituality": ["spiritual", "religion", "moksha", "guru"]
}


def extract_planets(text: str) -> list[str]:
    lower = text.lower()
    return [
        planet.title()
        for planet in PLANETS
        if re.search(rf"\b{planet}\b", lower)
    ]


def extract_houses(text: str) -> list[str]:
    lower = text.lower()
    found = []

    for label, number in HOUSES.items():
        if re.search(rf"\b{label}\s+house\b", lower):
            found.append(number)

    return sorted(set(found), key=int)


def extract_signs(text: str) -> list[str]:
    lower = text.lower()
    return [
        sign.title()
        for sign in SIGNS
        if re.search(rf"\b{sign}\b", lower)
    ]


def extract_topics(text: str) -> list[str]:
    lower = text.lower()
    topics = []

    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword in lower for keyword in keywords):
            topics.append(topic)

    return topics


def detect_chunk_type(text: str) -> str:
    planets = extract_planets(text)
    houses = extract_houses(text)
    lower = text.lower()

    if "dasha" in lower:
        return "dasha"

    if "yoga" in lower:
        return "yoga"

    if planets and houses:
        return "planet_house_placement"

    if planets:
        return "planet_general"

    if houses:
        return "house_general"

    return "general"


def enrich_metadata(text: str, source: str) -> dict:
    return {
        "source": source,
        "planets": extract_planets(text),
        "houses": extract_houses(text),
        "signs": extract_signs(text),
        "topics": extract_topics(text),
        "chunk_type": detect_chunk_type(text),
        "tradition": "vedic",
        "language": "english"
    }