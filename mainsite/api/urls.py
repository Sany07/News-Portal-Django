
from django.urls import path, include
from .views import NewsApiView, SingleNewsApiView


urlpatterns = [
     path('news/', NewsApiView.as_view()),
     path('news/<int:pk>', SingleNewsApiView.as_view())
    
]
