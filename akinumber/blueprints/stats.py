from flask import Blueprint

from utils import get_module_name

bp = Blueprint(
    get_module_name(__name__),
    __name__,
    url_prefix="/stats",
)
