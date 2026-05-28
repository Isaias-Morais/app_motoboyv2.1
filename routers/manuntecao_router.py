from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from database.db import get_db
from schermas.manutencao_schermas import ManutencaoCreate
from security.depends import get_current_user_id
from service.manutencao_service import registra_manutencao_service

router = APIRouter(prefix="/manutencao")

@router.post("/criar", response_model=ManutencaoCreate)
def criar_manutencao(manutencao:ManutencaoCreate,db:Session=Depends(get_db),motoboy_id:int=Depends(get_current_user_id)):
    return registra_manutencao_service(manutencao=manutencao,session=db,motoboy_id=motoboy_id)
