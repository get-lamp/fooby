import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db_session
from fastapi import status


def test_healthcheck():
    client = TestClient(app)
    response = client.get("/healthcheck")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_create_user(db_session):

    app.dependency_overrides[get_db_session] = lambda: db_session

    client = TestClient(app)

    response = client.post(
        "/users/", json={"name": 'John', 'email': 'john@fooby.com'}
    )
    app.dependency_overrides.clear()
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "John"
    assert data["email"] == "john@fooby.com"
    assert data["id"] is not None
