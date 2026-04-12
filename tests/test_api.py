from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


@pytest.fixture
def created_task():
    # Create user
    client.post(
        "/users/",
        json={"email": "u@test.com", "username": "u", "password": "pass"},
    )
    # Create task and return it
    response = client.post("/tasks/", json={"title": "Test Task"})
    return response.json()


def test_create_task():
    # First create a user (tasks need a user)
    client.post(
        "/users/",
        json={
            "email": "taskuser@example.com",
            "username": "taskuser",
            "password": "testpass123",
        },
    )
    # Then create a task
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "Test Description"},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"


def test_get_task_not_found():
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_get_task_by_id(created_task):
    task_id = created_task["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200


def test_update_task(created_task):
    task_id = created_task["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Title"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_task(created_task):
    task_id = created_task["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
