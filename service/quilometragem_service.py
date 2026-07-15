from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from service.moto_service import Moto
from models.abastecimento_model import Abastecimento
from models.dia_de_trabalho_model import Dia_de_trabalho
from models.manutencao_model import Manutencao
from repository.base_repository import atualizar_objeto
from repository.manutencao_repository import buscar_quilometragem_manutencao_anterior,buscar_quilometragem_manutencao_posterior
from repository.abastecimento_repository import buscar_quilometragem_abastecimento_anterior,buscar_quilometragem_abastecimento_posterior
from repository.dia_de_trabalho_repositorio import buscar_quilometragem_dia_de_trabalho_anterior,buscar_quilometragem_dia_de_trabalho_posterior
from schermas.moto_scherma import MotoKmUpdate
from service.motoboy_service import busca_moto_ativa_service


def  quilometragem_anterior(moto_id:int,data:date,session:Session):

    registro_manutencao_anter:Manutencao = buscar_quilometragem_manutencao_anterior(session=session,data=data,moto_id=moto_id)
    registro_abastecimento_anter:Abastecimento = buscar_quilometragem_abastecimento_anterior(session=session,data=data,moto_id=moto_id)
    registro_dia_anter:Dia_de_trabalho = buscar_quilometragem_dia_de_trabalho_anterior(session=session,data=data,moto_id=moto_id)

    registros_anter = []

    if registro_manutencao_anter:
        registros_anter.append(
            (registro_manutencao_anter.data_manutencao, registro_manutencao_anter)
        )

    if registro_abastecimento_anter:
        registros_anter.append(
            (registro_abastecimento_anter.data_abastecimento, registro_abastecimento_anter)
        )

    if registro_dia_anter:
        registros_anter.append(
            (registro_dia_anter.data_trabalhada, registro_dia_anter)
        )

    if not registros_anter:
        return None

    return max(registros_anter, key=lambda x: x[0])[1]



def quilometragem_posterior(moto_id:int,data:date,session:Session):

    registro_manutencao_poster: Manutencao = buscar_quilometragem_manutencao_posterior(session=session,data=data,moto_id=moto_id)
    registro_abastecimento_poster: Abastecimento = buscar_quilometragem_abastecimento_posterior(session=session,data=data,moto_id=moto_id)
    registro_dia_poster: Dia_de_trabalho = buscar_quilometragem_dia_de_trabalho_posterior(session=session,data=data,moto_id=moto_id)

    registros_poster = []

    if registro_manutencao_poster:
        registros_poster.append(
            (registro_manutencao_poster.data_manutencao, registro_manutencao_poster)
        )

    if registro_abastecimento_poster:
        registros_poster.append(
            (registro_abastecimento_poster.data_abastecimento, registro_abastecimento_poster)
        )

    if registro_dia_poster:
        registros_poster.append(
            (registro_dia_poster.data_trabalhada, registro_dia_poster)
        )

    if not registros_poster:
        return None

    return min(registros_poster, key=lambda x: x[0])[1]


def validacao_quilometregem(moto_id:int,data:date,km_nova:int,session:Session):

    registro_anterior = quilometragem_anterior(moto_id=moto_id,data=data,session=session)
    registro_posterior = quilometragem_posterior(moto_id=moto_id,data=data,session=session)

    if isinstance(registro_anterior,Manutencao):
        if km_nova < registro_anterior.quilometragem_manutencao:
            raise HTTPException(status_code=400, detail="A quilometragem não pode ser menor que a do registro anterior.")

    if isinstance(registro_anterior,Abastecimento):
        if km_nova < registro_anterior.quilometragem_abastecimento:
            raise HTTPException(status_code=400, detail="A quilometragem não pode ser menor que a do registro anterior.")

    if isinstance(registro_anterior,Dia_de_trabalho):
        if km_nova < registro_anterior.quilometragem_final:
            raise HTTPException(status_code=400, detail="A quilometragem não pode ser menor que a do registro anterior.")

    if isinstance(registro_posterior,Manutencao):
        if km_nova > registro_posterior.quilometragem_manutencao:
            raise HTTPException(status_code=400, detail="A quilometragem não pode ser maior que a do registro posterior.")

    if isinstance(registro_posterior,Abastecimento):
        if km_nova > registro_posterior.quilometragem_abastecimento:
            raise HTTPException(status_code=400, detail="A quilometragem não pode ser maior que a do registro posterior.")

    if isinstance(registro_posterior,Dia_de_trabalho):
        if km_nova > registro_posterior.quilometragem_final:
            raise HTTPException(status_code=400, detail="A quilometragem não pode ser maior que a do registro posterior.")

    return True


def atualizar_quilometragem_service(moto:Moto,data:date,km_nova:int,session:Session):

    validacao_quilometregem(moto_id=moto.id,data=data,km_nova=km_nova,session=session)

    if km_nova <= moto.quilometragem:
        return

    quilometragem = MotoKmUpdate(
        quilometragem = km_nova
    )

    atualizar_objeto(session=session, objeto=moto, dados=quilometragem)
