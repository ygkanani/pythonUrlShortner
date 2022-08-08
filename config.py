# urlShortner_app/config.py

# pydantics is a library that uses type annotation
# to validate data and manage settings.
from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name = "Local"
    base_url = "http://localhost:8000"
    db_url = "sqlite:///./shortner.db"

    class Config:
        env_file = ".env"


# lru_cache will help retain get_settings() result in cache.
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"loading settings for: {settings.env_name}")
    return settings
