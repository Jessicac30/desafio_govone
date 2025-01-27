from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('noticias/', NewsList.as_view(), name='news-list'),
    path('noticias/<uuid:pk>/', NewsDetail.as_view(), name='news-detail'),
]
