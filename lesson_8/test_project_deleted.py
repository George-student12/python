from lesson_8.config import HEADERS, BASE_URL, ADMIN_ID, PROJECT_ID
import requests


url = f"{BASE_URL}/projects/{PROJECT_ID}"


def test_project_deleted():
    payload = {
        "deleted": True,
        "title": "Skyeng",
        "users": {
            ADMIN_ID: "admin"
        }
    }

    response = requests.put(url, headers=HEADERS, json=payload)
    assert response.status_code == 200


# Отпечатка в ответе (Неправильный метод)
def test_project_deleted_failed():
    payload = {
        "deleted": True,
        "title": "Skyeng",
        "users": {
            ADMIN_ID: "admin"
        }
    }

    response = requests.put(url, headers=HEADERS, json=payload)
    assert response.status_code == 201
