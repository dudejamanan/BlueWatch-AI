from app.services.ai.agent import agent

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "show the recent trends of murder cases in the city"
            }
        ]
    }
)

print(response)


'''
User
   ↓
Agent
   ↓
Tool
   ↓
SQL Generator
   ↓
PostgreSQL
   ↓
Tool Result
   ↓
LLM
   ↓
Final Answer
'''