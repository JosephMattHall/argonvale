from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Define the database URL directly here
DATABASE_URL = "sqlite:///argonvale_db.db"
print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def setup_database():
    from models import Base
    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Perform other database setup tasks if needed
