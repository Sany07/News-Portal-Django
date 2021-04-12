
from django.urls import path, include
from .views import  CategoryApiView, SingleCategoryApiView, HomePageApiView, NewsFilterByTag


urlpatterns = [
     path('homepage/', HomePageApiView.as_view()),
     path('tag/<slug:tag>/', NewsFilterByTag),
     path('category/', CategoryApiView.as_view()),
     path('category/<int:pk>/', SingleCategoryApiView.as_view()),
    
]