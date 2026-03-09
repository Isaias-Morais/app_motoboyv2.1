from models.moto_model import Moto


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


def moto_existe(session,moto_id=0):
    moto = session.query(
        Moto
    ).filter(
        Moto.id == moto_id
    ).first()

    return moto is not None


def validar_quilometragem_nova(km_atual,km_novo):
    if not isinstance(km_atual,(int)) or km_atual <0:
        return False , 'QUILOMETRAGEM ATUAL INVALIDA'
    if not isinstance(km_novo,(int)) or km_atual <= km_novo:
        return False , 'QUILOMETRAGEM NOVA INVALIDA'
    else:
        return True