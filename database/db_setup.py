
from models.models import Base
from database.db_session import engine


# Create tables based on model definitions
Base.metadata.create_all(engine)

# Optionally, populate initial data
# ...
