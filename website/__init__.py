from flask import Flask
from website.db import DB
from website.config import Config
from website.utils.assets import bundles
from flask_assets import Environment, Bundle

db = DB()
assets = Environment ()

def create_app (config_class=Config):
    app = Flask (__name__)
    assets.init_app(app)
    assets.register(bundles)

    app.config.from_object(Config)
    
    db.init_app(app)

    from website.blueprints.\
         main.routes import main

    app.register_blueprint(main)

    return app

