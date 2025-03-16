from flask import Flask

from utils import get_valid_name

from . import db, game


def create_app():
    app = Flask(get_valid_name(__loader__.name))

    db.init_app(app)
    app.register_blueprint(game.bp)

    return app
