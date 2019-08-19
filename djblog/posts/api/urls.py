from django.urls import path

from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
    PostCreateAPIView)

app_name = 'posts-api'

urlpatterns = [
    path('', PostListAPIView.as_view(), name="list"),
    path('create/', PostCreateAPIView.as_view(), name="create"),
    path('<int:id>/', PostDetailAPIView.as_view(), name="detail"),
    path('<int:id>/edit/', PostUpdateAPIView.as_view(), name="edit"),
    path('<int:id>/delete/', PostDestroyAPIView.as_view(), name="delete"),
]
