import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

generation_config = {'temperature': 0}


template = """Given an image or a list of images, you need to extract the information an return the result in JSON format with the following keys:

{keys}
"""