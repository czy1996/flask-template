import pytest

from mongoengine import connect

from app import create_app, config
from app.models.Todo import Todo


@pytest.fixture
def app():
    app = create_app()

    Todo(title='test todo').save()
    Todo(title='test todo2').save()
    yield app  # 这行相当于隔开 setUp 和 tearDown

    db, host = config.TestingConfig.MONGODB_SETTINGS['db'], config.TestingConfig.MONGODB_SETTINGS['host']
    connect(db=db, host=host).drop_database(db)
    connect(db='test', host=host).drop_database('test')


@pytest.fixture
def client(app):
    yield app.test_client()
