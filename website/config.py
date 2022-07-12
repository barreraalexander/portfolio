import json
from os import path


local_config = path.expanduser('~/etc/portfolio_config.json')
launch_config = '/etc/portfolio_config.json'

with open(local_config) as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('SECRET_KEY')

    RECAPTCHA_PUBLIC_KEY = config.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = config.get('RECAPTCHA_SECRET_KEY')

    MAIL_USERNAME = config.get('EMAIL_USER')
    MAIL_DEFAULT_SENDER = config.get('EMAIL_USER')
    MAIL_PASSWORD = config.get('EMAIL_PW')

    MAIL_PORT = 587
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_TLS = True

cacheConfig = {
    "DEBUG" : True,
    "CACHE_TYPE" : "simple",
    "CACHE_DEFAULT_TIMEOUT" : 300
}
