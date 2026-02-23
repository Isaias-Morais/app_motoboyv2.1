def validacao_moto(marca,modelo,ano,quilometragem,consumo):
    if not isinstance(marca,(str)) or len(marca) ==0 or marca == None:
        return False, 'MARCA INVALIDA'
    if not isinstance(modelo,(str)) or len(modelo)==0 or modelo == None:
        return False,'MODELO INVALIDO'
    if not isinstance(ano,(int)) or ano <=1900 or  ano == None:
        return False,'ANO INVALIDO'
    if not isinstance(quilometragem,(float,int)) or quilometragem <0 or quilometragem == None:
        return False,'QUILOMETRAGEM INVALIDA'
    if not isinstance(consumo,(int,float)) or consumo <0 or consumo == None:
        return False, 'CONSUMO INVALIDO'
    else:
        return True,  'SUCESSO'
