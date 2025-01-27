import uuid
from django.db import models

class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField(max_length=500)
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.titulo} | Autor: {self.autor} | Publicado em: {self.data_publicacao.strftime("%d/%m/%Y %H:%M")}'
