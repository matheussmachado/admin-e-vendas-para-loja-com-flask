from flask import Blueprint, request, render_template, redirect, url_for, session, abort
from app.ext.db.main import Produtos, Credenciais, RegistroDeVendas, db
from .src import RegistrarForm, RemoverItemForm, CancelarVendaForm, IntermediarioDeVenda, Carrinho, IntermediarioDeEstoque, RequisicaoDeProduto, RegistradorDeVendas
bp = Blueprint('vendedor', __name__)
registrador = RegistradorDeVendas(RegistroDeVendas)
estoque = IntermediarioDeEstoque(Produtos)
carrinho = Carrinho()
venda = IntermediarioDeVenda(estoque, carrinho, registrador, db)

@bp.route('/vendedor/', methods=('GET', 'POST'))
def vendedor():
    registrar_form = RegistrarForm(request.form)
    rm_form = RemoverItemForm(request.form)
    cancel_form = CancelarVendaForm(request.form)
    registrar_form_error = None
    cancel_form_error = None
    rm_form_error = None
    req_error = None
    context = {'registrar_form':registrar_form, 
     'rm_form':rm_form, 
     'cancel_form':cancel_form, 
     'registrar_form_error':registrar_form_error, 
     'rm_form_error':rm_form_error, 
     'itens':venda.carrinho.itens, 
     'subtotal':venda.subtotal, 
     'req_error':req_error, 
     'operacao':None}
    if 'operador' in session:
        operador = session['operador']['nome']
        context.update(operador=operador)
        if request.method == 'GET':
            operacao = request.args.get('operacao', None)
            if operacao == 'concluir_venda':
                venda.concluir_venda(operador)
                return redirect(url_for('vendedor.vendedor'))
            return render_template(*('vendedor.html', ), **context)
            if registrar_form.registrar_codigo.data:
                if registrar_form.validate():
                    req = RequisicaoDeProduto(registrar_form.registrar_codigo.data, registrar_form.quantidade.data)
                    venda.validar_requisicao(req)
                    context['req_error'] = req.error
        else:
            context['registrar_form_error'] = 'Insira os dados corretamente'
    else:
        if cancel_form.cancel_senha.data:
            if cancel_form.validate():
                credencial = Credenciais.query.filter_by(credencial=(cancel_form.cancel_senha.data)).first()
                if credencial:
                    print(credencial)
                    venda.esvaziar_carrinho()
                    context['itens'] = venda.carrinho.itens
                else:
                    context['cancel_form_error'] = 'Senha inválida'
            else:
                context['cancel_form_error'] = 'Insira os dados corretamente'
        else:
            if rm_form.rm_senha.data:
                if rm_form.validate():
                    credencial = Credenciais.query.filter_by(credencial=(rm_form.rm_senha.data)).first()
                    if credencial:
                        print(credencial)
                        venda.carrinho.remover_item(rm_form.rm_codigo.data)
                    else:
                        print('ok')
                        context['rm_form_error'] = 'Senha inválida'
                else:
                    context['rm_form_error'] = 'Insira os dados corretamente'
            context['subtotal'] = venda.subtotal
            return render_template(*('vendedor.html', ), **context)
            return redirect(url_for('login.login'))


@bp.route('/concluir_venda/', methods=['GET', 'POST'])
def concluir_venda():
    print(venda.carrinho.itens)
    return (f"{venda.carrinho.itens}")
# okay decompiling app/ext/site/vendedor/__pycache__/main.cpython-38.pyc
