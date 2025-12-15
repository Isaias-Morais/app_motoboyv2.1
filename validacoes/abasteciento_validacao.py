from datetime import datetime
def validacao_abastecimento(valor,litros,completo = False,quilometragem_de_abastecimento = None,  data = None):

    if not isinstance(valor, (int, float)) or valor < 0:
        return False, f'Digite um valor valido'
    if not isinstance(litros, (int, float)) or litros <= 0:
        return False, f'Digite um litragem valida'
    if not isinstance(completo, (bool)):
        return False, f'Digite um valor bool valido'
    if not isinstance(quilometragem_de_abastecimento,(int, float)) or quilometragem_de_abastecimento < 0:
        return False, f'Digite quilometragem valida'
    dia = data or datetime.today()
    if not isinstance(dia, (datetime)):
        return False,  f'Digite uma data valida'
    else:
        tanque_completo = completo
        preco_litro = valor / litros


