from typing import Literal, LiteralString

from flask import Blueprint

from akinumber.core import game
from utils import get_module_name

bp = Blueprint(
    get_module_name(__name__),
    __name__,
    url_prefix="/game",
)


@bp.route("/start")
def start_game(user_id: int) -> Literal["Success"]:
    game.init_game()
    return "Success"


@bp.route("/make-guess")
def make_guess(user_id: int) -> LiteralString:
    return "You could make a guess here, but this feature isn't currently implemented"


@bp.route("/stop")
def force_stop(user_id: int) -> LiteralString:
    return (
        "The game should be stopped here, but this feature isn't currently implemented"
    )
