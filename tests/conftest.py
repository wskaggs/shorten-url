from collections.abc import Generator
from flask import Flask
from flask.testing import FlaskClient
from pytest import fixture
from instance import configs
from shorten_url import create_app


def config_callback(app: Flask) -> None:
    """
    A callback to configure the flask application

    :param app: the flask application to configure
    """
    app.config.from_object(configs.Testing)


@fixture
def app() -> Flask:
    """
    Fixture to create the flask app in a testing environment

    :return: the flask app
    """
    app = create_app(config_callback)
    return app


@fixture
def client(app: Flask) -> Generator[FlaskClient, None, None]:
    """
    Fixture to create a test client, preventing the need for
    a live, running server while testing

    :return: a generator yielding the test client
    """
    with app.test_client() as client:
        yield client
