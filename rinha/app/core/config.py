
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, PostgresDsn, validator, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOSTNAME: str
    POSTGRES_PORT: str
    # DATABASE_URI: Optional[PostgresDsn] = None

    # @field_validator("SQLALCHEMY_DATABASE_URI", mode="before", check_fields=False)
    # @classmethod
    # def assemble_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
    #     if isinstance(v, str):
    #         print("Loading SQLALCHEMY_DATABASE_URI from .docker.env file ...")
    #         return v
    #     print("Creating SQLALCHEMY_DATABASE_URI from .env file ...")
    #     return PostgresDsn.build(
    #         scheme="postgresql",
    #         username=values.data.get("POSTGRES_USER"),
    #         password=values.data.get("POSTGRES_PASSWORD"),
    #         host=values.data.get("POSTGRES_SERVER"),
    #         path=f"{values.data.get('POSTGRES_DB') or ''}",
    #     )      
    

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
