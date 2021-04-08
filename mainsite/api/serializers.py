from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


from news.models import News, Author, Category
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField,TaggitSerializer)



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
            category=obj.id, is_published=True).order_by('-id').values('title')
        return news_list

# class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
#     author = AuthorDetailSerializer(read_only=True)
#     category = CategorySerializer(read_only=True)
#     tags = TagListSerializerField()

#     class Meta:
#         model = News
#         fields = "__all__"

# class NewsDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
#     author = AuthorDetailSerializer(read_only=True)
#     category = CategorySerializer(read_only=True)
#     tags = TagListSerializerField()

#     class Meta:
#         model = News
#         fields = "__all__"