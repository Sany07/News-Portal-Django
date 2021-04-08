from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response

from .serializers import NewsSerializer, CategorySerializer, NewsDetailSerializer

from mainsite.models import HomePageSettings
from news.models import Category, News


class HomePageApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):

        home_page_settings = HomePageSettings.objects.last()
        news_list = News.objects.all()
        post_catalog_one = news_list.filter(category=home_page_settings.post_catalog_one).order_by('-id')[:3]
        post_catalog_two = news_list.filter(category=home_page_settings.post_catalog_two).order_by('-id')[:2]
        post_catalog_three = news_list.filter(category=home_page_settings.post_catalog_three).order_by('-id')[:2]
        post_catalog_four = news_list.filter(category=home_page_settings.post_catalog_four).order_by('-id')[:3]
        post_catalog_five = news_list.filter(category=home_page_settings.post_catalog_five).order_by('-id')[:2]
        
        post_catalog_one = NewsSerializer(post_catalog_one, many=True)
        post_catalog_two = NewsSerializer(post_catalog_two, many=True)
        post_catalog_three = NewsSerializer(post_catalog_three, many=True)
        post_catalog_four = NewsSerializer(post_catalog_four, many=True)
        post_catalog_five = NewsSerializer(post_catalog_five, many=True)

        data = {
        'post_catalog_one': post_catalog_one.data,
        'post_catalog_two': post_catalog_two.data,
        'post_catalog_three': post_catalog_three.data,
        'post_catalog_three': post_catalog_three.data,
        'post_catalog_five': post_catalog_five.data,
        }

        return Response(data, status=status.HTTP_200_OK)

class NewsApiView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_published=True)
    permission_classes = [AllowAny]


class SingleNewsApiView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_published=True)
    permission_classes = [AllowAny]


class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [AllowAny]

class SingleCategoryApiView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [AllowAny]