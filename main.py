from flask import Flask

from containers import Container


class FlaskMicroservice(Flask):
    container: Container


def create_app() -> FlaskMicroservice:
    app = FlaskMicroservice(__name__)
    app.container = Container()

    return app
