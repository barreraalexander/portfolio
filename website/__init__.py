from flask import Flask
from flask_assets import Environment
from flask_mail import Mail
from flask_caching import Cache

from website.config import Config, cacheConfig
from website.utils.assets import bundles


assets = Environment ()
cache = Cache(config=cacheConfig)
mail = Mail()

from website.utils.assets import bundles

def create_app (config_class=Config):
    app = Flask (__name__)
    app.config.from_object(Config)
    
    assets.init_app(app)
    assets.register(bundles)
    mail.init_app(app)
    cache.init_app(app)

    
    from website.blueprints.main.routes import main
    from website.blueprints.api.routes import api

    app.register_blueprint(main)
    app.register_blueprint(api)

    return app

