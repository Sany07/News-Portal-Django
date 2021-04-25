from django.contrib.auth import get_user_model, login
from requests.exceptions import HTTPError
from rest_framework import permissions, status
from rest_framework import response, decorators
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])
# def registration(request):
#     serializer = UserCreateSerializer(data=request.data)
#     if not serializer.is_valid(raise_exception=True):
#         return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#     user = serializer.save()
#     res = {
#         "status": True,
#         "message": "Registration Successfull",
#     }
#     return response.Response(res, status.HTTP_201_CREATED)
    
class registration(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    #     data = {"message": "Your commet was posted"}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if not serializer.is_valid(raise_exception=True):
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
   
        # self.perform_create(serializer)
        user = serializer.save()
        res = {
        "status": 'success',
        "message": "Registration Successfull",
    }
        return Response(res, status=status.HTTP_201_CREATED)