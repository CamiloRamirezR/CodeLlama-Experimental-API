from flask import Flask
import os
from containers import Container
from db import db

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


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
