from modelos.abastecimento import Abastecimento
from validacoes.abasteciento_validacao import validacao_abastecimento
from BancoDeDados.abastecimento_repositorio import salvar_abastecimeto
from datetime import datetime

data_sql = datetime.now().strftime("%Y-%m-%d")

def registra_abastecimento(
        data=None,
        posto="",
        litros=0,
        valor=0,
        tanque_completo=False,
        quilometragem_abastecimento=None
    ):

    valido , erro = validacao_abastecimento(data,posto,litros,valor,tanque_completo,quilometragem_abastecimento)

    if not valido:
        return erro
    else:
        abastecimento = Abastecimento(
            data=data,
            posto=posto,
            litros=litros,
            valor=valor,
            tanque_completo=tanque_completo,
            quilometragem_abastecimento=quilometragem_abastecimento
        )
        salvar_abastecimeto(abastecimento)
        return abastecimento


