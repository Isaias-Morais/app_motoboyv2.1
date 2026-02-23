from models.moto_model import Moto
from validacoes.moto_exitente import moto_existe
from database.session import SessionLocal

session = SessionLocal()

def listar_moto(session):
    return session.query(Moto).all()


def excluir_moto(session,moto_id):

    moto = session.query(Moto).filter(Moto.id == moto_id).first()
    if moto:
        session.delete(moto)
        session.commit()
    else:
        return False




