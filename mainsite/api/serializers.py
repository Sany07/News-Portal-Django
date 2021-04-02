from rest_framework import serializers
from rest_framework.response import Response


from django.contrib.auth import get_user_model
User = get_user_model()


from news.models import News, Author, Category
from taggit.models import Tag

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)



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




# class CategorySerializer(serializers.ModelSerializer):
#     total_ads = serializers.SerializerMethodField()

#     class Meta:
#         model = Category
#         fields = "__all__"

#     def get_total_ads(self, obj):
#         return obj.ad_set.count()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = AuthorDetailSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = News
        fields = "__all__"
    

        

