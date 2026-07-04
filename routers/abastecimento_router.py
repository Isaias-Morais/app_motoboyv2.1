from typing import Dict
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service.abastecimento_service import *
from database.db import get_db
from schermas.abastecimento_schermas import *
from security.depends import get_current_user_id

router = APIRouter(prefix='/abastecimento')

@router.post('/create',response_model=AbastecimentoResponse)
def adicionar_abastecimento(
        abastecimento:AbastecimentoCreate,
        db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)):

    return registra_abastecimento_service(abastecimento=abastecimento,session=db,motoboy_id=motoboy_id)


@router.get('/list',response_model=list[AbastecimentoResponse])
async def listar_abstecimentos(
        db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)):

    return listar_abastecimentos_service(session=db,motoboy_id=motoboy_id)


@router.get('/date',response_model=list[AbastecimentoResponse])
async def abastecimento_por_data(
        data:date,db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)):

    return abastecimento_por_data_service(session=db,motoboy_id=motoboy_id,data=data)


@router.patch('/update',response_model=AbastecimentoResponse)
def atualizar_abastecimento(
        id:int,
        abastecimento:AbastecimentoUpdate,
        db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)):

    return atualizar_abastecimento_service(session=db,motoboy_id=motoboy_id,abastecimento_update=abastecimento,abastecimento_id=id)


@router.delete("/delete",response_model=AbastecimentoResponse)
def deletar_abastecimento(
        abastecimento_id:int,
        db:Session = Depends(get_db),
        motoboy_id:int = Depends(get_current_user_id)):

    return deletar_abastecimento_service(session=db,motoboy_id=motoboy_id,abastecimento_id=abastecimento_id)
