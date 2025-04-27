from fastapi.testclient import TestClient
from app.main import app
from app.models.item import Item
from app.schemas.item import ItemCreate

client = TestClient(app)

def test_create_item():
    item_data = {"name": "Test Item", "description": "This is a test item", "price": 10.0}
    response = client.post("/api/v1/items/", json=item_data)
    assert response.status_code == 201
    assert response.json()["name"] == item_data["name"]

def test_read_item():
    response = client.get("/api/v1/items/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_item():
    item_data = {"name": "Updated Item", "description": "This is an updated test item", "price": 15.0}
    response = client.put("/api/v1/items/1", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == item_data["name"]

def test_delete_item():
    response = client.delete("/api/v1/items/1")
    assert response.status_code == 204
    response = client.get("/api/v1/items/1")
    assert response.status_code == 404