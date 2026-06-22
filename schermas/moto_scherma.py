from pydantic import BaseModel

class MotoBase(BaseModel):
    marca:str
    modelo:str
    ano:int

class MotoCreate(MotoBase):
    quilometragem:int
    consumo:float=0

class MotoResponse(MotoBase):
    id: int
    quilometragem: int
    consumo: float = 0

class MotoUpdate(BaseModel):
    marca : str
    modelo : str
    ano : int