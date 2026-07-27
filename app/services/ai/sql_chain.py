
from langchain_classic.chains import create_sql_query_chain
from app.services.ai.llm import llm
from app.services.ai.database import db

sql_chain = create_sql_query_chain(
    llm=llm,
    db=db,
)