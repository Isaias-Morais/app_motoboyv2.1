from sqlalchemy.orm import Session
from models.abastecimento_model import Abastecimento
from datetime import date


def buscar_abastecimento_id(session,moto_id,abastecimento_id:int):
    abastecimento = (
        session.query(
            Abastecimento
    ).filter(
            Abastecimento.id == abastecimento_id,
            Abastecimento.moto_id == moto_id
    ).first()
    )

    return abastecimento


def listar_abastecimento(session):
    abastecimentos = session.query(Abastecimento).all()
    return abastecimentos


def historico_abastecimentos(session:Session,moto_id:int):

    abastecimentos = session.query(
        Abastecimento
    ).filter(
        Abastecimento.moto_id == moto_id
    ).order_by(
        Abastecimento.data_abastecimento
    ).all()

    if not abastecimentos:
        return None

    return abastecimentos


def abastecimento_existe(session,moto_id,quilometragem):
    abastecimento:Abastecimento = session.query(
        Abastecimento
    ).filter(
        Abastecimento.moto_id == moto_id,
        Abastecimento.quilometragem_abastecimento == quilometragem
    ).first()

    return abastecimento is not None


def abstecimento_por_data(session:Session,moto_id:int,data:date):

    abastecimento:Abastecimento = session.query(
        Abastecimento
    ).filter(
        Abastecimento.moto_id == moto_id,
        Abastecimento.data_abastecimento == data
    ).all()

    if not abastecimento:
        return None

    return abastecimento

