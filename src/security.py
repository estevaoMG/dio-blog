import time
from typing import Annotated
from uuid import uuid4

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel

SECRET = "minha-chave-super-segura-com-mais-de-32-bytes-123"
ALGORITHM = "HS256"
TOKEN_EXPIRE_SECONDS = 60 * 30


# 📦 Modelo do token
class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: int
    iat: int
    nbf: int
    jti: str


# 🔐 Geração do token
def sign_jwt(user_id: int) -> str:
    now = int(time.time())

    payload = {
        "iss": "curso-fastapi.com.br",
        "sub": str(user_id),
        "aud": "curso-fastapi",
        "exp": now + TOKEN_EXPIRE_SECONDS,
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }

    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


# 🔓 Decode do token
def decode_jwt(token: str) -> AccessToken:
    try:
        payload = jwt.decode(
            token,
            SECRET,
            algorithms=[ALGORITHM],
            options={"verify_aud": False},
        )

        payload["sub"] = int(payload["sub"])
        return AccessToken.model_validate(payload)

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )


# 🔥 JWT Bearer (CORRIGIDO: evita 403 automático do FastAPI)
class JWTBearer(HTTPBearer):
    def __init__(self):
        super().__init__(auto_error=False)  # 👈 essencial para testes

    async def __call__(self, request: Request) -> AccessToken:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        # 🚨 SEM TOKEN → sempre 401 (não 403)
        if credentials is None or not credentials.credentials:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
            )

        # 🚨 esquema inválido
        if credentials.scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme",
            )

        return decode_jwt(credentials.credentials)


# 👤 usuário atual
def get_current_user(
    token: Annotated[AccessToken, Depends(JWTBearer())],
) -> dict:
    return {"user_id": token.sub}


# 🔐 proteção de rota
def login_required(
    current_user: dict = Depends(get_current_user),
) -> dict:
    return current_user
