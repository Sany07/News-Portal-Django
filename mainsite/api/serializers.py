from taggit_serializer.serializers import (
    TagListSerializerField, TaggitSerializer)
from taggit.models import Tag
from news.models import News, Author, Category
from django.db.models import Count
from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]


class AuthorDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    news = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_news(self, obj):
        news_list = News.objects.filter(
            category=obj.id, is_published=True).order_by('-id').values('title', 'slug', 'description', 'timestamp', 'author', 'author__user__username', 'thumbnail', 'thumbnail_url')
        return news_list


class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AuthorDetailSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()
    # comments = CommentSerializer()
    total_comment_count = serializers.SerializerMethodField()
    # custom_field = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "__all__"

    def get_total_comment_count(self, obj):
        comment_count = obj.post.aggregate(Count('post__id'))
        return comment_count['post__id__count']

    # def get_custom_field(self, obj):
    #     # foo = self.context.get('foo')
    #     # print(self.context.get('foo'))
    #     return self.category


class NewsDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AuthorDetailSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()
    related_post = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "__all__"

    def get_related_post(self, obj):
        return self.Meta.model.objects.filter(is_published='True', category=obj.category.id).exclude(id=obj.id).order_by('-id').values('id', 'title', 'thumbnail', 'thumbnail_url')
