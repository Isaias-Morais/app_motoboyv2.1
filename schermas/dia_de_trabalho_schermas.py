from pydantic import BaseModel
from datetime import date

class DiaDeTrabalhoBase(BaseModel):
    quilometragem_inicial:int
    quilometragem_final:int
    ganho_bruto:float

class DiaDeTrabalhoCreate(DiaDeTrabalhoBase):
    data_trabalhada:date
    moto_id:int

class DiaDeTrabalhoResponse(DiaDeTrabalhoBase):
    id:int
    data_trabalhada: date
    moto_id: int