from flask import Blueprint

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def root() -> str:
    """
    Temporary endpoint to ensure the application is running

    :return: html as a string
    """
    return "Hello, world"
