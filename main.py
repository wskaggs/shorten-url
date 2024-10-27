from src.shorten_url import create_app


def main() -> None:
    """
    Entry point for running the application
    """
    app = create_app()
    app.run()


if __name__ == "__main__":
    main()
