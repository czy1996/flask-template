import os

from .models import db, Todo

from flask import Flask, render_template


def create_app(**config_overrides):
    app = Flask(__name__)

    app_env = os.environ.get('APP_ENV')

    # 这里不能使用相对导入
    config_object = {
        'Production': 'app.config.ProductionConfig',
        'Development': 'app.config.DevelopmentConfig',
        'Testing': 'app.config.TestingConfig',
    }
    if app_env:
        app.config.from_object(config_object.get(app_env, 'config.Config'))

    app.config.update(**config_overrides)

    db.init_app(app)

    @app.route('/')
    def hello_world():
        Todo(title='new').save()
        return render_template('index.html', todos=Todo.objects)

    @app.route('/hello')
    def hello_page():
        app.logger.info("hello viewed")
        return 'Hello page edited 2'

    return app


if __name__ == '__main__':
    create_app().run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
