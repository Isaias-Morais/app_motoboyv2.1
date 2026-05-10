from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from models.motoboy_model import Motoboy
from repository.base_repository import salvar_objeto
from repository.moto_repository import listar_moto
from security.hash import *
from security.jwt import criar_token
from sqlalchemy.orm import Session
from schermas.motoboy_scherma import MotoboyCreate
from security.hash import gerar_hash
from repository.motoboy_repository import definir_moto_ativa_motoboy


def registrar_motoboy(session:Session,motoboy:MotoboyCreate):

    if not motoboy:
        raise HTTPException(status_code=404,detail='usuario nao passado de maneira correta')

    if not motoboy.idade >=18:
        raise HTTPException(status_code=403,detail='idade isuficiente')

    motoboy_db = Motoboy(
        nome=motoboy.nome,
        idade=motoboy.idade,
        email=motoboy.email,
        senha=gerar_hash(motoboy.senha)
    )

    return salvar_objeto(session, motoboy_db)

def login_user(user: OAuth2PasswordRequestForm,session:Session):
    usuario : Motoboy=session.query(Motoboy).filter(Motoboy.email==user.username).first()

    if not usuario:
        raise HTTPException(status_code=404,detail='credenciais invalidas')

    if not verificar_senha(user.password,usuario.senha):
        raise HTTPException(status_code=404,detail='credenciais invalidas')

    if verificar_senha(user.password, usuario.senha):
        token = criar_token({'sub': str(usuario.id)})
        return {
            "access_token": token,
            "token_type": "bearer"
        }

def definir_moto_ativa_service(user):
    pass






