from models.dia_de_trabalho_model import Dia_de_trabalho
from sqlalchemy import func

def listar_dia_de_trabalho(session):
    dias_trabalhados_geral = session.query(
        Dia_de_trabalho
    ).all

    if dias_trabalhados_geral:
        return dias_trabalhados_geral
    else:
        return False


def excluir_dias_trabalhados(session,moto_id):
    dia_trabalhado = session.query(
        Dia_de_trabalho
    ).filter(
        Dia_de_trabalho.moto_id == moto_id
    ).first()
    if dia_trabalhado:
        session.delete(dia_trabalhado)
        session.commit()
        return True
    else:
        return False

def historico_dias(session,moto_id):
    dias = session.query(
        Dia_de_trabalho.data_trabalhada,
            (Dia_de_trabalho.quilometragem_final - Dia_de_trabalho.quilometragem_final),
            Dia_de_trabalho.ganho_bruto
        ).filter(
            Dia_de_trabalho.moto_id == moto_id
        ).all()

    return dias

