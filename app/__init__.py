from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from app.config import config

db = SQLAlchemy()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    db.init_app(app)

    from app.resource import catalogo
    app.register_blueprint(catalogo, url_prefix='/api/v1')

    return app

