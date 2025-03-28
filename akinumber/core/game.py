import random

from bson.typings import _DocumentType

from akinumber.db import get_profiles

from .user import user_projection

MAX_ABS = 1_000_000


def new_hidden_number() -> int:
    return random.randint(-MAX_ABS, MAX_ABS)


def new_game() -> _DocumentType:
    return {
        "game": {
            "hidden_number": new_hidden_number(),
            "total_attempts": 0,
            "end": False,
        },
    }


def init_game(user_id: int):
    get_profiles().update_one(  # dont raise error if there arent
        user_projection(user_id),
        {"$set": new_game()},
    )
