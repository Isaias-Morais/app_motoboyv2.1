from database.session import SessionLocal
from models.motoboy_model import Motoboy

session = SessionLocal()

def listar_motoboys(session):
    return session.query(Motoboy).all()
