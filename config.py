from typing import Optional
from textwrap import dedent

# --- GLOBAL CONFIGURABLE PARAMETERS ---

# Default art style used in image prompts
DEFAULT_ART_STYLE = "warm, colorful, hand-drawn style suitable for children"

# Default tone used for storytelling prompts
DEFAULT_TONE = "friendly and imaginative"

# Banned topics to filter from input and output (ensures child-safe content)
BANNED_TOPICS = ['violence', 'drugs', 'kill', 'blood', 'weapon', 'death']

"""
NOTES:
- Children aged 1–5 prefer bright, funny, cartoonish characters and simple plots.
- Children aged 5–10 enjoy visually appealing characters with familiar personalities (e.g., Dora, Doremon),
  and more involved but still safe storytelling.
"""