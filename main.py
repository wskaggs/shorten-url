from flask import Flask


def main() -> None:
    """
    Entry point for running the application
    """
    app = Flask(__name__)

    @app.route("/")
    def root() -> str:
        """
        Temporary endpoint to ensure the application is running

        :return: html as a string
        """
        return "Hello, world"
    
    app.run()


if __name__ == "__main__":
    main()
