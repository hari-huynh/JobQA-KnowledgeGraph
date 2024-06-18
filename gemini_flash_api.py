import google.generativeai as genai

from config import API_KEY

genai.configure(api_key=API_KEY)


class GeminiAPI:
    def __init__(self, generation_config, safety_settings):
        self.gemini_api = genai.GenerativeModel(model_name = "gemini-1.5-flash-latest",
                                                 generation_config=generation_config,
                                                 safety_settings=safety_settings)

    def generate_output(self, imgs_list, prompt):
        response = self.gemini_api.generate_content([prompt, *imgs_list])
        return response.text