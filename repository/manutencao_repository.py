from datetime import date
from models.manutencao_model import Manutencao


def listar_manutencao(session):
    return session.query(Manutencao).all()


def excluir_manutencao(session,dia,mes,ano,moto_id):
    data = date(ano,mes,dia)
    manutencao = session.query(Manutencao).filter(
        Manutencao.moto_id,
        Manutencao.data_manutencao == data
    ).first()
    session.delete(manutencao)
    session.commit()

def historico_manutencoes(session,moto_id):
    session.query(Manutencao).filter(
        Manutencao.id == moto_id
    )