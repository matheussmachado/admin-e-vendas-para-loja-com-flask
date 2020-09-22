from .main import db

def init_app(app):
    db.init_app(app)
    app.db = db
