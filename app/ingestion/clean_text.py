import re


def clean_text(text: str) -> str:
    """
    Cleans raw astrology text before chunking.

    Removes:
    - extra line breaks
    - repeated spaces
    - page number patterns
    - common OCR spacing noise
    """

    text = text.replace("\r", "\n")

    # Remove page number patterns like "Page 12"
    text = re.sub(r"\bPage\s+\d+\b", "", text, flags=re.IGNORECASE)

    # Replace multiple new lines with paragraph breaks
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Replace tabs/multiple spaces with single space
    text = re.sub(r"[ \t]+", " ", text)

    # Clean spaces around new lines
    text = re.sub(r" *\n *", "\n", text)

    return text.strip()