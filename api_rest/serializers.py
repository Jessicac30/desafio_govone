from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'titulo', 'conteudo', 'autor', 'data_publicacao']

    def validate_titulo(self, value):
        if not value:
            raise serializers.ValidationError("O título não pode estar vazio.")
        return value

    def validate_conteudo(self, value):
        if not value:
            raise serializers.ValidationError("O conteúdo não pode estar vazio.")
        return value

    def validate_autor(self, value):
        if not value:
            raise serializers.ValidationError("O autor não pode estar vazio.")
        return value
