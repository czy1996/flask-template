import pytest

from app import create_app


@pytest.fixture
def app():
    yield create_app()


@pytest.fixture
def client(app):
    yield app.test_client()
