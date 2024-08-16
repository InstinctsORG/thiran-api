from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app, base_url="http://myapp.com:8080")


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
