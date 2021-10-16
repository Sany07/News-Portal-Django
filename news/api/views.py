from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from news.models import News
from .serializers import NewsSerializer, NewsDetailSerializer


class NewsApiView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_published=True)
    permission_classes = [AllowAny]

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['foo'] = 'bar'
    #     return context


class SingleNewsApiView(RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_published=True)
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
