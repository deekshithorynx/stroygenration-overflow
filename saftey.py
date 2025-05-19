from typing import Optional
from textwrap import dedent
from config import BANNED_TOPICS

def validate_safe_input(text: str) -> bool:
    """
    Basic safety check to ensure no banned content is in the prompt or story.
    """
    lowered = text.lower()
    return not any(word in lowered for word in BANNED_TOPICS)
