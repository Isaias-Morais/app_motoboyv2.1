from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from security.depends import get_current_user_id, get_data
from service.dashboard_service import dashboard_dia_service


router = APIRouter(prefix="/dashboard")

@router.get('/resumo')
def dashboard_resumo(motoboy_id:int = Depends(get_current_user_id),db:Session = Depends(get_db),data:date = Depends(get_data)):
    return dashboard_dia_service(session=db,motoboy_id=motoboy_id,data=data)



