from flask import Flask
from environment import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from containers import Container
from db import db


class FlaskMicroservice(Flask):
    container: Container


def create_app(database_uri: str | None = None) -> FlaskMicroservice:
    app = FlaskMicroservice(__name__)
    app.container = Container()

    # Configure the database URI
    if database_uri:  # pragma: no cover
        app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = (
            f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

    # Initialize the database
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register the blueprints

    return app
