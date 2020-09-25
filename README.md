# admin-e-venda-para-loja-física-com-flask

## Sobre o projeto.

O projeto consiste em fornecer uma sistema de vendas de produtos e administração geral de comércio físico, nesse caso um petshop. A simples interface de vendas é semelhante a de sistemas de vendas de um(a) operador(a) de caixa registradora presente nos comércios.

## Por que?
Esse projeto foi concebido como parte de meu aprendizado do framework Flask.

## Funcionalidades.
### Venda:
- Processar produtos a serem vendidos a partir de seus "códigos de barra"
- Reverter o processamento descrito acima, como remover itens processados ou cancelar a venda por completa. Esse processo consiste em autenticação de uma credencial que possua permissão para tal, registrada pelo administrador.
- Concluir a venda.

### Admin:
- Consiste em um CRUD de produtos e credenciais, bem como uma visualização das vendas registradas e suas características.

## Features.
Algumas das ferramentas utilizadas:
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Admin
- Flask-Migrate
- SQLite
- Bootstrap 3

## Como executar o projeto

### Pre requisitos:
- Python 3.8+

### Instalando:
No seu emulador de terminal:
- Ative sua virtual env.
- Configure a variável de ambiente do flask como: app

Comandos seguintes:

`pip install -r requirements.txt`
`flask db init`
`flask db migrate`
`flask db upgrade`
`flask run`

Com isso, é possível acessar a aplicação Flask e em seguida a rota  `/admin`  para criar uma credencial de funcionário que irá operar a venda. Assim, poderá se autenticar e obter acesso à interface de vendas.