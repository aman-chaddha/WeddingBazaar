from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import AnyUrl, Field
from typing import List, Optional
import os


class Settings(BaseSettings):
    APP_NAME: str = "WeddingBazaar API"
    API_V1_PREFIX: str = "/api/v1"
    CORS_ALLOW_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]

    # Security
    SECRET_KEY: str = Field(default="change-me", description="JWT secret key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Database
    DATABASE_URL: str = Field(
        default="postgresql+psycopg2://postgres:postgres@localhost:5432/weddingbazaar",
        description="SQLAlchemy database URL",
    )

    # Dev convenience
    AUTO_CREATE_TABLES: bool = True

    # Optional services
    REDIS_URL: str | None = None
    STRIPE_API_KEY: str | None = None
    MAIL_USERNAME: Optional[str] = None
    MAIL_PASSWORD: Optional[str] = None
    MAIL_FROM: Optional[str] = None

    class Config:
        # Look for .env at project root (four levels up from this file)
        env_file = os.path.join(
            os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            ),
            ".env",
        )
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings() -> "Settings":
    return Settings()


settings = get_settings()
