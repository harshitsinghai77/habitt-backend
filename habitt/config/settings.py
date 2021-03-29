import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    APP_NAME = "Habitt"
    REGISTRATION_TOKEN_LIFETIME = 60 * 60
    TOKEN_ALGORITHM = "HS256"
    SMTP_SERVER: str = "localhost:25"
    MAIL_SENDER = "harshitsinghai77@gmail.com"
    API_PREFIX = "/api"
    HOST = "localhost"
    PORT = 8000
    BASE_URL = "{}:{}/".format(HOST, str(PORT))
    MODELS = [
        "habitt.models.users",
    ]

    class Config:
        case_sensitive: bool = True


@lru_cache
def get_setting():
    return Settings()
