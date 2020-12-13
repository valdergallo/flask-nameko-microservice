from .app import app
from flask_sqlalchemy import SQLAlchemy, models_committed
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# start database
db = SQLAlchemy(app)

# add model marshmallow
ma = Marshmallow(app)

# add alembic
Migrate(app, db)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
