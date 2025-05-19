from typing import Optional
from textwrap import dedent
def story_title_prompt(theme: str, genre: str, age_group: str = "5–10") -> str:
    """
    Generate a creative and age-appropriate story title.
    """
    return f"""Suggest 3 creative and catchy titles for a children's story themed around "{theme}", in the genre "{genre}".
The titles should appeal to children aged {age_group}, be friendly and imaginative, and avoid complex or scary words."""