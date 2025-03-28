from typing import Literal

from flask import Blueprint

from akinumber.core import user
from utils import get_module_name

bp = Blueprint(
    get_module_name(__name__),
    __name__,
    url_prefix="/<int:user_id>",
)


@bp.route("/register")
def register_user(user_id: int) -> Literal["Success"]:
    user.init_user(user_id)
    return "Success"
