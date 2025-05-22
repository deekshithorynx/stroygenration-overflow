# === Import necessary tools ===
from typing import Optional  # For optional typing (though not used in this specific function)
from textwrap import dedent  # Removes common leading whitespace from multiline strings
from config import BANNED_TOPICS  # A list of inappropriate or disallowed topics for safety

def character_prompt(title: str, genre: str, age_group: str = "5–10") -> str:
    """
    Generates a prompt to create a main character description for a children's story.

    Parameters:
        title (str): The title of the story provided by the user.
        genre (str): The genre of the story (e.g., Fantasy, Adventure, Mystery).
        age_group (str): The age group the story is intended for; default is "5–10".

    Returns:
        str: A formatted text prompt to be sent to a language model like OpenAI's GPT.
    """

    # Use dedent to format the prompt neatly (removes unnecessary indentation from multiline string)
    # The prompt instructs the AI to act as a children's author and create a friendly, age-appropriate character.
    # It specifies what the character description should include: name, looks, personality, and a short backstory.

    # The last line dynamically inserts banned topics (like violence, drugs, etc.) to ensure safe content generation.
    return dedent(f"""
        You are a children's author creating a main character for a story titled "{title}" in the genre "{genre}".
        The story is for children aged {age_group}. The character should have:
        - a memorable name,
        - clear physical traits (color, clothing, species if non-human),
        - positive personality traits,
        - a simple and heartwarming backstory.

        Keep the description safe and friendly, under 100 words, and free from any content involving {', '.join(BANNED_TOPICS)}.
    """)
