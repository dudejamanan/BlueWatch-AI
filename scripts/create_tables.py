from app.database.base import Base
from app.database.connection import engine

# Import all models so SQLAlchemy knows about them
from app.database.models import *

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Done!")