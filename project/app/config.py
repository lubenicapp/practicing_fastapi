import logging
from functools import cache

from pydantic import BaseSettings, AnyUrl

log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    environment: str = 'dev'
    testing: bool = 0
    database_url: AnyUrl = None

@cache
def get_settings() -> BaseSettings:
    log.info('Loading config settings form the environment..')
    return Settings()
