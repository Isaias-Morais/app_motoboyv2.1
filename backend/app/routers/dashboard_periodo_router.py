from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.database.db import get_db
from backend.app.security.depends import get_current_user_id
from backend.app.service.dashboard_periodo_service import dashboard_periodo_service

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/relatorio")
def dashboard_relatorio_periodo(
    data_inicio: date = Query(..., description="Data inicial no formato AAAA-MM-DD"),
    data_fim: date = Query(..., description="Data final no formato AAAA-MM-DD"),
    motoboy_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db),
):
    return dashboard_periodo_service(
        session=db,
        motoboy_id=motoboy_id,
        data_inicio=data_inicio,
        data_fim=data_fim,
    )
