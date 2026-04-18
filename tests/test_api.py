import pytest


@pytest.fixture
def created_task(client):
    # Create task and return it
    response = client.post("/tasks/", json={"title": "Test Task"})
    return response.json()


def test_create_task(client):
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


def test_get_task_not_found(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_get_task_by_id(client, created_task):
    task_id = created_task["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200


def test_update_task(created_task, client):
    task_id = created_task["id"]
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated Title"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_delete_task(created_task, client):
    task_id = created_task["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
