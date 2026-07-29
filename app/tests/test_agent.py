from app.services.ai.agent import agent

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Show the criminal network."
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