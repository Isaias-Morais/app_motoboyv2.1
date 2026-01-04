from servicos.moto_ativa import *
from BancoDeDados.finaceiro_repositorio import *
from servicos.calculos import *

busca_moto_ativa()
moto_id = busca_moto_ativa()
dia_de_trabalho  = buscar_dia_de_trabalho(moto_id)
abastecimento_geral = busca_abastecimento(moto_id)
abastecimneto_cheios = busca_abastecimento_consumo_medio(moto_id)
manutencoes = busca_manutencoes(moto_id)
consumo = busca_consumo_moto(moto_id)


valor_do_dia = dia_de_trabalho['ganho'] or 0
km_dia = dia_de_trabalho['km_dia'] or 0

valor_manutencao = manutencoes['valor_manutencao'] or 0
km_manutencao = manutencoes['km_manutencao'] or 0

valor_abastecimento = abastecimento_geral['valor_abastecimento']
km_abastecimeto = abastecimento_geral['km_abastecimento']
litros_abastecimento = abastecimento_geral['litros']

preco_gasolina = calcular_preco_medio_combustivel(valor_abastecimento,litros_abastecimento)
resumo_abastecimento = calcular_km_rodados(abastecimneto_cheios)
consumo_medio = calcular_consumo_medio_real(resumo_abastecimento)
custo_manutencao = calcular_custo_manutecao_km(valor_manutencao,km_manutencao)
custo_combustivel = calcular_custo_combustivel_km(valor_abastecimento,km_abastecimeto)
custo_total = calcular_custo_total_km(custo_combustivel,custo_manutencao)
liquido = calcular_lucro_liquido(valor_do_dia,km_dia,custo_total)

