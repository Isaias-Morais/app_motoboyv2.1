from datetime import date ,timedelta
from sqlalchemy import func
from models.abastecimento_model import Abastecimento
from models.dia_de_trabalho_model import Dia_de_trabalho
from service.manutencao_service import session
from database.setup import get_conexao


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


def busca_abastecimento(sesion, moto_id):
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

def busca_manutencoes(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = ''' 
                SELECT
                    SUM(m.valor) AS valor,
                    MAX(m.quilometragem) - MIN(m.quilometragem) AS km
                FROM manutencao m 
                JOIN moto mo ON mo.id = m.moto_id
                WHERE mo.id = %s
                AND m.data_manutencao >= NOW() - INTERVAL '30 days'
                AND m.data_manutencao <= NOW()
            '''
            cursor.execute(sql,(moto_id,))
            valor,km = cursor.fetchone()

            return {
                'valor_manutencao':valor,
                'km_manutencao':km
            }

def busca_abastecimento_consumo_medio(moto_id):
    with get_conexao() as conn:
        with conn.cursor as cursor:

            sql = '''
                SELECT 
                    a.quilometragem AS km,
                    a.litros AS litros
                FROM abastecimento a
                JOIN moto m ON m.id = a.moto_id
                WHERE m.id = %s
                    AND a.tanque_completo = True
                ORDER BY a.quilometragem ASC
                LIMIT 10
            '''

            cursor.execute(sql, (moto_id,))
            dados = cursor.fetchall()

            return dados



def busca_consumo_moto(moto_id):
    with get_conexao() as conn:
        with conn.cursor() as cursor:
            sql = '''
                SELECT
                    mo.consumo AS consumo
                FROM moto mo
                JOIN moto m ON m.id = m.id
                WHERE m.id =%s
            '''

            cursor.execute(sql,(moto_id,))
            consumo = cursor.fetchone()

            return consumo
