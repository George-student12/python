from lesson_8.config import HEADERS, BASE_URL, PROJECT_ID
import requests


url = f"{BASE_URL}/projects/{PROJECT_ID}"


def test_find_project_id(payload=None):
    response = requests.get(url, headers=HEADERS, json=payload)
    assert response.status_code == 200


# Неправильный id.
def test_find_project_id_failed(payload=None):
    url = f"{BASE_URL}/projects/4099b97aa2-7d21-478d-9345-5bdf57445090"
    response = requests.get(url, headers=HEADERS, json=payload)
    assert response.status_code == 404
