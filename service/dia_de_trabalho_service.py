from sqlalchemy.orm import Session
from models.dia_de_trabalho_model import Dia_de_trabalho
from repository.base_repository import salvar_objeto
from schermas.dia_de_trabalho_schermas import DiaDeTrabalhoCreate
from service.moto_service import busca_moto_id_service
from validators.dia_de_trabalho_validators import validacao_dia_de_trabalho
from models.moto_model import Moto
from service.motoboy_service import  busca_moto_ativa_service
from datetime import date

def registra_dia_de_trabalho_service(
        session:Session,
        dia:DiaDeTrabalhoCreate,
        motoboy_id:int
):
    moto: Moto = busca_moto_ativa_service(session=session, motoboy_id=motoboy_id)

    data_trabalhada = dia.data_trabalhada
    if not data_trabalhada:
        data_trabalhada = date.today()

    dia_de_trabalho = Dia_de_trabalho(
        data_trabalhada=data_trabalhada,
        quilometragem_inicial=dia.quilometragem_inicial,
        quilometragem_final=dia.quilometragem_final,
        ganho_bruto=dia.ganho_bruto,
        moto_id=moto.id
    )
    salvar_objeto(session,dia_de_trabalho)

    #adiciona atualiza km verificando o km antigo e o atual

    return dia_de_trabalho
