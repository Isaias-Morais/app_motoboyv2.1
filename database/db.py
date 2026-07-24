from database.session import SessionLocal

#retorna Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()