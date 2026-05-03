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


def parse_query(query: str) -> dict:
    lower = query.lower()

    planet = None
    house = None

    for p in PLANETS:
        if re.search(rf"\b{p}\b", lower):
            planet = p.title()
            break

    for label, number in HOUSES.items():
        if re.search(rf"\b{label}\b", lower):
            house = number
            break

    return {
        "planet": planet,
        "house": house
    }


if __name__ == "__main__":
    query = "mars in 11th house"
    parsed = parse_query(query)
    print(parsed)