from flask_migrate import Migrate

def init_app(app):
    Migrate(app, app.db, render_as_batch=True)
