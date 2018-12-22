class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass
    MONGODB_SETTINGS = {
        'db': 'Todo',
        'host': 'mongodb',
        'port': 27017
    }


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'Todo',
        'host': 'mongodb',
        'port': 27017
    }


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'testing',
        'host': 'mongo',
        'port': 27017,
    }
