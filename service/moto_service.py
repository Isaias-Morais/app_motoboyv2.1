from fastapi import HTTPException
from models.moto_model import Moto
from sqlalchemy.orm import Session
from repository.base_repository import salvar_objeto
from schermas.moto_scherma import MotoCreate
from validators.abastecimento_validators import validacao_consumo
from repository.moto_repository import *
from repository.motoboy_repository import redefinir_moto_ativa_motoboy, busca_moto_ativa_motoboy,busca_motoboy_id
from repository.dia_de_trabalho_repositorio import excluir_dias_trabalhados
from repository.manutencao_repository import excluir_manutencao
from repository.abastecimento_repository import excluir_abastecimentos



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

    moto = busca_moto(session=session,id_motoboy=motoboy_id,id_moto=moto_id)

    if not moto:
        raise HTTPException(status_code=404,detail='nenhuma moto com esse id vinculado ao motoboy')

    return moto



def atualizar_consumo_moto(session,moto_id=0,consumo=0):

    if not moto_existe(session,moto_id):
        return False, 'moto não existe'

    if not validacao_consumo(consumo):
        return False, 'consumo invalido'

    atualizar_consumo(session,moto_id,consumo)
    return True,"consumo atualizado"


def excluir_moto_geral(session,moto_id):
    id = busca_moto_ativa_motoboy(session)
    if not moto_existe(session,moto_id):
        return False, 'Moto nao existente'

    excluir_manutencao(session,moto_id)
    excluir_abastecimentos(session,moto_id)
    excluir_dias_trabalhados(session,moto_id)
    excluir_moto(session,moto_id)

    if id == moto_id:
        redefinir_moto_ativa_motoboy(session)

    return True,'Moto excluida com sucesso'