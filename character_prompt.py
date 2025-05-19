from typing import Optional
from textwrap import dedent
from config import BANNED_TOPICS

def character_prompt(title: str, genre: str, age_group: str = "5–10") -> str:
    """
    Create a character prompt based on title and genre, tailored to a specific age group.
    """
    return f"""You are a children's author creating a main character for a story titled "{title}" in the genre "{genre}".
                    The story is for children aged {age_group}. The character should have:
                    - a memorable name,
                    - clear physical traits (color, clothing, species if non-human),
                    - positive personality traits,
                    - a simple and heartwarming backstory.

                    Keep the description safe and friendly, under 100 words, and free from any content involving {', '.join(BANNED_TOPICS)}."""

"""
    we will create a full stroy for the children based on the charater they liked
                            
                            
                            """
