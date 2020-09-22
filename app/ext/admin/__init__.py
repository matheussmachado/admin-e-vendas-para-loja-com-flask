from flask_admin import Admin
from .main import ProdutoView, CredenciaisView, RegistroDeVendasView
from app.ext.db.main import Produtos, Credenciais, RegistroDeVendas, db
admin = Admin()

def init_app(app):
    admin.name = 'PetClub'
    admin.template_mode = 'bootstrap3'
    admin.init_app(app)
    admin.add_view(ProdutoView(Produtos, db.session))
    admin.add_view(CredenciaisView(Credenciais, db.session))
    admin.add_view(RegistroDeVendasView(RegistroDeVendas, db.session))
