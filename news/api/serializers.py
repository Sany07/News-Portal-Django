from taggit_serializer.serializers import (
    TagListSerializerField, TaggitSerializer)
from mainsite.api.serializers import AuthorDetailSerializer, CategorySerializer
from taggit.models import Tag
from news.models import News, Author, Category
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Count
User = get_user_model()


class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AuthorDetailSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()
    total_comment_count = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "__all__"

    def get_total_comment_count(self, obj):
        comment_count = obj.post.aggregate(Count('post__id'))
        return comment_count['post__id__count']


class NewsDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AuthorDetailSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()
    related_post = serializers.SerializerMethodField()
    total_comment_count = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "__all__"

    def get_related_post(self, obj):
        return self.Meta.model.objects.filter(is_published='True', category=obj.category.id).exclude(id=obj.id).order_by('-id').values('id', 'slug', 'timestamp', 'thumbnail_url', 'author', 'thumbnail', 'title')

    def get_total_comment_count(self, obj):
        comment_count = obj.post.aggregate(Count('post__id'))
        return comment_count['post__id__count']
