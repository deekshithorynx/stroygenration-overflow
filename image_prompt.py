from typing import Optional  # Allows art_style to be optional
from textwrap import dedent  # (Not used in this function, but useful for multiline strings if needed later)
from config import DEFAULT_ART_STYLE  # Default visual style for image generation prompts

def image_prompt(character_description: str, scene_text: str, art_style: Optional[str] = None) -> str:
    """
    Generates a prompt string for an AI image generation model (like Leonardo.Ai).
    
    Parameters:
        character_description (str): Description of the main character (e.g., name, appearance).
        scene_text (str): Narrative text describing the scene on the page.
        art_style (Optional[str]): Optional custom style for the illustration. Defaults to a child-friendly style.
    
    Returns:
        str: A complete prompt combining scene, character, and art style.
    """

    # Use the custom art_style if provided; otherwise fall back to a safe default.
    # This helps keep visual consistency and avoids inappropriate styles like realism or horror.
    style = art_style or DEFAULT_ART_STYLE

    # Construct the final image prompt:
    # - Asks the AI to "illustrate" a scene (clear intent)
    # - Combines the current scene's text and the character’s appearance
    # - Ends with stylistic instruction to ensure visual appropriateness
    return (
        f"Illustrate this children's book scene: {scene_text} "
        f"The main character appears as: {character_description} "
        f"Use a {style}."
    )
