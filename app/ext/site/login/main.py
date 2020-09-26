from flask import Blueprint, request, redirect, render_template, url_for, session, flash
from wtforms import Form, PasswordField
from wtforms.validators import DataRequired

from app.ext.db.main import Credenciais

class LoginForm(Form):
	credencial = PasswordField("credencial", validators=[DataRequired()])


bp = Blueprint("login", __name__)

@bp.route('/', methods=["GET", "POST"])
@bp.route('/login/', methods=["GET", "POST"])
def login():
	error = None
	login_form = LoginForm(request.form)
	if request.method == "GET":
		return render_template('login.html', form=login_form)
	user = login_form.credencial.data
	if login_form.validate():
		result = Credenciais.query.filter_by(credencial=user).first()
		if result:
			session['operador'] = None
			session['operador'] = {
				'credencial': result.credencial, 
				'nome': result.nome_do_funcionario
			}

			return redirect(url_for('vendedor.vendedor'))
		else:
			flash('Credencial inválida', 'error')
			return render_template('login.html', form=login_form)
	else:
		error = "Insira o dado corretamente."
		return render_template('login.html', form=form, error=error)



@bp.route('/logout/')
def logout():
	session.pop('operador', None)
	return redirect(url_for('login.login'))
