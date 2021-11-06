from rest_framework import response
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly
from django.http import JsonResponse
# from news.models import Category, News
from .serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status, serializers


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # print('s', self.request.user)
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {"message": "Your comment was posted", "comment": serializer.data}
        return Response(response, status=status.HTTP_201_CREATED)


# class CommentDetail(RetrieveUpdateDestroyAPIView):
#     serializer_class = CommentSerializer
#     queryset = serializer_class.Meta.model.objects.all()
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]


class CommentsFilterByNews(RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get(self, *args, **kwargs):
        data = self.queryset.filter(
            post=self.kwargs['id'],reply=None).order_by('-id') #reply=None
        comments = CommentSerializer(data, many=True)
        return Response(comments.data, status=status.HTTP_200_OK)
