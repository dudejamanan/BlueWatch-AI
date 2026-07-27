from app.services.ai.database import db
from app.services.ai.utils.sql_validator import validate_sql
import re


def clean_sql(sql: str) -> str:
    match = re.search(r"```(?:sql)?\s*(.*?)\s*```", sql, re.DOTALL)
    if match:
        return match.group(1).strip()

    sql = sql.replace("Question:", "")
    sql = sql.replace("SQLQuery:", "")
    return sql.strip()


def execute_sql(query: str):

    query = clean_sql(query)

    query = validate_sql(query)

    return db.run(query)