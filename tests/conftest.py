import pytest

@pytest.fixture(scope="session")
def test_client():
    from fastapi.testclient import TestClient
    from app.main import app

    client = TestClient(app)
    yield client

@pytest.fixture
def sample_item():
    return {
        "name": "Sample Item",
        "description": "This is a sample item.",
        "price": 10.99,
        "tax": 1.5
    }