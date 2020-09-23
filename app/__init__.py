from flask import Flask, render_template, request
from app.ext import config
from app.ext import db
from app.ext import migrate
from app.ext import admin
from app.ext.site import home
from app.ext.site import vendedor
from app.ext.site import login


def create_minimal_app():
    app = Flask(__name__)
    return app


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    admin.init_app(app)
    login.init_app(app)
    home.init_app(app)
    vendedor.init_app(app)
    return app
