from langchain.tools import tool

from app.database.connection import SessionLocal
from app.services.analytics.crime_analytics import CrimeAnalytics
from app.services.analytics.matcher import match_metric
from app.services.analytics.formatter import format_result


@tool
def crime_analytics(question: str):
    """
    Use for crime statistics, trends,
    dashboards, reports,
    aggregations and analytics.
    """

    metric = match_metric(question)

    if metric is None:
        return {
            "success": False,
            "error": "Analytics capability not found."
        }

    print("=" * 60)
    print("Question :", question)
    print("Metric   :", metric.name)
    print("Handler  :", metric.handler)
    print("=" * 60)

    db = SessionLocal()

    try:
        fn = getattr(CrimeAnalytics, metric.handler)

        result = fn(db)

        return {
            "success": True,
            **format_result(metric, result)
        }

    except AttributeError:
        return {
            "success": False,
            "error": f"Analytics function '{metric.handler}' does not exist."
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

    finally:
        db.close()