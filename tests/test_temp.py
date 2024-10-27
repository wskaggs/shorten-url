from flask.testing import FlaskClient


def test_root(client: FlaskClient) -> None:
    """
    A temporary test to ensure pytest is properly configured

    :param client: the test client
    """
    response = client.get("/")
    assert response.data == b"Hello, world"
