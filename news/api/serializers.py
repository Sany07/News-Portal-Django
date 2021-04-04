from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


from news.models import News, Author, Category
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,TaggitSerializer)

from mainsite.api.serializers import AuthorDetailSerializer, CategorySerializer

class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AuthorDetailSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = News
        fields = "__all__"

class NewsDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AuthorDetailSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = News
        fields = "__all__"