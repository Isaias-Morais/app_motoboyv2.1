from models.dia_de_trabalho_model import Dia_de_trabalho
from sqlalchemy.orm import Session
from datetime import date
from sqlalchemy import func

def listar_dia_de_trabalho(session:Session,moto_id:int):
    historico_dia_de_trabalho = session.query(
        Dia_de_trabalho
    ).filter(
        Dia_de_trabalho.moto_id == moto_id
    ).all()

    if not historico_dia_de_trabalho:
        return None

    return historico_dia_de_trabalho



def buscar_dia_de_trabalho_data(session:Session,moto_id:int,data:date):
    dia_de_trabalho = session.query(
        Dia_de_trabalho
    ).filter(
        Dia_de_trabalho.moto_id == moto_id,
        Dia_de_trabalho.data_trabalhada == data
    ).first()

    if not dia_de_trabalho:
        return None

    return dia_de_trabalho


def historico_dias(session,moto_id):
    dias = session.query(
        Dia_de_trabalho.data_trabalhada,
            (Dia_de_trabalho.quilometragem_final - Dia_de_trabalho.quilometragem_final),
            Dia_de_trabalho.ganho_bruto
        ).filter(
            Dia_de_trabalho.moto_id == moto_id
        ).all()

    return dias


def buscar_dia_de_trabalho_id(session:Session,moto_id:int,id:int):
    dia_de_trabalho = session.query(
        Dia_de_trabalho
    ).filter(
        Dia_de_trabalho.moto_id == moto_id,
        Dia_de_trabalho.id == id
    ).first()

    if not dia_de_trabalho:
        return None

    return dia_de_trabalho


def buscar_quilometragem_dia_de_trabalho_posterior(session:Session,moto_id:int,data:date):

    registro:Dia_de_trabalho = session.query(
        Dia_de_trabalho
    ).filter(
        Dia_de_trabalho.moto_id == moto_id,
        Dia_de_trabalho.data_trabalhada > data
    ).order_by(
        Dia_de_trabalho.data_trabalhada.asc()
    ).first()

    if not registro:
        return None

    return registro


def buscar_quilometragem_dia_de_trabalho_anterior(session: Session, moto_id: int, data: date):
    registro: Dia_de_trabalho = session.query(
        Dia_de_trabalho
    ).filter(
        Dia_de_trabalho.moto_id == moto_id,
        Dia_de_trabalho.data_trabalhada < data
    ).order_by(
        Dia_de_trabalho.data_trabalhada.desc()
    ).first()

    if not registro:
        return None

    return registro

