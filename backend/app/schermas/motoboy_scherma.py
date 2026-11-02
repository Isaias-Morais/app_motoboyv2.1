from pydantic import BaseModel, ConfigDict, EmailStr

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
    model_config = ConfigDict(from_attributes=True)

    idade: int
    moto_ativa: int | None = None


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


class MotoboyMotoUpdate(BaseModel):
    moto_ativa:int
