from models.moto_model import Moto
from database.session import SessionLocal
from repository.base_repository import salvar_objeto
from validacoes.moto_validacao import validacao_moto

session = SessionLocal()

def registra_moto(
        marca=None,
        modelo=None,
        ano=None,
        quilometragem=None,
        consumo=None
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

        print(moto.__dict__)
        salvar_objeto(session,moto)

        return moto
