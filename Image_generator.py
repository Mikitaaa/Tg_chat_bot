from huggingface_hub import InferenceClient
from PIL import Image
import os
from Config_handler import load_config

config = load_config('config.txt')

client = InferenceClient(
    provider="fal-ai",
    api_key = config['api_key']
)

def getImagePath(prompt: str) -> str:
   
    try:
        image = client.text_to_image(prompt, model="black-forest-labs/FLUX.1-dev")
        
        image_path = "generated_image.png"
        image.save(image_path)
        
        return image_path  
    
    except Exception as e:
        print(f"Ошибка при генерации изображения: {e}")
        return None 
