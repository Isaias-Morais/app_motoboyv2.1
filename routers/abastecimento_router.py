from typing import Dict

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.abastecimento_service import registra_abastecimento, listar_abastecimentos_service, \
    abastecimento_por_data_service

from database.db import get_db
from schermas.abastecimento_schermas import *
from security.depends import get_current_user_id

router = APIRouter(prefix='/abastecimento')

@router.post('/cria',response_model=AbastecimentoResponse)
def adicionar_abastecimento(abastecimento:AbastecimentoCreate,db:Session = Depends(get_db),motoboy_id:int = Depends(get_current_user_id)):
    return registra_abastecimento(abastecimento=abastecimento,session=db,motoboy_id=motoboy_id)

@router.get('/listar',response_model=list[AbastecimentoResponse])
async def listar_abstecimentos(db:Session = Depends(get_db),motoboy_id:int = Depends(get_current_user_id)):
    return listar_abastecimentos_service(session=db,motoboy_id=motoboy_id)

@router.get('/id',response_model=list[AbastecimentoResponse])
async def abastecimento_por_data(data:date,db:Session = Depends(get_db),motoboy_id:int = Depends(get_current_user_id)):
    return abastecimento_por_data_service(session=db,motoboy_id=motoboy_id,data=data)