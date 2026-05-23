from fastapi import APIRouter, Depends
from schermas.moto_scherma import MotoResponse
from service.motoboy_service import *
from sqlalchemy.orm import Session
from database.db import get_db
from fastapi.security import OAuth2PasswordRequestForm
from service.motoboy_service import *
from security.depends import get_current_user, get_current_user_id

router = APIRouter(prefix="/Motoboy")

@router.post('/create',response_model=MotoboyCreate)
def cria_motoboy(motoboy:MotoboyCreate,session:Session=Depends(get_db)):
    return registrar_motoboy(session=session,motoboy=motoboy)


@router.post('/auth')
def loginUser(data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    resultado =  login_user(data,session=db)
    return resultado


@router.get('/me')
def meu_user(user = Depends(get_current_user)):
    return user


@router.patch('/ativa/moto')
async def definir_moto_ativa(moto_id:int,motoboy_id:int = Depends(get_current_user_id), db:Session=Depends(get_db)):
    return definir_moto_ativa_service(session=db,motoboy_id=motoboy_id,moto_id=moto_id)


@router.get('/busca/moto',response_model=MotoResponse)
async def busca_moto_ativa(db:Session = Depends(get_db),motoboy_id:int = Depends(get_current_user_id)):
    return busca_moto_ativa_service(session=db,motoboy_id=motoboy_id)