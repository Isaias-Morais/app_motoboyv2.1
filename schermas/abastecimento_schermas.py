from pydantic import BaseModel
from datetime import date
from decimal import Decimal

from sqlalchemy import false


class AbatecimentoBase(BaseModel):
    dia:None
    mes:None
    ano:None
    posto:str
    litros:float
    valor:float
    tanque_completo:bool = False
    quilometragem_abastecimento:int


class AbastecimentoResponse(BaseModel):
    data_abastecimento:date
    posto: str
    litros: float
    valor: float
    tanque_completo: bool = False
    quilometragem_abastecimento: int
    id:int


class AbastecimentoCreate(AbatecimentoBase):
    moto_id:None