from lesson_8.config import HEADERS, BASE_URL, PROJECT_ID
import requests


url = f"{BASE_URL}/projects/{PROJECT_ID}"


def test_find_project_id(payload=None):
    response = requests.get(url, headers=HEADERS, json=payload)
    assert response.status_code == 200


# Переменная payload не определена в коде перед её использованием.
def test_find_project_id_failed(payload=None):
    response = requests.get(url, headers=HEADERS, json=payload)
    assert response.status_code == 200
