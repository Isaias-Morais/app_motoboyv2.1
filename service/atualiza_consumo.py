from repository.moto_repository import atualizar_consumo
from validators.moto_validacao import moto_existe
from validators.abasteciento_validacao import validacao_consumo
from database.session import SessionLocal

session = SessionLocal()

def atualizar_consumo_svc(session,moto_id=0,consumo=0):

    if not moto_existe(moto_id):
        return False, 'moto não existe'

    if not validacao_consumo(consumo):
        return False, 'consumo invalido'

    atualizar_consumo(session,moto_id,consumo)
    return True," consumo atualizado"