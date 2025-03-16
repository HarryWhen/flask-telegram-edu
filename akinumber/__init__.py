from flask import Flask

from utils import get_valid_name


def create_app():
    app = Flask(get_valid_name(__loader__.name))

    return app
