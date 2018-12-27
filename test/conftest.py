import pytest

from mongoengine import connect

from app import create_app, config
from app.models.Todo import Todo


@pytest.fixture
def app():
    app = create_app()

    for i in range(1, 22):
        Todo(title='test todo' + str(i)).save()
    yield app  # 这行相当于隔开 setUp 和 tearDown

    db, host = config.TestingConfig.MONGODB_SETTINGS['db'], config.TestingConfig.MONGODB_SETTINGS['host']
    connect(db=db, host=host).drop_database(db)
    connect(db='test', host=host).drop_database('test')


@pytest.fixture
def client(app):
    yield app.test_client()
