# test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    res = client.get("/")
    assert res.status_code == 200
    # assert 'Добро пожаловать' in res.text 
    assert 'Hello from Flask CD!' in res.text 