import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from jose import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "")
if len(SECRET_KEY.encode("utf-8")) < 32:
    raise RuntimeError("SECRET_KEY deve ter pelo menos 32 bytes para assinar tokens JWT.")

ALGORITHM = "HS256"
ACCESS_TOKEN_TIME = 30


def criar_token(dados: dict):
    dados_copia = dados.copy()
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_TIME)
    dados_copia.update({"exp": expiracao})
    return jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)
