from pytest import fixture
from flask_pytest import flaskr


@fixture
def app():
    app = flaskr.create_app()
    app.debug = True
    return app.test_client()


def test_hello(app):
    res = app.get('/hello')
    assert res.status_code == 200
