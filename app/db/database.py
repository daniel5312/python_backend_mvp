from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.db.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
