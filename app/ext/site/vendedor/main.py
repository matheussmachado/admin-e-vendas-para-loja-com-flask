from flask import Blueprint, request, render_template, redirect, url_for, session, abort, flash
from app.ext.db.main import Produtos, Credenciais, RegistroDeVendas, db
from .src import RegistrarForm, RemoverItemForm, CancelarVendaForm, ConcluirVendaForm, IntermediarioDeVenda, Carrinho, IntermediarioDeEstoque, RequisicaoDeProduto, RegistradorDeVendas

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
    concluir_form = ConcluirVendaForm(request.form)
    context = {
        'registrar_form':registrar_form, 
        'rm_form':rm_form,
        'cancel_form':cancel_form,
        'concluir_form': concluir_form,
        'itens':venda.carrinho.itens,
        'subtotal':venda.subtotal, 
        'operacao':None
    }
    if 'operador' in session:
        
        operador = session['operador']['nome']
        context.update(operador=operador)
        if request.method == 'GET':
            return render_template('vendedor.html', **context)
        if concluir_form.submit.data:
            print(concluir_form.submit.data)
            print('ok')
            venda_concluida = venda.concluir_venda(operador)
            if venda_concluida:
                flash('Venda concluída com sucesso!', 'success')
        if registrar_form.registrar_codigo.data:
            if registrar_form.validate():
                req = RequisicaoDeProduto(registrar_form.registrar_codigo.data, registrar_form.quantidade.data)
                venda.validar_requisicao(req)
                if req.error:
                    flash(req.error, 'error')
            else:
                flash('Insira os dados corretamente', 'error')
        elif cancel_form.cancel_senha.data:
            if cancel_form.validate():
                credencial = Credenciais.query.filter_by(credencial=(cancel_form.cancel_senha.data)).first()
                if credencial:
                    venda.esvaziar_carrinho()
                    context['itens'] = venda.carrinho.itens
                else:
                    flash('Senha inválida', 'error')
            else:
                #context['cancel_form_error'] = 'Insira os dados corretamente'
                flash('Insira os dados corretamente', 'error')
        elif rm_form.rm_senha.data:
            if rm_form.validate():
                credencial = Credenciais.query.filter_by(credencial=(rm_form.rm_senha.data)).first()
                if credencial:
                    venda.carrinho.remover_item(rm_form.rm_codigo.data)
                else:
                    #context['rm_form_error'] = 'Senha inválida'
                    flash('Senha inválida', 'error')
            else:
                #context['rm_form_error'] = 'Insira os dados corretamente'
                flash('Insira os dados corretamente', 'error')
        context['subtotal'] = venda.subtotal
        return render_template('vendedor.html', **context)
    else:
        return redirect(url_for('login.login'))

