import os
import json
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_outline(prompt: str, character: str, setting: str, tone: str, art_style: str):
    """
    Generates a structured 5-panel comic outline using Gemini Flash.
    """
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    
    structured_prompt = f"""
    Create a 5-panel comic outline based on:
    Prompt: {prompt}
    Character: {character}
    Setting: {setting}
    Tone: {tone}
    Art Style: {art_style}

    Return ONLY a JSON array with 5 objects containing:
    - "panel": panel number (1-5)
    - "title": panel title
    - "scene_description": short scene background context
    - "image_prompt": detailed visual prompt for Stable Diffusion in '{art_style}' style
    """
    
    response = model.generate_content(structured_prompt)
    try:
        text = response.text.strip().lstrip("```json").rstrip("```").strip()
        return json.loads(text)
    except Exception:
        # Fallback panel generation
        return [
            {
                "panel": i,
                "title": f"Panel {i}",
                "scene_description": f"{character} in {setting}",
                "image_prompt": f"A comic panel of {character} in {setting}, style of {art_style}"
            }
            for i in range(1, 6)
        ]