from datetime import date

from sqlalchemy.orm import Session

from models.manutencao_model import Manutencao

def buscar_manutencao(session:Session,moto_id:int,id:int):
    manutencao = (
        session.query(Manutencao)
    .filter(
            Manutencao.id == id,
            Manutencao.moto_id == moto_id
        )
    .first()
    )

    return manutencao


def listar_manutencao(session:Session,moto_id:int):
    manutencoes =  session.query(Manutencao).filter(Manutencao.moto_id == moto_id).all()

    if not manutencoes:
        return None

    return manutencoes


def listar_manutencao_data(session:Session,moto_id:int,data:date):
    manutencoes =  session.query(Manutencao).filter(Manutencao.moto_id == moto_id, Manutencao.data_manutencao == data).all()

    if not manutencoes:
        return None

    return manutencoes


def buscar_quilometragem_manutencao_posterior(session:Session,moto_id:int,data:date):

    registro:Manutencao = session.query(
        Manutencao
    ).filter(
        Manutencao.moto_id == moto_id,
        Manutencao.data_manutencao > data
    ).order_by(
        Manutencao.data_manutencao.asc()
    ).first()

    if not registro:
        return None

    return registro


def buscar_quilometragem_manutencao_anterior(session: Session, moto_id: int, data: date):
    registro: Manutencao = session.query(
        Manutencao
    ).filter(
        Manutencao.moto_id == moto_id,
        Manutencao.data_manutencao < data
    ).order_by(
        Manutencao.data_manutencao.desc()
    ).first()

    if not registro:
        return None

    return registro
