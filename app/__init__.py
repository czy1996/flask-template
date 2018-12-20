import os

from . import config
from .models import db

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    app_env = os.environ.get('APP_ENV')
    config_object = {
        'Production': 'config.ProductionConfig',
        'Development': 'config.DevelopmentConfig',
    }
    if app_env:
        app.config.from_object(config_object.get(app_env, 'config.Config'))

    db.init_app(app)

    @app.route('/')
    def hello_world():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    create_app().run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
