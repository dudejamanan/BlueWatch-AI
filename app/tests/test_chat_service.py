from app.services.ai.chat_service import ask_database

response = ask_database("How many accused are victims?")

print(response)