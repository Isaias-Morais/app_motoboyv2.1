from fastapi import HTTPException
from models.moto_model import Moto
from sqlalchemy.orm import Session
from repository.base_repository import salvar_objeto, atualizar_objeto, deletar_objeto
from schermas.moto_scherma import MotoCreate, MotoUpdate
from service.motoboy_service import buscar_motoboy_service
from repository.moto_repository import *
from repository.motoboy_repository import busca_motoboy_id



def registra_moto(moto:MotoCreate,session:Session,motoboy_id:int):

    if not moto:
        raise HTTPException(status_code=404,detail='moto não existe ')

    moto = Moto(
        marca=moto.marca,
        modelo=moto.modelo,
        ano=moto.ano,
        quilometragem=moto.quilometragem,
        consumo=moto.consumo,
        motoboy_id=motoboy_id
    )

    salvar_objeto(session,moto)

    return moto


def busca_motos_motoboy_service(session:Session,motoboy_id:int):

    if not busca_motoboy_id(session=session,motoboy_id=motoboy_id):
        raise HTTPException(status_code=404,detail='motoboy invalido')

    return listar_moto(session=session,id=motoboy_id)



def busca_moto_id_service(session:Session,motoboy_id:int,moto_id:int):

    if not busca_motoboy_id(session=session,motoboy_id=motoboy_id):
        raise HTTPException(status_code=404,detail='motoboy invalido')

    moto:Moto = busca_moto(session=session,id_motoboy=motoboy_id,id_moto=moto_id)

    if not moto:
        raise HTTPException(status_code=404,detail='nenhuma moto com esse id vinculado ao motoboy')

    if moto.motoboy_id != motoboy_id:
        raise HTTPException(status_code=404,detail='moto nao vinculada ao motoboy')

    return moto



def atualizar_moto_service(session:Session,motoboy_id:int,moto_id:int,moto_update:MotoUpdate):

    buscar_motoboy_service(session=session,motoboy_id=motoboy_id)

    moto = busca_moto_id_service(session=session,motoboy_id=motoboy_id,moto_id=moto_id)

    return atualizar_objeto(session=session,objeto=moto,dados=moto_update)


def deletar_moto_service(session:Session,moto_id:int,motoboy_id:int):

    buscar_motoboy_service(session=session,motoboy_id=motoboy_id)

    moto : Moto = busca_moto(session=session,id_motoboy=motoboy_id,id_moto=moto_id)

    if not moto:
        raise HTTPException(status_code=404,detail='moto nao encontrada')

    return deletar_objeto(session=session,objeto=moto)


