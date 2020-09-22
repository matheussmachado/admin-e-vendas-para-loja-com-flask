def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/petshop.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '123452'
    app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
