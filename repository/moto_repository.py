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


def quilometragem_atual(session,moto_id):

    quilometragem_atual = session.query(
        Moto.quilometragem
    ).filter(
        Moto.id == moto_id
    ).first()

    if quilometragem_atual:
        return quilometragem_atual[0]


def atualizar_quilometragem(session,moto_id,quilometragem_nova):
    moto = session.query(
        Moto
    ).filter(
        Moto.id == moto_id
    ).first()
    if moto:
        moto.quilometragem = quilometragem_nova
        session.commit()
        return True
    else:
        return False


def moto_existe(session,moto_id=0):
    moto = session.query(
        Moto
    ).filter(
        Moto.id == moto_id
    ).first()

    return moto

