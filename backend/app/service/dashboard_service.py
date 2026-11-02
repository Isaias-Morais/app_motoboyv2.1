from datetime import date, timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from backend.app.models.dia_de_trabalho_model import Dia_de_trabalho
from backend.app.models.moto_model import Moto
from backend.app.schermas.dashboard_schemas import DashboardGastoMedio
from backend.app.repository.abastecimento_repository import listar_abastecimentos_periodo
from backend.app.repository.dia_de_trabalho_repositorio import (
    buscar_dia_de_trabalho_data,
    listar_dias_de_trabalho_periodo,
)
from backend.app.repository.manutencao_repository import listar_manutencoes_periodo
from backend.app.service.motoboy_service import busca_moto_ativa_service


def dashboard_dia_service(session:Session,motoboy_id:int,data:date):

    moto:Moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)

    dia:Dia_de_trabalho = buscar_dia_de_trabalho_data(session=session, moto_id=moto.id, data=data)

    if not dia:
        raise HTTPException(status_code=(404),detail='dia de trabalho não registrado')

    km_pecorrido = (dia.quilometragem_final - dia.quilometragem_inicial)
    data_inicio_periodo = data - timedelta(days=29)

    dias_registrados = listar_dias_de_trabalho_periodo(
        session, moto.id, data_inicio_periodo, data
    )
    abastecimentos = listar_abastecimentos_periodo(
        session, moto.id, data_inicio_periodo, data
    )
    manutencoes = listar_manutencoes_periodo(
        session, moto.id, data_inicio_periodo, data
    )

    km_periodo = sum(
        max(0, item.quilometragem_final - item.quilometragem_inicial)
        for item in dias_registrados
    )
    valor_abastecimento_periodo = sum(float(item.valor) for item in abastecimentos)
    valor_manutencao_periodo = sum(float(item.valor) for item in manutencoes)
    valor_abastecimento_km = (
        valor_abastecimento_periodo / km_periodo if km_periodo else 0
    )
    valor_manutencao_km = (
        valor_manutencao_periodo / km_periodo if km_periodo else 0
    )
    valor_abastecimento_dia = km_pecorrido * valor_abastecimento_km
    valor_manutencao_dia = km_pecorrido * valor_manutencao_km
    lucro_liquido = float(dia.ganho_bruto) - (
        valor_manutencao_dia + valor_abastecimento_dia
    )

    dashboard = DashboardGastoMedio(
        lucro_bruto=round(float(dia.ganho_bruto),2),
        gasto_manutencao_km=round(valor_manutencao_km,2),
        gasto_combustivel_km=round(valor_abastecimento_km,2),
        km_rodados=round(km_pecorrido,2),
        gasto_media_abastecimento=round(valor_abastecimento_dia,2),
        gasto_medio_manutencao=round(valor_manutencao_dia,2),
        lucro_liquido=round(lucro_liquido,2)
    )
    return dashboard






