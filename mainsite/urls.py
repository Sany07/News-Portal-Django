
from django.urls import path
from .views import *


app_name = "newspaper"

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('single/', SinglePage.as_view(), name='single-page'),
    path('blog/', BlogPage.as_view(), name='blog'),
    path('category/', CategoryPage.as_view(), name='category'),
]
