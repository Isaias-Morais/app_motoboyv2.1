from datetime import date ,timedelta
from sqlalchemy import func
from models.abastecimento_model import Abastecimento
from models.dia_de_trabalho_model import Dia_de_trabalho
from models.manutencao_model import Manutencao
from models.moto_model import Moto


def buscar_dia_de_trabalho(session,moto_id):
    hoje =  date.today()

    return (session.query(
            Dia_de_trabalho.ganho_bruto.label('ganho'),
            (Dia_de_trabalho.quilometragem_final - Dia_de_trabalho.quilometragem_inicial).label('km')
        ).filter(
            Dia_de_trabalho.moto_id == moto_id,
            Dia_de_trabalho.data_trabalhada == hoje
        ).first()
    )


def busca_abastecimento(session, moto_id):
    hoje = date.today()
    inicio = hoje - timedelta(days=30)

    resumo = (session.query(
        func.coalesce(func.sum(Abastecimento.valor),0).label('valor'),
        func.coalesce(func.sum(Abastecimento.litros),0).label('litros'),
        func.coalesce(func.max(Abastecimento.quilometragem_abastecimento) - func.min(Abastecimento.quilometragem_abastecimento),0).label('km')
    ).filter(
        Abastecimento.moto_id == moto_id,
        Abastecimento.data_abastecimento.between(inicio,hoje)
    ).first()
              )

    return resumo._asdict() if resumo else {}


def busca_manutencoes(session, moto_id):
    hoje = date.today()
    inicio = hoje - timedelta(days=30)

    resumo = (session.query(
        func.coalesce(func.sum(Manutencao.valor), 0).label('valor'),
        func.coalesce(func.max(Manutencao.quilometragem_manutencao) - func.min(Manutencao.quilometragem_manutencao),0).label('km')
    ).filter(
        Manutencao.moto_id == moto_id,
        Manutencao.data_manutencao.between(inicio, hoje)
    ).first()
              )

    return resumo._asdict() if resumo else {}

def busca_abastecimento_consumo_medio(session,moto_id):

    resumo = (session.query(
        Abastecimento.quilometragem_abastecimento.label('km'),
        Abastecimento.litros.label('litros'
            )).filter(
            Abastecimento.moto_id == moto_id,
            Abastecimento.tanque_completo == True
        ).order_by(Abastecimento.quilometragem_abastecimento.asc()).limit(10).all()
              )

    return resumo

def busca_consumo_moto(session,moto_id):
    consumo = (session.query(
        Moto.consumo
    ).filter(
        Moto.id == moto_id
    ).first()
              )
    return consumo
