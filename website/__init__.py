from flask import Flask
from flask_assets import Environment
from flask_mail import Mail
from flask import g
from website.config import settings, Settings
from website.utils.assets import bundles


assets = Environment ()
mail = Mail()

from website.utils.assets import bundles
from website import schemas


def create_app (config_class=settings):
    app = Flask (__name__)
    app.config.from_object(config_class)

    assets.init_app(app)
    assets.register(bundles)
    mail.init_app(app)

    
    from website.blueprints.main.routes import main
    from website.blueprints.api.routes import api

    app.register_blueprint(main)
    app.register_blueprint(api)


    # app.before_request(_before_request)

    return app



def _before_request():
    g.schemas = schemas
    # g.language = schemas.metaLanguage()
