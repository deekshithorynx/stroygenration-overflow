# main.py or pipeline.py

from dotenv import load_dotenv
from IPython.display import Image, display 

import os
import openai # if its version >1.11 than us this 
#from opeanai import OpenAI
from character_prompt import character_prompt
from story_prompt import story_prompt
from image_prompt import image_prompt
from story_title_prompt import story_title_prompt   
from utils import split_story_into_pages
from utils import split_story_into_pages

#client = OpenAI() # disable if you importing as openai
#openai=client # diable as above
# Load API keys
load_dotenv()
openai.api_key = # Input the api/scret key
def generate_image(prompt: str) -> str:
    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )
    return response["data"][0]["url"]

def run_story_pipeline(title: str, genre: str, age_group: str = "5–10"):
    # Step 1: Character
    char_msg = character_prompt(title, genre, age_group)
    char_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": char_msg}],
        temperature=0.7
    )
    character = char_response["choices"][0]["message"]["content"].strip()
    print(f"✅ Character Created:\n{character}\n")

    # Step 2: Story
    story_msg = story_prompt(title, genre, character)
    story_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": story_msg}],
        temperature=0.7
    )
    story = story_response["choices"][0]["message"]["content"].strip()
    print("✅ Story Generated.")

    # Step 3: Pages
    pages = split_story_into_pages(story, total_pages=20)

    # Step 4: Images
    for page in pages:
        page["image_prompt"] = image_prompt(character, page["text"])
        try:
            page["image_url"] = generate_image(page["image_prompt"])
            print(f"✅ Page {page['page']} image generated.")
        except Exception as e:
            print(f"❌ Page {page['page']} image failed: {e}")
            page["image_url"] = None

    return {
        "title": title,
        "genre": genre,
        "character": character,
        "pages": pages
    }

if __name__ == "__main__":
    print("📚 Welcome to the Storybook Creator!")
    title = input("Enter your story title: ").strip()
    genre = input("Enter the genre (e.g., Adventure, Fantasy, Animal): ").strip()

    if not title or not genre:
        print("❌ Both title and genre are required. Please try again.")
    else:
        storybook = run_story_pipeline(title, genre)
        print(f"\n🎉 Storybook '{title}' generated successfully!")

        for page in storybook["pages"]:
            print(f"\n📖 Page {page['page']}:\n{page['text']}")
            if page["image_url"]:
                display(Image(url=page["image_url"]))
            else:
                print("⚠️ No image found.")
display(Image(url=page["image_url"]))

    
