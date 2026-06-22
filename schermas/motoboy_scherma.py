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


class MotoboyUpdate(BaseModel):
    nome:str
    email:EmailStr
    idade:int


class MotoboyPassUpdate(BaseModel):
    email:EmailStr
    senha_nova:str
    senha_atual:str
