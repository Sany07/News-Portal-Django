
from django.urls import path, include
from .views import registration
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)


urlpatterns = [
     path("register/", registration.as_view(), name="register"),
     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]