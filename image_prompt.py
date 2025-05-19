
from typing import Optional
from textwrap import dedent
from config import DEFAULT_ART_STYLE

def image_prompt(character_description: str, scene_text: str, art_style: Optional[str] = None) -> str:
    """
    Create an image generation prompt from a scene and the character description.
    """
    style = art_style or DEFAULT_ART_STYLE
    return (
        f"Illustrate this children's book scene: {scene_text} "
        f"The main character appears as: {character_description} "
        f"Use a {style}."
    )
