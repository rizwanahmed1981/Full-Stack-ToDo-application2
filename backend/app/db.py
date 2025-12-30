from sqlmodel import create_engine, Session
from sqlalchemy import text
import os

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./task.db")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    """Dependency to provide database session"""
    with Session(engine) as session:
        yield session

def test_connection():
    """Test database connection"""
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False