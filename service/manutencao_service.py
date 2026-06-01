from fastapi import HTTPException
from models.manutencao_model import Manutencao
from sqlalchemy.orm import Session
from repository.base_repository import salvar_objeto
from repository.manutencao_repository import listar_manutencao, listar_manutencao_data
from repository.moto_repository import quilometragem_atual, atualizar_quilometragem
from service.motoboy_service import busca_moto_ativa_service
from models.moto_model import Moto
from validators.moto_validacao import validar_quilometragem_nova
from datetime import date
from schermas.manutencao_schermas import ManutencaoCreate

def registra_manutencao_service(manutencao:ManutencaoCreate,session:Session,motoboy_id:int):
    data = manutencao.data_manutencao
    if not data:
        data = date.today()

    moto:Moto = busca_moto_ativa_service(session=session, motoboy_id=motoboy_id)

    manutencao = Manutencao(
        data_manutencao=data,
        tipo=manutencao.tipo,
        descricao=manutencao.descricao,
        valor=manutencao.valor,
        quilometragem_manutencao=manutencao.quilometragem_manutencao,
        moto_id=moto.id
        )

    if not manutencao:
        raise HTTPException(status_code=400,detail='dados invalidos')
    salvar_objeto(session,manutencao)

    return manutencao


def busca_manutencoes_moto_service(session:Session,motoboy_id:int):

    moto:Moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)

    if not moto:
        raise HTTPException(status_code=400,detail='campo moto invalido')

    lista = listar_manutencao(session=session,moto_id=moto.id)

    if not lista:
        raise HTTPException(status_code=400,detail='lista vazia')

    return lista


def busca_manutencoes_moto_data_service(session: Session, motoboy_id: int, data:date):

    moto: Moto = busca_moto_ativa_service(session=session, motoboy_id=motoboy_id)

    if not moto:
        raise HTTPException(status_code=400, detail='campo moto invalido')

    lista = listar_manutencao_data(session=session, moto_id=moto.id,data=data)

    if not lista:
        raise HTTPException(status_code=400, detail='lista vazia')

    return lista
    #cria funcao para atualizar os kms com base na quilometragem atual