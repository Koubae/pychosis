import pytest
from starlette.testclient import TestClient


@pytest.mark.unit
class TestUnitIndexController:
    web_client: TestClient

    @pytest.fixture(autouse=True)
    def _setup(self, web_client: TestClient):
        self.web_client = web_client

        yield

    def test_index(self):
        response = self.web_client.get("/")
        assert response.status_code == 200

    def test_health(self):
        response = self.web_client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"message": "OK"}

    def test_ready(self):
        response = self.web_client.get("/ready")
        assert response.status_code == 200
        assert response.json() == {"message": "OK"}
