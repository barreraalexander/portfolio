from flask import Flask
from website.config import Config
from website.utils.assets import bundles
from flask_assets import Environment, Bundle

assets = Environment ()

def create_app (config_class=Config):
    app = Flask (__name__)
    assets.init_app(app)
    assets.register(bundles)

    app.config.from_object(Config)
    
    from website.blueprints.\
         main.routes import main

    app.register_blueprint(main)

    return app

