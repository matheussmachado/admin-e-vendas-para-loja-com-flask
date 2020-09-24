from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Produtos(db.Model):
    id = db.Column((db.Integer), primary_key=True, autoincrement=True)
    nome = db.Column((db.String(255)), unique=True, nullable=False)
    codigo = db.Column((db.Integer), unique=True, nullable=False)
    valor = db.Column((db.Float), nullable=False)
    quantidade = db.Column((db.Integer), nullable=False)

    def __init__(self, nome, codigo, valor, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.valor = valor
        self.quantidade = quantidade


class Credenciais(db.Model):
    id = db.Column((db.Integer), primary_key=True, autoincrement=True)
    nome_do_funcionario = db.Column((db.String(55)), nullable=False)
    credencial = db.Column((db.Integer), unique=True, nullable=False)
    cargo = db.Column((db.String(25)), nullable=False)
    permissao = db.Column((db.Boolean), nullable=False)

    def __init__(self, nome_funcionario, credencial,
        cargo, permissao):
        self.nome_funcionario = nome_funcionario
        self.credencial = credencial
        self.cargo = cargo
        self.permissao = permissao


class RegistroDeVendas(db.Model):
    id = db.Column((db.Integer), primary_key=True)
    recibo = db.Column((db.Integer), nullable=False)
    codigo = db.Column((db.Integer), nullable=False)
    quantidade = db.Column((db.Integer), nullable=False)
    operador = db.Column((db.String(20)), nullable=False)
    data_hora = db.Column(db.TIMESTAMP(timezone=False),
      nullable=False)

    def __init__(self, recibo, codigo, quantidade, operador):
        self.recibo = recibo
        self.codigo = codigo
        self.quantidade = quantidade
        self.operador = operador
        self.data_hora = datetime.now()
