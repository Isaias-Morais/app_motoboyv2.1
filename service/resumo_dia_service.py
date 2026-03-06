from database.session import SessionLocal
from repository.finaceiro_repository import *
from repository.motoboy_repository import busca_moto_ativa_motoboy
from service.calculos_service import *

session = SessionLocal()

def resumo_dia():
    moto_id = busca_moto_ativa_motoboy(session)
    dia_de_trabalho  = buscar_dia_de_trabalho(session,moto_id) or {}
    abastecimento_geral = busca_abastecimento(session,moto_id) or {}
    manutencoes = busca_manutencoes(session,moto_id) or {}
    consumo = busca_consumo_moto(session,moto_id) or 0


    valor_do_dia = dia_de_trabalho.ganho if dia_de_trabalho else 0
    km_dia = dia_de_trabalho.km if dia_de_trabalho else 0

    valor_manutencao = manutencoes.get('valor',0 )
    km_manutencao = manutencoes.get('km',0)

    valor_abastecimento = abastecimento_geral.get('valor',0)
    km_abastecimeto = abastecimento_geral.get('km_abastecimento',0)
    litros_abastecimento = abastecimento_geral.get('litros',0)


    preco_gasolina = calcular_preco_medio_combustivel(valor_abastecimento,litros_abastecimento)
    custo_manutencao = calcular_custo_manutecao_km(valor_manutencao,km_manutencao)
    custo_combustivel = calcular_custo_combustivel_km(valor_abastecimento,km_abastecimeto)
    custo_total = calcular_custo_total_km(custo_combustivel,custo_manutencao)
    liquido = calcular_lucro_liquido(valor_do_dia,km_dia,custo_total)

    resumo_dia = {
        'bruto':valor_do_dia,
        'km':km_dia,
        'preco_gasolina':preco_gasolina,
        'custo_combustivel_km':custo_combustivel,
        'custo_manutencao_km':custo_manutencao,
        'custo_km_total':custo_total,
        'consumo_medio': consumo,
        'lucro':liquido
    }
    return resumo_dia

