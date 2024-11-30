from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_migrate import Migrate
from sqlalchemy import MetaData
import os
# from pdchaos.middleware.contrib.flask.flask_middleware import FlaskMiddleware
from app.config import config, cache_config

db = SQLAlchemy(metadata= MetaData(schema= 'catalogo'))
migrate = Migrate()
# middleware = FlaskMiddleware()
cache = Cache()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    # app.config['CHAOS_MIDDLEWARE_APPLICATION_NAME'] = 'MS1'
    # app.config['CHAOS_MIDDLEWARE_APPLICATION_ENV'] = 'development'


    db.init_app(app)
    migrate.init_app(app, db, version_table='alembic_version_catalogo')
    cache.init_app(app, config=cache_config)

    from app.resource import catalogo
    app.register_blueprint(catalogo, url_prefix='/api/v1')

    return app

