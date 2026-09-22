from pydantic import BaseModel
from datetime import date

class ManutencaoBase(BaseModel):
    data_manutencao: date
    tipo: str
    descricao: str = None

class ManutencaoResponse(ManutencaoBase):
    id: int
    moto_id: int
    valor: float
    quilometragem_manutencao: int

class ManutencaoCreate(ManutencaoBase):
    valor: float
    quilometragem_manutencao: int


class ManutencaoUpdate(BaseModel):
    valor: float
    tipo: str
    descricao: str = None


class ManutencaoDelete(BaseModel):
    id: int

