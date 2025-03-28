from bson.typings import _DocumentType

from akinumber.db import get_profiles


def new_user(user_id: int) -> _DocumentType:
    return {
        "user": {
            "user_id": user_id,
        },
    }


def user_projection(user_id: int) -> _DocumentType:
    return {
        "user": {
            "user_id": user_id,
        },
    }


def init_user(user_id: int):
    get_profiles().update_one(  # dont raise error if there arent
        user_projection(user_id),
        {"$set": new_user(user_id)},
        upsert=True,
    )
