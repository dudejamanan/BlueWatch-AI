from app.services.ai.llm import llm

response = llm.invoke("Who are you?")

print(response.content)