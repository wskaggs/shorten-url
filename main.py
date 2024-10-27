from flask import Flask
from src.shorten_url import create_app


def config_callback(app: Flask) -> None:
    """
    A callback to configure the flask application

    :param app: the flask application to configure
    """
    app.config.update(DEBUG=True)


def main() -> None:
    """
    Entry point for running the application
    """
    app = create_app(config_callback)
    app.run()


if __name__ == "__main__":
    main()
