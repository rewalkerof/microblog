from django.urls import path
from django.contrib import admin

from .views import (
    PostListAPIView
)

app_name = 'posts-api'

urlpatterns = [
    path('', PostListAPIView.as_view(), name="list"),

]
