from datetime import date
from flask_admin.model import typefmt
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from wtforms.validators import required

class ProdutoView(ModelView):
    column_list = ('codigo', 'nome', 'valor', 'quantidade')
    column_editable_list = ('nome', 'valor', 'quantidade')
    form_args = {'nome':{'label':'Nome', 
      'validators':[
       required()]}, 
     'codigo':{'label':'Codigo', 
      'validators':[
       required()]}, 
     'valor':{'label':'Preço', 
      'validators':[
       required()]}, 
     'quantidade':{'label':'Quantidade', 
      'validators':[
       required()]}}
    form_edit_rules = [
     rules.FieldSet(('nome', 'valor', 'quantidade'))]


class CredenciaisView(ModelView):
    form_args = {
        'permissao': {
            'label': 'Permissão'
        }
    }
    column_labels = dict(permissao="Permissão")

def datetime_format(view, value):
    return value.strftime('%d/%m/%Y --- %H:%M:%S')


MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({type(None): typefmt.null_formatter, 
 date: datetime_format})

class RegistroDeVendasView(ModelView):
    can_create = False
    can_edit = False
    can_delete = False
    column_default_sort = [
     ('recibo', True), ('codigo', True),
     ('quantidade', True), ('operador', True), ('data_hora', True)]
    column_labels = dict(data_hora='Data --- Hora',
      codigo='Cód. do Produto',
      quantidade='Qtd.',
      recibo='Recibo Nº',
      operador='Operador(a)')
    column_type_formatters = MY_DEFAULT_FORMATTERS
