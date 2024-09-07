import os
import base64
from openai import OpenAI
from dotenv import load_dotenv
import requests
from telegram_bot import server_push_notifications
class AccidentAnalyzer:
    def __init__(self):
        load_dotenv() 
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def analyze_accident(self, image_path): 
        base64_image = self.encode_image(image_path)
         
        response = self.client.chat.completions.create(
            model="gpt-4o",  
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Please explain the case of the accident in this image. in 1.Situation 2. analyzer what happened and show another information involve about situation"},
                        {
                            "type": "image_url",
                            "image_url": {
                                 "url": f"data:image/jpeg;base64,{base64_image}",
                            }
                        },
                    ],
                }
            ],
            max_tokens=300,
        )
        
        message_content = response.choices[0].message.content
        server_push_notifications(message_content)
        
        return message_content