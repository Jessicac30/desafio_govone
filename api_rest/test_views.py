from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import News
from .serializers import NewsSerializer

class NewsAPITests(APITestCase):

    def setUp(self):
        self.news_data = {
            'titulo': 'Notícia Teste Views',
            'conteudo': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
            'autor': 'Autor Teste',
        }
        self.news = News.objects.create(titulo='Notícia Inicial', conteudo='Conteúdo da notícia inicial.', autor='Autor Inicial')
        self.url = reverse('news-list')

    def test_list_news(self):
        """Testar a listagem de notícias."""
        response = self.client.get(self.url)
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_news(self):
        """Testar a criação de uma nova notícia."""
        response = self.client.post(self.url, self.news_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(News.objects.count(), 2)
        self.assertEqual(News.objects.get(id=response.data['id']).titulo, 'Notícia Teste Views')

    def test_retrieve_news(self):
        """Testar a recuperação de uma notícia específica."""
        url = reverse('news-detail', args=[self.news.id])
        response = self.client.get(url)
        serializer = NewsSerializer(self.news)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_news(self):
        """Testar a atualização de uma notícia existente."""
        url = reverse('news-detail', args=[self.news.id])
        new_data = {'titulo': 'Notícia Atualizada', 'conteudo': 'Conteúdo atualizado.', 'autor': 'Autor Atualizado'}
        response = self.client.put(url, new_data)
        self.news.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.news.titulo, 'Notícia Atualizada')

    def test_delete_news(self):
        """Testar a exclusão de uma notícia."""
        url = reverse('news-detail', args=[self.news.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(News.objects.filter(id=self.news.id).exists())
