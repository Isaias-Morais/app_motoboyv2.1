from models.moto_model import Moto

def listar_moto(session):
    return session.query(Moto).all()


def excluir_moto(session,moto_id):

    moto = session.query(Moto).filter(Moto.id == moto_id).first()
    if moto:
        session.delete(moto)
        session.commit()
    else:
        return False




