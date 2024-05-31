from flask import Flask, json
from werkzeug.exceptions import HTTPException

from src.routes.pong import ping


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    blueprints = [ping]

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = e.get_response()
        response.data = json.dumps(
            {
                "error": {
                    "code": e.code,
                    "name": e.name,
                    "description": e.description,
                }
            }
        )
        print(response.data)
        response.content_type = "application/json"
        return response

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
