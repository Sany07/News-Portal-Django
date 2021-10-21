from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from news.api.serializers import NewsSerializer
from mainsite.api.serializers import UserDetailSerializer, NewsSerializer
from comment.models import Comment
from account.api.serializers import UserSerializer
from news.models import News

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    # comments = NewsSerializer(many=True)

    class Meta:
        model = Comment
        fields = "__all__"

    # def get_comments(self, obj):
    #     news_list = News.objects.filter(
    #         category=obj.id, is_published=True).order_by('-id').values('title', 'slug', 'description', 'timestamp', 'author', 'author__user__username', 'thumbnail', 'thumbnail_url')
    #     return news_list
