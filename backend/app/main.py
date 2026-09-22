from fastapi import FastAPI
from backend.app.database.base import Base
from backend.app.database.engine import engine
from backend.app.routers.motoboy_router import router as router_motoboy
from backend.app.routers.moto_router import router as router_moto
from backend.app.routers.abastecimento_router import router as router_abastecimento
from backend.app.routers.manuntecao_router import router as router_manuntecao
from backend.app.routers.dia_de_trabalho_router import router as router_dia_de_trabalho
from backend.app.routers.dashboard_router import router as router_dashboard

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


