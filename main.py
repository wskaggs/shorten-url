from flask import Flask
from instance import configs
from src.shorten_url import create_app


def config_callback(app: Flask) -> None:
    """
    A callback to configure the flask application

    :param app: the flask application to configure
    """
    app.config.from_object(configs.Development)


def main() -> None:
    """
    Entry point for running the application
    """
    app = create_app(config_callback)
    app.run()


if __name__ == "__main__":
    main()
