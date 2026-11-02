from datetime import date

from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.app.repository.abastecimento_repository import listar_abastecimentos_periodo
from backend.app.repository.dia_de_trabalho_repositorio import listar_dias_de_trabalho_periodo
from backend.app.repository.manutencao_repository import listar_manutencoes_periodo
from backend.app.service.motoboy_service import busca_moto_ativa_service


def dashboard_periodo_service(
    session: Session,
    motoboy_id: int,
    data_inicio: date,
    data_fim: date,
):
    """Gera um resumo financeiro com base nos registros reais do período."""
    if data_inicio > data_fim:
        raise HTTPException(
            status_code=400,
            detail="A data inicial não pode ser posterior à data final.",
        )

    moto = busca_moto_ativa_service(session=session, motoboy_id=motoboy_id)

    dias = listar_dias_de_trabalho_periodo(session, moto.id, data_inicio, data_fim)
    abastecimentos = listar_abastecimentos_periodo(session, moto.id, data_inicio, data_fim)
    manutencoes = listar_manutencoes_periodo(session, moto.id, data_inicio, data_fim)

    total_dias = len(dias)
    ganhos = sum(float(dia.ganho_bruto) for dia in dias)
    km_rodados = sum(
        max(0, dia.quilometragem_final - dia.quilometragem_inicial)
        for dia in dias
    )
    gasto_combustivel = sum(float(item.valor) for item in abastecimentos)
    gasto_manutencao = sum(float(item.valor) for item in manutencoes)
    gastos = gasto_combustivel + gasto_manutencao
    lucro_liquido = ganhos - gastos

    return {
        "data_inicio": data_inicio,
        "data_fim": data_fim,
        "total_dias_trabalhados": total_dias,
        "ganhos": round(ganhos, 2),
        "gasto_combustivel": round(gasto_combustivel, 2),
        "gasto_manutencao": round(gasto_manutencao, 2),
        "gastos": round(gastos, 2),
        "lucro_liquido": round(lucro_liquido, 2),
        "km_rodados": km_rodados,
        "media_ganhos_por_dia": round(ganhos / total_dias, 2) if total_dias else 0.0,
        "media_gastos_por_dia": round(gastos / total_dias, 2) if total_dias else 0.0,
        "lucro_medio_por_dia": round(lucro_liquido / total_dias, 2) if total_dias else 0.0,
        "custo_por_km": round(gastos / km_rodados, 2) if km_rodados else 0.0,
    }
