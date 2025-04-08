from flask import Flask

from . import core, db
from .blueprints import bp
from config import Config


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    core.init_app(app)

    app.register_blueprint(bp)

    return app
