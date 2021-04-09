
from django.urls import path, include
from .views import EmailSubscription


urlpatterns = [
    path('email-subscription/', EmailSubscription.as_view()),
    
]
