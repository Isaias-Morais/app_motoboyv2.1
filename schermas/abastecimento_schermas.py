from pydantic import BaseModel
from datetime import date
from decimal import Decimal

from sqlalchemy import false


class AbatecimentoBase(BaseModel):
    data:date
    posto:str
    litros:float
    valor:float
    tanque_completo:bool = False
    quilometragem_abastecimento:int


class AbastecimentoResponse(BaseModel):
    data_abastecimento:date=None
    posto: str
    litros: float
    valor: float
    tanque_completo: bool = False
    quilometragem_abastecimento: int
    id:int


class AbastecimentoCreate(AbatecimentoBase):
    moto_id:None