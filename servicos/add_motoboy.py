from models.motoboy import Motoboy
from validacoes.motoboy_validacao import validacao_motoboy
from repository.motoboy_repository import salvar_motoboy

def registrar_motoboy(nome='',idade=0,email=''):
    valido , erro = validacao_motoboy(nome,idade,email)
    if not valido:
        return erro
    else:
        motoboy = Motoboy(nome=nome,idade=idade,email=email)
        salvar_motoboy(motoboy)
        return True,'Registrado com sucesso'