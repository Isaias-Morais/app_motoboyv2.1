from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from database.db import get_db
from schermas.manutencao_schermas import *
from security.depends import get_current_user_id
from service.manutencao_service import *
router = APIRouter(prefix="/manutencao")

@router.post("/create", response_model=ManutencaoResponse)
def criar_manutencao(
        manutencao:ManutencaoCreate,
        db:Session=Depends(get_db),
        motoboy_id:int=Depends(get_current_user_id)):

    return registra_manutencao_service(manutencao=manutencao,session=db,motoboy_id=motoboy_id)


@router.get("/list", response_model=list[ManutencaoResponse])
def listar_manutencoes_moto(
        db:Session=Depends(get_db),
        motoboy_id:int=Depends(get_current_user_id)):

    return busca_manutencoes_moto_service(session=db,motoboy_id=motoboy_id)


@router.get('/date', response_model=list[ManutencaoResponse])
def buscar_manutencao_data(
        data:date,db:Session=Depends(get_db),
        motoboy_id:int=Depends(get_current_user_id)):

    return busca_manutencoes_moto_data_service(session=db,motoboy_id=motoboy_id,data=data)


@router.patch("/update", response_model=ManutencaoResponse)
def atualizar_manutencao(
        id:int,
        manutencao:ManutencaoUpdate,
        db:Session=Depends(get_db),
        motoboy_id:int=Depends(get_current_user_id)):

    return atualizar_manutencao_service(id_manutencao=id,session=db,manutencao_update=manutencao,motoboy_id=motoboy_id)


@router.delete("/delete", response_model=ManutencaoResponse)
def deletar_manutencao(
        manutencao_id:int,
        db:Session = Depends(get_db),
        motoboy_id:int=Depends(get_current_user_id)):

    return deletar_manutencao_service(manutencao_id=manutencao_id,session=db,motoboy_id=motoboy_id)

