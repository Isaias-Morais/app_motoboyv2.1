from sqlalchemy.orm import Session
from models.motoboy_model import Motoboy
from models.moto_model import Moto


def busca_motoboy_id(session:Session,motoboy_id:int):
    motoboy =  session.query(Motoboy).filter(Motoboy.id == motoboy_id).first()

    if not motoboy:
        return None

    return motoboy


def listar_motoboys(session):
    return session.query(Motoboy).all()


def definir_moto_ativa_motoboy(session:Session,motoboy_id:int,moto:Moto):
    motoboy = session.query(Motoboy).filter(Motoboy.id == motoboy_id).first()

    if not motoboy:
        return None

    motoboy.moto_ativa = moto.id

    session.commit()
    session.refresh(motoboy)

    return motoboy


def redefinir_moto_ativa_motoboy(session:Session,motoboy:Motoboy):

    try:
        motoboy.moto_ativa = None
        session.commit()
    except Exception as e:
        return e


def motoboy_existe_id(session,id_motoboy=1):
    motoboy = session.query(
        Motoboy
    ).filter(
        Motoboy.id == id_motoboy
    ).first()

    return motoboy
