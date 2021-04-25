
from django.urls import path, include
from .views import registration


urlpatterns = [
     path("register/", registration.as_view(), name="register"),
#     path("login/", MyTokenObtainPairView.as_view()),
#     path("token/refresh/", TokenRefreshView.as_view()),
]