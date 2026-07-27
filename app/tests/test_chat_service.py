from app.services.ai.chat_service import ask_database

response = ask_database(
    "Show the names of first 5 employees"
)

print(response)


'''
User
   │
   ▼
Natural Language
   │
   ▼
LLM
   │
   ▼
SQL Generation
   │
   ▼
SQL Execution
   │
   ▼
Database
   │
   ▼
Result
   │
   ▼
LLM
   │
   ▼
Natural Language Answer
'''