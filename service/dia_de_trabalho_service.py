from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.dia_de_trabalho_model import Dia_de_trabalho
from repository.base_repository import salvar_objeto
from schermas.dia_de_trabalho_schermas import DiaDeTrabalhoCreate
from models.moto_model import Moto
from service.motoboy_service import  busca_moto_ativa_service
from datetime import date
from repository.dia_de_trabalho_repositorio import *

def registra_dia_de_trabalho_service(
        session:Session,
        dia:DiaDeTrabalhoCreate,
        motoboy_id:int
):
    moto: Moto = busca_moto_ativa_service(session=session, motoboy_id=motoboy_id)

    data_trabalhada = dia.data_trabalhada
    if not data_trabalhada:
        data_trabalhada = date.today()

    dia_verific = buscar_dia_de_trabalho(session=session,moto_id=moto.id,data=data_trabalhada)

    dia_de_trabalho = Dia_de_trabalho(
        data_trabalhada=data_trabalhada,
        quilometragem_inicial=dia.quilometragem_inicial,
        quilometragem_final=dia.quilometragem_final,
        ganho_bruto=dia.ganho_bruto,
        moto_id=moto.id
    )
    if dia_verific:
        raise HTTPException(status_code=409,detail='dia ja foi registrado')

    #adiciona atualiza km verificando o km antigo e o atual

    salvar_objeto(session,dia_de_trabalho)
    return dia_de_trabalho



def listar_dia_de_trabalho_service(session:Session,motoboy_id:int):

    moto:Moto= busca_moto_ativa_service(session=session, motoboy_id=motoboy_id)

    historico = listar_dia_de_trabalho(session=session,moto_id=moto.id)

    if not historico:
        raise HTTPException(status_code=404,detail='nenhum dia encontrado')

    return historico


def dia_de_trabalho_service(data:date,session:Session,motoboy_id:int):

    moto:Moto = busca_moto_ativa_service(session=session, motoboy_id=motoboy_id)

    dia_de_trabalho = buscar_dia_de_trabalho(session=session,data=data,moto_id=moto.id)

    if not dia_de_trabalho:
        raise HTTPException(status_code=404,detail='nenhum dia encontrado')

    return dia_de_trabalho

