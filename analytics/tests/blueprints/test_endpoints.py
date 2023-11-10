from fastapi.testclient import TestClient
from unittest.mock import patch
from src.blueprints.endpoints import router

client = TestClient(router)

def test_who_route():
    response = client.get("/who")
    assert response.status_code == 200
    assert response.text == '"/routes"'

def test_ping_endpoint():
    response = client.get("/routes/ping")
    assert response.status_code == 200
    assert response.text == "pong"

def test_reset_database_endpoint():
    response = client.post("/routes/reset")
    assert response.status_code == 200
    assert response.json() == {"msg": "Todos los datos fueron eliminados"}

"""def test_reset_database_endpoint():
    response = client.post("/routes/")
    assert response.status_code == 200
    assert response.json() == {"id": "Todos los datos fueron eliminados",}"""

