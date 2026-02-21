from models.motoboy_model import Motoboy
from validacoes.motoboy_validacao import validacao_motoboy
from repository.base_repository import salvar_objeto
from database.session import SessionLocal

session = SessionLocal()

def registrar_motoboy(
        nome='',
        idade=0,
        email=''
    ):

    valido , erro = validacao_motoboy(nome,idade,email)

    if not valido:
        return erro
    else:
        motoboy = Motoboy(
            nome=nome,
            idade=idade,
            email=email
        )
        salvar_objeto(session,motoboy)
        return True,'Registrado com sucesso'