from langchain_community.utilities import SQLDatabase

from app.core.config import settings

db = SQLDatabase.from_uri(
    settings.database_url,
)