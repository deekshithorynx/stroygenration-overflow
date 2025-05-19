from typing import Optional
from textwrap import dedent
from config import DEFAULT_TONE, BANNED_TOPICS

def story_prompt(title: str, genre: str, character_description: str, tone: str = DEFAULT_TONE, age_group: str = "5–10") -> str:
    """
    Prompt to generate a full children's story based on the character and genre.
    """
    return f"""Write a 20-page illustrated children's story titled "{title}".
The genre is "{genre}", and the main character is described as follows:

{character_description}

The tone should be {tone}, appropriate for children aged {age_group}.
Avoid any themes of {', '.join(BANNED_TOPICS)}. Each page should describe a distinct scene or moment in the story."""

def extend_story_prompt(existing_text: str, character_description: str, tone: str = DEFAULT_TONE) -> str:
    """
    Extend an existing story with a new scene while preserving tone and character.
    """
    return f"""You are continuing a children's story using a consistent tone and character style.
Main character:
{character_description}

Current story:
{existing_text}

Write the next scene, keeping the tone {tone}, and do not introduce any themes of {', '.join(BANNED_TOPICS)}."""
