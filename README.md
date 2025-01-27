<h1 align="center">
    Desafio Govone - Api de notícias
</h1>

## Sobre o Desafio

Desenvolver uma API REST para gerenciamento de notícias. 
Essa API deve seguir as boas práticas de desenvolvimento e respeitar os verbos HTTP adequados para cada operação. 

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