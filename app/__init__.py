from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World from container!'

    return app


if __name__ == '__main__':
    create_app().run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
