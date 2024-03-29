from flask import Flask
from config import Config

from .api.routes import api
from .auth.routes import auth

app=Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(api)
app.register_blueprint(auth)

from . import routes

