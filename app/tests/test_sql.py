from app.services.ai.sql_chain import sql_chain

question = "How many employees are there?"

response = sql_chain.invoke(
    {
        "question": question
    }
)

print(response)