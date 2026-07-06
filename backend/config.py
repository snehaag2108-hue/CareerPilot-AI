import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

UPLOAD_FOLDER = "uploads"
MEMORY_FOLDER = "data"

MODEL_NAME = "gemini-2.5-flash"