from datetime import datetime,timedelta,timezone
from jose import jwt
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

ALGORITHM = 'HS256'
ACCESS_TOKEN_TIME = 30

def criar_token(dados:dict):
    dados_copia = dados.copy()

    expiraca = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_TIME)

    dados_copia.update({'exp' : expiraca})

    token = jwt.encode(dados_copia,SECRET_KEY,algorithm=ALGORITHM)

    return token