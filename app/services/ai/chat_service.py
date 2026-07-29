from app.services.ai.llm import llm
from app.services.ai.sql_chain import sql_chain
from app.services.ai.sql_executor import execute_sql


def ask_database(question: str):
    # Step 1: Generate SQL
    sql = sql_chain.invoke({"question": question})
    print("\nGenerated SQL:")
    print("-" * 50)
    print(repr(sql))
    print("-" * 50)

    # Step 2: Execute SQL
    result = execute_sql(sql)

    # Step 3: Generate a human-friendly response
    prompt = f"""
You are BlueWatch AI.

A user asked:
{question}

The SQL generated was:
{sql}

The SQL returned:
{result}

Answer the user's question naturally and concisely.
Do not mention SQL unless explicitly asked.
If the result is empty, clearly say no records were found.
"""


    return {
        "question": question,
        "sql": sql,
        "result": result,
    }