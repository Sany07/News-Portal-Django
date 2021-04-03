
from django.urls import path, include
from .views import NewsApiView, SingleNewsApiView, CategoryApiView, SingleCategoryApiView


urlpatterns = [
     path('news/', NewsApiView.as_view()),
     path('news/<int:pk>/', SingleNewsApiView.as_view()),
     path('category/', CategoryApiView.as_view()),
     path('category/<int:pk>/', SingleCategoryApiView.as_view()),
    
]
