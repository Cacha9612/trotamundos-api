from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi.security import HTTPBearer
from fastapi import HTTPException, Depends, HTTPException
from pydantic import ValidationError
from calendar import timegm

SECRET_KEY = "054cfd6c36da00d8a26cb2b11cfb5d8026f04a306d027a482141fcc9c559a2ec"
ALGORITHM = "HS256"

oauth2_scheme = HTTPBearer(
    scheme_name='Authorization'
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class utilsclass():
    async def verify_password(plain_password, hashed_password):
        resultado = pwd_context.verify(plain_password, hashed_password)
        print(resultado)
        return resultado

    async def get_password_hash(password):
        return pwd_context.hash(password)

    async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    async def validate_token(http_authorization_credentials=Depends(oauth2_scheme)) -> str:
        try:
            payload = jwt.decode(
                http_authorization_credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
            now = timegm(datetime.utcnow().utctimetuple())
            if payload.get('exp') < now:
                raise HTTPException(status_code=403, detail="Token expirado")
            return payload.get('username')
        except(JWTError, ValidationError):
            raise HTTPException(
                status_code=403,
                detail=f"Credenciales no validas",
            )
