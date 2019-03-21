from pytest import fixture
from flaskr import create_app


@fixture
def test_client():
    app = create_app()
    app.debug = True

    return app.test_client()


def test_hello(test_client):
    response = test_client.get("/hello")
    response_payload = response.get_json()

    assert response.status_code == 200
    assert response_payload == {"Message": "Hello world!"}
