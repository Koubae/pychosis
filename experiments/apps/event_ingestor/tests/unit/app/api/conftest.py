from typing import Generator

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from src.app.asgi import create_app


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, None, None]:
    app = create_app()

    yield app


@pytest.fixture(scope="function")
def web_client(app: FastAPI) -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client
