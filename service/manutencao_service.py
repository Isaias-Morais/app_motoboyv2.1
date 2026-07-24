from fastapi import HTTPException
from models.manutencao_model import Manutencao
from sqlalchemy.orm import Session
from repository.base_repository import salvar_objeto, atualizar_objeto, deletar_objeto
from repository.manutencao_repository import listar_manutencao, listar_manutencao_data, buscar_manutencao
from repository.moto_repository import quilometragem_atual, atualizar_quilometragem
from service.motoboy_service import busca_moto_ativa_service, buscar_motoboy_service
from models.moto_model import Moto
from service.quilometragem_service import validacao_quilometregem
from service.quilometragem_service import atualizar_quilometragem_service
from datetime import date
from schermas.manutencao_schermas import ManutencaoCreate, ManutencaoUpdate


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

    nova_manutencao = salvar_objeto(session,manutencao)
    atualizar_quilometragem_service(moto=moto, data=data, km_nova=manutencao.quilometragem_manutencao,session=session)

    return nova_manutencao


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


def atualizar_manutencao_service(id_manutencao:int,manutencao_update:ManutencaoUpdate,session:Session,motoboy_id:int):

    buscar_motoboy_service(session=session,motoboy_id=motoboy_id)

    moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)

    manutencao:Manutencao = buscar_manutencao(session=session,moto_id=moto.id,id=id_manutencao)

    if not manutencao:
        raise HTTPException(status_code=404,detail='nenhum registro encontrado ')

    return atualizar_objeto(session=session,objeto=manutencao,dados=manutencao_update)


def deletar_manutencao_service(manutencao_id:int ,session:Session,motoboy_id:int):

    buscar_motoboy_service(session=session,motoboy_id=motoboy_id)

    moto : Moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)

    manutencao = buscar_manutencao(session=session,moto_id=moto.id,id=manutencao_id)

    if not manutencao:
        raise HTTPException(status_code=404,detail='nenhum registro encontrado ')

    return deletar_objeto(session=session,objeto=manutencao)

