from modelos.abastecimento import Abastecimento
from validacoes.abasteciento_validacao import validacao_abastecimento
from BancoDeDados.abastecimento_repositorio import salvar_abastecimeto
from validacoes.valida_data import valida_data
from datetime import date


def registra_abastecimento(
        dia=None,
        mes=None,
        ano=None,
        posto="",
        litros=0,
        valor=0,
        tanque_completo=False,
        quilometragem_abastecimento=None,
        moto_id=1
    ):

    valido , erro = validacao_abastecimento(posto,litros,valor,tanque_completo,quilometragem_abastecimento,moto_id)
    if not valido:
        return erro

    valido_data , data = valida_data(dia,mes,ano)
    if not valido_data:
        data = date.today()

    abastecimento = Abastecimento(
        data=data,
        posto=posto,
        litros=litros,
        valor=valor,
        tanque_completo=tanque_completo,
        quilometragem_abastecimento=quilometragem_abastecimento,
        moto_id=moto_id
        )
    salvar_abastecimeto(abastecimento)
    return abastecimento


