import os
import re
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

# Initialize Stable Diffusion pipeline
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
if torch.cuda.is_available():
    pipe = pipe.to("cuda")

def generate_image(prompt: str, panel_num: int) -> str:
    """
    Generates a comic illustration based on the image prompt and saves it locally.
    """
    output_dir = "static/panels"
    os.makedirs(output_dir, exist_ok=True)
    
    clean_prompt = re.sub(r'[^a-zA-Z0-9_\- ]', '', prompt)[:30].replace(" ", "_")
    file_path = f"{output_dir}/panel_{panel_num}_{clean_prompt}.png"

    image = pipe(prompt).images[0]
    image.save(file_path)
    
    return file_path