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
    
    # Register blueprints
    from . import blueprints

    app.register_blueprint(blueprints.main_blueprint)

    # Register/initialize extensions
    from . import extensions

    extensions.database.init_app(app)

    # Create database tables if not already done
    with app.app_context():
        extensions.database.create_all()

    return app
