import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_story(outline: list, tone: str) -> list:
    """
    Expands comic panel outlines into detailed narration and character dialogues using Gemini Pro.
    """
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    
    story_panels = []
    for panel in outline:
        prompt = f"""
        Expand this comic panel into narration and character dialogue:
        Tone: {tone}
        Panel Title: {panel['title']}
        Scene: {panel['scene_description']}

        Provide output in the format:
        Caption: [Brief background ambient description]
        Narration: [Main character actions/dialogue]
        """
        response = model.generate_content(prompt)
        panel_text = response.text if response.text else f"Caption: {panel['scene_description']}\nNarration: {panel['title']}"
        
        story_panels.append({
            "panel": panel["panel"],
            "title": panel["title"],
            "scene_description": panel["scene_description"],
            "image_prompt": panel["image_prompt"],
            "story_text": panel_text
        })
        
    return story_panels