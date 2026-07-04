from fastapi import APIRouter

router = APIRouter(prefix="/dashboard")

@router.get('/resumo')
def dashboard_resumo():
    pass

