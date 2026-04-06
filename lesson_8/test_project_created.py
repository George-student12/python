import requests
from lesson_8.config import BASE_URL, HEADERS, ADMIN_ID


url = f"{BASE_URL}/projects"


def test_project_create():
    payload = {
      "title": "Skyeng",
      "users": {ADMIN_ID: "admin"}
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    assert response.status_code == 201


# Отпечатка в html
def test_project_create_failed():
    url = f"{BASE_URL}/project"
    payload = {
      "title": "Skyeng",
      "users": {"60b08e14-2d93-413a-80dd-c8e23b942e44": "admin"}
    }

    response = requests.post(url, headers=HEADERS, json=payload)

    assert response.status_code == 201
