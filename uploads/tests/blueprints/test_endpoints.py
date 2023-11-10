from fastapi.testclient import TestClient
from unittest.mock import patch
from src.blueprints.endpoints import router

client = TestClient(router)

def test_who_route():
    response = client.get("/who")
    assert response.status_code == 200
    assert response.text == '"/routes"'

def test_ping_endpoint():
    response = client.get("/uploadFiles/ping")
    assert response.status_code == 200
    assert response.text == "pong"

def test_reset_database_endpoint():
    response = client.post("/uploadFiles/mergeinto")
    assert response.status_code == 200
    assert response.json() == {"msg": "Merge succeeded"}


