from datetime import date

from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.app.models.abastecimento_model import Abastecimento
from backend.app.models.dia_de_trabalho_model import Dia_de_trabalho
from backend.app.models.manutencao_model import Manutencao
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

    dias = (
        session.query(Dia_de_trabalho)
        .filter(
            Dia_de_trabalho.moto_id == moto.id,
            Dia_de_trabalho.data_trabalhada >= data_inicio,
            Dia_de_trabalho.data_trabalhada <= data_fim,
        )
        .order_by(Dia_de_trabalho.data_trabalhada.asc())
        .all()
    )

    abastecimentos = (
        session.query(Abastecimento)
        .filter(
            Abastecimento.moto_id == moto.id,
            Abastecimento.data_abastecimento >= data_inicio,
            Abastecimento.data_abastecimento <= data_fim,
        )
        .all()
    )

    manutencoes = (
        session.query(Manutencao)
        .filter(
            Manutencao.moto_id == moto.id,
            Manutencao.data_manutencao >= data_inicio,
            Manutencao.data_manutencao <= data_fim,
        )
        .all()
    )

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
