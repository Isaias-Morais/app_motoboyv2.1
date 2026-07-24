from datetime import date
from turtledemo import round_dance
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.motoboy_model import Motoboy
from models.abastecimento_model import Abastecimento
from models.dia_de_trabalho_model import Dia_de_trabalho
from models.manutencao_model import Manutencao
from models.moto_model import Moto
from schermas.dashboard_schemas import DashboardGastoMedio
from service.manutencao_service import busca_manutencoes_moto_service
from repository.abastecimento_repository import historico_abastecimentos_recentes
from service.dia_de_trabalho_service import buscar_dia_de_trabalho_data
from service.motoboy_service import buscar_motoboy_service, busca_moto_ativa_service


def calcular_media_valor_manutencao(manutencoes:list,moto:Moto):
    valor_total_manutencao:float = 0

    for manutencao in manutencoes:
       
        valor_total_manutencao += manutencao.valor

    valor_manutencao_km = valor_total_manutencao / moto.quilometragem

    return valor_manutencao_km


def calcula_media_valor_abastecimento(abastecimentos:list,moto:Moto):


    quilometragem_maxima: Abastecimento = max(
        abastecimentos,
        key=lambda abastecimento: abastecimento.quilometragem_abastecimento
    )

    quilometragem_minima: Abastecimento = min(
        abastecimentos,
        key=lambda abastecimento: abastecimento.quilometragem_abastecimento
    )

    quilometragem_pecorrida = quilometragem_maxima.quilometragem_abastecimento - quilometragem_minima.quilometragem_abastecimento

    valor_total_abastecimento:float = 0

    for abastecimento in abastecimentos:
        valor_total_abastecimento += abastecimento.valor

    valor_por_km_abastecimento = valor_total_abastecimento / quilometragem_pecorrida

    return valor_por_km_abastecimento


def dashboard_dia_service(session:Session,motoboy_id:int,data:date):

    motoboy:Motoboy = buscar_motoboy_service(session=session,motoboy_id=motoboy_id)

    moto:Moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)

    dia:Dia_de_trabalho = buscar_dia_de_trabalho_data(session=session, moto_id=moto.id, data=data)

    if not dia:
        raise HTTPException(status_code=(404),detail='dia de trabalho não registrado')

    manutencoes:list = busca_manutencoes_moto_service(session=session,motoboy_id=motoboy_id)

    abastecimentos:list = historico_abastecimentos_recentes(session=session,moto_id=moto.id,data=data,quantidade=10)

    valor_manutencao_km = calcular_media_valor_manutencao(manutencoes,moto)

    valor_abastecimento_km = calcula_media_valor_abastecimento(abastecimentos=abastecimentos,moto=moto)

    km_pecorrido = (dia.quilometragem_final - dia.quilometragem_inicial)

    valor_abastecimento_media_dia = km_pecorrido * valor_abastecimento_km

    valor_manutencao_media_dia = km_pecorrido * valor_manutencao_km

    lucro_liquido = dia.ganho_bruto - (valor_manutencao_media_dia + valor_abastecimento_media_dia)

    dashboard = DashboardGastoMedio(
        lucro_bruto=round(dia.ganho_bruto,2),
        gasto_manutencao_km=round(valor_manutencao_km,2),
        gasto_combustivel_km=round(valor_abastecimento_km,2),
        km_rodados=round(km_pecorrido,2),
        gasto_media_abastecimento=round(valor_abastecimento_media_dia,2),
        gasto_medio_manutencao=round(valor_manutencao_media_dia,2),
        lucro_liquido=round(lucro_liquido,2)
    )
    return dashboard






