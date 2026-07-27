from langchain.tools import tool

from app.services.ai.chat_service import ask_database


@tool
def query_database(question: str) -> str:
    """
    Query the BlueWatch crime database.

    Use this tool whenever the user asks about:
    - employees
    - accused
    - victims
    - FIRs
    - cases
    - police stations
    - crimes
    """

    response = ask_database(question)

    return response["answer"]