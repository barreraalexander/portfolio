from flask import Flask
from website.config import Config
from website.utils.assets import bundles
from flask_assets import Environment, Bundle
from flask_mail import Mail

assets = Environment ()

mail = Mail()

from website.utils.assets import bundles

def create_app (config_class=Config):
    app = Flask (__name__)
    app.config.from_object(Config)
    
    assets.init_app(app)
    mail.init_app(app)
    assets.register(bundles)

    
    from website.blueprints.\
         main.routes import main

    from website.blueprints.\
         api.routes import api

    app.register_blueprint(main)
    app.register_blueprint(api)

    return app

