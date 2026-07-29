from app.services.analytics.metrics import Metric

REGISTRY = [

    Metric(

        name="total_cases",

        description="Total registered cases",

        keywords=[
            "total cases",
            "case count",
            "how many cases",
            "number of cases"
        ],

        handler="total_cases"
    ),

    Metric(

        name="district_cases",

        description="Cases by district",

        keywords=[
            "district",
            "district wise",
            "district statistics",
            "district ranking"
        ],

        handler="cases_by_district"
    ),

    Metric(

        name="crime_trend",

        description="Recent crime trend",

        keywords=[
            "recent crime",
            "crime trend",
            "crime rate",
            "latest crime",
            "monthly crime"
        ],

        handler="monthly_trend"
    ),

]