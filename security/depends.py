from fastapi import HTTPException, status,Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt,JWTError
from schermas.motoboy_scherma import MotoboyResponse
from security.jwt import SECRET_KEY,ALGORITHM
from sqlalchemy.orm import Session
from database.db import get_db
from models.motoboy_model import Motoboy

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/Motoboy/auth")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

    except JWTError as e :
        raise HTTPException (status_code=401, detail=f" {e}")

    usuario = db.query(Motoboy).filter(Motoboy.id == int(user_id)).first()

    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    return usuario


def get_current_user_id(user:Motoboy = Depends(get_current_user)):
    return user.id