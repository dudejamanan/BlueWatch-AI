from app.services.ai.sql_chain import sql_chain
from app.services.ai.sql_executor import execute_sql

question = "How many victims are there thaqt occur twice?"

sql = sql_chain.invoke({"question": question})

print("Generated SQL:")
print(sql)

print("\nExecuting...\n")

result = execute_sql(sql)

print(result)