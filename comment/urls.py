
from django.urls import path
from .views import *


app_name = "commentapp"

urlpatterns = [
    path('comment/create/', create_comment_View, name='comment'),

]
