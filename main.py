from fastapi import FastAPI
from database.base import Base
from database.engine import engine
from routers.motoboy_router import router as router_motoboy
from routers.moto_router import router as router_moto
from routers.abastecimento_router import router as router_abastecimento
from routers.manuntecao_router import router as router_manuntecao
from routers.dia_de_trabalho_router import router as router_dia_de_trabalho
from routers.dashboard_router import router as router_dashboard
from models.motoboy_model import Motoboy
from models.moto_model import Moto
from models.manutencao_model import Manutencao
from models.abastecimento_model import Abastecimento
from models.dia_de_trabalho_model import Dia_de_trabalho
app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "online",
        "api": "App Motoboy V2",
        "version": "1.0.0"
             }

@app.on_event('startup')
def startup():
        Base.metadata.create_all(engine)

app.include_router(router_motoboy)
app.include_router(router_moto)
app.include_router(router_abastecimento)
app.include_router(router_manuntecao)
app.include_router(router_dia_de_trabalho)
app.include_router(router_dashboard)


