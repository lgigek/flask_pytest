from flask import Flask
from flask_pytest.route import example


def setup_app(app):
    """ Setups the flask application up. """
    app.register_blueprint(example)

def create_app():
    """ Creates a flask application. """
    app = Flask(__name__)
    setup_app(app)

    return app


if __name__ == '__main__':
    # creates the flask app
    app = create_app()

    # sets the blueprints for the app
    setup_app(app)

    # run!
    app.run()
