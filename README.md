<h1 align="center">
    Desafio GovOne - Api de notícias
</h1>

# Sobre o Desafio

Desenvolver uma API REST para gerenciamento de notícias. <br/> 
Essa API deve seguir as boas práticas de desenvolvimento e respeitar os verbos HTTP adequados para cada operação. <br/> 

### A API deve conter os seguintes endpoints:
```ruby
● Listar todas as notícias → GET /noticias/ 
● Obter uma notícia específica por ID → GET /noticias/{id}/ 
● Criar uma nova notícia → POST /noticias/ 
● Atualizar uma notícia existente → PUT /noticias/{id}/ ou PATCH /noticias/{id}/ 
● Remover uma notícia → DELETE /noticias/{id}/ 
```
### Modelo de dados esperado: 

> Cada notícia deve possuir os seguintes campos: 
```ruby
● id (string ou inteiro, identificador único) 
● titulo (string, obrigatório) 
● conteudo (string, obrigatório) 
● autor (string, obrigatório) 
● data_publicacao (datetime, gerado automaticamente) 
```

# Organização do Projeto
```ruby
├── .github/                # Arquivo de configuração do GitHub Actions
│
├── api_rest/               # Aplicativo Django para a API
│   ├── migrations/         # Migrações do banco de dados
│   ├── __init__.py         # Arquivo de inicialização do Python
│   ├── admin.py            # Configurações do admin
│   ├── apps.py             # Configuração do aplicativo
│   ├── models.py           # Modelos do Django
│   ├── serializers.py      # Serializers para a API
│   ├── test_views.py       # Testes para as views
│   ├── urls.py             # URLs do aplicativo
│   └── views.py            # Views da aplicação
│
├── api_root/               # Configurações do projeto Django
│   ├── __init__.py         # Arquivo de inicialização do Python
│   ├── asgi.py             # Configuração para ASGI
│   ├── settings.py         # Configurações gerais do projeto
│   ├── urls.py             # URLs principais do projeto
│   └── wsgi.py             # Configuração para WSGI
│
├── .gitignore              # Arquivo para ignorar arquivos/módulos no git
├── db.sqlite3              # Banco de dados SQLite
├── docker-compose.yml      # Configuração do Docker Compose
├── Dockerfile              # Dockerfile para construir a imagem
├── manage.py               # Script de gerenciamento do Django
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```
## Por quê utilizar o Django com Django REST Framework?

Utilizar `Django` com `Django REST Framework` é ideal para desenvolver `APIs` robustas e escaláveis de forma rápida. <br/> 
`Django` fornece uma estrutura sólida e testes integrados, enquanto o `Django REST Framework` facilita a criação de endpoints `RESTful`, <br/> 
incluindo serialização e autenticação, tornando o desenvolvimento mais eficiente e organizado. <br/> 

## Dependências para executar localmente

- Ter uma IDE de sua preferência
- Instalar Python3: [Download](https://www.python.org/downloads/)
- Instalar Docker (opcional): [Docker](https://docs.docker.com/desktop/setup/install/windows-install/)

<h1 align="center">
Executando o projeto
</h1>

> Clone o projeto
``` ruby
git clone https://github.com/Jessicac30/desafio_govone.git
```

## Instruções de execução 
- Use os comandos listados abaixo no terminal, diretamente na pasta raiz:

> Crie um ambiente virtual
``` ruby
python -m venv venv 
```
### Ative o ambiente virtual:
  
> No Windows:
``` ruby
./venv/Scripts/activate
```

> No macOS/Linux::
``` ruby
source venv/bin/activate
```

### Instalar as dependências listadas:
``` ruby
pip install -r requirements.txt
``` 

### Realizar as migrações do banco de dados:
```ruby
python manage.py migrate
``` 

### Criar um super usuário (opcional): 
> Se você desejar acessar o painel administrativo do Django, pode criar um superusuário com o comando:
```ruby
python manage.py createsuperuser
```
Siga as instruções para definir um nome de usuário, e-mail e senha.

## Executar o servidor de desenvolvimento: 

> Para iniciar o servidor de desenvolvimento do Django, use o seguinte comando:
```ruby
python manage.py runserver
```
- O servidor será iniciado e você verá uma saída no terminal indicando em qual endereço ele está rodando (http://127.0.0.1:8000/).


# Executar com docker
Inicie o docker desktop

> Executar o Build
```ruby
docker-compose up --build   
```
> Se você apenas deseja reiniciar os serviços sem rebuildar as imagens, pode usar:
```ruby
docker-compose up
```

<h1 align="center">
Acessando os endpoints da API
</h1>
Agora você pode acessar os endpoints definidos na API através do navegador ou ferramentas como Postman. <br/> <br/>  

> Baixar Collections
[Govone.postman_collection.json](https://github.com/user-attachments/files/18566624/Govone.postman_collection.json)

## Acessar através do Postman 
![Postman](https://github.com/user-attachments/assets/611a376f-926f-482e-8b6f-553a43f1f982)

# Acessar através do navegador
```ruby
http://127.0.0.1:8000/api/noticias/
```
![Navegador](https://github.com/user-attachments/assets/54414ff5-5207-48c8-a31c-9c1534d20e16)

# Acessar através do Swagger
```ruby
http://127.0.0.1:8000/api/swagger/
```
![Swagger](https://github.com/user-attachments/assets/cf336c67-f520-463d-a5da-29525d0ab156)

## Vídeo Swagger
![SwaggerGif](https://github.com/user-attachments/assets/4a376f84-d33f-46b6-949a-6c27a122eb6b)

# Acessar através do Curl
> Listar todas as notícias → GET /noticias/ 
```ruby
curl -X 'GET' \
  'http://127.0.0.1:8000/api/noticias/' \
  -H 'accept: application/json' \
  -H 'X-CSRFTOKEN: vh4v5YHQnw4W0pG3oiwdykugbLUCj33KKv8oH3e9Itl3zzNN5jkJGFL3NwvV9vZ1'
```

> Criar uma nova notícia → POST /noticias/ 
```ruby
curl -X 'POST' \
  'http://127.0.0.1:8000/api/noticias/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFTOKEN: vh4v5YHQnw4W0pG3oiwdykugbLUCj33KKv8oH3e9Itl3zzNN5jkJGFL3NwvV9vZ1' \
  -d '{
  "titulo": "Nova Noticia",
  "conteudo": "Teste nova noticia",
  "autor": "Carlos Silva"
}'
```

> Atualizar uma notícia existente → PUT /noticias/{id}/ ou PATCH /noticias/{id}/ 
```ruby
curl -X 'PUT' \
  'http://127.0.0.1:8000/api/noticias/919ffd0b-a9a0-4537-be49-13f5bbf2173f/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFTOKEN: vh4v5YHQnw4W0pG3oiwdykugbLUCj33KKv8oH3e9Itl3zzNN5jkJGFL3NwvV9vZ1' \
  -d '{
  "titulo": "Nova Noticia 3",
  "conteudo": "Teste nova noticia",
  "autor": "Carlos Silva"
}'
```

> Remover uma notícia → DELETE /noticias/{id}/ 
```ruby
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/noticias/919ffd0b-a9a0-4537-be49-13f5bbf2173f/' \
  -H 'accept: application/json' \
  -H 'X-CSRFTOKEN: vh4v5YHQnw4W0pG3oiwdykugbLUCj33KKv8oH3e9Itl3zzNN5jkJGFL3NwvV9vZ1'
```

<h1 align="center">
Executar os testes
</h1>

> Para executar os teste
```ruby
python manage.py test api_rest
```
![Test](https://github.com/user-attachments/assets/e52cbd5c-3fdb-4245-968f-141aa651ddd2)

## Executando no CI
![CI2](https://github.com/user-attachments/assets/91642896-566f-41c6-b9ec-ce82cf0e8731)