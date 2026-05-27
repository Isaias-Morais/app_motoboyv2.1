from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from database.db import get_db
from schermas.manutencao_schermas import ManutencaoCreate
from security.depends import get_current_user_id

router = APIRouter(prefix="/manutencao")

@router.post("/criar")
def criar_manutencao(manutencao:ManutencaoCreate,db:Session=Depends(get_db),motoboy_id:int=Depends(get_current_user_id)):
    pass
