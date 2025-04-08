from bson.typings import _DocumentType
from flask import Flask, g
from pymongo import MongoClient
from pymongo.synchronous import collection, database


def init_app(app: Flask):
    app.teardown_appcontext(_close_db)


def _init_db_context():
    g._client = MongoClient("db")
    g.db = g._client.app
    g.profiles = g.db.profiles


def _close_db(e=None):
    if "_client" in g:
        g._client.close()


def get_db() -> database.Database[_DocumentType]:
    if "db" not in g:
        _init_db_context()
    return g.db


def get_profiles() -> collection.Collection[_DocumentType]:
    if "profiles" not in g:
        _init_db_context()
    return g.profiles
