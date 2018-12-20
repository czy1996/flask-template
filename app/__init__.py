import os

from . import config


from flask import Flask


def create_app():
    app = Flask(__name__)

    app_env = os.environ.get('APP_ENV')
    config_object = {
        'Production': 'config.ProductionConfig',
        'Development': 'config.DevelopmentConfig',
    }
    if app_env:
        app.config.from_object(config_object.get(app_env, 'config.Config'))

    @app.route('/')
    def hello_world():
        return 'Hello World from container! {} {}'.format(app_env, app.config.get('DB'))

    return app


if __name__ == '__main__':
    create_app().run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
