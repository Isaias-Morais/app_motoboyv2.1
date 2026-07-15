from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from security.depends import get_current_user_id

router = APIRouter(prefix="/dashboard")

@router.get('/resumo')
def dashboard_resumo(motoboy_id:int = Depends(get_current_user_id),db:Session = Depends(get_db)):
    pass



