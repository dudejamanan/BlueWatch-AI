from langchain.tools import tool

from app.database.connection import SessionLocal

from app.services.network.network_matcher import match_network
from app.services.network.network_formatter import format_network
from app.services.network.crime_network import CrimeNetwork


@tool
def crime_network(question: str):
    """
    Analyze criminal relationships, gangs, accomplices,
    and crime networks based on the user's question.
    """

    metric = match_network(question)

    if metric is None:

        return {

            "error": "Network capability not found."

        }

    db = SessionLocal()

    try:

        fn = getattr(

            CrimeNetwork,

            metric.handler

        )

        # placeholder until entity extraction
        result = fn(db)

        return format_network(

            metric,

            result

        )

    finally:

        db.close()