# === Import necessary libraries and local modules ===
from dotenv import load_dotenv  # Loads environment variables from .env file
import os
import openai  # OpenAI API for character and story generation
from character_prompt import character_prompt  # Custom module to generate character prompt
from story_prompt import story_prompt  # Custom module to generate story prompt
from image_prompt import image_prompt  # Custom module to create image prompts
from utils import split_story_into_pages  # Utility to split a story into multiple pages
import config  # (Assumed) configuration file for global settings
from saftey import validate_safe_input  # Function to check if input is safe (e.g., no bad content)
from story_title_prompt import story_title_prompt  # Unused in this script but potentially helpful
from IPython.display import Image, display  # Used to visually display generated images in notebooks

# === Load API keys from .env file ===
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set OpenAI API key
LEONARDO_API_KEY = os.getenv("LEONARDO_API_KEY")  # Set Leonardo API key for image generation

# === Set up configuration for Leonardo image model ===
MODEL_ID = "e316348f-7773-490e-adcd-46757c738eb7"  # Specific model ID for Leonardo Creative v2

import requests  # Used for making HTTP requests to Leonardo.Ai
import time  # Used for polling/waiting between image generation checks
from datetime import datetime  # Used to generate unique filenames for image saving

def generate_image(prompt: str) -> str:
    """
    Sends a prompt to Leonardo.Ai to generate an image, waits for completion, and downloads it.
    Returns the local path to the saved image.
    """
    # Make sure API key exists
    if not LEONARDO_API_KEY:
        raise ValueError("API key is missing. Set the LEONARDO_API_KEY environment variable.")

    # Endpoint and headers for the Leonardo API
    url = "https://cloud.leonardo.ai/api/rest/v1/generations"
    headers = {
        "Authorization": f"Bearer {LEONARDO_API_KEY}",
        "Content-Type": "application/json"
    }

    # Image generation parameters
    data = {
        "prompt": prompt,
        "modelId": MODEL_ID,
        "num_images": 1,
        "width": 1024,
        "height": 1024,
        "guidance_scale": 8,  # Controls how closely image follows the prompt
        "num_inference_steps": 30  # Number of steps for generating the image
    }

    print(f"🖼️ Sending to Leonardo: {prompt[:100]}...")  # Truncated for readability
    try:
        # Submit image generation job
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        generation_id = response.json()["sdGenerationJob"]["generationId"]
    except Exception as e:
        raise RuntimeError(f"Failed to submit generation: {e}")

    # === Polling the API to check when image generation is complete ===
    status_url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}"
    for _ in range(20):  # Try polling every 2 seconds, up to 40 seconds
        time.sleep(2)
        try:
            status_response = requests.get(status_url, headers=headers)
            status_response.raise_for_status()
            images = status_response.json().get("generations_by_pk", {}).get("generated_images", [])
            if images:
                image_url = images[0]["url"]
                return download_image(image_url)
        except Exception as e:
            print(f"⚠️ Polling error: {e}")
            continue  # Continue polling rather than giving up immediately

    raise TimeoutError("Leonardo image generation timed out.")

def download_image(url: str, folder_name="leonardo_images") -> str:
    """
    Downloads the image from the given URL and saves it in a local folder.
    Returns the path to the saved image.
    """
    # Determine local folder path in the user's home directory
    home_dir = os.path.expanduser("~")
    folder_path = os.path.join(home_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

    # Generate a unique filename using timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder_path, f"leonardo_image_{timestamp}.png")

    try:
        # Download and save image
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"💾 Image saved to: {filename}")
        return filename
    except Exception as e:
        raise RuntimeError(f"Failed to download image: {e}")

def run_story_pipeline(title: str, genre: str, age_group: str = "5–10"):
    """
    Generates a complete storybook including:
    1. Character generation
    2. Story creation
    3. Splitting the story into pages
    4. Image generation per page
    """
    # Optional: Validate input for safety (e.g., avoid harmful prompts)
    if not validate_safe_input(title) or not validate_safe_input(genre):
        raise ValueError("Unsafe input detected. Please revise your title/genre.")

    # === Step 1: Generate a character based on title and genre ===
    char_msg = character_prompt(title, genre, age_group)
    char_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": char_msg}],
        temperature=0.7
    )
    character = char_response.choices[0].message["content"].strip()
    print(f"\n✅ Character Created:\n{character}\n")

    # === Step 2: Create the story with the character ===
    story_msg = story_prompt(title, genre, character)
    story_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": story_msg}],
        temperature=0.7
    )
    story = story_response.choices[0].message["content"].strip()
    print("✅ Story Generated.\n")

    # === Step 3: Divide story into 5 logical pages ===
    pages = split_story_into_pages(story, total_pages=5)

    # === Step 4: Generate one image per page ===
    for page in pages:
        page["image_prompt"] = image_prompt(character, page["text"])  # Create image prompt
        try:
            page["image_url"] = generate_image(page["image_prompt"])  # Generate and download image
            print(f"✅ Page {page['page']} image generated.")
        except Exception as e:
            print(f"❌ Page {page['page']} image failed: {e}")
            page["image_url"] = None  # Handle failure gracefully

    # Return full storybook data
    return {
        "title": title,
        "genre": genre,
        "character": character,
        "story": story,
        "pages": pages
    }

# === CLI Entry Point ===
if __name__ == "__main__":
    print("📚 Welcome to the Storybook Creator!")

    # Get user input for story title and genre
    title = input("Enter your story title: ").strip()
    genre = input("Enter the genre (e.g., Adventure, Fantasy, Animal): ").strip()

    # Basic input validation
    if not title or not genre:
        print("❌ Both title and genre are required. Please try again.")
    else:
        # Run the full storybook generation pipeline
        storybook = run_story_pipeline(title, genre)
        print(f"\n🎉 Storybook '{title}' generated successfully!")

        # Print each page's text and show its image if available
        for page in storybook["pages"]:
            print(f"\n📖 Page {page['page']}:\n{page['text']}")
            if page["image_url"]:
                display(Image(filename=page["image_url"]))  # Display image from local file
            else:
                print("⚠️ No image found.")
