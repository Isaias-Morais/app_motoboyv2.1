from datetime import date
from models.manutencao_model import Manutencao


def listar_manutencao(session):
    return session.query(Manutencao).all()


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