
from django.urls import path, include
from .views import CommentList, CommentsFilterByNews


urlpatterns = [
    path('comments/', CommentList.as_view()),
    path('comments/<int:id>/', CommentsFilterByNews.as_view()),

]
