from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schermas.dia_de_trabalho_schermas import DiaDeTrabalhoCreate, DiaDeTrabalhoResponse
from database.db import get_db
from service.dia_de_trabalho_service import *
from security.depends import get_current_user_id

router = APIRouter(prefix="/dia_de_trabalhada")

@router.post('/registrar',response_model=DiaDeTrabalhoCreate)
def registrar_dia_de_trabalho(
        dia_de_trabalhado:DiaDeTrabalhoCreate,
        db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)
    ):

    return registra_dia_de_trabalho_service(session=db, motoboy_id=motoboy_id,dia=dia_de_trabalhado)


@router.get('/historico',response_model=list[DiaDeTrabalhoResponse])
def historico_dia_de_trabalho(
        db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)
    ):

    return listar_dia_de_trabalho_service(db,motoboy_id)


@router.get('/buscar_dia_de_trabalho_data',response_model=DiaDeTrabalhoResponse)
def buscar_dia_de_trabalho_data(
        data:date,
        db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)
    ):

    return dia_de_trabalho_service(session=db, motoboy_id=motoboy_id, data=data)