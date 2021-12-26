import json

with open('/etc/portfolio_config.json') as config_file:
    config = json.load(config_file)


class Config:
    SECRET_KEY = config.get('secret_key')
