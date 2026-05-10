from pydantic import BaseModel,EmailStr

class MotoboyBase(BaseModel):
    id:int
    nome:str
    email:str


class MotoboyCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    idade:int = None


class MotoboyResponse(MotoboyBase):
    idade:int
    moto_ativa:int


class MotoboyMoto(BaseModel):
    motos:list



