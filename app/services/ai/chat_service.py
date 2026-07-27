from app.services.ai.sql_chain import sql_chain
from app.services.ai.sql_executor import execute_sql


def ask_database(question: str):
    sql = sql_chain.invoke({"question": question})

    result = execute_sql(sql)

    return {
        "question": question,
        "sql": sql,
        "result": result,
    }