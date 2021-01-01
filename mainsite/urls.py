
from django.urls import path
from .views import *


app_name = "newspaper"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('single/', SingleView.as_view(), name='single-page'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('post/<slug:slug>/', PostSingleView.as_view(), name='single-post'),
    path('tag/<slug:tag>/', FilterByTag, name='tag'),
]
