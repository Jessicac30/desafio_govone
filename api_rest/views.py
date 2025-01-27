from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import News
from .serializers import NewsSerializer

import json

@api_view(['GET'])
def get_news(request):

    if request.method == 'GET':

        news = News.objects.all()

        serializer = NewsSerializer(news, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)