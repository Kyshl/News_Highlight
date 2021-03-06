from flask import Flask
from flask_bootstrap import Bootstrap
from .main import main as main_blueprint
from config import config_options
from .requests import configure_request


bootstrap = Bootstrap()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config_options[config_name])
	app.register_blueprint(main_blueprint)

	bootstrap.init_app(app)
	configure_request(app)
	return app