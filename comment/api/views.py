from rest_framework.decorators import  permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.http import JsonResponse


# from news.models import Category, News
from .serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status


class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #     data = {"message": "Your commet was posted"}
    #     return Response({"success": data,"comment":serializer.data}, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        data = {"message": "Your comment was posted"}
        return Response({"success": data,"comment":serializer.data}, status=status.HTTP_201_CREATED)

class CommentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = serializer_class.Meta.model.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]