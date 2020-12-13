def load_app():
    from .app import app

    return app


def load_db():
    from .database import db

    return db


def load_api():
    from .urls import api

    return api


def start_server():
    app = load_app()
    load_db()
    load_api()

    return app