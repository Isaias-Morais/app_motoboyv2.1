from pydantic import BaseModel
from datetime import date

class ManutencaoBase(BaseModel):
    data_manutencao: date
    tipo: str
    descricao: str = None

class ManutenacaoResponse(ManutencaoBase):
    id: int
    moto_id: int
    valor: float
    quilometragem_manutencao: int

class ManutencaoCreate(ManutencaoBase):
    valor: float
    quilometragem_manutencao: int

