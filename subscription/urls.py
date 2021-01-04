
from django.urls import path
from .views import *


app_name = "subscriptionapp"

urlpatterns = [
    
    path('create/', email_sub, name='create'),
]