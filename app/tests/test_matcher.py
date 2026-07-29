from app.services.analytics.matcher import match_metric

print(match_metric("What is the recent crime rate in the city?"))
print(match_metric("crime rate"))
print(match_metric("recent crime"))
print(match_metric("total number of cases"))