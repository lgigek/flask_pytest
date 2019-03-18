from flask import Flask
from route import example


def create_app():
    app = Flask(__name__)
    app.register_blueprint(example)

    return app


if __name__ == '__main__':
    my_app = create_app()
    my_app.run()
