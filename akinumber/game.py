from flask import Blueprint
from utils import get_valid_name

bp = Blueprint(get_valid_name(__loader__.name), __name__, url_prefix="/game")


@bp.route("/start")
def start_game():
    return (
        "The game should be started here, but this feature isn't currently implemented"
    )


@bp.route("/make-guess")
def make_guess():
    return "You could make a guess here, but this feature isn't currently implemented"


@bp.route("/stop")
def force_stop():
    return (
        "The game should be stopped here, but this feature isn't currently implemented"
    )
