from rest_framework.decorators import  permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

# from news.models import Category, News
from .serializers import CommentSerializer

class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = serializer_class.Meta.model.objects.all()

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]