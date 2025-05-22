from typing import Optional  # Optional can be used elsewhere in your codebase
from textwrap import dedent  # Useful for creating clean multiline strings (used in prompts)

# --- GLOBAL CONFIGURABLE PARAMETERS ---

# Default art style used when generating image prompts
# This ensures the visuals are appropriate for children's books — warm, colorful, and hand-drawn,
# like classic illustrated storybooks (think: soft lines, playful, safe imagery).
DEFAULT_ART_STYLE = "warm, colorful, hand-drawn style suitable for children"

#  Default tone for storytelling prompts
# Keeps the story's language and narrative tone safe, fun, and creative.
DEFAULT_TONE = "friendly and imaginative"

#  Banned topics list
# These are words or themes that should never appear in a children's book.
# You use this to filter input prompts and also reinforce safety in AI instructions.
BANNED_TOPICS = ['violence', 'drugs', 'kill', 'blood', 'weapon', 'death']

"""
     NOTES ON AGE APPROPRIATENESS:

- Children aged 1–5:
  Prefer simple stories, bright visuals, and funny, cartoonish characters.
  They should easily recognize shapes, animals, and expressive facial features.

- Children aged 5–10:
  Still love color and fun characters, but can handle a bit more plot complexity.
  Stories can involve friendship, teamwork, and light conflict resolution — still staying safe and optimistic.
  Think of familiar icons like Dora the Explorer, Bluey, or Doremon.

👶 This config helps ensure that the entire system — from prompts to images — 
produces stories that are enjoyable, safe, and developmentally appropriate.
"""
