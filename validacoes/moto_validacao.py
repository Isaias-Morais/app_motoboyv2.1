def validacao_moto(marca,modelo,ano,quilometragem,consumo):
    if not isinstance(marca,(str)) or len(marca) ==0:
        return False, 'MARCA INVALIDA'
    if not isinstance(modelo,(str)) or len(modelo)==0:
        return False,'MODELO INVALIDO'
    if not isinstance(ano,(int)) or ano <=1900:
        return False,'ANO INVALIDO'
    if not isinstance(quilometragem,(float,int)) or quilometragem <0:
        return False,'QUILOMETRAGEM INVALIDA'
    if not isinstance(consumo,(int,float)) or consumo <0:
        return False, 'CONSUMO INVALIDO'
    else:
        return True,  'SUCESSO'
