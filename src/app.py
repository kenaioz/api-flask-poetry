from flask import Flask
from src.routes.pong import ping


def create_app():
    app = Flask(__name__)
    app.register_blueprint(ping)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
