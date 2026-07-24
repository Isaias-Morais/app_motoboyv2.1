from fastapi import HTTPException
from repository.abastecimento_repository import *
from database.session import SessionLocal
from models.abastecimento_model import Abastecimento
from models.moto_model import Moto
from repository.base_repository import salvar_objeto, atualizar_objeto, deletar_objeto
from repository.moto_repository import quilometragem_atual, atualizar_quilometragem
from sqlalchemy.orm import Session
from service.quilometragem_service import validacao_quilometregem
from service.motoboy_service import busca_moto_ativa_service, buscar_motoboy_service
from service.quilometragem_service import atualizar_quilometragem_service
from datetime import date
from schermas.abastecimento_schermas import AbastecimentoCreate, AbastecimentoUpdate, AbastecimentoDelete
from repository.moto_repository import busca_moto


def registra_abastecimento_service(abastecimento:AbastecimentoCreate,session:Session,motoboy_id:int):
    data = abastecimento.data
    if not data:
        data = date.today()

    moto:Moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)
    if not moto:
        raise HTTPException(status_code=404, detail='nenhuma moto encontrada ')

    novo_abastecimento = Abastecimento(
            data_abastecimento=data,
            posto=abastecimento.posto,
            litros=abastecimento.litros,
            valor=abastecimento.valor,
            tanque_completo=abastecimento.tanque_completo,
            quilometragem_abastecimento=abastecimento.quilometragem_abastecimento,
            moto_id=moto.id
        )

    if not abastecimento_existe(session, moto.id, abastecimento.quilometragem_abastecimento):

        validacao_quilometregem(moto_id=moto.id, data=data, km_nova=abastecimento.quilometragem_abastecimento, session=session)

        if abastecimento.quilometragem_abastecimento <= moto.quilometragem and data == date.today():
            raise HTTPException(status_code=400,detail='quilometragem não pode ser menor q a atual')

        novo_abastecimento = salvar_objeto(session, novo_abastecimento)

        if abastecimento.quilometragem_abastecimento > moto.quilometragem:
            atualizar_quilometragem_service(moto=moto, data=data, km_nova=abastecimento.quilometragem_abastecimento,session=session)

        return novo_abastecimento
    else:
        raise HTTPException(status_code=409, detail='abastecimento ja existente')


def listar_abastecimentos_service(session:Session,motoboy_id:int):

    moto:Moto = busca_moto_ativa_service(session,motoboy_id)

    lista = historico_abastecimentos(session=session,moto_id=moto.id)

    if not lista:
        raise HTTPException(status_code=404,detail='nenhum registro encontrado ')

    return lista


def abastecimento_por_data_service(session:Session,motoboy_id:int,data:date):
    if not data:
        data = date.today()

    moto: Moto = busca_moto_ativa_service(session, motoboy_id)

    lista = abstecimento_por_data(session=session, moto_id=moto.id,data=data)

    if not lista:
        raise HTTPException(status_code=404, detail='nenhum registro encontrado ')

    return lista



def atualizar_abastecimento_service(
        session:Session,
        motoboy_id:int,
        abastecimento_id:int,
        abastecimento_update:AbastecimentoUpdate
    ):

    buscar_motoboy_service(session=session,motoboy_id=motoboy_id)

    moto:Moto = busca_moto_ativa_service(session=session,motoboy_id=motoboy_id)

    abastecimento = buscar_abastecimento_id(session=session,abastecimento_id=abastecimento_id,moto_id=moto.id)

    if not abastecimento:
        raise HTTPException(status_code=404, detail='nenhum registro encontrado ')

    return atualizar_objeto(session=session,objeto=abastecimento,dados=abastecimento_update)



def deletar_abastecimento_service(session:Session,motoboy_id:int,abastecimento_id:int):

    buscar_motoboy_service(session,motoboy_id)

    moto:Moto = busca_moto_ativa_service(session,motoboy_id)

    abastecimento : Abastecimento = buscar_abastecimento_id(session=session,abastecimento_id=abastecimento_id,moto_id=moto.id)

    if not abastecimento:
        raise HTTPException(status_code=404, detail='nenhum registro encontrado ')

    return deletar_objeto(session=session,objeto=abastecimento)
