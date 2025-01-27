from django.urls import path
from .views import NewsList, NewsDetail
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_view = get_schema_view(
    openapi.Info(
        title="API de Notícias Govone",
        default_version="V1",
        description="Documentação da API para gerenciar notícias Govone"
    ),
)

urlpatterns = [
    path('noticias/', NewsList.as_view(), name='news-list'),
    path('noticias/<uuid:pk>/', NewsDetail.as_view(), name='news-detail'),
    path('swagger/', swagger_view.with_ui('swagger'))
]
