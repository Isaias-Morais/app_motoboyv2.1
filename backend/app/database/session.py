from sqlalchemy.orm import sessionmaker
from backend.app.database.engine import engine

SessionLocal = sessionmaker(bind=engine)
