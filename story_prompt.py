from typing import Optional  # Allows optional function arguments (used here for 'tone')
from textwrap import dedent  # Useful for formatting multiline prompt strings (optional in this case)
from config import DEFAULT_TONE, BANNED_TOPICS  # Imports global tone default and banned content list

def story_prompt(
    title: str,
    genre: str,
    character_description: str,
    tone: str = DEFAULT_TONE,
    age_group: str = "5–10"
) -> str:
    """
    Creates a structured prompt for generating a full children's story.
    
    Parameters:
        title (str): Title of the story.
        genre (str): Genre like Adventure, Fantasy, Mystery, etc.
        character_description (str): Description of the main character (name, traits, backstory).
        tone (str): Narrative tone to use; defaults to a friendly, imaginative voice.
        age_group (str): Age group the story is intended for (used for tone and vocabulary).
    
    Returns:
        str: A formatted prompt for use with a language model like GPT.
    """

    # The prompt includes:
    # - Title, genre, character description for context
    # - Desired tone and age group to guide language complexity and positivity
    # - Banned topics to ensure safe storytelling
    return f"""Write a 20-page illustrated children's story titled "{title}".
The genre is "{genre}", and the main character is described as follows:

{character_description}

The tone should be {tone}, appropriate for children aged {age_group}.
Avoid any themes of {', '.join(BANNED_TOPICS)}. Each page should describe a distinct scene or moment in the story."""
