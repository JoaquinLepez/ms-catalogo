from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import os
from pdchaos.middleware.contrib.flask.flask_middleware import FlaskMiddleware
from app.config import config, cache_config

db = SQLAlchemy()
middleware = FlaskMiddleware()
cache = Cache()

def create_app():
    app_context = os.getenv("FLASK_CONTEXT")
    print(f"app_context: {app_context}")

    app = Flask(__name__)
    configuration = config[app_context if app_context else 'development']
    app.config.from_object(configuration)

    app.config['CHAOS_MIDDLEWARE_APPLICATION_NAME'] = 'MS1'
    app.config['CHAOS_MIDDLEWARE_APPLICATION_ENV'] = 'development'


    db.init_app(app)
    cache.init_app(app, config=cache_config)

    from app.resource import catalogo
    app.register_blueprint(catalogo, url_prefix='/api/v1')

    return app

