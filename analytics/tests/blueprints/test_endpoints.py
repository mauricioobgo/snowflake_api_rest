from fastapi.testclient import TestClient
from unittest.mock import patch
from src.blueprints.endpoints import router

client = TestClient(router)

def test_who_route():
    response = client.get("/who")
    assert response.status_code == 200
    assert response.text == '"/analytics"'

def test_ping_endpoint():
    response = client.get("/analytics/ping")
    assert response.status_code == 200
    assert response.text == "pong"

def test_reset_database_endpoint1():
    response = client.post("/jobDepartment/2021")
    assert response.status_code == 200

def test_reset_database_endpoint2():
    response = client.post("/DepartmentHired/2021")
    assert response.status_code == 200


