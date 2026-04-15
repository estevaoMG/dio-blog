from fastapi import APIRouter, status

from src.schemas.auth import LoginIn
from src.security import sign_jwt
from src.views.auth import LoginOut

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
)
async def login(data: LoginIn) -> LoginOut:
    token = sign_jwt(user_id=data.user_id)

    return LoginOut(access_token=token, token_type="bearer")
