from abc import ABC, abstractmethod
from datetime import datetime
from wtforms import IntegerField, Form, PasswordField, SubmitField
from wtforms.fields import html5
from wtforms.validators import DataRequired, NumberRange

class RequisicaoDeProduto:

    def __init__(self, codigo, quantidade):
        self.codigo = codigo
        self.quantidade = quantidade
        self.error = None
        self.status_error = ['Código inválido.', 'Quantidade insuficiente.']

    def set_error(self, status):
        self.error = self.status_error[status]


class Item:

    def __init__(self, codigo, nome, valor, quantidade_total, quantidade_requisitada):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.quantidade_total = quantidade_total
        self.quantidade_requisitada = quantidade_requisitada

    @property
    def quantidade_disponivel(self):
        diferenca = self.quantidade_total - self.quantidade_requisitada
        return diferenca


class IValidadorDeRequisicao(ABC):

    @abstractmethod
    def validar_requisicao(self):
        pass


class Carrinho(IValidadorDeRequisicao):

    def __init__(self):
        self.itens = []

    def inserir_item(self, item):
        self.itens.append(item)

    def remover_item(self, codigo):
        itens = [item for item in self.itens]
        for item in itens:
            if item.codigo == codigo:
                self.itens.remove(item)
                break

    def validar_requisicao(self, requisicao):
        for x, item in enumerate(self.itens):
            if item.codigo == requisicao.codigo:
                if item.quantidade_disponivel >= requisicao.quantidade:
                    self.itens[x].quantidade_requisitada += requisicao.quantidade
                    return True
                requisicao.set_error(1)
                return False


class IntermediarioDeEstoque(IValidadorDeRequisicao):

    def __init__(self, produto_model):
        self.model = produto_model

    def validar_requisicao(self, requisicao):
        resultado = self.model.query.filter_by(codigo=(requisicao.codigo)).first()
        if resultado:
            if resultado.quantidade >= requisicao.quantidade:
                return resultado
            requisicao.set_error(1)
        else:
            requisicao.set_error(0)

    def atualizar_estoque(self, itens):
        for item in itens:
            p = self.model.query.filter_by(codigo=(item.codigo)).first()
            p.quantidade = item.quantidade_disponivel
            break


class RegistradorDeVendas:

    def __init__(self, model):
        self.model = model

    def registrar_venda(self, itens, operador, db):
        ultimo = 1
        registros = self.model.query.group_by(self.model.recibo).all()
        if registros:
            ultimo = max([registro.recibo for registro in registros]) + 1
        for item in itens:
            db.session.add(self.model(ultimo, item.codigo, item.quantidade_requisitada, operador))


class IntermediarioDeVenda(IValidadorDeRequisicao):

    def __init__(self, inter_estoque, carrinho, rg_venda, db):
        self.inter_estoque = inter_estoque
        self.carrinho = carrinho
        self.db = db
        self.rg_venda = rg_venda

    @property
    def subtotal(self):
        total = 0
        for item in self.carrinho.itens:
            total += item.quantidade_requisitada * item.valor
        else:
            return total

    def validar_requisicao(self, requisicao):
        r_carrinho = self.carrinho.validar_requisicao(requisicao)
        if r_carrinho == None:
            r_produto = self.inter_estoque.validar_requisicao(requisicao)
            if r_produto:
                item = Item(r_produto.codigo, r_produto.nome, r_produto.valor, r_produto.quantidade, requisicao.quantidade)
                self.carrinho.inserir_item(item)

    def concluir_venda(self, operador):
        if not self.carrinho.itens:
            return
        self.inter_estoque.atualizar_estoque(self.carrinho.itens)
        self.rg_venda.registrar_venda(self.carrinho.itens, operador, self.db)
        self.db.session.commit()
        self.esvaziar_carrinho()

    def esvaziar_carrinho(self):
        self.carrinho.itens = []


class RegistrarForm(Form):
    registrar_codigo = IntegerField('Código',
      validators=[DataRequired()])
    quantidade = html5.IntegerField('Quantidade',
      validators=[DataRequired(), NumberRange(min=1)])


class RemoverItemForm(Form):
    rm_codigo = IntegerField('Código',
      validators=[DataRequired()])
    rm_senha = PasswordField('Código de Segurança',
      validators=[DataRequired()])


class CancelarVendaForm(Form):
    cancel_senha = PasswordField('Código de Segurança',
      validators=[DataRequired()])
