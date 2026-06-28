from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import get_db
from models.motoboy_model import Motoboy
from schermas.moto_scherma import MotoCreate, MotoBase,MotoResponse
from schermas.motoboy_scherma import MotoboyResponse
from security.depends import get_current_user_id
from service.moto_service import *

router = APIRouter(prefix='/moto')

@router.post('/create',response_model=MotoBase)
def adicionar_moto(
        moto:MotoCreate,
        motoboy:Motoboy = Depends(get_current_user_id),
        db:Session = Depends(get_db)):

   return registra_moto(moto=moto,session=db,motoboy_id=motoboy)

@router.get('/motos')
async def buscar_motos_motoboy(
        motoboy_id:int = Depends(get_current_user_id),
        db:Session=Depends(get_db)):

    return busca_motos_motoboy_service(session=db,motoboy_id=motoboy_id)

@router.get('/motos_id',response_model=MotoResponse)
async def buscar_moto_id(
        moto_id:int,
        motoboy_id:int = Depends(get_current_user_id),
        db:Session=Depends(get_db)):

   return busca_moto_id_service(motoboy_id=motoboy_id,session=db,moto_id=moto_id)


@router.patch('/update',response_model=MotoResponse)
def atualizar_moto(
        moto:MotoUpdate,
        moto_id:int,
        motoboy_id:int = Depends(get_current_user_id),
        db:Session=Depends(get_db)):

   return atualizar_moto_service(session=db,motoboy_id=motoboy_id,moto_id=moto_id,moto_update=moto)


@router.delete('/delete',response_model=MotoResponse)
def deletar_moto(
        moto_id:int,
        db:Session=Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)):

    return deletar_moto_service(session=db,motoboy_id=motoboy_id,moto_id=moto_id)