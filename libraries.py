# === Standard Library Imports ===
import os  # For accessing environment variables like API keys
import re  # For regex operations (e.g., content validation or filtering)
from typing import Optional  # Allows optional function parameters
from textwrap import dedent  # Useful for formatting multiline prompt strings

# === Third-Party Libraries ===
from dotenv import load_dotenv  # Loads environment variables from a .env file
import openai  # Used to access OpenAI's GPT models (e.g., ChatCompletion)
