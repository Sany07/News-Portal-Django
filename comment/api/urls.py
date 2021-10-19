
from django.urls import path, include
from .views import CommentList, CommentDetail, CommentFilterByNews


urlpatterns = [
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('cc/<int:pk>/', CommentFilterByNews.as_view()),

]
