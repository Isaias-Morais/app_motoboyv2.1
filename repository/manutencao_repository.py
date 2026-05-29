from datetime import date

from sqlalchemy.orm import Session

from models.manutencao_model import Manutencao


def listar_manutencao(session:Session,moto_id:int):
    manutencoes =  session.query(Manutencao).filter(Manutencao.moto_id == moto_id).all()

    if not manutencoes:
        return None

    return manutencoes


def excluir_manutencao(session,moto_id):
    manutencao = session.query(Manutencao).filter(
        Manutencao.moto_id == moto_id,
    ).all()
    session.delete(manutencao)
    session.commit()

def historico_manutencoes(session,moto_id):
    session.query(Manutencao).filter(
        Manutencao.id == moto_id
    )