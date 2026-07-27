import re


FORBIDDEN_KEYWORDS = {
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
    "MERGE",
    "GRANT",
    "REVOKE",
}


def validate_sql(sql: str) -> str:
    """
    Validate AI-generated SQL before execution.
    """

    query = sql.strip()

    # Must start with SELECT or WITH (CTEs)
    if not re.match(r"^(SELECT|WITH)\b", query, re.IGNORECASE):
        raise ValueError("Only SELECT queries are allowed.")

    upper = query.upper()

    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", upper):
            raise ValueError(f"Forbidden SQL detected: {keyword}")

    return query