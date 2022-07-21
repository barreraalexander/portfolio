from flask import Flask
from flask_assets import Environment
from flask_mail import Mail

from website.config import settings, Settings
from website.utils.assets import bundles


assets = Environment ()
mail = Mail()

from website.utils.assets import bundles

def create_app (config_class=Settings):
    app = Flask (__name__)
    app.config.from_object(settings)

    assets.init_app(app)
    assets.register(bundles)
    mail.init_app(app)
    
    from website.blueprints.main.routes import main
    from website.blueprints.api.routes import api

    app.register_blueprint(main)
    app.register_blueprint(api)

    return app

