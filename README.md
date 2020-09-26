# admin-e-venda-para-loja-física-com-flask

## Sobre o projeto.
![vendas](https://user-images.githubusercontent.com/63216146/94327395-21229500-ff81-11ea-8921-dd0a47b71a43.png)


O projeto consiste em fornecer um sistema de vendas de produtos e administração geral de comércio físico, nesse caso um petshop. A simples interface de vendas é semelhante a de sistemas de vendas de um(a) operador(a) de caixa registradora presente nos comércios.

## Por que?
Esse projeto foi concebido como parte de meu aprendizado do framework Flask.

## Funcionalidades.
### Venda:
- Processar produtos a serem vendidos a partir de seus "códigos de barra"
- Reverter o processamento descrito acima, como remover itens processados ou cancelar a venda por completa. Esse processo consiste em autenticação de uma credencial que possua permissão para tal, registrada pelo administrador.
- Concluir a venda.
- Lidar com possíveis inconsistências de: autenticações, código de produto inexistente e quantidade de requisição de produto incompatível.

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

Com isso, é possível acessar a aplicação Flask e em seguida a rota  `/admin` para criar uma credencial de funcionário que irá operar a venda. Assim, poderá se autenticar nas rotas `/` ou `/login` e obter acesso à interface de vendas. Abaixo a imagem da interface de admin:

![admin-credenciais](https://user-images.githubusercontent.com/63216146/94327660-dc97f900-ff82-11ea-988c-f37219751afe.png)


##Observações
- O sistema de vendas foi desenvolvido para atuar com apenas um terminal de trabalho ativo, não sendo compatível ainda com o que se encontra em comércios que possuem mais de um terminal de operação de caixa registradora.
- O sistema de admin. ainda não possui login.
- Não possuo direitos sobre o nome da empresa fictícia que aparece pelas interfaces, esta que foi escolhida apenas para ilustrar o projeto.
