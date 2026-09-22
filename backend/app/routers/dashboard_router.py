from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.database.db import get_db
from backend.app.security.depends import get_current_user_id, get_data
from backend.app.service.dashboard_service import dashboard_dia_service


router = APIRouter(prefix="/dashboard",tags=["dashboard"])

@router.get('/resumo')
def dashboard_resumo(motoboy_id:int = Depends(get_current_user_id),db:Session = Depends(get_db),data:date = Depends(get_data)):
    return dashboard_dia_service(session=db,motoboy_id=motoboy_id,data=data)



