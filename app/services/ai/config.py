import os
from dotenv import load_dotenv
from app.core.config import settings

load_dotenv()


GROQ_API_KEY = settings.groq_api_key

MODEL_NAME = "openai/gpt-oss-20b"
TEMPERATURE = 0
MAX_TOKENS = 2048