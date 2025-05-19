# 📚 Children's Storybook Generator

This project is a creative pipeline for generating safe, illustrated children's stories using OpenAI's GPT-4 and DALL·E 3. Users simply input a story title and genre, and the tool generates a lovable main character, a 20-page story, and corresponding illustrations.

---

## ✨ Features

- 🧒 **Main Character Generator** – Creates a memorable, kid-friendly character.
- 📖 **Story Writer** – Generates a 20-page story tailored to children aged 5–10.
- 🖼️ **Image Creator** – Uses DALL·E 3 to illustrate each page based on the story and character.
- 🔒 **Content Filtering** – Automatically removes inappropriate themes like violence, drugs, or death.

---

## 🚀 How It Works

1. **Input from user**:
   - Story Title (e.g., *The Flying Fox*)
   - Genre (e.g., *Fantasy*, *Adventure*, *Animal*)

2. **Pipeline execution**:
   - `character_prompt()` creates a description for the main character.
   - `story_prompt()` generates a full story using that character.
   - `split_story_into_pages()` breaks the story into 20 illustrated pages.
   - `image_prompt()` describes each scene visually.
   - `generate_image()` creates illustrations using OpenAI’s DALL·E 3 API.

3. **Output**:
   - A dictionary with:
     - Title
     - Character description
     - 20 pages of story text
     - 20 corresponding image URLs

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/storybook-generator.git
cd storybook-generator
### 2. install Dependencies
pip install -r requirements.txt
'''
---
 How to Improve
🧠 Functional
Add support for user-selected reading levels (early, intermediate)

Make number of pages configurable

Allow continuing existing stories with extend_story_prompt

💻 Technical
Add logging and error handling (e.g., retry if DALL·E fails)

Wrap the pipeline into a simple CLI or web interface

Move all hardcoded values to config

🖼️ Presentation
Export the final book as a PDF or interactive webpage

Add support for downloading all images and story text

