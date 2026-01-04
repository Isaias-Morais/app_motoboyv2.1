from servicos.moto_ativa import *
from BancoDeDados.finaceiro_repositorio import *
from servicos.calculos import *


moto_id = busca_moto_ativa()
dia_de_trabalho  = buscar_dia_de_trabalho(moto_id)
abastecimento_geral = busca_abastecimento(moto_id)
abastecimneto_cheios = busca_abastecimento_consumo_medio(moto_id)
manutencoes = busca_manutencoes(moto_id)
consumo = busca_consumo_moto(moto_id)

print(moto_id)
print(dia_de_trabalho)
print(abastecimento_geral)
print(abastecimneto_cheios)
print(manutencoes)
print(consumo)

valor_manutencao = manutencoes['valor_manutencao'] or 0
km_manutencao = manutencoes['km_manutencao'] or 0

valor_abastecimento = abastecimento_geral['valor_abastecimento']
km_abastecimeto = abastecimento_geral['km_abastecimento']
resumo_abastecimento = calcular_km_rodados(abastecimneto_cheios)
consumo_medio = calcular_consumo_medio_real(resumo_abastecimento)
custo_manutencao = calcular_custo_manutecao_km(valor_manutencao,km_manutencao)
custo_combustivel = calcular_custo_combustivel_km(valor_abastecimento,km_abastecimeto)
print(custo_manutencao)
print(custo_combustivel)
print(consumo_medio)
