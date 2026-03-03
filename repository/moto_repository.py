from models.moto_model import Moto

def listar_moto(session):
    return session.query(Moto).all()


def atualizar_consumo(session, moto_id, consumo):
    moto = session.query(
        Moto
    ).filter(
        Moto.id == moto_id
    ).first()
    if moto:
        moto.consumo = consumo
        session.commit()
        return True
    else:
        return False

def excluir_moto(session,moto_id):

    moto = session.query(Moto).filter(Moto.id == moto_id).first()
    if moto:
        session.delete(moto)
        session.commit()
        return True
    else:
        return False




