import os
from fastapi import APIRouter, Request
from google import genai
from google.genai import types

router = APIRouter()

try:
    client = genai.Client()
except Exception as e:
    client = None

@router.get("/")
async def index():
    return {"message": "Welcome to ComicCraft AI"}

@router.post("/generate-comic")
async def generate_comic(request: Request):
    if not client:
        return {"error": "Gemini API key is missing"}
        
    data = await request.json()
    user_prompt = data.get('prompt')
    
    if not user_prompt:
        return {"error": "Prompt is required"}

    system_instruction = "You are a comic artist. Break down the story into a panel-by-panel script."
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"Create a 4-panel comic for: {user_prompt}",
            config=types.GenerateContentConfig(system_instruction=system_instruction)
        )
        return {"success": True, "script": response.text}
    except Exception as e:
        return {"error": str(e)}