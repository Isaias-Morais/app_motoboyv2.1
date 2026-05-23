from pydantic import BaseModel
from datetime import date
from decimal import Decimal

from sqlalchemy import false


class AbatecimentoBase(BaseModel):
    dia:int
    mes:int
    ano:int
    posto:str
    litros:float
    valor:float
    tanque_completo:bool = False
    quilometragem_abastecimento:int


class AbastecimentoResponse(AbatecimentoBase):
    id:int


class AbastecimentoCreate(AbatecimentoBase):
    moto_id:None