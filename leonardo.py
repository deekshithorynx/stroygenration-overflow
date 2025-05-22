# main.py

from dotenv import load_dotenv
import os
import openai
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

from character_prompt import character_prompt
from story_prompt import story_prompt
from image_prompt import image_prompt
from story_title_prompt import story_title_prompt
from utils import split_story_into_pages

# Load API keys
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
LEONARDO_API_KEY = os.getenv("LEONARDO_API_KEY")

def generate_image(prompt: str, width: int = 1024, height: int = 1024) -> str:
    """
    Generate image from Leonardo.Ai
    """
    headers = {
        "Authorization": f"Bearer {LEONARDO_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "width": width,
        "height": height,
        "num_images": 1,
        "guidance_scale": 7.5,
        "num_inference_steps": 30
    }

    response = requests.post("https://cloud.leonardo.ai/api/rest/v1/generations", headers=headers, json=data)
    
    if response.status_code != 200:
        raise Exception(f"Leonardo API Error: {response.status_code} - {response.text}")
    
    image_url = response.json()["generations"][0]["generated_images"][0]["url"]
    return image_url

def save_image_from_url(url, filename):
    """
    Download and save image from URL
    """
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.save(filename)
    return filename

def create_pdf(storybook, output_path="storybook.pdf"):
    """
    Create a PDF from the storybook content
    """
    pages = []
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust path if needed
    font_size = 24

    for page in storybook["pages"]:
        img_path = f"page_{page['page']}.jpg"
        if not os.path.exists(img_path):
            continue
        img = Image.open(img_path).convert("RGB")
        draw = ImageDraw.Draw(img)

        # Add text
        font = ImageFont.truetype(font_path, font_size)
        text = page["text"]
        draw.text((50, 50), text, font=font, fill="black")

        pages.append(img)

    if pages:
        pages[0].save(output_path, save_all=True, append_images=pages[1:])
        print(f"PDF saved to {output_path}")
    else:
        print("No pages were available to save.")

def run_story_pipeline(title: str, genre: str, age_group: str = "5–10"):
    # Step 1: Character generation
    char_msg = character_prompt(title, genre, age_group)
    char_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": char_msg}],
        temperature=0.7
    )
    character = char_response["choices"][0]["message"]["content"].strip()
    print(f"Character Created:\n{character}\n")

    # Step 2: Story generation
    story_msg = story_prompt(title, genre, character)
    story_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": story_msg}],
        temperature=0.7
    )
    story = story_response["choices"][0]["message"]["content"].strip()
    print("Story Generated.")

    # Step 3: Split story into pages
    pages = split_story_into_pages(story, total_pages=2)

    # Step 4: Generate images with Leonardo
    for page in pages:
        page["image_prompt"] = image_prompt(character, page["text"])
        try:
            page["image_url"] = generate_image(page["image_prompt"])
            print(f"Page {page['page']} image generated.")
            image_path = f"page_{page['page']}.jpg"
            save_image_from_url(page["image_url"], image_path)
        except Exception as e:
            print(f"Page {page['page']} image failed: {e}")
            page["image_url"] = None

    storybook = {
        "title": title,
        "genre": genre,
        "character": character,
        "pages": pages
    }

    create_pdf(storybook)
    return storybook

if __name__ == "__main__":
    print("Welcome to the Storybook Creator!")
    title = input("Enter your story title: ").strip()
    genre = input("Enter the genre (e.g., Adventure, Fantasy, Animal): ").strip()

    if not title or not genre:
        print("Both title and genre are required. Please try again.")
    else:
        storybook = run_story_pipeline(title, genre)
        print(f"\nStorybook '{title}' generated and saved to PDF!")
