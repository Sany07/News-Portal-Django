from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


from comment.models import Comment
from mainsite.api.serializers import UserDetailSerializer, NewsSerializer
# from news.api.serializers import  NewsSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"