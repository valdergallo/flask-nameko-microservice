from base64 import b64encode
from uuid import uuid4

import pytest
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import create_database, database_exists, drop_database

from main import load_app, load_db

main_app = load_app()
db = load_db()


def create_test_database(main_app):
    SQLALCHEMY_DATABASE_URI = main_app.config.get("SQLALCHEMY_DATABASE_URI")
    print("CREATE SQLALCHEMY_DATABASE_URI ", SQLALCHEMY_DATABASE_URI)

    if database_exists(SQLALCHEMY_DATABASE_URI):
        drop_database(SQLALCHEMY_DATABASE_URI)
    create_database(SQLALCHEMY_DATABASE_URI)


@pytest.fixture(scope="session")
def app():
    main_app.config.from_object("main.config.Test")

    create_test_database(main_app)

    global db
    db = load_db()

    yield main_app


@pytest.fixture()
def client(app):
    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture
def app_config():
    return main_app.config


@pytest.fixture(scope="session")
def _db(app):
    """
    Provide the transactional fixtures with access to the database via a Flask-SQLAlchemy
    database connection.
    """
    return db
