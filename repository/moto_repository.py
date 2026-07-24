from sqlalchemy.orm import Session

from models.moto_model import Moto

def listar_moto(session:Session,id:int):
    return session.query(Moto).filter(Moto.motoboy_id == id).all()


def busca_moto(session:Session,id_moto:int,id_motoboy:int):
    moto = (
        session.query(Moto)
        .filter(
            Moto.id == id_moto,
            Moto.motoboy_id == id_motoboy
        )
        .first()
    )

    return moto


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
