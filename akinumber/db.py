from flask import g
from pymongo import MongoClient


def init_app(app):
    app.teardown_appcontext(close_db)


def get_db():
    if "db" not in g:
        g.db = MongoClient("db")
    return g.db


def close_db(e=None):
    if "db" in g:
        g.db.close()
