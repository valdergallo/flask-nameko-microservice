class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_NATIVE_UNICODE = True
    TEMPLATES_AUTO_RELOAD = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
    NAMEKO_AMQP_URI = "amqp://guest:guest@localhost:5672"


class Develop(Config):
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


class Test(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory"
    DATABASE_URI = "sqlite:///:memory:"
