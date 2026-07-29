from app.services.ai.tools.analytics_tool import crime_analytics

print(
    crime_analytics.invoke(
        {"question": "total number of cases"}
    )
)