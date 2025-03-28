from flask import Blueprint

from utils import get_module_name

from . import game, stats, user

bp = Blueprint(
    get_module_name(__name__),
    __name__,
    url_prefix="/<int:user_id>",
)

bp.register_blueprint(user.bp)
bp.register_blueprint(stats.bp)
bp.register_blueprint(game.bp)
