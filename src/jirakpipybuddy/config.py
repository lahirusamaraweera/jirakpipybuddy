
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    app_name: str = "pet_sync"
    debug: bool = False
    timeout_seconds: int = Field(default=10, ge=1)

    model_config = {
        "env_prefix": "APP_",
        "case_sensitive": False,
    }


@lru_cache
def get_config() -> AppConfig:
    """
    Cached config instance (singleton)
    """
    return AppConfig()
