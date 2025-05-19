import re
from config import BANNED_TOPICS


# List of banned words
# This list contains words that are considered inappropriate or unsafe for children's stories.
#banned_words = ['violence', 'drugs', 'kill', 'blood', 'weapon', 'death']


def is_input_safe(data: dict):
    """
    Check if the input data contains any banned words.
    This function takes a dictionary of input data and checks if any of the values contain
    words that are considered inappropriate or unsafe for children's stories.
    """
    combined = " ".join(str(value).lower() for value in data.values())
    return not any(bad in combined for bad in banned_words)

def format_story_by_level(story, reading_level="intermediate"):
    sentences = story.split(". ")
    pages = []

    if reading_level == "early":
        pages = sentences[:20]
    elif reading_level == "intermediate":
        for i in range(0, len(sentences), 2):
            pages.append(". ".join(sentences[i:i+2]))
    else:
        for i in range(0, len(sentences), 4):
            pages.append(". ".join(sentences[i:i+4]))

    return pages[:20]


def split_story_into_pages(story_text: str, total_pages: int = 20) -> list:
    """
    Splits a story into a specified number of pages.
    This function takes a string of story text and divides it into chunks that can be used as pages.
    It uses a simple heuristic to break the text into sentences and then groups them into the specified number of pages.
    """

    # Remove title if included
    story_text = re.sub(r"^Title:.*\n", "", story_text, flags=re.IGNORECASE)

    # Break into sentences (simple heuristic)
    sentences = re.split(r'(?<=[.!?])\s+', story_text.strip())

    # Group sentences into 20 chunks
    chunks = []
    avg = max(1, len(sentences) // total_pages)

    for i in range(0, len(sentences), avg):
        # chunk = " ".join(sentences[i:i + avg])

        chunk = " ".join(sentences[i:i + avg])
        chunk = re.sub(r'Page\s*\d+[:\-]?', '', chunk, flags=re.IGNORECASE).strip()

        chunks.append(chunk.strip())

    # Ensure exactly 20 chunks
    if len(chunks) > total_pages:
        chunks = chunks[:total_pages]
    elif len(chunks) < total_pages:
        # Pad with empty pages if short (rare)
        while len(chunks) < total_pages:
            chunks.append("")

    return [{"page": i + 1, "text": chunk} for i, chunk in enumerate(chunks)]
