from typing import Optional  # Optional is imported for consistency, though not used here
from textwrap import dedent  # Useful for formatting strings, not used directly in this function
from config import BANNED_TOPICS  # List of disallowed topics to help filter unsafe content

def validate_safe_input(text: str) -> bool:
    """
    Performs a basic safety check to ensure the input text does not include banned content.
    
    Parameters:
        text (str): The input string to check (e.g., title, genre, prompt).

    Returns:
        bool: True if the input is safe (i.e., contains none of the banned topics), False otherwise.
    """

    # Convert the input text to lowercase to make the check case-insensitive.
    lowered = text.lower()

    # Check if any banned topic is present in the input.
    # Returns False if any banned word is found.
    return not any(word in lowered for word in BANNED_TOPICS)
