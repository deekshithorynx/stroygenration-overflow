from typing import Optional  # Optional can be used if you later want to make parameters optional
from textwrap import dedent  # Helpful for formatting multiline prompt strings

def story_title_prompt(theme: str, genre: str, age_group: str = "5–10") -> str:
    """
    Generates a prompt for a language model to create story titles
    that are engaging, child-friendly, and genre-appropriate.

    Parameters:
        theme (str): The main idea or concept of the story (e.g., kindness, adventure, friendship).
        genre (str): The story’s genre (e.g., Fantasy, Mystery, Animal Tales).
        age_group (str): The intended age range for the story; defaults to "5–10".

    Returns:
        str: A prompt that instructs the AI to suggest 3 suitable story titles.
    """

    # The prompt:
    # - Gives the theme and genre to help guide the creative direction
    # - Emphasizes age appropriateness to ensure titles are simple, friendly, and imaginative
    # - Requests exactly 3 suggestions to keep output focused and useful
    return f"""Suggest 3 creative and catchy titles for a children's story themed around "{theme}", in the genre "{genre}".
The titles should appeal to children aged {age_group}, be friendly and imaginative, and avoid complex or scary words."""
