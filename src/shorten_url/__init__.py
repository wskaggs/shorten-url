from flask import Flask


def create_app() -> Flask:
    """
    Factory to create the url shortener flask application

    :return: the flask application
    """
    app = Flask(__name__)

    @app.route("/")
    def root() -> str:
        """
        Temporary endpoint to ensure the application is running

        :return: html as a string
        """
        return "Hello, world"
    
    return app
