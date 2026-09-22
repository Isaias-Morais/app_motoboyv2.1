from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from backend.app.models.motoboy_model import Motoboy
from backend.app.repository.base_repository import salvar_objeto, atualizar_objeto
from backend.app.repository.moto_repository import busca_moto
from backend.app.security.hash import *
from backend.app.security.jwt import criar_token
from sqlalchemy.orm import Session
from backend.app.schermas.motoboy_scherma import MotoboyCreate, MotoboyUpdate, MotoboyPassUpdate
from backend.app.security.hash import gerar_hash
from backend.app.repository.motoboy_repository import definir_moto_ativa_motoboy, busca_motoboy_id, \
    consultar_motoboy_email


def registrar_motoboy(session:Session,motoboy:MotoboyCreate):

    if not motoboy:
        raise HTTPException(status_code=404,detail='usuario nao passado de maneira correta')

    if not motoboy.idade >=18:
        raise HTTPException(status_code=403,detail='idade isuficiente')

    if consultar_motoboy_email(session,motoboy.email):
        raise HTTPException(status_code=409,detail="Já existe um motoboy cadastrado com este e-mail.")

    motoboy_db = Motoboy(
        nome=motoboy.nome,
        idade=motoboy.idade,
        email=motoboy.email,
        senha=gerar_hash(motoboy.senha)
    )

    return salvar_objeto(session, motoboy_db)



def login_user(user: OAuth2PasswordRequestForm,session:Session):
    usuario : Motoboy=session.query(Motoboy).filter(Motoboy.email==user.username).first()


    print("Usuario:", usuario)

    if usuario:
        print("Hash:", usuario.senha)
        print("Verify:", verificar_senha(user.password, usuario.senha))

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


def definir_moto_ativa_service(session:Session,motoboy_id:int,moto_id:int):

    moto = busca_moto(session=session,id_motoboy=motoboy_id,id_moto=moto_id)

    if not moto:
        raise HTTPException(status_code=404, detail='moto invalida')

    return definir_moto_ativa_motoboy(session=session,motoboy_id=motoboy_id,moto=moto)



def buscar_motoboy_service(session:Session,motoboy_id:int):

    motoboy = busca_motoboy_id(session=session,motoboy_id=motoboy_id)

    if not motoboy:
        raise HTTPException(status_code=404,detail='motoboy nao existe')

    return motoboy



def busca_moto_ativa_service(session:Session,motoboy_id:int):

    motoboy:Motoboy = buscar_motoboy_service(session=session,motoboy_id=motoboy_id)

    moto = busca_moto(session=session,id_motoboy=motoboy_id,id_moto=motoboy.moto_ativa)

    if not moto:
        raise HTTPException(status_code=404,detail='moto não encontrada')
    return moto



def atualizar_dados_motoboy(session:Session,motoboy_id:int,motoboy_update:MotoboyUpdate):

    motoboy: Motoboy = buscar_motoboy_service(session=session, motoboy_id=motoboy_id)

    return atualizar_objeto(session=session,objeto=motoboy,dados=motoboy_update)



def atualizar_senha_motoboy_service(session:Session,motoboy_id:int,motoboy_update:MotoboyPassUpdate):

    motoboy: Motoboy = buscar_motoboy_service(session=session, motoboy_id=motoboy_id)

    if not verificar_senha(senha=motoboy_update.senha_atual,hash=motoboy.senha):
        raise HTTPException(status_code=401,detail='senha atual invalida')

    if motoboy_update.senha_atual == motoboy_update.senha_nova:
        raise HTTPException(status_code=403,detail='senha não pode ser igual a anterior')

    return atualizar_objeto(session=session,objeto=motoboy,dados=motoboy_update)













