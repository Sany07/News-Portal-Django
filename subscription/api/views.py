from rest_framework.generics import CreateAPIView
from rest_framework.decorators import  permission_classes
from rest_framework import permissions
from .serializers import EmailSubscriptionSerializer

class EmailSubscription(CreateAPIView):
    serializer_class = EmailSubscriptionSerializer
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save()
    #     data = {"message": "Your commet was posted"}
    #     return Response({"success": data,"comment":serializer.data})

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     data = {"message": "Your comment was posted"}
    #     return Response({"success": data,"comment":serializer.data}, status=status.HTTP_201_CREATED)
