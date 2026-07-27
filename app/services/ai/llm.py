from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

from app.services.ai.config import (
    GROQ_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)

api_key = os.getenv("GROQ_API_KEY")
print("API KEY:", api_key)


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=MODEL_NAME,
    temperature=TEMPERATURE,
    max_tokens=MAX_TOKENS,
)

from dotenv import load_dotenv
import os

load_dotenv()

