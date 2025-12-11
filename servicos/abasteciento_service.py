def validacao_abastecimento(valor,litros,completo = False,quilometragem_de_abastecimento = None,  data = None):
    from datetime import datetime
    from BancoDeDados.add_abastecimento import salvar_abastecimento

    permisao = False

    if not isinstance(valor, (int, float)) or valor < 0:
        return False, f'Digite um valor valido'
    if not isinstance(litros, (int, float)) or litros <= 0:
        return False, f'Digite um litragem valida'
    if not isinstance(completo, (bool)):
        return False, f'Digite um valor bool valido'
    if not isinstance(quilometragem_de_abastecimento,(int, float)) or valor < 0:
        return False, f'Digite quilometragem valida'
    dia = data or datetime.today()
    if not isinstance(dia, (datetime)):
        return False,  f'Digite uma data valida'
    else:
        tanque_completo = completo
        preco_litro = valor / litros

        registro = {
                'Dia':dia.strftime('%d/%m/%Y'),
                'Valor':valor,
                'Litros':litros,
                'Preço_Do_litro':preco_litro,
                'Quilometragem_ultimo_abastecimento':quilometragem_de_abastecimento,
                'complet_bool':completo,
                'Completou':'Sim' if tanque_completo else 'Não'
            }
        salvar_abastecimento(registro)
        permisao = True,None
        return permisao

