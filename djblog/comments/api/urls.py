from django.urls import path

from .views import (
    CommentDetailAPIView,
    CommentListAPIView
)

app_name = 'comments-api'

urlpatterns = [
    path('', CommentListAPIView.as_view(), name="list"),
    path('<int:id>/', CommentDetailAPIView.as_view(), name="detail"),
]
