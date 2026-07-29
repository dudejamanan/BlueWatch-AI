from langchain.agents import create_agent

from app.services.ai.llm import llm
from app.services.ai.tools.sql_tool import query_database
from app.services.ai.tools.analytics_tool import crime_analytics
from app.services.ai.tools.network_tool import crime_network
from app.services.ai.prompts.system_prompt import SYSTEM_PROMPT
TOOLS = [
    query_database,
    crime_analytics,
    crime_network,
]

agent = create_agent(
    model=llm,
    tools=TOOLS,
    system_prompt=SYSTEM_PROMPT,
)