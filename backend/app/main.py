import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database.base import Base
from backend.app.database.engine import engine
from backend.app.routers.motoboy_router import router as router_motoboy
from backend.app.routers.moto_router import router as router_moto
from backend.app.routers.abastecimento_router import router as router_abastecimento
from backend.app.routers.manuntecao_router import router as router_manuntecao
from backend.app.routers.dia_de_trabalho_router import router as router_dia_de_trabalho
from backend.app.routers.dashboard_router import router as router_dashboard
from backend.app.routers.dashboard_periodo_router import router as router_dashboard_periodo

app = FastAPI()

origens_permitidas = [
    origem.strip()
    for origem in os.getenv(
        "CORS_ALLOWED_ORIGINS",
        "http://127.0.0.1:4173,http://localhost:4173",
    ).split(",")
    if origem.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origens_permitidas,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept"],
)


@app.get("/")
def home():
    return {
        "status": "online",
        "api": "App Motoboy V2",
        "version": "1.0.0"
    }


@app.on_event("startup")
def startup():
    Base.metadata.create_all(engine)


app.include_router(router_motoboy)
app.include_router(router_moto)
app.include_router(router_abastecimento)
app.include_router(router_manuntecao)
app.include_router(router_dia_de_trabalho)
app.include_router(router_dashboard)
app.include_router(router_dashboard_periodo)
