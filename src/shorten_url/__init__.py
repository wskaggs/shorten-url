from typing import Callable
from flask import Flask


def create_app(config_callback: Callable[[Flask], None]) -> Flask:
    """
    Factory to create the url shortener flask application

    :param config_callback: a callable to configure the flask application
    :return: the flask application
    """
    app = Flask(__name__)
    config_callback(app)
    
    @app.route("/")
    def root() -> str:
        """
        Temporary endpoint to ensure the application is running

        :return: html as a string
        """
        return "Hello, world"
    
    return app
