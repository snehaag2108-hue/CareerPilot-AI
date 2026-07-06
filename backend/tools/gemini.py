import google.generativeai as genai
from backend.config import GEMINI_API_KEY, MODEL_NAME


class GeminiClient:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("Gemini API Key not found!")

        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {e}"


# Singleton instance
gemini = GeminiClient()