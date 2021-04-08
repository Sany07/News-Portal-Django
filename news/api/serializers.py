from rest_framework import serializers
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()


from news.models import News, Author, Category
from taggit.models import Tag

from mainsite.api.serializers import AuthorDetailSerializer, CategorySerializer
from taggit_serializer.serializers import (TagListSerializerField,TaggitSerializer)

class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):
    # author = AuthorDetailSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    # tags = TagListSerializerField()

    class Meta:
        model = News
        fields = "__all__"

class NewsDetailSerializer(TaggitSerializer, serializers.ModelSerializer):
    # author = AuthorDetailSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    # tags = TagListSerializerField()
    related_post = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "__all__"


    def get_related_post(self):
        return self.Meta.model.filter(is_published='True', category=self.object.category.id).exclude(id=self.object.id).order_by('-id')

    # def get_related_post_filter_by_tag(self):
    #     for tag in Tag.objects.all():
    #         return self.get_related_post_by_category().filter(tags__name__in=[tag])[:4]
