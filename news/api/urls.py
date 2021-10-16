
from django.urls import path, include
from .views import NewsApiView, SingleNewsApiView


urlpatterns = [
    path('news/', NewsApiView.as_view()),
    path('news/<slug:slug>/', SingleNewsApiView.as_view()),
]
