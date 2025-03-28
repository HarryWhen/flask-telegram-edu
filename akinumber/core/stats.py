from bson.typings import _DocumentType


def new_stats() -> _DocumentType:
    return {
        "stats": {
            "games_end": 0,
            "games_win": 0,
            "amount_guess": 0,
        },
    }
