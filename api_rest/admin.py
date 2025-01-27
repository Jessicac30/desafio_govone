from django.contrib import admin

from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'conteudo', 'autor', 'data_publicacao')
    search_fields = ('titulo', 'autor')

admin.site.register(News, NewsAdmin)
