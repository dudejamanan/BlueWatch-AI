from langchain.agents import create_agent

from app.services.ai.llm import llm
from app.services.ai.tools.sql_tool import query_database
from app.services.ai.tools.analytics_tool import crime_analytics

agent = create_agent(
    model=llm,
    tools=[query_database,crime_analytics],
    system_prompt="""
You are BlueWatch AI.

You are an AI assistant for law enforcement.

Whenever the user asks about data in the database,
use the available tool.

Never invent database information.
"""
)