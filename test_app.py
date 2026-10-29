import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_push1(client):
    response = client.post('/calculate', json={"marks": [80, 90, 70]})
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data['total_marks'] == 240
    assert json_data['average_marks'] == 80.0