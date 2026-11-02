from datetime import date

from fastapi import Depends, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.database.db import get_db
from backend.app.repository.motoboy_repository import busca_motoboy_id
from backend.app.models.motoboy_model import Motoboy
from backend.app.security.jwt import ALGORITHM, SECRET_KEY
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/Motoboy/auth")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    try:
        usuario = busca_motoboy_id(db, int(user_id))
    except (TypeError, ValueError):
        raise HTTPException(status_code=401, detail="Token inválido")

    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    return usuario


def get_current_user_id(user:Motoboy = Depends(get_current_user)):
    return user.id

def get_data():
    hoje : date = date.today()
    return hoje
