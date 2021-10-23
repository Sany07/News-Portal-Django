from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from news.api.serializers import NewsSerializer
from mainsite.api.serializers import UserDetailSerializer, NewsSerializer
from comment.models import Comment
from account.api.serializers import UserSerializer
from news.models import News

User = get_user_model()

class CommentChildSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)
    replies =serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["reply"]

    def get_replies(self, obj):
        if obj.id:
            replies = self.Meta.model.objects.filter(reply=obj.id)
            return CommentChildSerializer(replies , many=True).data
        return None
        
