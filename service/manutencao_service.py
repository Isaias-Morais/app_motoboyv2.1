from fastapi import HTTPException

from models.manutencao_model import Manutencao
from sqlalchemy.orm import Session
from repository.base_repository import salvar_objeto
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

    #cria funcao para atualizar os kms com base na quilometragem atual