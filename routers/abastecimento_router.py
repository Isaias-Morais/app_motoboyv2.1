from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.abastecimento_service import registra_abastecimento

from database.db import get_db
from schermas.abastecimento_schermas import *
from security.depends import get_current_user_id

router = APIRouter(prefix='/abastecimento')

@router.post('/cria',response_model=AbastecimentoCreate)
def adicionar_abastecimento(abastecimento:AbastecimentoCreate,db:Session = Depends(get_db),motoboy_id:int = Depends(get_current_user_id)):
    return registra_abastecimento(abastecimento=abastecimento,session=db,motoboy_id=motoboy_id)