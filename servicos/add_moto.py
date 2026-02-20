from models.moto_model import Moto
from validacoes.moto_validacao import validacao_moto
from repository.base_repository import salvar_objeto
from database.session import SessionLocal

session = SessionLocal()

def registra_moto(
        marca='',
        modelo='',
        ano=0,
        quilometragem=0,
        consumo=0
    ):

    valido , erro = validacao_moto(marca,modelo,ano,quilometragem,consumo)

    if not valido:
        return erro
    else:
        moto = Moto(
            marca=marca,
            modelo=modelo,
            ano=ano,
            quilometragem=quilometragem,
            consumo=consumo,
            motoboy_id=1)

        salvar_objeto(session,moto)

        return moto
