
from django.urls import path, include
from .views import CategoryApiView, SingleCategoryApiView, HomePageApiView, NewsFilterByTag, PopularMostCommentedNewsApiView


urlpatterns = [
    path('homepage/', HomePageApiView.as_view()),
    path('sidebar/', PopularMostCommentedNewsApiView.as_view()),
    path('tag/<slug:tag>/', NewsFilterByTag),
    path('category/', CategoryApiView.as_view()),
    path('category/<slug:slug>/', SingleCategoryApiView.as_view()),

]
