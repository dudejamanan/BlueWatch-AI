import re
from app.services.ai.database import db


def clean_sql(response: str) -> str:
    # Extract SQL from a markdown code block
    match = re.search(r"```(?:sql)?\s*(.*?)\s*```", response, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Remove common LangChain prefixes
    response = re.sub(r"Question:.*?SQLQuery:", "", response, flags=re.DOTALL)

    return response.strip()


def execute_sql(query: str):
    query = clean_sql(query)
    return db.run(query)