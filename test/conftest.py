import pytest

from app import app


@pytest.fixture
def client():
    yield app.test_client()


def test_hello(client):
    r = client.get('/')
    print(r)
