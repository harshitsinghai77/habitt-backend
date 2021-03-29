import uuid
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import UUID4

from habitt.config.settings import Settings

settings = Settings()


class Auth:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls.password_context.hash(password)

    @staticmethod
    def get_token(data: dict, expires_delta: int):
        to_encode = data.copy()
        to_encode.update(
            {
                "exp": datetime.utcnow() + timedelta(seconds=expires_delta),
                "iss": settings.APP_NAME,
            }
        )
        return jwt.encode(
            to_encode, settings.SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM
        )

    @staticmethod
    def get_confirmation_token(user_id: int):
        jti = uuid.uuid4()
        claims = {"sub": user_id, "scope": "registration", "jti": str(jti)}
        return {
            "jti": jti,
            "token": Auth.get_token(claims, settings.REGISTRATION_TOKEN_LIFETIME),
        }

    @classmethod
    def get_password_hash(cls, password: str):
        return cls.password_context.hash(password)
