import logging
import os

from fastapi import FastAPI

from src.app.api.router import get_router


def create_app() -> FastAPI:
    setup()
    app = FastAPI()

    router = get_router()
    app.include_router(router)
    return app


def setup() -> None:
    log_level = logging.getLevelName(os.getenv("LOG_LEVEL", "INFO").upper())
    logging.basicConfig(level=log_level)
    logging.getLogger("uvicorn").setLevel(log_level)
    logging.getLogger("uvicorn.access").setLevel(log_level)
    logging.getLogger("uvicorn.error").setLevel(log_level)
    logging.getLogger("uvicorn.access").setLevel(log_level)
