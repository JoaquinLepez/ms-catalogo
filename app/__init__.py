from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from app.config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    db.init_app(app)
    migrate.init_app(app, db, version_table='alembic_version_catalogo')

    from app.resources import catalogo
    app.register_blueprint(catalogo, url_prefix='/api/v1')

    return app

