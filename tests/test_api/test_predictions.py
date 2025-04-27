import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_stress_low():
    response = client.post(
        "/predict-stress",
        json={
            "grades": [4.5, 4.0, 4.8],
            "attendance": 0.95,
            "total_hours": 30
        }
    )
    assert response.status_code == 200
    assert response.json()["stress_level"] == "BAJO"

def test_predict_stress_high():
    response = client.post(
        "/predict-stress",
        json={
            "grades": [2.5, 2.8, 3.0],
            "attendance": 0.6,
            "total_hours": 50
        }
    )
    assert response.status_code == 200
    assert response.json()["stress_level"] == "ALTO"

def test_predict_stress_invalid_data():
    response = client.post(
        "/predict-stress",
        json={
            "grades": [],
            "attendance": -1,
            "total_hours": 0
        }
    )
    assert response.status_code == 400
    assert "Datos insuficientes" in response.json()["detail"]