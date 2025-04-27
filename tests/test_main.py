from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"id": 1, "title": "Test Task"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_task():
    client.post("/tasks/", json={"id": 2, "title": "Another Task"})
    response = client.delete("/tasks/2")
    assert response.status_code == 200
    response = client.delete("/tasks/999")
    assert response.status_code == 404