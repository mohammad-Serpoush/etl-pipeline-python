from functools import lru_cache
from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "US Financial News Articles ETL"
    ENVIRONMENT: Optional[str]
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    DB_HOST: str
    DB_PORT: int = 6432

    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    S3_ROOT_USER: str

    S3_ROOT_PASSWORD: str
    S3_PORT: str
    S3_HOST: str

    S3_CHATFLOW_MEDIA_BUCKET: str

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("DB_HOST"),
            port=str(values.get("DB_PORT")),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        # env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()


"""
broker_url = 'redis://user:password@redishost:6379/0'

"""
